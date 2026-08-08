#!/usr/bin/env python3
"""Inspect a destination path before an agent changes durable files."""

from __future__ import annotations

import argparse
import os
import re
import sys
import tempfile
from dataclasses import dataclass, field
from pathlib import Path


VARIABLE_PATTERN = re.compile(
    r"(?<!\\)\$(?:[A-Za-z_][A-Za-z0-9_]*|\{[^}]+\})|%[A-Za-z_][A-Za-z0-9_]*%"
)
BACKTICK_PATTERN = re.compile(r"`([^`]+)`")


@dataclass
class Result:
    requested: str
    expanded_absolute: Path
    parent_exists: bool
    target_exists: bool
    governing_agents: Path | None
    established_equivalent_roots: list[Path] = field(default_factory=list)
    equivalent_candidates: list[Path] = field(default_factory=list)
    unresolved_variables: list[str] = field(default_factory=list)
    symlinks: list[tuple[Path, Path]] = field(default_factory=list)
    findings: list[str] = field(default_factory=list)
    resolved_existing_path: Path | None = None

    @property
    def suspicious(self) -> bool:
        return bool(self.findings)


def lexical_absolute(value: str, cwd: Path) -> Path:
    expanded = os.path.expanduser(os.path.expandvars(value))
    if not os.path.isabs(expanded):
        expanded = os.path.join(str(cwd), expanded)
    return Path(os.path.abspath(os.path.normpath(expanded)))


def existing_ancestor(path: Path) -> Path:
    candidate = path
    while not candidate.exists() and candidate != candidate.parent:
        candidate = candidate.parent
    return candidate


def nearest_agents(path: Path) -> Path | None:
    start = path if path.is_dir() else path.parent
    start = existing_ancestor(start)
    for directory in (start, *start.parents):
        anchor = directory / "AGENTS.md"
        if anchor.is_file():
            return anchor
    return None


def symlinks_in_existing_chain(path: Path) -> list[tuple[Path, Path]]:
    links: list[tuple[Path, Path]] = []
    current = Path(path.anchor)
    for part in path.parts[1:]:
        current = current / part
        if not os.path.lexists(current):
            break
        if current.is_symlink():
            links.append((current, current.resolve(strict=False)))
    return links


def discover_atlas(cwd: Path) -> Path | None:
    for directory in (cwd, *cwd.parents):
        atlas = directory / "DIRECTORY_ATLAS.md"
        if atlas.is_file():
            return atlas
    return None


def roots_from_atlas(atlas: Path | None) -> list[Path]:
    if atlas is None or not atlas.is_file():
        return []
    roots: list[Path] = []
    for raw in BACKTICK_PATTERN.findall(atlas.read_text(encoding="utf-8")):
        if any(marker in raw for marker in ("*", "REPLACE_", "credentials", "secrets")):
            continue
        candidate = lexical_absolute(raw, atlas.parent)
        if candidate.is_dir() and candidate not in roots:
            roots.append(candidate)
    return roots


