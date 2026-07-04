# Beginner's Guide to Agent Organization

`beginners-guide-to-agent-organization` gives non-technical users copy-paste prompts and starter files so their AI agent can walk them through where things belong, what folders mean, and when to stop guessing before creating new files or directories.

Its goal is to give people a simple, permanent organization system that reduces memory bloat, prevents folder sprawl, and makes future agent work easier to trust because the agent has clear placement rules to follow.

## What This Does

This package gives you a step-by-step way to ask your agent to guide you:

> Before you create files or folders, inspect my workspace, help me create a folder map, follow the placement rules we define, remember only what matters, and ask before guessing.

The runbook is designed for ordinary people using an AI agent that can read and write files. You do not need to be a programmer. You only need a folder where your agent works and permission to let the agent inspect that folder.

## Why This Matters

Agents are helpful, but they can make a mess when they do not know where things belong.

Without clear rules, an agent may:

- create duplicate project folders
- put research, drafts, logs, and final files in the same place
- save important notes in chat instead of files
- bloat long-term memory with details that should live in documents
- expose or summarize sensitive folders too deeply
- guess a new location instead of searching for an existing home

This runbook fixes that by creating three simple anchors:

- `DIRECTORY_ATLAS.md` - a plain-language map of where things go
- `AGENTS.md` placement rules - instructions the agent must follow before creating durable files
- memory rules - guidance for what should be remembered, filed, summarized, or ignored

## What Is Included

- `runbook/agent-organization-runbook.md` - full beginner-friendly implementation guide.
- `runbook/build-your-agent-organization-system.md` - step-by-step user-facing build plan.
- `runbook/quick-start-card.md` - one-page starter card.
- `prompts/` - copy-paste prompts for getting your agent to walk you through the setup.
- `templates/` - reusable templates for `DIRECTORY_ATLAS.md`, `AGENTS.md`, and memory rules.
- `starter-kit/` - starter files you can copy into an agent workspace.
- `examples/` - small examples showing what a finished setup can look like.
- `validate-agent-organization.py` - dependency-free checker for the package or a starter workspace.
- `CHANGELOG.md` - package history.
- `LICENSE` - MIT License.

Use `starter-kit/` if you want ready-to-go files you can copy into your workspace as-is.

Use `templates/` if you want to customize the wording before installing the files.

## Quick Start

1. Open `runbook/quick-start-card.md`.
2. Each prompt file contains a code block. Copy the text inside the code block and paste it into your agent chat.
3. Open `prompts/01-map-my-current-folders.md`, copy the text inside the code block, and paste it into your agent chat.
4. Let the agent inspect the workspace and explain what it found.
5. Open `prompts/02-create-directory-atlas.md`, copy the text inside the code block, and paste it into your agent chat.
6. Open `prompts/03-add-agent-placement-rules.md`, copy the text inside the code block, and paste it into your agent chat.
7. Open `prompts/04-review-memory-bloat.md`, copy the text inside the code block, and paste it into your agent chat.
8. Use `prompts/05-before-you-create-a-folder.md` whenever the agent wants to create a new durable folder.

If your agent can run commands, ask it to validate the package or starter workspace:

```bash
python3 validate-agent-organization.py .
```

## Optional: Validate With just

You do not need `just` to use this package. The validator works on its own:

```bash
python3 validate-agent-organization.py .
```

If you do have `just` installed, you can also run:

```bash
just agent-verify
just package
```

## What Success Looks Like

You are done with the first setup when:

- your workspace has a readable `DIRECTORY_ATLAS.md`
- your main `AGENTS.md` tells the agent when to consult the atlas
- the agent knows where projects, research, reports, references, memory, logs, and templates belong
- protected folders are named without exposing private contents
- the agent searches existing homes before creating new folders
- memory rules explain what should be remembered, filed, summarized, or ignored

## Important Safety Rule

This runbook does not ask your agent to publish anything, delete anything, or expose private data.

The agent should inspect folder names and purposes, not dump sensitive file contents into the atlas. Credentials, browser profiles, backups, private messages, caches, and runtime folders should be marked as protected.

## License

MIT. Use it, share it, adapt it, and improve it.
