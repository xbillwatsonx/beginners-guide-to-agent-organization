#!/usr/bin/env python3
"""Build a reviewed release zip from tracked public files only."""

from __future__ import annotations

import argparse
import hashlib
import re
import subprocess
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


VERSION_PATTERN = re.compile(r"^v\d+\.\d+\.\d+$")
EXCLUDED_FILES = {
    Path("IMPLEMENTATION_PLAN.md"),
    Path("REVIEW-INSTRUCTIONS.md"),
}


def run(command: list[str], root: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        command,
        cwd=root,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


def require_clean_git_tree(root: Path) -> list[str]:
    result = run(["git", "status", "--porcelain=v1", "--untracked-files=all"], root)
    if result.returncode != 0:
        return [f"git status failed: {result.stderr.strip() or result.stdout.strip()}"]
    if result.stdout.strip():
        return [
            "release tree is dirty or has untracked files; commit, stash, or remove them before packaging",
            result.stdout.rstrip(),
        ]
    return []


def tracked_public_files(root: Path) -> tuple[list[Path], list[str]]:
    result = subprocess.run(
        ["git", "ls-files", "-z"],
        cwd=root,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if result.returncode != 0:
        return [], [f"git ls-files failed: {result.stderr.decode(errors='replace').strip()}"]
    paths: list[Path] = []
    for raw in result.stdout.split(b"\0"):
        if not raw:
            continue
        relative = Path(raw.decode("utf-8"))
        path = root / relative
        if path.is_file() and relative not in EXCLUDED_FILES:
            paths.append(relative)
    return sorted(paths), []


def validate_package(root: Path) -> list[str]:
    validator = root / "validate-agent-organization.py"
    result = run(["python3", str(validator), str(root)], root)
    if result.returncode != 0:
        return [
            "validation failed before packaging",
            result.stdout.rstrip(),
            result.stderr.rstrip(),
        ]
    return []


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def build(root: Path, version: str) -> tuple[Path, Path, list[str]]:
    if not VERSION_PATTERN.fullmatch(version):
        return Path(), Path(), ["version must use vMAJOR.MINOR.PATCH format"]
    errors = require_clean_git_tree(root)
    if errors:
        return Path(), Path(), errors
    errors = validate_package(root)
    if errors:
        return Path(), Path(), errors
    files, errors = tracked_public_files(root)
    if errors:
        return Path(), Path(), errors
    if not files:
        return Path(), Path(), ["no tracked public files found; refusing to build empty archive"]

    output_dir = root / "downloads"
    output_dir.mkdir(exist_ok=True)
    output = output_dir / f"beginners-guide-to-agent-organization-{version}.zip"
    checksum = output.with_suffix(output.suffix + ".sha256")
    for path in (output, checksum):
        if path.exists():
            path.unlink()

    with ZipFile(output, "w", compression=ZIP_DEFLATED) as archive:
        for relative in files:
            archive.write(root / relative, relative)

    checksum.write_text(f"{sha256_file(output)}  {output.name}\n", encoding="utf-8")
    return output, checksum, []


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--version", required=True, help="Release version, such as v0.1.1.")
    parser.add_argument("--root", default=".", help="Package root.")
    args = parser.parse_args()

    output, checksum, errors = build(Path(args.root).resolve(), args.version)
    if errors:
        print("Release package build failed:")
        for error in errors:
            if error:
                print(error)
        return 1
    print(output)
    print(checksum)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
