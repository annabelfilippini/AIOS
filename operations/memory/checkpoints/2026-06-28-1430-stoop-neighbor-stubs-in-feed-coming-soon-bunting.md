---
date: 2026-06-28
time: 14:30
project: stoop
status: in-progress
next-session: Build #3 the parent view — the approve-orders / see-the-money rail (project doc calls it load-bearing)
---

# Session: Stoop — neighbor stubs in the feed, coming-soon toast, site-wide bunting

Follows `2026-06-28-1258-stoop-stand-neighborhood-step.md`. All work in the single
file `projects/stoop/index.html`. Tracker: `projects/stoop/in-progress.md`.

## What we worked on
Picked the checkpoint's recommended next move (#2: make the feed feel real), then
two small follow-ups Annabel asked for in the same session.

## What shipped
**Verified last session's fix first.** Confirmed the neighborhood-step fix (stand
creation always shows the geo picker, pre-filled for returning sellers) works live in
the preview — it was only static-traced before. No longer an unverified item.

**#2 Neighbor stubs in the feed.** The home feed used to show only the user's own
stand (Delaney) + the add-stand CTA — read as a one-stand demo.
- Hood-tagged `NEIGHBORS` (Mateo/honey, Priya/bracelets) with `hood:'country-club'`
  so they survive the `inFeed` geo filter.
- Rendered them in `renderHome`. Factored the card markup into one
  `standCard(p, onclick)` helper now shared by the real stand and the stubs.
- Geo filter intact: Hilltop buyer sees 0 stubs, Country-Club buyer sees both.

**Coming-soon toast.** Stubs have no real page, so a tap fired nothing (cards have
`cursor:pointer` → felt broken). Added a minimal toast (fixed pill, CSS + 4-line
`toast()` helper, 1.9s auto-dismiss). Stub tap → "<name>'s stand is coming soon";
real stand still opens its page. Apostrophe in the name escaped in the inline onclick.

**Site-wide bunting.** Annabel liked the flag strip at the top and wanted it on the
whole site. `go()` was hiding `#bunting` on every view except home — removed that one
toggle line. Bar isn't sticky, so the strip is just a flow element at the top of each
view. Verified `display:flex` on welcome/home/profile/onboard/neighborhood.

## Decisions made
- Both stubs tagged to the demo's default hood (`country-club`) so they reliably show
  in the no-account, seller, and Country-Club-buyer views — over splitting them across
  hoods, which would have hidden one in the common case.
- Stub cards are display + toast only (no real page behind them yet) rather than routing
  to Delaney's page as a placeholder, which would misrepresent them.

## Open questions
- None new. Prior empty-feed UX question (just-CTA vs "invite a neighbor" prompt) still open.

## Next steps
- **#3 Parent view** — approve-orders / see-the-money rail. Not built; project doc calls
  it load-bearing. Recommended next move now that the front-of-house feed feels complete.
- Multi-stand feed (needs a backend); wire stub cards to real pages once stands persist.
- Richer empty-feed state; real SMS/backend confirmations; per-week "copy to next 4 weeks".

## Context to preserve
- Drove the live preview this session (port 8762 free). python3 http.server + a
  cache-busting `?v=Date.now()` reload was needed — the browser held a stale copy of
  index.html until the query-string bust.
- Data model unchanged: `account={role,hoods:[],contact?,name?}` in `stoop-account-v1`;
  one `profile` in `stoop-profile-v2`. `inFeed(p)`: seller/no-account → all; buyer →
  `account.hoods.includes(p.hood)`.
- New shared helper `standCard(p, onclick)` renders any feed card; `p` reads
  name/age?/title/blurb?/loc?/price/unit?/theme/photo?/emoji?.

## System refinement candidates
- None this session.
