---
date: 2026-06-15
time: 16:32
project: ai-os / context-file architecture
status: delivered & pushed — AGENTS.md is the single source of truth; CLAUDE.md and HERMES.md are thin adapters that point at it
next-session: DONE. Universal rules now live in AGENTS.md; the two runtime adapters (CLAUDE.md, HERMES.md) only hold runtime-specific notes and route to AGENTS.md. If CLAUDE.md drifts ahead again (Annabel edits it because Claude Code auto-loads it), the fix is always "promote the universal bits UP into AGENTS.md," never "point AGENTS.md down at CLAUDE.md." Optional follow-up: trim the still-duplicated sections in CLAUDE.md (Read-What-Applies, Source Of Truth, the remaining Workspace bullets) down to pointers too, since AGENTS.md already mirrors them.
---

# Session: AI-OS context files restructured so everything points at AGENTS.md

## Ask

Annabel was confused about HERMES.md vs CLAUDE.md vs AGENTS.md ("who points
where?") and wanted all three kept current. Underlying instinct: "CLAUDE.md
feels most up to date, maybe point AGENTS.md and HERMES.md at CLAUDE.md."

## Decision (the durable part)

- **AGENTS.md = the hub / rulebook** (runtime-neutral, the real shared rules).
- **CLAUDE.md and HERMES.md = thin adapters** that each already say "read
  AGENTS.md." The arrows point UP to AGENTS.md. **Nothing points at CLAUDE.md.**
- Do NOT invert the routing (pointing the hub at a runtime adapter). That would
  (1) create a loop, (2) force Hermes to ingest Claude-specific plumbing, and
  (3) undo the recent runtime-neutral refactor.
- CLAUDE.md "felt most up to date" only because Claude Code auto-loads it, so
  universal rules kept getting typed there. Correct fix = promote that content
  UP into AGENTS.md, keep adapters thin.

## Why Hermes was missing rules

Hermes auto-loads only the first-match context file (HERMES.md, ~1.8 KB), which
routes to AGENTS.md. So anything universal stuck in CLAUDE.md never reached
Hermes. Both runtimes read the shared rules one hop away (adapter -> AGENTS.md),
not force-fed.

## Done this session

1. Committed `HERMES.md` to the repo (it had been untracked). Discovered the VPS
   autosync had already committed the identical file as `9a89e59`; cleaned up the
   duplicate local commit with `git reset --soft origin/main` (working tree of
   ~1,800 dirty files left untouched).
2. Moved universal content from CLAUDE.md into AGENTS.md: the whole `## Stack`
   section, the screenshot/loose-image placement rule, and the
   scratch/`_archive` generated-output line. Made the Stack wording
   runtime-neutral (Claude + Codex + Hermes as peer adapters).
3. CLAUDE.md trimmed to point at AGENTS.md for those. Committed as `0f8da63`,
   pushed to GitHub (so the VPS/Hermes get it on next sync).

## Verify / gotchas

- `git log origin/main` shows `0f8da63` on top of `9a89e59` — pushed.
- This repo has an active VPS autosync that commits + pushes AGENTS.md/CLAUDE.md
  on its own, so the Mac's `origin/main` can move underneath you. When the
  auto-push hook rejects with "fetch first," reconcile a clean 1-for-1 split with
  fetch + soft reset (if the remote already has your content) rather than a
  blind pull into the dirty tree.
- HERMES.md content + loader chain documented in memory
  `project-hermes-workdir-context` and checkpoint
  `2026-06-15-0927-hermes-scoped-to-aios-and-reads-context.md`.
</content>
</invoke>
