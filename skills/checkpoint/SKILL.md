---
name: checkpoint
description: Save Garry strategy session state for continuity. Captures decisions, reasoning, open questions, and next steps.
allowed-tools:
  - Bash
  - Read
  - Write
---

# Checkpoint

Save working state so the next Garry session can pick up without re-explaining context.

## What To Capture

1. What was discussed
2. Decisions made
3. Ideas killed, parked, researched, prototyped, or sent to Business Partner
4. Open questions
5. Next steps
6. Context worth preserving

## Output Location

Write durable checkpoints to:

`/Users/annabelfilippini/Documents/AI-OS/operations/memory/checkpoints/YYYY-MM-DD-HHMM-session-slug.md`

## Structure

```markdown
---
date: YYYY-MM-DD
time: HH:MM
project: project-name
status: complete | in-progress | paused
next-session: one-line hint for what to do next
---

# Session: short description

## What we worked on
## Decisions made
## Open questions
## Next steps
## Context to preserve
## System refinement candidates
```

## Rules

- Keep under 100 lines.
- Reference files by path.
- Do not store secrets.
- Never delete old checkpoint entries.
- Capture only useful continuity, not a transcript.
- `project:` must be a single canonical kebab-case slug matching the folder name under `projects/` (e.g. `style-feed`, `wayloft`, `life-os`), or `ai-os` for system work. Never prose, never a description.
- When a new checkpoint supersedes an older `in-progress` checkpoint for the same project, update the older file's `status:` to `superseded` in the same session.
