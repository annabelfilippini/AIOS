---
disable-model-invocation: true
---
I'm starting a new session. Get me up to speed.

## Argument

This command takes an optional project arg: `/begin`, `/begin wayloft`, `/begin pbp`, `/begin website-audit`.

- **No arg** → cross-project briefing (full sweep, both Wayloft + PBP).
- **With arg** → scope everything to that single project. Skip the sidebar project. Filter scratchpads and decisions to that project only. Don't read the other project's plan files, git logs, or CLAUDE.md.

## Project Map

When an arg is provided, use this map. The `slug` is what filters scratchpad frontmatter (`project:`) and decisions.jsonl (`"project":"<slug>"`).

| Arg | Slug | Working dir | Plan file | Notes |
|---|---|---|---|---|
| `wayloft` | `wayloft` | `~/Documents/AI-OS/MO` | `WAYLOFT-BUILD-PLAN.md` at project root | Has CLAUDE.md, is a git repo |
| `pbp` | `pickleball-portal` (also accept `pbp`) | `~/Documents/AI-OS/projects/Pickleball Portal/repo` | `~/Documents/AI-OS/projects/Pickleball Portal/scratchpad.md` (one level up from repo) | Has CLAUDE.md in repo, repo is the git root |
| `website-audit` | `website-audit` | `~/Documents/AI-OS/projects/website-audit` | `BUILD-PLAN.md` at project root | Doc-only project (no git repo expected); skip git steps if not a repo |

If an unknown arg is passed, list the valid args and stop. Don't guess.

## Gather Context

0. **Read the last scratchpad entry.** List `~/.claude/scratchpad/` (ignore README.md), sort by filename descending. Read the most recent.
   - **No-arg mode:** if the most recent is from today, also read the second-most-recent.
   - **Project-arg mode:** walk the list, skip entries whose frontmatter `project:` doesn't match the project slug. Read the most recent matching entry; if it's from today, also read the prior matching one. If no matching scratchpad exists, say so and skip.
   - If the surfaced entry's `status` is `in-progress` or `paused`, lift the `next-session` line into the "Where We Left Off" section.

1. **Read system map** at `~/.claude/bb/system-map.md` for directory layout orientation.

2. **Project scoping.**
   - **No-arg mode:** detect project from working directory — `~/Documents/AI-OS/MO` → Wayloft (primary), `~/Documents/AI-OS/projects/Pickleball Portal` → PBP (primary). Anywhere else → both projects, equal weight.
   - **Project-arg mode:** the arg wins. Ignore working directory.

3. **For the primary project** (or both, in no-arg cross-project mode):
   - Read CLAUDE.md "Current Status" section if it exists at the working dir
   - Run `git log --oneline -5` and `git status --porcelain` (skip if not a git repo)
   - Read the plan file from the project map

4. **Recent BB decisions** — Read the last 10 lines of `~/.claude/bb/knowledge/decisions.jsonl`. Filter to the relevant project slug(s). Show the last 3-5 as one-liners.

5. **BB strategy context** — Read `~/.claude/bb/knowledge/strategy.md`. In project-arg mode, only quote the sections relevant to that project.

6. **Sidebar project** — *Only in no-arg cross-project mode.* `git log --oneline -3` and a one-line status from its CLAUDE.md. Skip entirely in project-arg mode.

7. **Check memory** — Scan `~/.claude/projects/` memory for relevant session context or recent feedback. In project-arg mode, prefer entries tagged with that project.

8. **BB queue status** — Read `~/Documents/AI-OS/knowledge/outputs/business-ideas.md` and `ls ~/Documents/AI-OS/knowledge/ideas/`. Count ideas by state:
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
- **From last scratchpad** (filtered to project in arg mode): project, status, next-session hint, open questions

### BB Queue
- *Skipped in project-arg mode* unless ideas tie to the chosen project
- Otherwise: one line per state, plus next `/bb` move if obvious

### Suggested Starting Point
- What to pick up first, and why
- If a deferred decision has new data, flag it

Keep it concise. Context, not a novel.
