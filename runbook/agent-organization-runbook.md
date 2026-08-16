# Agent Organization Runbook

This runbook gives your AI agent enough context to walk you through where things belong on your system.

It is for people who have started using an agent and noticed messy folders, scattered notes, duplicate project homes, or confusing memory. The fix is not complicated. Your agent needs a map, a few rules, and a habit of checking before creating.

## The Big Idea

Agents work better when they have local rules.

A fresh agent may know how to read and write files, but it does not automatically know what your folders mean. It may treat every folder as equally important, or create a new folder because that seems easier than searching.

This runbook helps your agent guide you through a better pattern:

1. Inspect the existing workspace.
2. Identify the major homes.
3. Write a curated placement map.
4. Add rules that require the agent to use the map.
5. Protect sensitive areas.
6. Resolve and verify destinations before filesystem changes.
7. Keep memory small and useful.

## Terms

`DIRECTORY_ATLAS.md`
: A curated map of important folders and what belongs in them.

`AGENTS.md`
: A local instruction file that tells an agent how to behave in a workspace.

Durable file
: A file that should matter after the current chat is over.

Durable folder
: A folder that becomes a real home for ongoing work, not a temporary scratch space.

Protected area
: A folder that may exist, but should not be deeply summarized, copied, indexed, or exposed without a clear reason. The agent must ask before accessing any protected area.

## Step 1: Map The Current Workspace

Start with `prompts/01-map-my-current-folders.md`.

If the workspace feels overwhelming, do not try to map everything at once. Start with one area or two to three unclear folder decisions. For example: "Where should project notes go?" or "Is `projects-old` still active?" Resolve those first, then expand.

The agent should inspect folder names, nearby instruction files, and obvious project structure. It should not read private contents deeply. The goal is to understand the shape of the workspace, not to vacuum up data.

Good output from this step:

- likely project homes
- likely reference or research homes
- likely report/output homes
- memory or notes locations
- logs and generated-output areas
- protected areas
- unclear folders that need user confirmation

## Step 2: Create The Directory Atlas

Use `prompts/02-create-directory-atlas.md`.

The atlas should be short enough that a future agent will actually read it. It should not be a full tree dump. It should answer one question:

> Where should this kind of thing go?

Common atlas entries include:

- active projects
- reports
- research
- reference material
- templates
- logs
- memory
- generated outputs
- archives
- protected areas

## Step 3: Add Placement Rules To AGENTS.md

Use `prompts/03-add-agent-placement-rules.md`.

The key rule is simple:

> Before creating a durable file or folder, check the atlas, search existing homes, and ask if the destination is unclear.

The `AGENTS.md` rules should also say when to consult local instructions inside subfolders. If a project folder already has its own instructions, those local instructions should control that project.

## Step 4: Clean Up Memory Confusion

Use `prompts/04-review-memory-bloat.md`.

Memory bloat means long-term memory is carrying details that should live in daily notes, project files, archives, or nowhere at all. Symptoms include: memory is nearly full, the agent repeats outdated information, new facts have no room, project knowledge is mixed with behavior reminders, and retrieval becomes unreliable because the agent has to search through clutter.

Long-term memory should hold durable preferences, durable rules, important active projects, and recurring lessons. Daily notes or project notes should hold details that matter, but do not need to live forever in the agent's short hot memory.

Do not ask the agent to dump private memory into a public file. Ask it to summarize categories and rules.

### What to do with items found during review

For each item the agent finds during a memory review, use this decision rubric:

- **Keep**: short durable facts the agent needs almost every session (preferences, standing rules, active project pointers).
- **Move**: longer reference material that belongs in a knowledge base, project docs, or daily notes. Move it to the correct destination and leave a short pointer in memory if needed.
- **Archive**: material that may still be useful but should not be in memory or active project files. Move it to an archive folder. Keep it retrievable but out of the active path.
- **Delete**: one-time noise, duplicates where the authoritative copy is clearly identified, or outdated status after work is complete. Delete only after review and only when you are confident the information exists elsewhere or no longer matters.

