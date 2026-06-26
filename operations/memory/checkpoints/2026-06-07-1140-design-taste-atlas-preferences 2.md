---
date: 2026-06-07
time: 11:40
project: projects-websites/design-preferences
status: in-progress
next-session: Use design.md's vibe-lane rule before building the next client/site preview, and avoid defaulting to the four-item fact strip.
---

# Session: Design Taste Atlas + Vibe Lane Clarification

## What we worked on

- Built a static "Annabel Design Taste Atlas" preview to test how
  `projects/websites/design.md` behaves as an actual website brief.
- Preview path:
  `projects/websites/design-taste-atlas/index.html`
- Local generated assets:
  `projects/websites/design-taste-atlas/assets/`
- QA screenshots:
  `projects/websites/design-taste-atlas/desktop.png`
  `projects/websites/design-taste-atlas/mobile.png`

## Decisions made

- The preview intentionally combined multiple liked patterns as a taste mirror:
  cinematic hero, huge serif/italic type, lime accent, cream editorial grid,
  dark article split, experimental black proof band, detail block, and manifesto
  section.
- Annabel liked the range, but clarified that a real client site should not mix
  wildly different vibe worlds unless the brand clearly supports it.
- Updated `projects/websites/design.md` with a stronger rule: choose one
  dominant vibe lane before designing a client site.
- Named four current lanes:
  soft editorial/luxury, experimental black/poster, outdoor editorial/travel,
  and kinetic documentary/person.
- Added explicit guidance that the soft wellness/editorial lane and the
  experimental black/poster lane are different worlds and should usually become
  separate site directions.
- Added a repetition warning: the four-item fact/stat strip is liked, but has
  appeared too often and should not become a default house template.

## Open questions

- Which vibe lane should the next actual client website use?
- Should the Design Taste Atlas remain a diagnostic artifact, or should it be
  split into separate lane-specific mini-sites for comparison?
- Whether to remove QA screenshot files from the preview folder later if this
  becomes a cleaner publishable artifact.

## Next steps

- Before building any new website in `projects/websites/`, read
  `projects/websites/design.md` and explicitly choose one dominant vibe lane.
- For future previews, vary the proof/summary device: pullquote, detail list,
  timeline, single oversized number, editorial table, short checklist, or no
  proof strip.
- If continuing the taste-atlas exercise, create one page per lane so Annabel
  can compare coherent single-vibe sites rather than one combined sampler.

## Context to preserve

- Annabel's key feedback: "if i was creating a website for a client i would
  never want them on the same site"; this should guide future client concepts.
- The dark manifesto/poster section and black point-cloud section are liked, but
  they belong to a bolder experimental lane.
- The softer cinematic/cream/serif sections are also liked, but belong to a
  calmer editorial/luxury lane.
- The four-section/four-fact rhythm works visually but has been overused in
  recent website previews.

## System refinement candidates

- Consider adding a lightweight "vibe lane selected" checklist to any future
  website build workflow.
- If repeated module use continues, add a small preflight note to choose a fresh
  proof/summary pattern before writing HTML.
