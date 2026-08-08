# Directory Placement And Organization

Before saving, creating, moving, archiving, exporting, or organizing durable files, consult `DIRECTORY_ATLAS.md`.

Use this order:

1. Read `DIRECTORY_ATLAS.md`.
2. Read the nearest relevant `AGENTS.md` in the area you plan to work.
3. Search existing homes before creating a new folder.
4. Prefer established structure.
5. Ask before creating a new top-level durable folder if the destination is unclear.

Do not deeply expose or index protected areas such as memory files, credentials, backups, browser profiles, runtime folders, caches, private messages, or generated/vendor folders.

If something matters beyond the current chat, write it to the right file instead of relying only on chat memory.

When a new durable folder is approved, update `DIRECTORY_ATLAS.md` if future agents will need to know about it.

## Path Resolution Preflight

Before creating, moving, copying, or consolidating durable files or folders:

1. Run `python3 path-resolution-preflight.py '<requested-path>'`.
2. Review the requested path, expanded absolute path, immediate parent, nearest governing `AGENTS.md`, established atlas roots, duplicated segments, unresolved variables, and symlinks.
3. Treat a `SUSPICIOUS` result or exit status `2` as a stop condition. Ask the user to confirm the exact absolute destination before acting.
4. After the change, run `python3 path-resolution-preflight.py --verify-existing '<absolute-destination>'` and report the verified absolute destination.

Quote the requested path so the shell does not expand it before the helper can inspect it.
