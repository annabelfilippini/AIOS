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

1. **Read system map** at `~/.claude/bb/system-map.md` for directory layout orientation.

2. **Project scoping.**
   - **No-arg mode:** detect project from working directory: `projects/wayloft`
     means Wayloft, `projects/pickleball-portal` means PBP. Anywhere else
     means cross-project mode.
   - **Project-arg mode:** the arg wins. Ignore working directory.

3. **For the primary project** (or both, in no-arg cross-project mode):
   - Read CLAUDE.md "Current Status" section if it exists at the working dir
   - Run `git log --oneline -5` and `git status --porcelain` (skip if not a git repo)
   - Read the plan file from the project map

4. **Recent BB decisions** — Read the last 10 lines of `~/.claude/bb/knowledge/decisions.jsonl`. Filter to the relevant project slug(s). Show the last 3-5 as one-liners.

5. **BB strategy context** — Read `~/.claude/bb/knowledge/strategy.md`. In project-arg mode, only quote the sections relevant to that project.

6. **Sidebar project** — *Only in no-arg cross-project mode.* `git log --oneline -3` and a one-line status from its CLAUDE.md. Skip entirely in project-arg mode.

7. **Check deeper memory only if needed** — If startup recall did not surface
   enough context, search `operations/memory/checkpoints/`,
   `operations/memory/refinement-candidates/`, and then archive/raw stores on
   demand. Prefer entries tagged with the active project.

8. **BB queue status** — Read AI-OS knowledge/agent queues only if those files
   exist. Count ideas by state:
   - `status: active` with no `bb_file` → "N new ideas awaiting Phase 0 intake"
   - `status: active` with `stage: intake-done` → "N ideas ready for Phase 1 (office-hours)"
   - `status: hold` → "N ideas on HOLD (blocked on field assignments)"
   - `status: active` with `stage: office-hours-done` + no hold → "N ideas ready for Phase 2 (CEO review)"
   - `status: parked` → count only. Show as compact one-liner: "💤 N parked (say 'show parked ideas' or run `/bb parked` to list)"

   **Parked ideas never trigger this section on their own.** Only surface BB Queue if at least one idea has `status: active` OR `status: hold`. If only parked, skip the section.

   In **project-arg mode**, skip BB queue entirely *unless* an idea's `bb_file` or tags clearly tie to the chosen project (rare). Default to skipping — BB queue is a cross-cutting concern, not a project view.

   Skip if queue is empty or everything is killed. For HOLD'd ideas, name the canonical user and the first blocking assignment.

## Output

### [Project Name]
- Current status (one paragraph from CLAUDE.md or plan file)
- Last 3-5 commits (oneline) — skip if not a git repo
- Uncommitted work if any
- Blockers if any

### Recent Decisions
- Last 3-5 BB decisions for the relevant project(s), one line each
- Flag any deferred decisions that might be ready to revisit

### [Other Project Name] (sidebar)
- *No-arg cross-project mode only.* One-line status + last commit date.

### Where We Left Off
- What's in progress, what was next, what's blocked
- **From startup recall** (filtered to project in arg mode): project, status, next-session hint, open questions

### BB Queue
- *Skipped in project-arg mode* unless ideas tie to the chosen project
- Otherwise: one line per state, plus next `/bb` move if obvious

### Suggested Starting Point
- What to pick up first, and why
- If a deferred decision has new data, flag it

Keep it concise. Context, not a novel.
