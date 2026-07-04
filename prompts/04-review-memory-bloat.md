# Prompt 04: Review Memory Bloat

Copy this into your agent after the atlas and placement rules exist.

```text
Please review how memory should work in this workspace without exposing private memory contents.

Goal:
Make sure important information is written in the right place and long-term memory does not become a dumping ground.

Rules:
- Do not paste private memory contents into the chat unless I ask for a specific item.
- Do not delete or rewrite memory automatically.
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
8. A short proposed MEMORY rules section I can add to AGENTS.md or a memory guide.

Do not make edits until you show me the proposal.
```

