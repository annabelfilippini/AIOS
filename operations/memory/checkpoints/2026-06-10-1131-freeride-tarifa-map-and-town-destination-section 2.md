---
date: 2026-06-10
time: 11:31
project: websites / freeride-tarifa
status: in-progress
next-session: Fill the homepage "The town" section photo slots once Free Ride provides owned/permitted venue + town shots (TODO(photos) marker in index.html). Confirm the named favourites (Café Azul, Bar El Francés, Ola Ola, SOLOR) are ones Free Ride is happy to name-check, and re-verify ratings before any launch. Optionally draft the WhatsApp message asking Free Ride for town/venue photos. Watch the recurring browser-cache trap when reviewing on port 8791 (hard-refresh).
---

# Session: Freeride Tarifa map + town destination section

## What we worked on (this session)

- Diagnosed the "Lessons top tab still wrong" report: lessons.html on disk was
  already correct (4 tabs, Lessons active with green underline). The wrong view
  was a stale browser cache of the pre-header-unify copy (3 tabs + BOOK button).
  Fix is hard-refresh / cache bust, not code.
- Rebuilt the tarifa.html "Where to ride" section: replaced 3 reused photo tiles
  with a hand-built on-brand SVG map of the Tarifa coast (town + Los Lances,
  Valdevaqueros, Balneario pinned, ATLANTIC / Strait of Gibraltar / compass /
  distance note). Numbered pins match numbered spot cards beside it.
- Fixed tarifa.html copy/image bugs: title "Four spots" -> "Three spots" (matches
  3 cards and the "3 main kite beaches" fact); removed the misplaced
  "Every level gets real water time" caption and the duplicate street photo
  (cafe.jpg and oldtown.jpg are the same shot); after-kite grid now 2 honest cells
  (old-town street + yoga). Closing CTA swapped aerial.jpg -> grab.jpg so aerial
  appears only in the hero (was reused 4x -> felt like the homepage).
- Rebuilt the homepage (index.html) "A trip, not just a lesson slot" section into
  a real destination pitch: rewritten lead, a real-numbers stat band, and a
  "A few local favourites" row of named, top-rated venues. Anchored by the one
  owned old-town photo as a banner.

## Decisions made

- Tarifa map: on-brand hand-built SVG (no maps API / new infra), geographically
  faithful but stylized. Real interactive/static maps were declined to avoid new
  infra and a third-party look.
- Homepage town section uses REAL, sourced numbers, framed to be defensible:
  "300+" restaurants and "40,000+" traveler reviews (TripAdvisor lists 309 /
  42,023), "4.5-4.8★" for the top tier. Deliberately NOT an exact "4.5+ count"
  because nobody publishes that cleanly and an exact number would be fragile.
- Named favourites in copy is fine (names + ratings are facts): Café Azul ★4.6,
  Bar El Francés ★4.6 (2,000+ reviews), Ola Ola ★4.8, SOLOR boutique
  (Batalla del Salado). Annabel chose "specific named businesses."
- Did NOT place scraped/specific-venue photos. Every image search returned
  paid/copyrighted stock (Dreamstime, Alamy, Getty) or the venues' own
  copyrighted images; using those on a live client site is infringement +
  implied-endorsement risk. Left a TODO(photos) slot instead.

## Files changed

- `tarifa.html` (SVG map + spot cards CSS/markup, title fix, after-kite grid to
  2 cells, CTA image swap to grab.jpg)
- `index.html` (new town/destination CSS: .town-stats/.tstat/.fav-title/.fav-grid/
  .fav/.rate/.town-banner; rewritten #trip section markup with stats + named
  favourites + owned old-town banner + TODO(photos) comment)

## Verification completed

- tarifa.html: DOM-confirmed 4 nav tabs with only Tarifa active; map renders all
  3 pins + old-town marker + labels (collision between old-town label and Strait
  text fixed by repositioning); after-kite shows 2 captioned cells; no broken
  images; CTA uses grab.jpg; aerial.jpg now hero-only.
- index.html: DOM-confirmed stat band (300+/40,000+/4.5-4.8★/5 min), 4 favourite
  cards (Café Azul, Bar El Francés, Ola Ola, SOLOR), banner image loaded.
- Reviewed via Playwright on port 8791 with cache-busting query strings.

## Open questions

- Which town/venue photos can we actually use? Need Free Ride's owned shots or
  per-venue permission/press images before the homepage town section can launch.
- Is Free Ride comfortable name-checking these specific venues (it reads as a
  recommendation)?
- Should the tarifa.html after-kite section get more real town/lifestyle photos
  (bars, plazas, harbor) from Free Ride to feel richer than 2 cells?

## Notes / gotchas

- Recurring trap: python http.server (ports 8791/8792) sends no cache-control,
  so the browser AND Playwright serve stale copies. Always verify on-disk first,
  then cache-bust (?v=N) or hard-refresh before concluding code is wrong.
  Annabel declined adding this to CLAUDE.md this session.
- Image-licensing wall is real: firecrawl image search ignored includeDomains
  and returned paid stock. For free-license needs, go to Unsplash/Pexels/Wikimedia
  directly, not generic image search.
