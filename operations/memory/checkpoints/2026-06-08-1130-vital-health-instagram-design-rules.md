---
date: 2026-06-08
time: 11:30
project: websites / vital-health-review
status: in-progress
next-session: design.md is now Claude's rulebook for Vital Health Instagram posts (not a team self-service doc). Three example carousels live beside it in media/, hormone-optimization (canonical), what-are-peptides, and regenerative-medicine. Render from any carousel folder with NODE_PATH=/Users/annabelfilippini/Documents/AI-OS/projects/pickleball-portal/repo/node_modules node render.mjs.
---

# Vital Health Instagram — design.md as Claude's rulebook

## Where to start next session

`projects/websites/vital-health-review/media/design.md` is now my (Claude's) own rulebook for Vital Health Instagram posts, not a team self-service doc. Three carousels live next to it as examples:

- `media/2026-06-07-hormone-optimization-carousel-fresh/` — re-rendered to match the new rules. Canonical example of the hormone topic theme kit.
- `media/2026-06-08-what-are-peptides-carousel/` — stress test, peptide theme kit (cream + paper + terracotta).
- `media/2026-06-08-regenerative-medicine-carousel/` — stress test, new regenerative theme kit (paper + cream + gold).

Render command (from any carousel folder):
`NODE_PATH=/Users/annabelfilippini/Documents/AI-OS/projects/pickleball-portal/repo/node_modules node render.mjs`

## Decisions

- design.md is rules for Claude, not for the Vital Health team. Reframed accordingly.
- Hummingbird is fully specified: 80 px tall, 60/60 anchored, slide outer corner, every slide, color follows the 200 × 200 region directly under it.
- Cover slides are allowed to be cinematic. Info slides must be a uniform system that carries the cover's theme kit.
- Every carousel writes down its topic theme kit (field, card, accent, motif) at the top of post.md before drafting. Five standing motifs and four canonical kits are documented.
- Short 5-slide arc added alongside the existing 7–8 slide arc.
- Eyebrow micro-kicker, italic offer line, frame-cell grid, italic pull caption — all formalized as slide-level conventions.
- Pre-ship audit checklist added at the bottom of design.md.

## Open Questions

- The brand has exactly one photographic still-life PNG. Two test carousels share it (different crops + palette). A third topic that needs a different motif (labs / molecule lines, menopause / leaves only, patient-journey / cream linen) will need either a small photo batch or AI image generation. Worth deciding before shipping more topics.
- The hormone carousel was re-rendered locally but not pushed anywhere. If it should replace the current scheduled Instagram post, that is a separate handoff.
- Whether `skills/instagram-carousel/references/style.md` should be updated with the new bird-on-photo and motif-sharing rules so they apply across all brands, or stay project-specific.

## Next Steps

- If Annabel approves the hormone carousel re-render, swap in the new slide PNGs as the published version.
- If a new topic comes up (labs, menopause, peptides without reusing the existing photo), generate a small set of new still-life images or extend the kit using CSS-rendered motifs.
- Promote the bird-on-photo rule to `skills/instagram-carousel/references/style.md` if it generalizes.

## Files Touched

- `projects/websites/vital-health-review/media/design.md` — major rewrite, ~5 new sections.
- `projects/websites/vital-health-review/media/2026-06-07-hormone-optimization-carousel-fresh/index.html` + 4 new slide PNGs.
- `projects/websites/vital-health-review/media/2026-06-08-what-are-peptides-carousel/` — new (index.html, render.mjs, post.md, 5 slide PNGs).
- `projects/websites/vital-health-review/media/2026-06-08-regenerative-medicine-carousel/` — new (index.html, render.mjs, post.md, 5 slide PNGs).
