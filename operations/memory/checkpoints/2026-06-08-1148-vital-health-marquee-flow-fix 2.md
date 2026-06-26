---
date: 2026-06-08
time: 11:48
project: vital-health-webflow-review
status: complete
next-session: Confirm Annabel sees consistent marquee flow with no breaks/empty cards; proceed to Webflow rebuild phase with the same `.rev-marquee` structure once approved.
---

# Session: Vital Health Google reviews marquee flow fixes

## What we worked on

- Diagnosed why Google reviews marquee on
  `projects/websites/vital-health-review/home-review.html` was not flowing
  consistently. Annabel reported "5 cards pass, then a break, then on hover
  a few more pop up," plus screenshot of ghost text on the left edge with no
  card chrome.
- Verified marquee structure is mechanically correct: two identical
  `.rev-marquee-set` blocks of 68 cards each, track width 54,944px, seam
  alignment at sub-pixel precision (0.0005px gap). The "break" was not a
  structural gap.

## Root causes found

1. **Avatar lazy-loading**: all 136 `<img class="rev-card-avatar">` had
   `loading="lazy"`. As cards scrolled into view, each avatar fired a fresh
   request to Google's CDN. Cards appeared with empty avatar circles for a
   beat → reads as "break." Hovering paused the marquee long enough for
   queued image requests to drain, so avatars "popped" in.
2. **Edge-fade + transparent card bg**: `.rev-card` background was
   `rgba(248, 244, 235, .72)` (28% transparent). The wrapper mask-image
   faded edges to transparent. The semi-transparent card bg disappeared
   faster than the dark text, leaving naked text floating without its card
   on the left edge.

## Fixes applied

- Switched all 136 avatar `<img>` tags from `loading="lazy"` to
  `loading="eager" decoding="async"`. All 136 now load in ~4s on page load,
  zero pending after.
- Added `background: #e8e2d3` placeholder to `.rev-card-avatar` so even
  if an image is in-flight, the circle looks intentional cream, not blank.
- Made `.rev-card` background fully opaque (`#f8f4eb`) so cards fade as a
  unit when crossing the edge mask.
- Tightened edge-fade zone from `transparent → #000 6%` to
  `transparent → #000 2.5%` so more of the partial card stays visible
  before it fades.

## Decisions made

- Eager-loading 136 small (40×40) avatars up front is the right tradeoff
  for marquee smoothness; payload is small enough that one-time upfront
  load beats per-card popping.
- Mask edge stays — just narrower — because it still hides the hard seam
  cleanly without creating ghost-text artifacts now that cards are opaque.

## Open questions

- Does Annabel want the mask removed entirely (hard left/right edge) vs.
  the current narrower fade? Current narrower fade is cleaner but still a
  fade.
- For Webflow rebuild: keep static-baked reviews or wire live-sync via
  Google Places API → Make → Webflow CMS? Deferred from prior checkpoint.

## Next steps

- Annabel hard-refreshes `http://127.0.0.1:8765/home-review.html?v=4` and
  watches the marquee run uninterrupted for 30+ seconds.
- If approved, replicate the same `.rev-card { background: #f8f4eb }` and
  eager-loaded avatars when porting to Webflow.
- During Webflow rebuild, decide on live-sync method.

## Context to preserve

- Marquee structure verified bulletproof at:
  track width 54,944px, two sets of 27,472px each, animation
  `rev-scroll 240s linear infinite` translating 0 → -50%.
- The set-wrapper pattern (`.rev-marquee-set` with `padding-right: 24px`
  matching the inter-card `gap: 24px`) is the canonical seam-free recipe.
- All cards 380px flex-basis, 24px gap. 68 unique reviews × 2 sets = 136
  cards. Avatar CDN: `lh3.googleusercontent.com/a-/...`.

## System refinement candidates

- None this session. Friction was specific to this marquee implementation,
  not a pattern-level CLAUDE.md edit. The "always eager-load images that
  enter an auto-scrolling region" lesson is project-specific.
