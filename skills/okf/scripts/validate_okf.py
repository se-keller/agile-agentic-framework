#!/usr/bin/env python3
"""Validate the structural requirements of an OKF v0.2 knowledge bundle."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from typing import Any, Iterable

import yaml


FRONTMATTER_RE = re.compile(
    r"\A---[ \t]*\r?\n(?P<yaml>.*?)\r?\n---[ \t]*(?:\r?\n|\Z)(?P<body>.*)\Z",
    re.DOTALL,
)
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
RESERVED_NAMES = {"index.md", "log.md"}
OKF_STATUSES = {"draft", "stable", "deprecated"}
DATE_RE = re.compile(r"\d{4}-\d{2}-\d{2}\Z")


@dataclass(frozen=True)
class Finding:
    level: str
    path: Path
    message: str


@dataclass(frozen=True)
class Document:
    path: Path
    metadata: dict[str, Any]
    body: str


def parse_iso8601(value: Any) -> bool:
    if isinstance(value, (date, datetime)):
        return True
    if not isinstance(value, str) or not value.strip():
        return False
    try:
        datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return False
    return True


def parse_calendar_date(value: Any) -> bool:
    if isinstance(value, datetime):
        return False
    if isinstance(value, date):
        return True
    if not isinstance(value, str) or not DATE_RE.fullmatch(value):
        return False
    try:
        date.fromisoformat(value)
    except ValueError:
        return False
    return True


def parse_document(path: Path, require_frontmatter: bool) -> tuple[Document | None, list[Finding]]:
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        return None, [Finding("error", path, f"cannot read UTF-8 Markdown: {exc}")]

    match = FRONTMATTER_RE.match(text)
    if not match:
        if require_frontmatter:
            return None, [Finding("error", path, "missing YAML frontmatter")]
        return Document(path, {}, text), []

    try:
        metadata = yaml.safe_load(match.group("yaml"))
    except yaml.YAMLError as exc:
        return None, [Finding("error", path, f"invalid YAML frontmatter: {exc}")]
    if not isinstance(metadata, dict):
        return None, [Finding("error", path, "frontmatter must be a YAML mapping")]
    return Document(path, metadata, match.group("body")), []


def validate_actor_event(value: Any, field: str, path: Path) -> list[Finding]:
    if not isinstance(value, dict):
        return [Finding("error", path, f"{field} entries must be mappings")]

    findings: list[Finding] = []
    actor = value.get("by")
    if not isinstance(actor, str) or not actor.strip():
        findings.append(Finding("error", path, f"{field}.by must be non-empty"))
    if field == "verified" and "at" not in value:
        findings.append(Finding("error", path, "verified.at is required"))
    if "at" in value and not parse_iso8601(value["at"]):
        findings.append(Finding("error", path, f"{field}.at must be an ISO-8601 timestamp"))
    return findings


def validate_metadata(document: Document) -> list[Finding]:
    metadata = document.metadata
    findings: list[Finding] = []

    artifact_type = metadata.get("type")
    if not isinstance(artifact_type, str) or not artifact_type.strip():
        findings.append(Finding("error", document.path, "type must be a non-empty string"))

    status = metadata.get("status")
    if status is not None and status not in OKF_STATUSES:
        findings.append(
            Finding("error", document.path, f"status must be one of {sorted(OKF_STATUSES)}")
        )

    if "generated" in metadata:
        findings.extend(validate_actor_event(metadata["generated"], "generated", document.path))

    if "verified" in metadata:
        verified = metadata["verified"]
        events = verified if isinstance(verified, list) else [verified]
        for event in events:
            findings.extend(validate_actor_event(event, "verified", document.path))

    lifecycle_dates = {field: metadata.get(field) for field in ("created", "updated")}
    if any(value is not None for value in lifecycle_dates.values()):
        for field, value in lifecycle_dates.items():
            if value is None:
                findings.append(Finding("error", document.path, f"{field} is required when lifecycle dates are used"))
            elif not parse_calendar_date(value):
                findings.append(Finding("error", document.path, f"{field} must use YYYY-MM-DD format"))

    return findings


def validate_links(document: Document, bundle_root: Path) -> list[Finding]:
    findings: list[Finding] = []
    root = bundle_root.resolve()
    for raw_target in MARKDOWN_LINK_RE.findall(document.body):
        target_text = raw_target.strip().split("#", 1)[0]
        if not target_text or re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target_text):
            continue
        target = root / target_text.lstrip("/") if target_text.startswith("/") else document.path.parent / target_text
        try:
            resolved = target.resolve()
            resolved.relative_to(root)
        except ValueError:
            findings.append(Finding("error", document.path, f"link escapes bundle: {raw_target}"))
            continue
        if not resolved.exists():
            findings.append(Finding("warning", document.path, f"broken local link: {raw_target}"))
    return findings


def iter_markdown_files(root: Path) -> Iterable[Path]:
    return sorted(path for path in root.rglob("*.md") if path.is_file())


def validate_bundle(bundle_root: Path) -> list[Finding]:
    findings: list[Finding] = []
    for path in iter_markdown_files(bundle_root):
        reserved = path.name in RESERVED_NAMES
        document, parse_findings = parse_document(path, require_frontmatter=not reserved)
        findings.extend(parse_findings)
        if document is None:
            continue

        if not reserved:
            findings.extend(validate_metadata(document))
        elif path.name == "index.md" and path.parent == bundle_root:
            version = document.metadata.get("okf_version") if document.metadata else None
            if version is not None and str(version) != "0.2":
                findings.append(Finding("error", path, "root index okf_version must be '0.2'"))
        elif document.metadata:
            findings.append(
                Finding("error", path, "only the bundle-root index.md may have frontmatter")
            )

        findings.extend(validate_links(document, bundle_root))
    return findings


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("bundle_root", type=Path, help="OKF knowledge bundle root")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if not args.bundle_root.is_dir():
        print(f"ERROR: bundle root is not a directory: {args.bundle_root}", file=sys.stderr)
        return 2

    findings = validate_bundle(args.bundle_root)
    for finding in findings:
        print(f"{finding.level.upper()}: {finding.path}: {finding.message}")

    errors = sum(finding.level == "error" for finding in findings)
    warnings = sum(finding.level == "warning" for finding in findings)
    if errors:
        print(f"FAILED: {errors} error(s), {warnings} warning(s)")
        return 1
    print(f"OK: no errors, {warnings} warning(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
