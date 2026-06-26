# Memory

This folder holds durable memory for the AI-OS.

The memory model is deliberately small:

- **Store:** write checkpoints, refinement candidates, and optional raw notes to
  external files.
- **Inject:** load only routers and a short recall brief at session start.
- **Recall:** search deeper memory only when the task needs it.

## Folder Map

- `checkpoints/` - session handoffs written by the `checkpoint` skill.
- `refinement-candidates/` - proposed updates to `SOUL.md`, `USER.md`, `AGENTS.md`, `CLAUDE.md`, or skill references.
- `raw-sessions/` - raw or semi-raw captures kept out of startup recall by
  default.
- `archive/` - older checkpoints or candidates that remain useful but should not stay active.
- `scripts/recall.mjs` - startup recall helper that scores relevant checkpoints
  and candidates by current directory, optional query, recency, and status.
- `scripts/check-memory-safety.mjs` - safety check for likely secrets,
  missing checkpoint frontmatter, and overlong active checkpoints.
- `tmp/` - short-lived notes that can be deleted during cleanup.

## Startup Recall

At the start of an AI-OS session, run:

```bash
node operations/memory/scripts/recall.mjs --cwd "$PWD" --query "<task or project>"
```

Read the brief first. Open only the source files it surfaces when more detail is
needed. Use `--includeArchive` only when current checkpoints do not answer the
question. Search `raw-sessions/` manually only when checkpoints and candidates
are not enough.

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
- Condense useful raw session material into checkpoints or candidates
- Delete or summarize noisy `tmp/` notes
- Leave core files unchanged unless Annabel approves edits

## Rule Of Thumb

Save memory when the next session would be slower, riskier, or more confusing without it. Do not save memory just because something happened.
