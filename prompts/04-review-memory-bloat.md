# Prompt 04: Review Memory Bloat

Copy this into your agent after the atlas and placement rules exist.

```text
Please review how memory should work in this workspace without exposing private memory contents.

Goal:
Make sure important information is written in the right place and long-term memory does not become a dumping ground.

Rules:
- Do not paste private memory contents into the chat unless I ask for a specific item.
- Do not delete or rewrite memory automatically.
- Before any deletion, confirm a backup or version history exists.
- Archive uncertain material rather than permanently deleting it.
- Verify that moved information exists at its destination before removing the original.
- For each item found, classify it as keep, move, archive, or delete using this rubric:
  - Keep: short durable facts the agent needs almost every session.
  - Move: longer reference material that belongs in a knowledge base or project docs.
  - Archive: material that may be useful but should not be in active memory or project files.
  - Delete: one-time noise, confirmed duplicates, or outdated status. Delete only after review.
- If unsure whether something is safe to delete, archive it instead.
- For duplicates with different wording, compare them, preserve unique information in the correct destination, and only then propose removing the redundant copy.
- Summarize categories and placement rules.
- Separate long-term memory, daily notes, project files, reports, and temporary scratch notes.

Please return:
1. Where durable long-term memory appears to live.
2. Where daily or session notes appear to live.
3. Where project-specific notes should live.
4. What belongs in long-term memory.
5. What belongs in daily notes.
6. What belongs in project docs instead of memory.
7. What should not be remembered at all.
8. An inventory of items found, classified as keep, move, archive, or delete.
9. A short proposed memory-rules section I can add to AGENTS.md, MEMORY-rules.md, or another memory guide.

Do not make edits until you show me the proposal.
```
