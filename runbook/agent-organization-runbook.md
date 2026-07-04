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
6. Keep memory small and useful.

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
: A folder that may exist, but should not be deeply summarized, copied, indexed, or exposed without a clear reason.

## Step 1: Map The Current Workspace

Start with `prompts/01-map-my-current-folders.md`.

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

Memory is not a junk drawer. Long-term memory should hold durable preferences, durable rules, important active projects, and recurring lessons.

Daily notes or project notes should hold details that matter, but do not need to live forever in the agent's short hot memory.

Do not ask the agent to dump private memory into a public file. Ask it to summarize categories and rules.

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

## What Not To Do

Do not create a giant atlas that lists every file.

Do not put secrets, private messages, browser profiles, credentials, or backups into examples.

Do not create new top-level folders just because the agent likes clean categories.

Do not let the agent rewrite memory without explaining what changed and why.

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
