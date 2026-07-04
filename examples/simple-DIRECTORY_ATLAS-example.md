# Simple Directory Atlas Example

This example shows the level of detail to aim for. It is not a full tree dump.

## Major Homes

| Path | Use when |
|------|----------|
| `PROJECTS/` | Active work that may continue over time. |
| `REPORTS/` | Finished summaries, reviews, audits, or handoffs. |
| `RESEARCH/` | Source gathering and research notes. |
| `REFERENCE/` | Durable knowledge the agent may reuse. |
| `memory/` | Daily notes and session continuity. |

## Protected

- `backups/` - do not reorganize without explicit approval.
- `.venv/` - runtime folder, not a durable knowledge home.
- browser profile folders - private runtime data.
- credentials or secrets - do not expose or summarize.

## New Folder Rule

If the agent wants to create a new durable folder, it must search existing homes first and ask when unclear.

