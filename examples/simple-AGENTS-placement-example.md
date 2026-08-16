# Simple AGENTS Placement Example

This example shows the kind of placement section you can add to an `AGENTS.md` file.

```markdown
## Directory Placement

Before creating durable files or folders, consult `DIRECTORY_ATLAS.md`.

Search existing homes before creating new folders.

Prefer established structure.

Ask before creating a new top-level durable folder if the destination is unclear.

Treat memory, credentials, backups, browser profiles, runtime folders, caches, and private data as protected areas.

Protected area boundaries:
- `~/.ssh/` — SSH keys. Do not read, copy, or summarize.
- `~/.env` files — API keys and secrets. Do not read, copy, or summarize.
- `credentials/` — password stores and account exports. Do not inspect.
- `customers/` — customer personal data. Do not inspect without explicit approval.
- `financial/` — financial records and account numbers. Do not inspect.
- `browser-profiles/` — browser session data. Do not read.

If a protected area sits inside an approved folder, its protection applies to all files and subfolders inside it. The agent must ask before accessing any protected area.

If something matters beyond the current chat, write it to the right file instead of relying only on chat memory.
```

