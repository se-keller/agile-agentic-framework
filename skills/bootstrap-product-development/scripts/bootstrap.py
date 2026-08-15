#!/usr/bin/env python3
"""Create a minimal product-development workspace from the bundled skeleton."""

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


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("product_name", help="human-readable product name")
    parser.add_argument("--parent", type=Path, default=Path.cwd(), help="parent directory")
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
            },
        )

        if not args.no_git and not inside_git_worktree(parent):
            subprocess.run(["git", "init", str(staging)], check=True, stdout=subprocess.DEVNULL)
            initialized_git = True

        staging.rename(target)

    print(f"Created {target}")
    print(f"Git initialized: {'yes' if initialized_git else 'no (already nested or disabled)'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
