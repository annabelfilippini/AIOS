---
date: 2026-05-21
time: 19:30
project: ai-os-memory
status: complete
next-session: Test memory recall from a fresh Claude and Codex session; if it behaves well, consider adding a tiny alias or command wrapper for `memory recall`.
---

# Session: Memory Recall System

## What we worked on

- Turned the existing checkpoint habit into a lean startup recall system.
- Added `operations/memory/scripts/recall.mjs`, which scores checkpoints and
  refinement candidates by current directory, query terms, recency, status, and
  next-session hints.
- Updated `operations/memory/README.md` with the Store / Inject / Recall model:
  store durable memory externally, inject only a short recall brief, and search
  deeper memory only on demand.
- Updated `AGENTS.md`, `CLAUDE.md`, and Garry's `/begin` command so future
  sessions run startup recall before broad memory searches.

## Decisions made

- Keep startup context thin. Do not inject raw checkpoints, raw transcripts, or
  full memory folders by default.
- Use current working directory plus the active task as the default recall
  signal.
- Keep raw runtime transcript/session stores out of durable memory. Checkpoints
  and refinement candidates remain the active memory layer.
- Make recall readable in Markdown by default, with `--json` available for
  future automation.

## Verification

- `node --check operations/memory/scripts/recall.mjs` passed.
- Project-scoped test:
  `node operations/memory/scripts/recall.mjs --cwd projects/agency-audit-network --query "mansel audit tally next" --limit 1 --json`
  surfaced the in-progress Tally audit checkpoint first.
- AI-OS memory query:
  `node operations/memory/scripts/recall.mjs --cwd . --query "memory startup hooks" --limit 3`
  surfaced the startup-context checkpoint first.
- Self-query:
  `node operations/memory/scripts/recall.mjs --cwd . --query "memory recall system" --limit 2`
  surfaced this checkpoint first after adding phrase/coverage scoring.

## Open questions

- Whether to add a shell alias or wrapper such as `memory recall`.
- Whether to replace remaining legacy Garry `/begin` references to
  `~/.claude/bb` in a separate cleanup pass.
- Whether weekly consolidation should call `recall.mjs --json` as its first
  selection layer.

## Next steps

1. Start a fresh Claude/Garry session and run `/begin` to see if the recall
   step feels natural.
2. Start a fresh Codex session inside a project folder and verify it runs recall
   before broad searches.
3. If the command is annoying to type, add a small wrapper or documented alias.
