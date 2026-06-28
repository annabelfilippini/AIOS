---
date: 2026-06-28 12:00
project: stoop
status: in-progress
type: checkpoint
slug: stoop-batch2-account-front-door
---

# Stoop — Batch 2: account front door (account-free browse) shipped

Follows `2026-06-27-1815-stoop-neighborhood-polygons-and-flow.md`. All work in the
single file `projects/stoop/index.html`. Tracker: `projects/stoop/in-progress.md`.

## What shipped (Batch 2)
The front door + nav chain that ties the screens together, with browsing kept
account-free (account only appears when the user acts).

- **New `#view-welcome`** (front door): role split — "Open a stand" (seller) /
  "Shop the neighborhood" (buyer). Craft-fair lane, two `.role` cards. `chooseRole(r)`
  sets `selMode` ('one' seller / 'many' buyer) + `pendingRole`, routes to neighborhood.
- **`geo-go` rewired** (was just `go('home')`): writes `account {role, hoods:[...]}`
  to localStorage key `stoop-account-v1`, then routes seller→`onboard` (builder),
  buyer→`home` (feed).
- **Account-free browse:** welcome + neighborhood need no account. The account record
  gains `contact`/`name` only on an action — the request modal prefills `contact` from
  the account and persists it (plus kid name) on send.
- **Startup:** account on file → restore `selMode`/`pickedHoods`, skip straight to home;
  else land on welcome. Removed the temporary `#neighborhood` deep link. `geo-back`
  now → welcome (the only entry to neighborhood).
- `.place` top-bar indicator hidden on welcome (content still hardcoded "Country
  Club neighborhood" — that's Batch 3's job).

## Verified in preview (port 8762)
- Buyer: pick multiple hoods → account `{role:buyer, hoods:[...]}` → home.
- Seller: single-select collapses to one hood → account `{role:seller}` → builder.
- Returning visitor (account present) skips welcome, restores hoods + selMode.
- Request flow persists `contact`/`name`; fresh load → null account, empty prefill.
- geo-back → welcome. No console errors.

## NEXT — Batch 3: neighborhood filter + role-aware home
- Tag each stand with its neighborhood id; feed filters to `account.hoods`.
- Top-bar `.place` indicator reads `account.hoods` (currently hardcoded "Country Club").
- Reseed Delaney's stand in Country Club.
- Role-aware home: a buyer shouldn't see Delaney's seeded demo as "your page"
  (owner bar). Decide buyer vs seller home rendering.

## Open / deferred (unchanged from prior)
- Text confirmations need real plumbing (backend + SMS); v1 routes request via `sms:` link.
- Per-week availability "copy to next 4 weeks" (offered, not decided).
- Single profile slot → true multi-kid.
- "Too quiet" release valve for empty neighborhoods.
- Onboard back label still "Back to the neighborhood" → go('home'); minor, left as-is.
