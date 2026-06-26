---
date: 2026-06-07
time: 12:27
project: projects-websites/design-preferences
status: complete
next-session: Use the updated design.md rules before the next website preview; avoid automatic eyebrow labels, hero proof strips, and slogan-like section headers.
---

# Session: Wayloft timeline website design preference test

## What we worked on

- Built and iterated a static Wayloft timeline concept site:
  `projects/websites/wayloft-timeline/index.html`
- Used it to test `projects/websites/design.md` against a rich,
  credit-card-forward travel website direction.
- Refined the page through Annabel's live feedback in the in-app browser.
- Regenerated local QA screenshots in:
  `projects/websites/wayloft-timeline/desktop-playwright.png`
  `projects/websites/wayloft-timeline/mobile.png`
  `projects/websites/wayloft-timeline/potential.png`

## Decisions made

- A brand word is not a sentence. Do not add punctuation to large wordmark
  hero type unless the actual brand includes it.
- Hero pages do not need automatic proof strips, three summary cells, or fact
  rows when the image, brand, and copy already carry the section.
- Small uppercase eyebrow labels are optional. Remove them when they repeat the
  heading or do not add real orientation.
- Direct explanatory headings should stay in one font and color. Do not add
  italics or accent colors just to make them feel designed.
- Section headers should be concrete and scannable. Avoid vague metaphor
  headings when a reader cannot tell what the section is about.
- Timeline/item headers should read like labels, with no trailing periods.
- If a clear explanatory header is too long for huge display type, use a short
  big title and put the explanation underneath as a smaller subhead.

## Open questions

- Whether the Wayloft preview should remain a taste-test artifact or become a
  more complete public concept page.
- Whether future website previews should generate a small "design lessons"
  note automatically when Annabel gives repeated visual corrections.

## Next steps

- Use `projects/websites/design.md` before the next website preview.
- When building the next site, choose one dominant vibe lane and check for
  unnecessary repeated modules before presenting it.
- Refresh or reopen the Wayloft page if continuing visual review:
  `file:///Users/annabelfilippini/Documents/AI-OS/projects/websites/wayloft-timeline/index.html`

## Context to preserve

- Annabel likes the boujee, dramatic, editorial travel-credit direction, but
  wants it to stay clear and intentional rather than slogan-heavy.
- The page got better when it became simpler: `WAYLOFT` hero, no hero fact
  strip, concrete timeline labels, and fewer redundant eyebrow labels.
- `projects/websites/design.md` was updated during this session to capture
  these preferences.

## System refinement candidates

- Consider a tiny website QA checklist that asks: "Does every eyebrow label
  add orientation? Does every section header describe the section? Did we add
  a proof strip by habit?"
