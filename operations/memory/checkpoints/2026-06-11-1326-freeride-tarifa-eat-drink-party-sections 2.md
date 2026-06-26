---
date: 2026-06-11
time: 13:26
project: websites / freeride-tarifa
status: in-progress
next-session: Tarifa page now advertises real venues with live photos/ratings/review links. Open: (1) Hotels section is the next ask, same card pattern, from Free Ride's advertised hotels. (2) Shopping was intentionally skipped this pass, needs better shop photos + fuller list before building. (3) Decide map: shipped a keyless OpenStreetMap embed because Google Maps embed would not render reliably without a paid API key; Annabel may still want the exact Google look (needs API key or a static image). (4) Several venues have no official site / approximate Google review counts (Silos 19, Morena, Tumbao show "Read reviews" instead of a count). Watch the recurring python http.server stale-cache trap (cache-bust with ?v=).
---

# Session: Freeride Tarifa page rebuilt into an Eat / Drink / Party guide

## What we worked on

Annabel wanted the Tarifa page (tarifa.html) to make Tarifa look like a great
place to eat, drink and party, advertising the restaurants/bars Free Ride loves.
Source lists: freeridetarifa.com /the-best-places-to-eat-in-tarifa/ and
/the-most-famous-beach-bars-of-tarifa/. She specifically loves Agua and Balneario
for music and watching pro kiters.

## Changes made (tarifa.html)

- Replaced the illustrated SVG kite-beach map in #spots with a keyless,
  interactive OpenStreetMap embed framed on the kite coast (Valdevaqueros ->
  Tarifa), marker at Los Lances. Google Maps embed was tried first but Google
  refuses to frame the keyless output=embed URL (blank in preview, unreliable
  live without an API key); OSM renders everywhere.
- Removed the town-stats band (incl. the "5 min from beach to old town" stat),
  the text-only favourites grid, and the white-streets + yoga photo trip-grid.
- Rebuilt #after as "Eat, drink and party in Tarifa" with 5 guide blocks:
  Breakfast (Surla, Cafe Azul, Power House, Wanaka), Lunch (Chiringuito Tangana,
  La Burla, El Rancho, Meson El Picoteo), Dinner (El Lola, Ola Ola, Silos 19,
  Morena), Beach bars & nightlife (Agua, Balneario, Tumbao, Waikiki, The
  Chiringuito), Yoga (Respira, Free Your Mind, Holos Terapias).
- Each card = downloaded local photo + name + real Google star chip + review
  count; the whole card links to that venue's Google reviews (target _blank).
  Agua + Balneario carry a green "Freeride pick" tag. Holos has no rating so
  shows a "Yoga & pilates" tag instead of a star.
- New CSS: .guide-block/.guide-head, .venue-grid (+ cols-5/cols-3), .venue card
  with .rate-chip/.vibe-chip/.fave-chip/.review-link. Responsive: grids -> 2col
  at <=860px, 1col at <=520px; .ride-layout now stacks on mobile (was cramped).

## Images

- 20 venue images downloaded to assets/web/venues/ so the page is self-contained.
- IMPORTANT lesson: RestaurantGuru CDN images (img02.restaurantguru.com) are
  watermarked multi-photo collages (cartoon chef mascot) — unusable. Re-sourced
  10 clean single photos from venues' own sites + Tripadvisor dynamic-media-cdn.
  Clean own-site images: cafe-azul, el-lola, silos-19, morena, agua, balneario,
  tumbao, respira, free-your-mind, holos. All 20 visually spot-checked.
- Optimized heavy files (morena png->jpg 2.9MB->336K, silos/tumbao resized to
  1200px). Verified: 0 broken images, 20/20 cards render desktop + mobile.

## Decisions

- Show all real Google ratings including the weak ones (Balneario 3.3, The
  Chiringuito 3.7) per Annabel; Tarifa beach bars get review-bombed on price so
  the star understates the vibe, but she chose honesty over hiding.
- Skip Shopping this pass (research was thin: only SOLOR + Tarifa Soul strong).

## Verification

- Preview served via .claude/launch.json (python http.server, auto-port 8792).
- DOM: 5 guide blocks, 20 venue cards, no town-stats/trip-grid/SVG map. Grids
  resolve 4 / 5 / 3 cols at 1300px; stack on mobile. Map embed renders.

## Design preferences recorded (for next website)

- projects/websites/design.md (global, cross-project taste): added (1) map
  update — real interactive map embed now the default over an illustrated SVG
  when geography is the point, with the OSM-not-Google keyless note; (2) new
  reusable "Local recommendations / venue guide grid" module (photo + name +
  Google rating + review-count, card links to Google reviews, grouped by
  category, optional "[Brand] pick" tag); (3) promotional/directory licensing
  exception — using a venue's own photo to advertise it is wanted, but never use
  watermarked aggregator (RestaurantGuru) collages; prefer own-site/Tripadvisor,
  download locally, spot-check.
- projects/websites/freeride-tarifa/design.md: added a 2026-06-11 iteration-log
  entry capturing the eat/drink/party guide, the SVG->real-map swap (supersedes
  the 2026-06-10 SVG note), show-real-ratings, and the deferred shopping / next
  hotels ask.
- Memory: reference_venue_image_sourcing.md + MEMORY.md index line.
