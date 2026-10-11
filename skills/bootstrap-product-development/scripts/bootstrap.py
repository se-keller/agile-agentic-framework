#!/usr/bin/env python3
"""Create a product workspace beside a versioned AAF framework checkout."""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import tempfile
import unicodedata
from datetime import datetime, timezone
from pathlib import Path


TOKEN_RE = re.compile(r"\{\{([A-Z_]+)\}\}")
GERMAN_TRANSLITERATION = str.maketrans(
    {"ä": "ae", "ö": "oe", "ü": "ue", "Ä": "Ae", "Ö": "Oe", "Ü": "Ue", "ß": "ss"}
)
FRAMEWORK_DIRECTORY = "agile-agentic-framework"


def slugify(value: str) -> str:
    transliterated = value.translate(GERMAN_TRANSLITERATION)
    ascii_value = unicodedata.normalize("NFKD", transliterated).encode("ascii", "ignore").decode()
    slug = re.sub(r"[^a-z0-9]+", "-", ascii_value.lower()).strip("-")
    if not slug:
        raise ValueError("product name must contain at least one ASCII-transliterable letter or digit")
    return slug


def replace_tokens(root: Path, values: dict[str, str]) -> None:
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue

        def replacement(match: re.Match[str]) -> str:
            token = match.group(1)
            if token not in values:
                raise ValueError(f"unknown template token {token} in {path}")
            return values[token]

        path.write_text(TOKEN_RE.sub(replacement, content), encoding="utf-8")


def inside_git_worktree(path: Path) -> bool:
    result = subprocess.run(
        ["git", "-C", str(path), "rev-parse", "--is-inside-work-tree"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    return result.returncode == 0


def git_output(*args: str) -> str:
    """Return Git output or present a concise bootstrap error."""
    result = subprocess.run(
        ["git", *args],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if result.returncode:
        detail = result.stderr.strip() or result.stdout.strip()
        raise SystemExit(f"ERROR: git {' '.join(args)} failed: {detail}")
    return result.stdout.strip()


def is_git_checkout(path: Path) -> bool:
    result = subprocess.run(
        ["git", "-C", str(path), "rev-parse", "--show-toplevel"],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    return result.returncode == 0 and Path(result.stdout.strip()).resolve() == path.resolve()


def current_framework_root() -> Path:
    return Path(__file__).resolve().parents[3]


def public_repository_name(source: Path) -> str:
    """Prefer the origin URL, without copying HTTP credentials into a product."""
    result = subprocess.run(
        ["git", "-C", str(source), "remote", "get-url", "origin"],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    repository = result.stdout.strip() if result.returncode == 0 else str(source)
    return re.sub(r"^(https?://)[^/@]+@", r"\1", repository)


def ensure_framework_checkout(
    parent: Path,
    source: Path,
    requested_ref: str | None,
) -> tuple[Path, str]:
    """Reuse or create the sibling framework checkout and return its exact revision."""
    checkout = parent / FRAMEWORK_DIRECTORY
    if checkout.exists():
        if not checkout.is_dir() or not is_git_checkout(checkout):
            raise SystemExit(f"ERROR: framework target is not a Git checkout: {checkout}")
        if requested_ref is not None:
            expected_revision = git_output("-C", str(checkout), "rev-parse", f"{requested_ref}^{{commit}}")
            actual_revision = git_output("-C", str(checkout), "rev-parse", "HEAD")
            if actual_revision != expected_revision:
                raise SystemExit(
                    "ERROR: existing framework checkout does not match "
                    f"--framework-ref {requested_ref}: {checkout}"
                )
        return checkout, git_output("-C", str(checkout), "rev-parse", "HEAD")

    ref = requested_ref or git_output("-C", str(source), "rev-parse", "HEAD")
    git_output("clone", "--no-checkout", str(source), str(checkout))
    git_output("-C", str(checkout), "checkout", "--detach", ref)
    return checkout, git_output("-C", str(checkout), "rev-parse", "HEAD")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("product_name", help="human-readable product name")
    parser.add_argument("--parent", type=Path, default=Path.cwd(), help="parent directory")
    parser.add_argument(
        "--framework-source",
        type=Path,
        help="Git checkout to clone as the sibling framework (defaults to this checkout)",
    )
    parser.add_argument(
        "--framework-ref",
        help="commit, tag, or branch to check out; required to match an existing framework checkout",
    )
    parser.add_argument("--no-git", action="store_true", help="do not initialize a Git repository")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    parent = args.parent.expanduser().resolve()
    if not parent.is_dir():
        raise SystemExit(f"ERROR: parent directory does not exist: {parent}")

    try:
        product_slug = slugify(args.product_name)
    except ValueError as exc:
        raise SystemExit(f"ERROR: {exc}") from exc
    target = parent / f"product-development-{product_slug}"
    if target.exists():
        raise SystemExit(f"ERROR: refusing to overwrite existing target: {target}")

    framework_source = (args.framework_source or current_framework_root()).expanduser().resolve()
    if not framework_source.is_dir() or not is_git_checkout(framework_source):
        raise SystemExit(f"ERROR: framework source is not a Git checkout: {framework_source}")
    framework_existed = (parent / FRAMEWORK_DIRECTORY).exists()
    framework_checkout, framework_revision = ensure_framework_checkout(
        parent, framework_source, args.framework_ref
    )
    framework_repository = public_repository_name(
        framework_checkout if framework_existed else framework_source
    )

    skeleton = Path(__file__).resolve().parent.parent / "assets" / "product-development-skeleton"
    generated_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    generated_date = generated_at[:10]
    initialized_git = False
    with tempfile.TemporaryDirectory(prefix=f".{target.name}-bootstrap-", dir=parent) as temp_dir:
        staging = Path(temp_dir) / target.name
        shutil.copytree(
            skeleton,
            staging,
            ignore=shutil.ignore_patterns(".DS_Store", "__pycache__", "*.pyc"),
        )
        (staging / ".aafe" / "agents").mkdir()
        (staging / ".aafe" / "skills").mkdir()
        (staging / "artefacts" / "product-backlog" / "items").mkdir()
        replace_tokens(
            staging,
            {
                "PRODUCT_NAME": args.product_name,
                "PRODUCT_SLUG": product_slug,
                "GENERATED_AT": generated_at,
                "GENERATED_DATE": generated_date,
                "FRAMEWORK_DIRECTORY": framework_checkout.name,
                "FRAMEWORK_REPOSITORY": framework_repository,
                "FRAMEWORK_REVISION": framework_revision,
            },
        )

        if not args.no_git and not inside_git_worktree(parent):
            subprocess.run(["git", "init", str(staging)], check=True, stdout=subprocess.DEVNULL)
            initialized_git = True

        staging.rename(target)

    print(f"Created {target}")
    print(f"Framework checkout: {framework_checkout} ({framework_revision})")
    print(f"Git initialized: {'yes' if initialized_git else 'no (already nested or disabled)'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
