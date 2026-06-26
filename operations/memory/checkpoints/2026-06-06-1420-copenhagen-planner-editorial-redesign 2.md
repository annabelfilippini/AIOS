---
date: 2026-06-06
time: 14:20
project: personal-travel / projects-websites
status: paused
next-session: Recreate/redesign the Copenhagen planner in projects/websites/copenhagen-trip with the editorial visual direction from projects/websites/design.md.
---

# Session: Copenhagen planner editorial redesign direction

## What we worked on

Annabel asked to turn the Copenhagen short-trip checkpoint into a local HTML
planner with day tabs, walking routes, editable stops, Google Maps routing, and
practical place/shop information. A first functional version was built and
served locally, but Annabel clarified that the look was not aligned with her
new website taste references.

Annabel then created a `projects/websites/` collection idea and asked for a
design file there. `projects/websites/design.md` now captures the first design
preference batch: cinematic, editorial, full-bleed, photo-led, boutique, serif
and script typography, cream/black/green/pink palettes, atmospheric imagery,
and minimal copy.

Annabel also uploaded a route/map inspiration screenshot: clean white layout,
bold route title on the left, simplified neon-lime map illustration on the
right, and concise route copy. This should influence the route module.

## Decisions made

- Keep the Copenhagen planner concept. The utility is right.
- Redesign the visual system. The first planner felt like a practical
  dashboard, while Annabel wants an editorial travel companion.
- Keep the work under `projects/websites/`, with future sites collected there.
- Use `projects/websites/design.md` as the shared design preference source.
- The redesigned Copenhagen planner should still support day tabs, editable
  route stops, add/skip/done/reorder behavior, and Google Maps route links.
- Add richer place cards: description, Google Maps review link, and practical
  reasons to go.
- Add better shopping cards with enough product/vibe detail and imagery cues so
  Annabel can decide based on what she needs that day.

## Open questions

- The previously built `projects/websites/copenhagen-trip/copenhagen-trip-planner.html`
  was no longer visible on disk after a context/environment shift, though the
  browser had shown it earlier. Recreate it rather than assume it exists.
- Need current place/shop research for Copenhagen: Google Maps links, reviews
  access links, official/shop pages where available, and image/product cues.
- Decide whether to use real external images, generated editorial placeholders,
  or CSS/illustrated map treatments for the first redesign pass.
- Decide whether the route map should be a live Google iframe, a stylized
  editorial map module, or both.

## Next steps

- Update `projects/websites/design.md` with the new route-map preference:
  clean white route explainer, strong title, concise description, simplified
  neon-lime map linework, and pin markers.
- Recreate `projects/websites/copenhagen-trip/copenhagen-trip-planner.html`.
- Rebuild the UI in the new direction: full-bleed Copenhagen hero, elegant
  serif/italic typography, dark/cream editorial sections, day tabs that feel
  designed, and route/shop panels that are useful but not dashboard-like.
- Research and add Google Maps links for key stops: Urban Camper, Superkilen,
  Assistens Cemetery, Nørreport, Rosenborg, King's Garden, La Cabra,
  Torvehallerne, Nyhavn, Amalienborg, Marble Church, AIRE, La Banchina,
  CopenHot, Cantina, Gasoline Grill, and shopping stops.
- Add shopping options with vibe/product notes for OSV Second Hand, AMAV II,
  Crush Vintage, Pico, Sui Ava, A.KJAERBEDE, Ganni, Norse Projects, Alohas,
  Naked, and other TikTok-derived candidates from the checkpoint.
- Run browser QA after rebuilding, including desktop and mobile-ish widths.

## Context to preserve

- Trip dates: Friday June 5 to Sunday June 7, 2026.
- Home base: Urban Camper Hostel, Lygten 2C, 2400 Copenhagen NV, near
  Nørrebro Station.
- Route strategy from checkpoint: one full Saturday plus two travel edges.
- Saturday core: Superkilen / Assistens if energy allows, Nørreport,
  Rosenborg and King's Garden, La Cabra Møntergade, Torvehallerne, shopping,
  Nyhavn / Amalienborg / Marble Church, then bath/sauna or dinner.
- Best bath recommendation from prior checkpoint: AIRE for reliability; La
  Banchina and CopenHot are more atmospheric but less convenient and more
  availability-sensitive.
- Annabel's taste signal: the planner should feel more like a beautiful
  editorial Copenhagen mini-site than an admin itinerary dashboard.

## System refinement candidates

- Future website builds in `projects/websites/` should read
  `projects/websites/design.md` before styling.
- For travel planners, pair the functional route editor with an editorial
  presentation layer instead of default app/dashboard styling.
