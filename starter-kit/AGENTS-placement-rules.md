# Directory Placement And Organization

Before creating durable files or folders, consult `DIRECTORY_ATLAS.md`.

Search existing homes before creating new folders. Prefer established structure. Ask before creating a new top-level durable folder if the correct home is unclear.

Treat memory, credentials, backups, browser profiles, runtime folders, caches, generated outputs, and private data as protected areas.

If something matters beyond the current chat, write it to the right file instead of relying only on chat memory.

## Path Resolution Preflight

Before creating, moving, copying, or consolidating durable files or folders:

1. Run `python3 path-resolution-preflight.py '<requested-path>'`.
2. Inspect the expanded absolute path, immediate parent, nearest `AGENTS.md`, established atlas roots, duplicated segments, unresolved variables, and symlinks.
3. If the helper reports `SUSPICIOUS` or exits with status `2`, stop and ask the user to confirm the exact absolute destination.
4. After the filesystem change, run `python3 path-resolution-preflight.py --verify-existing '<absolute-destination>'` and report the verified absolute path.

Keep paths quoted so the helper sees the original `~` or variable instead of receiving a value already expanded by the shell.
