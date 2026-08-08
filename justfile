# Beginner's Guide to Agent Organization repo tasks

default:
    just --list

# Show available repo commands.
help:
    just --list

# Open command menu.
menu:
    @if command -v justx >/dev/null 2>&1; then justx; else just --list; fi

# Validate package structure, links, and public-content risks.
validate:
    python3 validate-agent-organization.py .
    python3 -m py_compile validate-agent-organization.py
    python3 -m py_compile make-release-zip.py
    python3 -m py_compile starter-kit/path-resolution-preflight.py
    rm -rf __pycache__
    rm -rf starter-kit/__pycache__

# Run safe temporary fixtures for Path Resolution Preflight.
path-preflight-test:
    python3 starter-kit/path-resolution-preflight.py --self-test

# Inspect one requested destination without changing it.
path-preflight path:
    python3 starter-kit/path-resolution-preflight.py --atlas starter-kit/DIRECTORY_ATLAS.md {{quote(path)}}

# Verify one existing absolute destination after a filesystem change.
path-preflight-verify path:
    python3 starter-kit/path-resolution-preflight.py --atlas starter-kit/DIRECTORY_ATLAS.md --verify-existing {{quote(path)}}

# Build downloadable zip package.
package:
    python3 make-release-zip.py --version v0.1.1

# Quick context check for agents before editing.
agent-preflight:
    @echo "Repo: beginners-guide-to-agent-organization"
    @if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then git status --short; else echo "No git history (distributed as zip)."; fi
    @find . -maxdepth 2 -type f | sort

# Verification after edits.
agent-verify:
    @if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then git diff --check; else echo "No git history (distributed as zip); running validation only."; fi
    just validate
    just path-preflight-test

# Show current repo status.
agent-status:
    @if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then git status --short; git log --oneline -5; else echo "No git history (distributed as zip)."; fi
