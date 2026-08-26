#!/usr/bin/env python3
"""Run the inexpensive framework checks required before every commit."""

from __future__ import annotations

import re
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
LOCAL_LINK = re.compile(r"\[[^]]*\]\(([^)#]+)(?:#[^)]+)?\)")
PLACEHOLDER = re.compile(r"\{\{|\}\}|<PRODUCT|TODO_PLACEHOLDER")


def run(*args: str, cwd: Path = ROOT) -> str:
    result = subprocess.run(
        args,
        cwd=cwd,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return result.stdout


def repository_files() -> list[Path]:
    output = run("git", "ls-files", "--cached", "--others", "--exclude-standard", "-z")
    return [ROOT / item for item in output.split("\0") if item]


def check_yaml() -> None:
    for path in repository_files():
        if path.suffix == ".yaml":
            with path.open(encoding="utf-8") as stream:
                yaml.safe_load(stream)


def check_local_links() -> None:
    missing: list[str] = []
    for path in repository_files():
        if path.suffix != ".md" or path.name == "SPEC.md":
            continue
        for target in LOCAL_LINK.findall(path.read_text(encoding="utf-8")):
            if "://" in target or target.startswith(("mailto:", "/")):
                continue
            if not (path.parent / target).resolve().exists():
                missing.append(f"{path.relative_to(ROOT)}: {target}")
    if missing:
        raise RuntimeError("Missing local Markdown links:\n" + "\n".join(missing))


def check_bootstrap() -> None:
    with tempfile.TemporaryDirectory(prefix="aaf-commit-check-") as parent:
        run(
            sys.executable,
            "skills/bootstrap-product-development/scripts/bootstrap.py",
            "Commit Check",
            "--parent",
            parent,
            "--no-git",
        )
        workspace = Path(parent) / "product-development-commit-check"
        run(
            sys.executable,
            "skills/okf/scripts/validate_okf.py",
            str(workspace / "artefacts"),
        )
        for path in workspace.rglob("*"):
            if path.is_file() and PLACEHOLDER.search(path.read_text(encoding="utf-8")):
                raise RuntimeError(f"Unresolved placeholder in {path.relative_to(workspace)}")


def check_documentation() -> None:
    documentation = ROOT / "docs"
    if documentation.is_dir():
        run(
            sys.executable,
            "skills/okf/scripts/validate_okf.py",
            str(documentation),
        )


def main() -> int:
    run("git", "diff", "HEAD", "--check")
    check_yaml()
    check_local_links()
    check_bootstrap()
    check_documentation()
    print("OK: diff, YAML, links, bootstrap, placeholders, and OKF validation")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
