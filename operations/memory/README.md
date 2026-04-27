# Memory

This folder holds durable memory for the AI-OS.

## Folder Map

- `checkpoints/` - session handoffs written by the `checkpoint` skill.
- `refinement-candidates/` - proposed updates to `SOUL.md`, `USER.md`, `AGENTS.md`, `CLAUDE.md`, or skill references.
- `archive/` - older checkpoints or candidates that remain useful but should not stay active.
- `tmp/` - short-lived notes that can be deleted during cleanup.
- `_active` - legacy compatibility link to the old `_system/memory` folder.

## Lifecycle

After each meaningful session, run `checkpoint`.

The checkpoint should capture:

- What changed
- Decisions made
- Open questions
- Next steps
- Context worth preserving
- System refinement candidates

Every Sunday evening, the weekly consolidation automation should:

- Review recent checkpoints and candidates
- Propose permanent updates to core files
- Move stale-but-useful notes to `archive/`
- Delete or summarize noisy `tmp/` notes
- Leave core files unchanged unless Annabel approves edits

## Rule Of Thumb

Save memory when the next session would be slower, riskier, or more confusing without it. Do not save memory just because something happened.
