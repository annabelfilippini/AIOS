---
date: 2026-05-25
project: ai-os-memory
status: processed
next-session: If you approve the core-file edits, apply them as one focused commit; then do a separate deliberate `knowledge/` repo reconciliation pass.
---

# Weekly System Consolidation — 2026-05-25

This is the condensed, active refinement candidate for the memory system.
Older, longer investigative notes were moved to `operations/memory/archive/`.

## Proposed permanent updates (needs Annabel approval)

### `USER.md`

- Update the “Active Garry/Claude surface” skill names:
  - Replace `garry-office-hours-lite` → `office-hours-lite`
  - Replace `garry-ceo-review-lite` → `ceo-review-lite`

Rationale: top-level canonical skills are now `skills/office-hours-lite` and
`skills/ceo-review-lite` and are what runtime symlinks point to.

### `AGENTS.md` / `CLAUDE.md` / `SOUL.md`

- No proposed changes from this week’s evidence.

## Skill references: proposed updates

- No new “good/bad examples” captured this week that are specific enough to
  promote. The most actionable recent examples were flightscope + iMessage,
  but they are better kept as project checkpoints for now.

## Open threads worth keeping active (not core-file edits)

1. **Rotate/move any previously-exposed keys** that lived in plaintext runtime
   config before the credential-shape cleanup.
2. **Deliberate `knowledge/` vault reconciliation:** `knowledge/` is its own Git
   repo and remains behind remote with local deletes + new raw imports; handle
   as a dedicated pass so it doesn’t pollute AI-OS memory work.
