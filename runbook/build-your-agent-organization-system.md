# Build Your Agent Organization System

This is the user-facing build plan.

Use it when you want your agent to walk you through creating a simple organization system for your workspace.

## What Your Agent Will Help You Build

By the end, your workspace should have:

1. a `DIRECTORY_ATLAS.md` that explains where things go
2. `AGENTS.md` placement rules that tell future agents to use the atlas
3. memory rules that keep long-term memory from becoming a dumping ground
4. a habit of searching existing homes before creating new folders

## Before You Start

Choose the workspace you want organized. This should be the folder where your agent normally works.

Copy this into your agent:

```text
Please walk me through building an organization system for this workspace. Use the runbook and prompts in this package. Do not move, delete, rename, publish, or upload anything unless I explicitly approve it.
```

## Step 1: Inspect The Workspace

Open `prompts/01-map-my-current-folders.md`, copy the text inside its code block, and paste that text into your agent.

The agent should identify major folders, protected areas, unclear folders, and likely homes for projects, reports, research, reference material, memory, logs, and templates.

Do not ask the agent to deeply read private contents. Folder names and existing instruction files are usually enough for the first map.

## Step 2: Create DIRECTORY_ATLAS.md

Open `prompts/02-create-directory-atlas.md`, copy the text inside its code block, and paste that text into your agent.

The atlas should be short and useful. It should explain where durable files belong. It should not list every file on the system.

Good atlas entries answer:

- What belongs here?
- What does not belong here?
- Should this area be protected?
- Should the agent read local instructions before editing?

## Step 3: Add AGENTS.md Placement Rules

Open `prompts/03-add-agent-placement-rules.md`, copy the text inside its code block, and paste that text into your agent.

The agent should preserve existing instructions and add a focused placement section.

The most important rule is:

```text
Before creating durable files or folders, consult DIRECTORY_ATLAS.md and search existing homes first.
```

## Step 4: Set Memory Rules

Open `prompts/04-review-memory-bloat.md`, copy the text inside its code block, and paste that text into your agent.

The goal is to decide what belongs in long-term memory, daily notes, project files, reports, or nowhere.

Long-term memory should hold durable rules and important context. It should not hold every task detail.

## Step 5: Use The Folder-Creation Gate

When the agent wants to create a new durable folder, open `prompts/05-before-you-create-a-folder.md`, copy the text inside its code block, and paste that text into your agent.

This step prevents folder sprawl. The agent must explain what it checked and why a new folder is needed.

## Step 6: Validate The Setup

If Python is available, run:

```bash
python3 validate-agent-organization.py .
```

If `just` is available, run:

```bash
just agent-verify
```

Validation does not prove the workspace is perfect. It checks that the package structure and starter files are present and avoids obvious release mistakes.

## Step 7: Maintain It

Once a week, or after a large project, ask your agent:

```text
Please review whether our DIRECTORY_ATLAS.md still matches the workspace. Do not reorganize anything yet. Report what changed, what is unclear, and whether any new durable folders need to be added to the atlas.
```

## Done Means

- The agent knows where important files belong.
- New durable folders are rare and justified.
- Important context is written to files, not only chat.
- Protected areas are named carefully.
- Long-term memory stays small and useful.
