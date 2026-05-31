---
date: 2026-05-22
time: 09:54
project: ai-os-memory
status: complete
next-session: Consider normalizing older checkpoint frontmatter and adding a tiny `memory recall` wrapper after recall behavior feels good in fresh sessions.
---

# Session: Memory Recall Sharpening

## What we worked on

- Sharpened `operations/memory/scripts/recall.mjs` so startup recall uses stronger relevance signals.
- Fixed the `Where To Start` bug: the start hint now comes from the top-ranked entry only.
- Added inferred project detection for older checkpoints that lack YAML frontmatter but include a project path/body label.
- Added `operations/memory/scripts/check-memory-safety.mjs` and wired it into `operations/compound-engineering/lint-aios-system.sh`.
- Added `operations/memory/raw-sessions/README.md` as an explicit raw-capture layer that is not searched by default.

## Decisions made

- Keep recall file-based and lightweight; no vector layer yet.
- Treat broad tokens like `memory`, `system`, and `next` as weak evidence.
- Fail memory safety only on likely secret literals; warn on older checkpoint hygiene issues so existing useful notes still work.
- Search raw sessions manually only when checkpoints and refinement candidates are not enough.

## Open questions

- Whether to normalize older checkpoint frontmatter now or let weekly consolidation handle it.
- Whether to add a wrapper/alias once fresh-session recall feels natural.

## Next steps

1. Test recall in a fresh Codex/Claude session on a real project switch.
2. Normalize old Wayloft and Annabel-site checkpoints with frontmatter if warnings get noisy.
3. Add a tiny wrapper only after the command proves useful across repeated sessions.

## Context to preserve

- Verified `recall.mjs` with `memory recall system`, `wayloft`, and `mansel audit tally next` queries.
- Verified `check-memory-safety.mjs`; it currently reports warnings for old checkpoint shape but no secret-literal failures.
- Targeted markdown lint for memory docs passed.
