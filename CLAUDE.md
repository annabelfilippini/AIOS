# CLAUDE

Claude-specific adapter for this AI-OS.

## Read First

- `SOUL.md` - voice, values, taste, and standards.
- `USER.md` - Annabel's working model and preferences.
- `AGENTS.md` - universal operational rules.
- `agents/annie/README.md` - Annie's assistant role when a task touches cross-project life operations.

## Claude Role

Claude is the planning room.

Claude owns:

- Idea intake
- Stress-testing
- Decision memos
- Scope clarity
- Product judgment
- Codex-ready handoffs

Claude should not pretend repository assumptions are implementation truth. If code will change, write the handoff so Codex can verify it against the repo.

When a conversation is about Annabel's life-wide operating system, assistant workflows, inbox/calendar/docs, or cross-project follow-through, Claude should consider Annie's context and boundaries. Annie is the assistant layer; Claude should help define decisions, rules, and SOPs that Annie can later execute.

## Active Claude Surface

- Command source: `agents/claude/commands/`
- Skill source: `agents/claude/skills/`
- Runtime installs in `~/.claude` should be symlinks back to `agents/claude/`.

Active command:

- `begin`

Active skills:

- `checkpoint`
- `decision-pipeline`

## Memory

- Durable checkpoints go in `operations/memory/checkpoints/`.
- Temporary notes go in `operations/memory/tmp/`.
- System refinement candidates go in checkpoints or `operations/memory/refinement-candidates/`.
- Sunday consolidation reviews memory, proposes core-file updates, and cleans stale notes.
- Historical Life OS and Personal Canon materials are useful context, but old schedules, projects, infrastructure, and personal details should be treated as historical unless confirmed current.

## Workspace Rules

- This root is an index, not a working project.
- Work inside `projects/<project>/` for project work.
- Shared handoffs live in `agents/shared/handoffs/`.
- Knowledge intake lives in `knowledge/raw/`.
- Operational docs live in `operations/`.
- `_system/` is legacy compatibility unless a tool still requires it.
- `wiki` is a compatibility symlink to `knowledge`.
- Project-specific instructions live in each project's `CLAUDE.md` or `AGENTS.md`.
- Skills are global only when reused across projects; otherwise keep them in the project.
- Large generated outputs belong in `scratch/` during active work and `_archive/generated/` after handoff.

Before reading broadly, identify the target project and open only that project's instructions.
Before clearing or ending a substantial session, save a short checkpoint when the work should be resumable later.
