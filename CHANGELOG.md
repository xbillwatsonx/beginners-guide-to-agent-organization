# Changelog

## v0.1.1 - 2026-08-08

- Added a portable, dependency-free Path Resolution Preflight helper with eight safe fixtures.
- Added stop-and-confirm behavior for duplicated segments, unresolved variables, missing parents, and symlinked ancestors.
- Added post-change absolute-destination verification and beginner instructions across the runbook, quick-start card, prompt, templates, and starter kit.
- Added `just` recipes and validator coverage for the new helper while retaining the existing package exclusions.
- Replaced recursive release packaging with a tracked-file-only builder and SHA-256 checksum output.

## v0.1.0 - 2026-07-04

- Created the first public-ready package structure.
- Added a beginner README, full runbook, quick-start card, and user-facing build plan.
- Added five copy-paste prompts for folder mapping, atlas creation, AGENTS placement rules, memory review, and new-folder approval.
- Added templates and starter-kit files for `DIRECTORY_ATLAS.md`, `AGENTS.md` placement rules, and memory rules.
- Added simple examples for atlas, AGENTS placement, and memory rules.
- Added a dependency-free validator and standard `justfile` commands for verification and packaging.
