---
purpose: agent file-placement and directory navigation map
scope: REPLACE_WITH_WORKSPACE_PATH
status: starter template
---

# Directory Atlas

Use this file before choosing where to save, create, move, archive, export, or organize durable files.

This is a curated placement map, not a full filesystem dump.

## Placement Order

1. Check this atlas.
2. Read the nearest relevant `AGENTS.md`.
3. Search existing folder names before creating a new durable folder.
4. Prefer established homes.
5. Ask before creating a new top-level durable folder if the right home is unclear.
6. Run the Path Resolution Preflight before acting on a new, shorthand, variable-containing, or ambiguous destination.

## Major Folder Homes

| Path | Use when | Notes |
|------|----------|-------|
| `PROJECTS/` | Active projects and implementation work. | Add your local meaning here. |
| `REFERENCE/` | Durable reference material. | Add your local meaning here. |
| `RESEARCH/` | Research in progress or source-backed research packets. | Add your local meaning here. |
| `REPORTS/` | Reviews, audits, summaries, and decision-ready outputs. | Add your local meaning here. |
| `TEMPLATES/` | Reusable starter files and examples. | Keep generic. |
| `memory/` | Daily or session memory notes. | Do not dump everything into long-term memory. |
| `logs/` | Raw logs and troubleshooting traces. | Do not treat raw logs as polished reports. |

## Protected Areas

Mention protected areas by purpose only. Do not deeply summarize private contents.

| Path | Boundary |
|------|----------|
| `MEMORY.md` | Curated durable memory. Update carefully. |
| credentials or secrets folders | Do not expose, copy, or summarize secrets. |
| backups | Do not reorganize without explicit approval. |
| browser profiles | Treat as private runtime data. |
| caches and generated folders | Do not use as durable homes. |

## New Durable Folder Rule

Before creating a new durable folder, the agent must:

1. explain what it is trying to store
2. list the existing homes it checked
3. explain why existing homes do not fit
4. propose the exact path
5. ask for approval when the folder is top-level, sensitive, or unclear

The agent must also compare the helper's expanded absolute path with the established homes in this atlas. A duplicated segment, unresolved variable, missing parent, unexpected symlink, or conflicting established root requires confirmation before acting.
