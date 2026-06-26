---
date: 2026-06-07
time: 11:54
project: personal-travel / projects-websites / copenhagen-trip
status: complete
next-session: Open the Copenhagen planner, reload the file URL, and decide whether the route-order sketch is enough or should become a true embedded/live map.
---

# Session: Copenhagen planner redesign and image cleanup

## What we worked on

Annabel asked to continue the Copenhagen short-trip planner redesign from the
checkpoint and `projects/websites/design.md`. The planner was recreated as a
single static HTML site at
`projects/websites/copenhagen-trip/copenhagen-trip-planner.html`.

The first redesigned version kept the useful planner concept but made it more
editorial: full-bleed Copenhagen hero, serif/italic typography, dark/cream
sections, day tabs, editable stops, Google Maps route links, place cards,
bath/dinner options, and shopping cards.

Annabel then clarified two issues:

- The site map graphic was not correct.
- Shopping images repeated too much. Future site work should either use all
  distinct images in a card set or no images, and shopping should prefer store
  images or Google Maps-style lookup imagery when possible.

## Decisions made

- Keep the planner as a static local HTML file for now.
- Replace the faux geographic map with a route-order sketch and a clear note:
  it is not a live map, and Google Maps should be used for exact streets,
  reviews, and transit.
- Add a durable image rule to `projects/websites/design.md`: do not repeat the
  same image across multiple cards in the same content set; either source
  distinct images for every card or remove images from that set.
- Remove the repeated shopping product-thumbnail strips.
- Use one unique shop/source image per shopping card.
- Rename shopping card CTA from "Google Maps" to "Maps photos" so Annabel can
  jump to live Google Maps listings/reviews/photo galleries.

## Open questions

- Whether the route-order sketch now feels acceptable, or whether Annabel wants
  a true map embed/module.
- Whether place and bath cards should also be upgraded to real location/source
  images instead of some generic atmospheric images.
- Whether the planner should become a reusable travel-planner template under
  `projects/websites/`.

## Next steps

- Reload
  `file:///Users/annabelfilippini/Documents/AI-OS/projects/websites/copenhagen-trip/copenhagen-trip-planner.html`
  in the in-app browser.
- Review the updated route-order sketch visually.
- Review the shopping section and decide if any saved-list shops should be
  removed, reordered, or replaced based on current trip needs.
- If continuing polish, replace remaining generic place/bath imagery with real
  source/location images and possibly add a "No image available, open Maps
  photos" fallback pattern.

## Context to preserve

- Trip dates: Friday June 5 to Sunday June 7, 2026.
- Base: Urban Camper Hostel, Lygten 2C, 2400 Copenhagen NV, near Nørrebro
  Station.
- Planner route strategy: one full Saturday plus two travel edges.
- Saturday route core: Urban Camper, Superkilen, Assistens Cemetery, Nørreport,
  Rosenborg, King's Garden, La Cabra Møntergade, Torvehallerne, shopping,
  Nyhavn, Amalienborg, Marble Church.
- Shopping cards now include 12 unique images for 12 cards, with no duplicate
  shop images detected during QA.
- QA completed on local preview: script parses, desktop loads, mobile 390px
  loads, no broken images, no horizontal overflow.

## System refinement candidates

- Carry the "no repeated images within a card set" rule into future website
  builds in `projects/websites/`.
- For travel/shopping cards, prefer live Maps links for reviews/photos and
  direct official/source images for static previews. Avoid scraping or pretending
  Google Maps images are embedded when they are only linked.
