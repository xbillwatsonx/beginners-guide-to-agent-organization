# Implementation Plan

## Goal

Create a beginner-friendly runbook package that helps non-technical users give their AI agent clear folder-placement rules, memory rules, and copy-paste prompts for staying organized over time.

## Package Name

`beginners-guide-to-agent-organization`

## Placement

The package belongs in `ready-to-distribute-runbook-packages/` because it is a public/distributable beginner runbook package.

## Deliverables

1. Public README that explains the problem, value, contents, and quick start.
2. Full runbook in `runbook/`.
3. One-page quick-start card in `runbook/`.
4. First-class `prompts/` directory with copy-paste prompts.
5. `templates/` directory with reusable starter text.
6. `starter-kit/` directory with copy-ready starter files.
7. `examples/` directory showing a simple finished setup.
8. Small dependency-free validator.
9. Standard package `justfile`.
10. Changelog and MIT license.

## Folder Plan

```text
beginners-guide-to-agent-organization/
  README.md
  IMPLEMENTATION_PLAN.md
  CHANGELOG.md
  LICENSE
  justfile
  validate-agent-organization.py
  runbook/
  prompts/
  templates/
  starter-kit/
  examples/
  downloads/
```

## Prompt Plan

- `01-map-my-current-folders.md` - ask the agent to inspect the current workspace safely.
- `02-create-directory-atlas.md` - ask the agent to draft or update `DIRECTORY_ATLAS.md`.
- `03-add-agent-placement-rules.md` - ask the agent to add placement rules to `AGENTS.md`.
- `04-review-memory-bloat.md` - ask the agent to review memory placement without dumping private data.
- `05-before-you-create-a-folder.md` - reusable gate before any new durable folder is created.

## Acceptance Criteria

- A beginner can follow the quick-start card without understanding Git or programming.
- The runbook explains where files go and when the agent must stop guessing.
- The prompts are copy-paste ready.
- The starter kit includes a usable atlas template and AGENTS placement rules.
- The validator passes on this package.
- The package avoids internal-only wording in public files.

## Review Plan

1. Run `just --list`.
2. Run `just agent-verify`.
3. Read `README.md`.
4. Read `runbook/quick-start-card.md`.
5. Read each prompt in `prompts/`.
6. Confirm the user could hand the folder to an agent without extra explanation.

