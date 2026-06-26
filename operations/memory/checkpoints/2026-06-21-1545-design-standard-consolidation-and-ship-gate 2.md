---
date: 2026-06-21
time: 15:45
project: aios / design-standard (global design.md + website Ship Gate)
status: complete (all edits made + hook verified; no follow-up blocking)
next-session: Nothing required. Optional: when the next website is built, watch whether the Ship Gate actually catches the recurring misses in practice and tighten wording if anything still slips. The hook + skill gate now run it automatically.
---

# Session: Global design standard consolidated + website Ship Gate created

## What this session resolved

Two linked asks: (1) read every design.md and bring the global design standard
current, point the global CLAUDE.md at it; (2) solve the recurring friction that
Annabel keeps re-giving the same website feedback. Root cause found: the rules
already exist in the docs but are consumed as start-of-build vibes, never checked
against the finished page. Fix = a binary pre-delivery gate, wired to fire
automatically.

## 1. Global design trunk rewritten

- **`~/.claude/design.md`** grew from a slim ~70-line file into the real
  universal trunk. Added the durable taste that previously only lived in project
  files: the six **vibe lanes** (soft editorial/luxury, experimental
  black/poster, outdoor travel, kinetic documentary, data-forward instrument,
  soft UI/dashboard) + the warm-editorial house language for personal tools;
  Hero, Photography/licensing, Maps sections; a real Anti-patterns / AI-slop
  list; Proven reusable patterns (venue grid, sponsor photo-hover, data-shaped
  empty state, left scroll rail); references-are-ingredients + don't-rebuild +
  don't-template process rules. Kept it project-agnostic (no client/brand/URL
  names). Added pointers to the two deeper libraries instead of duplicating them.
- **`~/.claude/CLAUDE.md`** — the design pointer was a buried one-liner under
  Working Style. Promoted it to a bolded directive covering website + app +
  dashboard + general style work, naming the website taste library
  (`projects/websites/design.md`) and the audit index
  (`knowledge/wiki/design-library.md`).

Judgment call recorded: treated `~/.claude/design.md` as THE global trunk (what
CLAUDE.md points to); kept `projects/websites/design.md` as the deep website
library and had the trunk point to it, rather than merging the two and creating
duplication. Annabel agreed the design.md files should cross-point and evolve.

## 2. The recurring-feedback fix (Ship Gate)

Core insight: there are two kinds of guidance, and they'd been blended in prose.
**Art direction** (lane, references, imagery, rhythm) is MEANT to vary — that's
uniqueness. **Craft hygiene** (real headings, no orphan subtitles, clean
punctuation, clear/sourced images, honest nav) is invariant — that's the stuff
Annabel keeps repeating. Locking the hygiene into a checklist protects BOTH:
hygiene consistent, art direction free. The gate touches zero look-and-feel
decisions, so it doesn't push sites toward sameness.

Built as three layers, each closing a different gap:

- **Checklist (the what):** new **Ship Gate** section at the top of
  `projects/websites/design.md` — 9 binary pass/fail items (real headings, no
  orphan subtitles, clean punctuation, clear/well-framed images, really-sourced
  images via gallery-dl etc., fact-checked copy, honest nav, one lane held,
  browser-verified). "Fix failing items, do not present and explain."
- **Skill gate (auto-run in the workflow):** `client-website-refresh/SKILL.md`
  got a new Operating Loop step 7 (run the gate before showing Annabel),
  renumbered the rest, a References pointer, and a hard guardrail. The prose QA
  file `references/html-preview-quality.md` now ends pointing at the Ship Gate as
  the binary final check so the two can't drift.
- **Hook backstop (catches work that bypassed the skill):** extended
  `~/.claude/hooks/update-design-docs.sh` so the **Ship Gate reminder fires
  whenever buildable site files (.html/.css/.js/...) changed** under
  projects/websites/, independent of the existing doc-staleness nudge (which
  still appends only when design.md/content.md weren't touched). Switched JSON
  emission from a static heredoc to `jq -n` for safe encoding of the dynamic
  message.

## Verification

- Hook: `bash -n` clean; tested both branches with fake transcripts — (A) site
  work + no doc update → gate + doc reminder; (B) site work + doc update → gate
  only. Both valid JSON. Test markers cleaned so the next real session isn't
  suppressed.
- Doc edits applied via Edit/Write (no separate render to verify — they're docs).

## Files touched

- `~/.claude/design.md` (rewritten trunk)
- `~/.claude/CLAUDE.md` (prominent design pointer)
- `projects/websites/design.md` (Ship Gate section added)
- `skills/client-website-refresh/SKILL.md` (loop step + reference + guardrail)
- `skills/client-website-refresh/references/html-preview-quality.md` (final-gate pointer)
- `~/.claude/hooks/update-design-docs.sh` (Ship Gate reminder + jq encoding)

## Open / next

- Nothing blocking. Validate the gate against a real next-site build and tighten
  any item wording that still lets a miss through.
- Not done (deliberately deferred earlier, now also covered by the hook): no
  separate mechanism beyond the three layers above.
