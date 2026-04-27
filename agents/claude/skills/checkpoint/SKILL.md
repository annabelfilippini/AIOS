---
name: checkpoint
description: Save session state for continuity. Captures what was done, decisions made, and next steps. Use when ending a session or switching context.
allowed-tools:
  - Bash
  - Read
  - Write
---

# Checkpoint

Save working state so the next session can pick up without re-explaining context.

## What to capture

1. **Git state:** current branch, last commit, uncommitted changes
2. **What was worked on:** bullet points of accomplishments
3. **Decisions made:** choices and their reasoning
4. **Open questions:** unresolved items, things flagged for later
5. **Next steps:** what to pick up first next session
6. **Context to preserve:** subtle things not obvious from code/git alone

## Output

Write durable checkpoints to:

`/Users/annabelfilippini/Documents/AI-OS/operations/memory/checkpoints/YYYY-MM-DD-HHMM-session-slug.md`

Use `~/.claude/scratchpad/` only for Claude runtime scratch that does not need to become part of the AI-OS memory system.

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
- Keep under 100 lines — summarize, don't journal
- Reference files by path, don't paste content
- No secrets in scratchpads
- Never delete old entries — append only
- Put noisy, temporary notes in `operations/memory/tmp/`
- The Sunday consolidation automation cleans, archives, or discards stale memory notes

## System Refinement Candidates

Capture proposed updates, but do not edit core files directly from a checkpoint:

- `SOUL.md` — voice, taste, agent identity
- `USER.md` — Annabel preferences, patterns, goals, blind spots
- `AGENTS.md` — operational rules and path conventions
- `CLAUDE.md` — Claude-specific adapter behavior
- Skill references — real good/bad examples from the session

## References

- See `references/good-bad-examples.md` for good and bad examples of this skill in practice.
