---
date: 2026-06-07
time: 16:43
project: websites/freeride-tarifa
status: in-progress
next-session: Continue visual QA from the local preview at http://127.0.0.1:8097/, especially instructors, map sizing, rent page polish, and whether this direction is client-review ready.
---

# Session: Freeride Tarifa Static Preview Iteration

## What we worked on

- Continued the Freeride Tarifa static preview in `projects/websites/freeride-tarifa/`.
- Kept the hybrid direction: cinematic homepage hero, calm rail-style homepage sections, and separate top-level pages for Lessons and Rent gear.
- Added a new `rent.html` page and a three-tab nav: `Freeride`, `Lessons`, `Rent gear`.
- Reworked public section headings so the large headings are direct labels, not explanatory headlines.
- Updated Location and Instructor sections with exact assets Annabel provided or approved.

## Decisions made

- Use direct section titles as the visible heading norm:
  - Homepage: `About Freeride`, `Instructors`, `Location`, `Options`
  - Lessons: `Lessons`, `Pricing`, `Course roadmap`, `IKO certification syllabus`
  - Rent: `Rent gear`, `Prices`, `Rider level`, `Rescue card`
- Remove small green kicker headings such as `Lessons` and `Pricing` when they duplicate the main heading.
- Do not list a school base. Freeride does not have a fixed base. Removed the old Hostal Africa / Calle Maria Antonia Toledo copy.
- Location spots should be `Los Lances`, `Palmones`, and `Valdevaqueros`.
- Use the exact map image from `assets/tarifa-kite-spots-map.png`, not the previous local SVG map.
- Use the exact Vanessa image from `assets/vanessa-kitesurf.jpg`.
- Vanessa's card should align with Olivier and Certified coaches. Her image currently fills the same `24rem` image block with `object-fit: cover`.

## Open questions

- Whether Vanessa's full-bleed crop is acceptable or should be nudged with `object-position` to show more face/board.
- Whether the map image should stay inside the current split Location layout or become wider/full-width for readability.
- Whether `Palmones` spelling should remain as corrected, or match Annabel's earlier typed `Polmones`.
- Whether the Rent gear page should become more visual/editorial after the first structured version.
- Whether instructor photos for Olivier/coaches should be replaced with more accurate official team photos.

## Next steps

- Review the current preview at `http://127.0.0.1:8097/`.
- Check desktop and mobile for:
  - Instructor card crop and alignment.
  - Map size/readability in Location.
  - Rent page first viewport and pricing sections.
  - Three-tab nav wrapping on mobile.
- If direction is approved, consider preparing client-review notes or moving toward an editable platform plan.
- Before committing, remember `projects/websites/freeride-tarifa/` is currently untracked inside a very dirty AI-OS tree.

## Context to preserve

- Files currently relevant:
  - `projects/websites/freeride-tarifa/index.html`
  - `projects/websites/freeride-tarifa/lessons.html`
  - `projects/websites/freeride-tarifa/rent.html`
  - `projects/websites/freeride-tarifa/assets/vanessa-kitesurf.jpg`
  - `projects/websites/freeride-tarifa/assets/tarifa-kite-spots-map.png`
- Local preview server was running at `http://127.0.0.1:8097/`.
- Browser QA during the session repeatedly showed `0` console errors after updates.
- Freeride factual/assets sources used:
  - `https://freeridetarifa.com/es/escuela-de-kitesurf-en-tarifa/`
  - `https://freeridetarifa.com/kitesurf-rental-tarifa/`
  - Vanessa image URL provided by Annabel: `https://freeridetarifa.com/wp-content/uploads/2020/03/Ecole-De-Kitesurf-Tarifa-Freeride-freeridetarifa.jpg`

## System refinement candidates

- For client site previews, when Annabel says "insert these images exactly," ask for/upload/use actual file paths immediately. Inline chat images are not enough to copy into the repo.
- Strengthen the website refresh guidance: avoid duplicated kicker-plus-heading patterns unless the kicker adds different information.
