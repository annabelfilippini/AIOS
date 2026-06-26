---
date: 2026-06-14
time: 13:50
project: websites / freeride-tarifa
status: in-progress
next-session: Added Mathieu-Crepel-style scroll reveal + a partners logo grid to index.html (homepage only). "Mathew's website" = Mathieu Crepel, mathieu-crepel.com (the project's North Star reference, in design.md). Scroll reveal = IntersectionObserver adds .in (fade + 30px lift, 0.75s) to .reveal elements; full-bleed wind chapter also slow-zooms via .reveal-zoom; staggered choice/crew cards via --rd; prefers-reduced-motion respected + no-IO fallback. Partners = 4x2 logo grid (2-col mobile) of Free Ride's 8 real advertised partners (Eleveight, Ketos, Mystic, Billabong, Kitetrip Planner, Jeewin, Nereide, Surfrider), logos grayscale+0.45 opacity by default, full colour + scale-up + white cell on hover ("logo appears" = his look, adapted to logo-only assets). Logos saved local in assets/web/sponsors/ (16 files, from Free Ride's own homepage). OPEN: (1) confirm grid-hover vs the dropped cursor-follow name-list variant; (2) roll scroll-reveal out to lessons/rent/tarifa/stay; (3) get partner-logo clearance before any live launch. Preview launch name resolves to "freeride" on port 8792; serves freeride-tarifa as root; cache-bust ?v=. NOTE: Claude_Preview only paints top-of-page reliably + viewport width oscillates (reload+explicit 1280 resize workaround); IntersectionObserver breaks after in-page reload in the preview (fine in real browsers). Playwright screenshot hit a 5s capture timeout on this animation-heavy page.
---

# Session: Freeride scroll-reveal animations + Crepel-style partners logo grid

## What we worked on

Annabel: "i like how mathew's website flows... when you scroll down images appear
popping up. can you try to do that with the freeride site? also... make their
sponsors look like mathew's... when you hover over the sponsor their company logo
or image appears." Resolved "Mathew" = Mathieu Crepel (mathieu-crepel.com),
already the documented North Star reference in design.md. Scoped to index.html.

## What shipped (index.html)

- **Scroll reveal.** One IntersectionObserver toggles `.in` on `.reveal` /
  `.reveal-zoom` elements as they enter view: fade + 30px lift (0.75s
  cubic-bezier). Applied to positioning band, wind chapter (+ slow 1.14->1 image
  zoom via `.reveal-zoom`), the three choice cards (staggered with inline `--rd`),
  crew heading + both crew cards, reviews head, partners, and CTA. Hero left
  visible (above the fold). `prefers-reduced-motion: reduce` shows everything
  instantly; non-IO browsers get a fallback that reveals all.
- **Partners logo grid** (new section before the CTA), matching Crepel's real
  partners block (confirmed this session: a grid of muted logos on a pale field
  that come alive on hover; his scroll is literally "sections fade and move up").
  4x2 grid (2-col mobile), thin dividers, eyebrow "Who we ride with" + "Our
  partners". 8 real partners Free Ride advertises, each cell a link. Default =
  `grayscale(1)` + opacity 0.45 + slight scale-down; hover = white cell +
  `grayscale(0)` + opacity 1 + scale(1.05). Touch shows full-colour logos.
- **Assets.** 16 partner images downloaded from Free Ride's own homepage into
  `assets/web/sponsors/` (a wordmark + a secondary mark per brand; all are Free
  Ride's blue-recoloured logos, no action photos).
- **Considered then dropped.** First pass was a vertical name list with a
  cursor-following logo card (honoured the words but did not LOOK like Crepel's
  grid). Replaced with the grid for fidelity to the named reference; removed the
  cursor-follow JS. Can revert if Annabel prefers the flashier version.
- **Docs updated.** design.md iteration log (2026-06-14 entry) + content.md (new
  "Partners and sponsors" section with the 8 brands, links, local-asset + logo
  clearance note).

## Verification

- No console errors. Below-fold `.reveal` elements start hidden (opacity 0,
  translateY 30px) and flip to visible (opacity 1) on scroll. All 8 partner logos
  load (naturalWidth 250). Grid grayscale by default, full colour on hover
  (captured a screenshot of the grid with Mystic hovered). Hero renders; reviews
  marquee + 2 crew videos still intact; no stale list/reveal refs.

## Open questions / next

1. Grid hover vs the dropped cursor-follow name-list reveal: confirm direction.
2. Roll scroll-reveal out to lessons.html / rent.html / tarifa.html / stay.html.
3. Partner-logo trademark clearance before any live client launch.
4. Carried from prior sessions: Shopping section, OSM-vs-Google map, Oleg/Leah
   unconfirmed names, hotel Google review-count verification.