If you are unsure whether something is safe to delete, archive it instead. When duplicates have different wording, compare them, preserve any unique information in the correct destination, and only then propose removing the redundant copy.

Before any deletion: confirm a backup or version history exists. Archive uncertain material rather than permanently deleting it. Verify that moved information actually exists at its destination before removing the original.

## Step 5: Use The Folder-Creation Gate

Use `prompts/05-before-you-create-a-folder.md` whenever the agent wants to create a new durable folder.

The agent should answer:

- What are you trying to store?
- Which existing folders did you check?
- Why do existing homes not fit?
- Is this temporary or durable?
- What name do you propose?
- What will belong there?
- What will not belong there?

If the answer is weak, do not create the folder yet.

## Step 6: Resolve The Exact Destination

Before the agent creates, moves, copies, or consolidates durable files, run the starter helper with the requested path quoted:

```bash
python3 path-resolution-preflight.py '<requested-path>'
```

Quoting matters. It lets the helper see shorthand such as `~` and variables before the shell changes them.

The helper reports:

- the requested path
- the expanded absolute path
- whether the immediate parent exists
- the nearest governing `AGENTS.md`
- established roots found in `DIRECTORY_ATLAS.md`
- likely equivalent destinations
- duplicated path segments
- unresolved variables
- symlinks in the existing ancestor chain

If it reports `SUSPICIOUS` or exits with status `2`, the agent must stop and ask the user to confirm the exact absolute destination.

If no `DIRECTORY_ATLAS.md` exists yet, the preflight helper prints `directory atlas: none found`. A missing atlas is not a clearance signal. The agent should stop and build or confirm the atlas before creating durable folders, not treat the absence as safe to proceed.

If the proposed path is outside every established atlas root, the agent should warn that the destination is outside the known homes and suggest the atlas-listed home instead. The preflight helper may report `status: CLEAR` in this case, but the agent must still apply the placement rule: check the atlas, search existing homes, and ask if the destination is unclear.

For example, when the current home folder already ends in `sam`, `~/sam/projects/site` adds a second `sam` segment. The repeated name is a warning that the user may have meant `~/projects/site`.

After the approved change, verify what actually exists:

```bash
python3 path-resolution-preflight.py --verify-existing '<absolute-destination>'
```

The agent should report that verified absolute destination, not only the shorthand from chat.

## What Not To Do

Do not create a giant atlas that lists every file.

Do not put secrets, private messages, browser profiles, credentials, customer data, financial records, backups, or runtime folders into examples.

Protected areas include: credentials and API keys, customer or client data, financial records and account numbers, browser profiles, password stores, SSH keys, medical records, legal documents, and private correspondence.

The agent must ask before accessing any protected area. It should not open, read, summarize, copy, or index protected contents without explicit user approval.

When a protected area sits inside an otherwise approved folder, the protection inherits to all subfolders and files inside it. The agent must treat the entire subtree as protected, not just the top-level folder name. For example, if `~/projects/client-work/` is protected and contains a `notes/` subfolder, `notes/` is also protected.

When listing protected areas in the atlas, include only the folder name, its purpose (e.g., "contains credentials, do not inspect"), and its boundary. Do not include filenames, file counts, content summaries, or any actual data from inside the protected area.

Do not create new top-level folders just because the agent likes clean categories.

Do not let the agent rewrite memory without explaining what changed and why.

Do not continue after a suspicious preflight until the exact absolute destination is confirmed.

Do not use the atlas as a replacement for common sense. It is a guide for placement decisions, not a command to move everything.

## Maintenance

Once a week or after a large project:

1. Ask the agent whether new durable homes were created.
2. Update `DIRECTORY_ATLAS.md` if a new home is now important.
3. Remove outdated placement notes.
4. Move temporary files to an archive or delete them only after review.
5. Trim long-term memory if it is carrying details that belong in project files.

## Review Checklist

You can trust the setup more when:

- future agents can find the right home without asking every time
- new folders are rare and justified
- important decisions are written to files, not only chat
- memory is smaller and clearer
- protected areas are named carefully
- the agent reports what it changed and where
- durable filesystem changes have a clear preflight and verified absolute destination
