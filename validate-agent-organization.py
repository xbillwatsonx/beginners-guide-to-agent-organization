#!/usr/bin/env python3
"""Validate the beginner agent-organization runbook package."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REQUIRED_FILES = [
    "README.md",
    "CHANGELOG.md",
    "LICENSE",
    "justfile",
    "runbook/agent-organization-runbook.md",
    "runbook/build-your-agent-organization-system.md",
    "runbook/quick-start-card.md",
    "prompts/01-map-my-current-folders.md",
    "prompts/02-create-directory-atlas.md",
    "prompts/03-add-agent-placement-rules.md",
    "prompts/04-review-memory-bloat.md",
    "prompts/05-before-you-create-a-folder.md",
    "templates/DIRECTORY_ATLAS-template.md",
    "templates/AGENTS-placement-rules-template.md",
    "templates/MEMORY-rules-template.md",
    "starter-kit/DIRECTORY_ATLAS.md",
    "starter-kit/AGENTS-placement-rules.md",
    "starter-kit/MEMORY-rules.md",
    "examples/simple-DIRECTORY_ATLAS-example.md",
    "examples/simple-AGENTS-placement-example.md",
    "examples/simple-MEMORY-rules-example.md",
]

REQUIRED_DIRS = [
    "runbook",
    "prompts",
    "templates",
    "starter-kit",
    "examples",
]

PUBLIC_RISK_PATTERNS = [
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"sk-[A-Za-z0-9_-]{20,}"),
    re.compile(r"BEGIN (RSA|OPENSSH|EC) PRIVATE KEY"),
    re.compile(r"password\s*[:=]\s*\S{4,}", re.IGNORECASE),
    re.compile(r"api[_-]?key\s*[:=]", re.IGNORECASE),
]

INTERNAL_PATTERNS = [
    re.compile(r"\bOP-\d{3,}\b"),
    re.compile(r"/home/[A-Za-z0-9_-]+"),
    re.compile(r"\bPRIVATE_AGENT_NAME\b"),
    re.compile(r"\bPRIVATE_SYSTEM_NAME\b"),
]

LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def markdown_files(root: Path) -> list[Path]:
    return sorted(path for path in root.rglob("*.md") if ".git" not in path.parts)


def check_required(root: Path) -> list[str]:
    errors: list[str] = []
    for rel in REQUIRED_DIRS:
        if not (root / rel).is_dir():
            errors.append(f"missing directory: {rel}")
    for rel in REQUIRED_FILES:
        if not (root / rel).is_file():
            errors.append(f"missing file: {rel}")
    return errors


def check_public_risks(root: Path) -> list[str]:
    errors: list[str] = []
    for path in markdown_files(root):
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(root)
        for pattern in PUBLIC_RISK_PATTERNS:
            if pattern.search(text):
                errors.append(f"possible secret-like text in {rel}: {pattern.pattern}")
        for pattern in INTERNAL_PATTERNS:
            if pattern.search(text):
                errors.append(f"internal-only wording in public file {rel}: {pattern.pattern}")
    return sorted(set(errors))


def check_links(root: Path) -> list[str]:
    errors: list[str] = []
    for path in markdown_files(root):
        text = path.read_text(encoding="utf-8")
        for match in LINK_RE.finditer(text):
            target = match.group(1).strip()
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            if target.startswith("app://"):
                continue
            target = target.split("#", 1)[0]
            if not target:
                continue
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(root.resolve())
            except ValueError:
                errors.append(f"link escapes package in {path.relative_to(root)}: {target}")
                continue
            if not resolved.exists():
                errors.append(f"broken local link in {path.relative_to(root)}: {target}")
    return errors


def check_prompt_count(root: Path) -> list[str]:
    prompts = sorted((root / "prompts").glob("*.md")) if (root / "prompts").exists() else []
    if len(prompts) < 5:
        return [f"expected at least 5 prompts, found {len(prompts)}"]
    return []


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", default=".", help="package root")
    args = parser.parse_args()

    root = Path(args.path).resolve()
    errors: list[str] = []
    errors.extend(check_required(root))
    errors.extend(check_prompt_count(root))
    errors.extend(check_public_risks(root))
    errors.extend(check_links(root))

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Validation passed.")
    print(f"Package root: {root}")
    print(f"Markdown files: {len(markdown_files(root))}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
