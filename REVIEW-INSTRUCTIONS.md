# Review Instructions

Use this file to review the package before publishing or turning it into a release.

## Package Location

```text
<package-root>
```

## Review Goal

Decide whether this package is clear enough for a non-technical user to hand to an AI agent and get a useful organization system:

- folder-placement rules
- a `DIRECTORY_ATLAS.md`
- `AGENTS.md` placement instructions
- memory rules
- copy-paste prompts
- a simple validation path

## Quick Verification

From the package root, run:

```bash
just --list
just agent-verify
just package
```

If `just` is not installed, run:

```bash
python3 validate-agent-organization.py .
python3 -m py_compile validate-agent-organization.py
```

## Human Review Path

Read these first:

1. `README.md`
2. `runbook/quick-start-card.md`
3. `runbook/agent-organization-runbook.md`

Then review the copy-paste workflow:

1. `prompts/01-map-my-current-folders.md`
2. `prompts/02-create-directory-atlas.md`
3. `prompts/03-add-agent-placement-rules.md`
4. `prompts/04-review-memory-bloat.md`
5. `prompts/05-before-you-create-a-folder.md`

Then review the reusable files:

1. `templates/DIRECTORY_ATLAS-template.md`
2. `templates/AGENTS-placement-rules-template.md`
3. `templates/MEMORY-rules-template.md`
4. `starter-kit/DIRECTORY_ATLAS.md`
5. `starter-kit/AGENTS-placement-rules.md`
6. `starter-kit/MEMORY-rules.md`

## Review Questions

1. Could a beginner understand what problem this solves?
2. Are the prompts safe enough for a normal user to give an agent?
3. Does the package make `prompts/` feel central, not optional?
4. Does it clearly tell the agent to search existing homes before creating folders?
5. Does it prevent memory from becoming a dumping ground?
6. Does it protect sensitive folders without over-explaining private contents?
7. Is anything too technical, too vague, or too long?
8. Is anything missing before this becomes a public repo?

## Suggested Second-Agent Review Prompt

```text
Please review this package as a public beginner runbook:

<package-root>

Review goal:
Can a non-technical user hand this folder to an AI agent and get clear folder-placement rules, memory rules, and prompts that reduce folder sprawl?

Please check:
1. README clarity
2. quick-start usability
3. full runbook flow
4. prompt safety and completeness
5. template usefulness
6. whether prompts/ feels like a first-class directory
7. whether anything exposes internal/private details
8. whether any file should be added, renamed, shortened, or rewritten

Run:
just --list
just agent-verify
just package

Return findings first, ordered by severity, with file paths and exact suggested changes.
```
