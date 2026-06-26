---
date: 2026-06-19
time: 10:40
project: style-feed (personal shopping feed, "The Edit")
status: in-progress
next-session: Occasion/use-case filter shipped (Work / Casual / Going out / Active / Vacation chips that cross-filter with the category tabs). Natural next moves: (1) add a free-text search box if chip buckets feel too coarse; (2) tune the occasion regexes if any bucket feels off after real use; (3) resume the earlier backlog — add another old-money store (Sézane/Tuckernuck), full Aritzia pull, recover the 1 dropped Lululemon tile.
---

# Session: The Edit — occasion / use-case filter ("show me work clothes")

## What Annabel asked
Make results more "caterable" — e.g. ask for work clothes and have the feed
know which pieces work for work and pull them up.

## What shipped
Occasion filter, orthogonal to the existing garment-category sidebar. Six chips
in the main header: All / Work / Casual / Going out / Active / Vacation. They
cross-filter (AND) with the category tabs, so "Work + Bottoms" = tailored
trousers + midi skirts only. Counts on each chip respect the active tab, and the
tab counts respect the active chip.

## How it works (no re-scrape needed)
Every item is already AI vision-tagged with a `formality` axis (loungewear →
casual → smart-casual → formal → evening) plus fabric/silhouette/length. New
`occasions_of(it)` in build_feed.py derives a use-case list from formality
(primary) + fabric/silhouette + title keywords + brand:
- **work**: formality smart-casual/formal OR WORK_RE (blazer/trouser/tailored/
  oxford/loafer/...); excluded if athleisure brand/active keyword or swim.
- **active**: athleisure brand (lululemon/alo/varley/set active/...) OR
  ACTIVE_RE (legging/sports bra/jogger/...) OR formality loungewear. Active
  also BLOCKS work.
- **going-out**: formality formal/evening OR silhouette bodycon OR GOINGOUT_RE.
- **vacation**: swim cat OR fabric linen OR VACATION_RE (crochet/cover-up/resort).
- **casual**: formality casual/smart-casual OR CASUAL_RE (jean/tee/sneaker/...).
Multi-tag allowed (tailored trouser = casual + work). Emitted as `data-occ` on
each card, mirrored by JS `matchOcc()` in the live filter.

## Verified (Playwright on localhost:8801)
- Chips render: Work 145 · Casual 393 · Going out 80 · Active 25 · Vacation 82.
- Work filter: 145 visible, 0 non-work leaks, all tailored tops/oxfords/trousers.
- Work + Bottoms cross-filter: 4 items, all wide-leg/tailored pants + midi skirt,
  0 leaks; count label + tab count both = 4.
- occbar sits above the grid; hidden on the Loved view; Reset clears occ to All.
- Empty-occ items (181) are exactly beauty/jewelry/scarves/home — occasion-
  neutral by design; only 1 top + 2 bags fell through (negligible).

## Files touched
- build_feed.py: + occasions_of() and ATHLEISURE/ACTIVE_RE/WORK_RE/GOINGOUT_RE/
  VACATION_RE/CASUAL_RE; data-occ on cards; .occbar/.chip CSS (+ mobile rule);
  JS occ state, matchOcc, chip handlers, cross-filter counts in applyView, reset;
  OCC_DEFS + occbar render injected into main_html.
- feed.html rebuilt; ~/Desktop/the-edit-feed.html refreshed by the build.
