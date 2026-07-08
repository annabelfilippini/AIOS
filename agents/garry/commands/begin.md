---
disable-model-invocation: true
---
I'm starting a new session. Get me up to speed.

## Argument

This command takes an optional project arg: `/begin`, `/begin wayloft`,
`/begin pbp`.

- **No arg** -> cross-project briefing.
- **With arg** -> scope everything to that single project. Skip the sidebar
  project. Filter checkpoints and decisions to that project only.

## Project Map

When an arg is provided, use this map. The `slug` is what filters checkpoint
frontmatter (`project:`) and decisions.jsonl (`"project":"<slug>"`).

| Arg | Slug | Working dir | Plan file | Notes |
| --- | --- | --- | --- | --- |
| `wayloft` | `wayloft` | `~/Documents/AI-OS/projects/wayloft` | `docs/` and project root docs | Has CLAUDE.md/AGENTS.md, is a git repo |
| `pbp` | `pickleball-portal` | `~/Documents/AI-OS/projects/pickleball-portal/repo` | Project root docs | Has AGENTS.md in repo, repo is the git root |

If an unknown arg is passed, list the valid args and stop. Don't guess.

## Gather Context

0. **Run startup recall.** Use
   `node operations/memory/scripts/recall.mjs --cwd "$PWD" --query "<arg or current request>"`
   from `~/Documents/AI-OS`.
   - **No-arg mode:** use an empty query or `cross-project`.
   - **Project-arg mode:** use the mapped slug as the query.
   - Read the recall brief first. Open only the surfaced checkpoint/candidate
     files if the brief is not enough.
   - If the top surfaced entry's `status` is `in-progress` or `paused`, lift the
     `next-session` line into the "Where We Left Off" section.

1. **Project scoping.**
   - **No-arg mode:** detect project from working directory: `projects/wayloft`
     means Wayloft, `projects/pickleball-portal` means PBP. Anywhere else
     means cross-project mode.
   - **Project-arg mode:** the arg wins. Ignore working directory.

2. **For the primary project** (or both, in no-arg cross-project mode):
   - Read CLAUDE.md "Current Status" section if it exists at the working dir
   - Run `git log --oneline -5` and `git status --porcelain` (skip if not a git repo)
   - Read the plan file from the project map

3. **Sidebar project** — *Only in no-arg cross-project mode.* `git log --oneline -3` and a one-line status from its CLAUDE.md. Skip entirely in project-arg mode.

4. **Check deeper memory only if needed** — If startup recall did not surface
   enough context, search `operations/memory/checkpoints/`,
   `operations/memory/refinement-candidates/`, and then archive/raw stores on
   demand. Prefer entries tagged with the active project.

## Output

### [Project Name]
- Current status (one paragraph from CLAUDE.md or plan file)
- Last 3-5 commits (oneline) — skip if not a git repo
- Uncommitted work if any
- Blockers if any

### [Other Project Name] (sidebar)
- *No-arg cross-project mode only.* One-line status + last commit date.

### Where We Left Off
- What's in progress, what was next, what's blocked
- **From startup recall** (filtered to project in arg mode): project, status, next-session hint, open questions

### Suggested Starting Point
- What to pick up first, and why

Keep it concise. Context, not a novel.