def is_within(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


def analyze(
    requested: str,
    cwd: Path,
    atlas: Path | None = None,
    verify_existing: bool = False,
) -> Result:
    home = Path.home().resolve()
    identity_segment = home.name
    expanded_variables = os.path.expandvars(requested)
    unresolved = sorted(set(VARIABLE_PATTERN.findall(expanded_variables)))
    expanded = lexical_absolute(requested, cwd)
    roots = roots_from_atlas(atlas if atlas is not None else discover_atlas(cwd))
    result = Result(
        requested=requested,
        expanded_absolute=expanded,
        parent_exists=expanded.parent.is_dir(),
        target_exists=expanded.exists(),
        governing_agents=nearest_agents(expanded),
        unresolved_variables=unresolved,
        resolved_existing_path=expanded.resolve(strict=False),
    )
    result.established_equivalent_roots = [root for root in roots if is_within(expanded, root)]

    duplicated_home_prefix = home / identity_segment
    if is_within(expanded, duplicated_home_prefix):
        corrected = home / expanded.relative_to(duplicated_home_prefix)
        result.findings.append(
            f"duplicated home/username segment: {duplicated_home_prefix}"
        )
        result.equivalent_candidates.append(corrected)
        for root in roots:
            if is_within(corrected, root) and root not in result.established_equivalent_roots:
                result.established_equivalent_roots.append(root)

    parts = [part for part in expanded.parts if part != expanded.anchor]
    for left, right in zip(parts, parts[1:]):
        if left == right:
            finding = f"adjacent duplicated path segment: {left}/{right}"
            if finding not in result.findings:
                result.findings.append(finding)

    if unresolved:
        result.findings.append("unresolved variable reference(s) remain in the requested path")
    if not result.parent_exists:
        result.findings.append("immediate parent directory does not exist")

    result.symlinks = symlinks_in_existing_chain(expanded)
    if result.symlinks:
        result.findings.append("existing ancestor chain contains one or more symlinks")

    if verify_existing and not result.target_exists:
        result.findings.append("post-change verification target does not exist")

    return result


def print_result(result: Result, atlas: Path | None, verify_existing: bool) -> None:
    print(f"requested path: {result.requested}")
    print(f"expanded absolute path: {result.expanded_absolute}")
    print(f"immediate parent exists: {'yes' if result.parent_exists else 'no'}")
    print(f"target exists: {'yes' if result.target_exists else 'no'}")
    print(
        "nearest governing AGENTS.md: "
        + (str(result.governing_agents) if result.governing_agents else "none found")
    )
    print(f"directory atlas: {atlas if atlas else 'none found'}")
    print("established equivalent roots:")
    if result.established_equivalent_roots:
        for root in result.established_equivalent_roots:
            print(f"  - {root}")
    else:
        print("  - none found")
    print("equivalent destination candidates:")
    if result.equivalent_candidates:
        for candidate in result.equivalent_candidates:
            print(f"  - {candidate}")
    else:
        print("  - none")
    print("unresolved variables:")
    if result.unresolved_variables:
        for variable in result.unresolved_variables:
            print(f"  - {variable}")
    else:
        print("  - none")
    print("symlinks in existing ancestor chain:")
    if result.symlinks:
        for source, target in result.symlinks:
            print(f"  - {source} -> {target}")
    else:
        print("  - none")
    if verify_existing:
        print(f"resolved verification path: {result.resolved_existing_path}")
    print("findings:")
    if result.findings:
        for finding in result.findings:
            print(f"  - {finding}")
        print("status: SUSPICIOUS, confirmation required before acting")
    else:
        print("  - none")
        print("status: CLEAR")


def self_test() -> int:
    checks = 0
    home = Path.home().resolve()
    identity_segment = home.name

    duplicated = analyze(f"~/{identity_segment}/example-project", Path.cwd())
    assert duplicated.expanded_absolute == home / identity_segment / "example-project"
    assert any("duplicated home/username" in item for item in duplicated.findings)
    assert home / "example-project" in duplicated.equivalent_candidates
    checks += 1

    unresolved = analyze("$PATH_PREFLIGHT_UNDEFINED_FOR_TEST/project", Path.cwd())
    assert unresolved.unresolved_variables and unresolved.suspicious
    checks += 1

    previous = os.environ.get("PATH_PREFLIGHT_RESOLVED_FOR_TEST")
    try:
        os.environ["PATH_PREFLIGHT_RESOLVED_FOR_TEST"] = str(Path.cwd())
        resolved_variable = analyze("$PATH_PREFLIGHT_RESOLVED_FOR_TEST/project", Path.cwd())
        assert not resolved_variable.unresolved_variables
    finally:
        if previous is None:
            os.environ.pop("PATH_PREFLIGHT_RESOLVED_FOR_TEST", None)
        else:
            os.environ["PATH_PREFLIGHT_RESOLVED_FOR_TEST"] = previous
    checks += 1

    with tempfile.TemporaryDirectory(prefix="path-preflight-") as temp:
        fixture = Path(temp)
        projects = fixture / "projects"
        projects.mkdir()
        (fixture / "AGENTS.md").write_text("# Fixture rules\n", encoding="utf-8")
        atlas = fixture / "DIRECTORY_ATLAS.md"
        atlas.write_text(
            "# Directory Atlas\n\n| Path | Use |\n|---|---|\n"
            "| `projects/` | Project work |\n",
            encoding="utf-8",
        )

        safe_target = projects / "future-project"
        safe = analyze(str(safe_target), fixture, atlas)
        assert safe.parent_exists and not safe.suspicious
        assert projects in safe.established_equivalent_roots
        assert safe.governing_agents == fixture / "AGENTS.md"
        checks += 1

        missing = analyze(str(fixture / "missing-parent" / "future-project"), fixture, atlas)
        assert not missing.parent_exists and missing.suspicious
        checks += 1

        link = fixture / "linked-projects"
        link.symlink_to(projects, target_is_directory=True)
        linked = analyze(str(link / "future-project"), fixture, atlas)
        assert linked.symlinks and linked.suspicious
        checks += 1

        relative = analyze("projects/future-project", fixture, atlas)
        assert relative.expanded_absolute == safe_target and not relative.suspicious
        checks += 1

        verified = analyze(str(projects), fixture, atlas, verify_existing=True)
        assert verified.target_exists and not verified.suspicious
        checks += 1

    print(f"Path Resolution Preflight self-test passed: {checks} fixtures checked.")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Inspect how a durable destination resolves without changing it."
    )
    parser.add_argument("path", nargs="?", help="requested destination path")
    parser.add_argument("--atlas", type=Path, help="DIRECTORY_ATLAS.md to consult")
    parser.add_argument(
        "--verify-existing",
        action="store_true",
        help="require the destination to exist after a filesystem change",
    )
    parser.add_argument("--self-test", action="store_true", help="run temporary fixtures")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.self_test:
        return self_test()
    if not args.path:
        print("error: path is required unless --self-test is used", file=sys.stderr)
        return 1
    atlas = args.atlas.resolve() if args.atlas else discover_atlas(Path.cwd())
    result = analyze(args.path, Path.cwd(), atlas, args.verify_existing)
    print_result(result, atlas, args.verify_existing)
    return 2 if result.suspicious else 0


if __name__ == "__main__":
    raise SystemExit(main())
