---
date: 2026-06-07
time: 11:41
project: websites / freeride-tarifa
status: in-progress
next-session: Review the local Freeride preview starting at http://127.0.0.1:8097/ and continue from the mix-and-match direction.
---

# Session: Freeride mix-match two-page direction

## What we worked on

- Iterated `projects/websites/freeride-tarifa/index.html` after Annabel said the Santic-inspired version had the right scroll/rail structure but lost the earlier hero.
- Restored the earlier full-bleed Freeride hero direction on the homepage.
- Kept the calmer Santic-style left rail for the homepage content after the hero: About Freeride, Instructors, Location, Options.
- Split Lessons into a separate prototype page at `projects/websites/freeride-tarifa/lessons.html` instead of leaving it below the homepage scroll.
- Updated `projects/websites/design.md` with the reusable preference: mix and match the best proven pieces across drafts instead of recreating the entire site every iteration.

## Decisions made

- Freeride homepage should start with the cinematic image hero from the earlier draft.
- After the hero, the homepage should become simpler and more Santic-like: white content field, left scroll rail, big black headings, fewer modules.
- Lessons is a true separate top-level page/tab, not a section below the Freeride homepage.
- The Santic reference is about information architecture and scroll behavior, not copying Santic's brand styling literally.
- Future iterations should preserve liked sections unless Annabel explicitly rejects them.

## Open questions

- Whether the homepage after-hero rail content should stay all-white or reintroduce one darker/editorial reset later.
- Whether the Lessons page should keep the simplified pricing table or use a more visual but less busy version of Freeride's current pricing cards.
- Whether instructor photos should be replaced with better verified team-specific assets if Freeride provides them.

## Next steps

- Visually review `http://127.0.0.1:8097/` and `http://127.0.0.1:8097/lessons.html`.
- Continue from this hybrid direction: old hero plus calm left-rail content.
- If the structure feels right, polish copy, section spacing, and image choices rather than rebuilding the whole site again.

## Context to preserve

- Local server is still expected at `http://127.0.0.1:8097/`.
- Files touched: `projects/websites/freeride-tarifa/index.html`, `projects/websites/freeride-tarifa/lessons.html`, `projects/websites/design.md`.
- Mechanical checks passed: no duplicate IDs, no missing hash anchors, no `border-radius` mentions in either HTML page, and `lessons.html` returns `200` locally.

## System refinement candidates

- Add a stronger website-iteration rule: preserve liked sections across drafts and treat new references as composable patterns, not total replacement instructions.
