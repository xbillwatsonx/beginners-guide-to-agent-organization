# Quick Start Card

Use this card when you want your agent to walk you through cleaning up folder confusion and memory sprawl.

## What Your Agent Will Help You Make

Your agent will help you make three simple things:

1. `DIRECTORY_ATLAS.md` - a map of where files belong.
2. `AGENTS.md` placement rules - instructions your agent must follow.
3. memory rules - guidance for what should be remembered, filed, summarized, or ignored.

## Copy-Paste Workflow

Give these prompts to your agent in order so it can walk you through setup:

1. Open `prompts/01-map-my-current-folders.md`, copy only the text inside the code block, and paste that into your agent chat.
2. Open `prompts/02-create-directory-atlas.md`, copy only the text inside the code block, and paste that into your agent chat.
3. Open `prompts/03-add-agent-placement-rules.md`, copy only the text inside the code block, and paste that into your agent chat.
4. Open `prompts/04-review-memory-bloat.md`, copy only the text inside the code block, and paste that into your agent chat.

Any time the agent wants to create a new durable folder, open `prompts/05-before-you-create-a-folder.md`, copy only the text inside the code block, and paste that into your agent chat.

## Simple Rule

Your agent should search before it creates.

If the right home already exists, use it. If several homes could fit, explain the options. If the agent is still unsure, it should ask before creating a new durable folder.

## What To Tell Your Agent

```text
Please use this runbook to walk me through organizing my agent workspace. Start with the quick-start card, use the prompts in order, and do not create or delete anything until you have inspected the existing folder structure and explained your plan.
```

## Done Means

- `DIRECTORY_ATLAS.md` exists.
- `AGENTS.md` includes placement rules.
- protected areas are listed without exposing private contents.
- memory rules are clear.
- the agent knows to ask before guessing.

## Ready-Made Files

If you want a head start, copy the files from `starter-kit/` into your workspace.

Use `templates/` if you want to customize the wording before installing the files.
