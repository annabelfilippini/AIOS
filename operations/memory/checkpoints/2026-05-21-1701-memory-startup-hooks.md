---
date: 2026-05-21
time: 17:01
project: ai-os-memory
status: complete
next-session: Continue memory-system cleanup by slimming ~/.claude/CLAUDE.md and aligning it with AI-OS/CLAUDE.md.
---

# Session: Startup Context And Hook Cleanup

## What we worked on

- Reviewed what Claude loads at session start: global `~/.claude/CLAUDE.md`,
  project/upward `CLAUDE.md` files, imports, session hooks, and project-specific
  routers.
- Reviewed what Codex loads at session start: runtime/developer rules, tiny
  `~/.codex/AGENTS.md`, home `~/AGENTS.md`, session environment, and task-driven
  reads of AI-OS/project docs.
- Compared Claude and Codex startup weight while Annabel was watching a video
  about memory systems.
- Inspected Claude/Codex hook wiring and explained prehook/posthook behavior.
- Removed the unused wiki auto-ingest hook scripts from both runtimes.

## Decisions made

- Keep Codex startup context thin: runtime rules plus routers, not durable
  memory dumps.
- Treat `~/.claude/CLAUDE.md` as a stale-but-useful global router that should be
  slimmed and updated, not expanded.
- Durable memory should live under
  `~/Documents/AI-OS/operations/memory/`, with checkpoints and refinement
  candidates used as the review path.
- Auto-ingesting wiki/raw files on session start is unnecessary for the current
  memory system direction.

## Open questions

- How small should `~/.claude/CLAUDE.md` become: direct copy of home rules, or a
  tiny pointer like `~/.codex/AGENTS.md`?
- Should Claude and Codex share a single canonical runtime-adapter pattern, with
  separate agent-specific files only for behavior differences?
- Should the old BB/Garry stop-hook checks that reference `~/.claude/bb` remain,
  or be replaced with AI-OS `operations/memory` checks?

## Next steps

- Update `~/.claude/CLAUDE.md` to reflect current AI-OS routing:
  Annie as front door, Garry as strategy specialist, Business Partner/Codex as
  implementation/QA, canonical `skills/`, `cli-connections/`, and
  `operations/memory/`.
- Consider adding a Claude-side pointer to
  `~/Documents/AI-OS/CLAUDE.md` rather than duplicating lots of content.
- Review `~/.claude/settings.json` and `~/.codex/hooks.json` stop hooks for
  stale `~/.claude/bb` assumptions before the new memory design.
- Keep `wiki-session-report.sh` for now; it is a reminder, not an automatic
  ingest action.

## Context to preserve

- `~/.codex/AGENTS.md` is already a good tiny runtime adapter:
  it points to `~/AGENTS.md` and AI-OS-specific instructions.
- `~/AGENTS.md` contains Annabel's global Codex rules and file-placement map.
- `~/Documents/AI-OS/AGENTS.md` contains the broader AI-OS routing, agent roles,
  handoff workflow, skill source-of-truth rules, and memory lifecycle.
- `~/Documents/AI-OS/CLAUDE.md` is fresher than `~/.claude/CLAUDE.md` and should
  guide the Claude runtime cleanup.
- Removed files:
  - `~/.claude/hooks/wiki-auto-ingest.sh`
  - `~/.codex/hooks/wiki-auto-ingest.sh`

## System refinement candidates

- Consolidate Claude/Codex runtime adapters so both are small routers into
  canonical AI-OS docs.
- Replace any automatic memory-ingest behavior with explicit commands or skills.
- Audit stop hooks so they report useful memory obligations without reviving
  legacy `~/.claude/bb` workflows unless those are still intentional.
