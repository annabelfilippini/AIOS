---
date: 2026-06-27 18:15
project: stoop
status: in-progress
type: checkpoint
slug: stoop-neighborhood-polygons-and-flow
---

# Stoop — neighborhood map = real boundary polygons + account-free flow decided

Follows `2026-06-27-1745-stoop-onboarding-neighborhood-select.md`. All work in the
single file `projects/stoop/index.html`. Tracker: `projects/stoop/in-progress.md`.

## What shipped this session (map upgrade to Batch 1)
Annabel disliked the center-dot map: selecting Country Club just lit a dot, didn't
show what *qualifies* as the neighborhood. Replaced dots with **real neighborhood
boundary polygons**.

- **Data is now a swappable `CITY` block** (`{name, center, zoom, hoods[], boundaries}`).
  This is the reproducibility answer for other cities: to add Chicago, swap the CITY
  block (pull that city's neighborhood GeoJSON from its open-data portal, trim to the
  hoods you want, keep the same `id` keys). Map/select code is city-agnostic.
- **Denver boundaries** = official "statistical neighborhoods"
  (opendata-geospatialdenver, ArcGIS FeatureServer layer 13), trimmed to the matching
  hoods, coords rounded to 5dp, inlined (~28KB). Endpoint used:
  `services1.arcgis.com/zdB7qR0BtYrg0Xpl/.../ODC_ADMN_NEIGHBORHOOD_A/FeatureServer/13/query?f=geojson&outSR=4326`.
- **Behavior:** selected hood fills its real shape in accent; unselected = faint
  outline (so every region is legible at a glance); map fitBounds to picks.
- **Fallback for no-official-boundary hoods:** a dashed bubble at the label point
  (the path suburbs/small towns without boundary data will use). `buildHoodLayers()`
  draws polygon where `boundaries` has the id, else `L.circle`.
- **Hardened `initGeo`:** rAF re-`invalidateSize()` so tiles fill on first paint
  (was half-filling due to layout settling after the 80ms timeout).

## Decisions locked this session
1. **Crestmoor removed.** It is NOT an official Denver statistical neighborhood
   (city folds it into Hilltop). Hilltop's polygon now covers that ground. Down to
   9 hoods, all with real boundaries.
2. **Browsing is account-free** (Annabel agreed). Account is required only to *act*
   (request a lesson, buy, save, follow), never to look. Avoids rebuilding the
   Nextdoor signup wall; matches link-first ethos. THIS DRIVES BATCH 2 WIRING.
3. Removed the "Nothing from anywhere else. Just these." promise line from the
   summary card (block-card now = label + neighborhood names only).
4. Map hint copy "tap a dot" → "tap a region".

## Flow agreed (the two front doors)
- **Door 1 — kid's link (the v1 wedge):** Delaney shares link → lands on her page,
  no wall → "Request a lesson" → routes to her PARENT (not the kid) → both get
  confirmation → optional soft nudge "see other stands near you?". One kid + one
  link works with no neighborhood populated.
- **Door 2 — browse-first (stoop.com):** land → "Where are you?" (the neighborhood
  picker, NO account) → see feed of those hoods immediately → account prompt only
  when they reach for an action; picked hoods then persist to the account.
- The neighborhood picker serves BOTH: browser homepage (multi) + stand setup (one).

## Preview / how to view
- Server: preview MCP `stoop`, port 8762 (`projects/stoop` via python http.server).
- Nothing links to the neighborhood screen from home yet (that's Batch 2). Added a
  temporary deep link: **`http://localhost:8762/index.html#neighborhood`** lands
  straight on neighborhood select (hash check in startup, `selMode='many'`).
- Verified in preview: 9 hoods, no Crestmoor, polygons fill real shapes, fallback
  path exists, deep link works, no console errors.

## NEXT — Batch 2: account front door (account-free browse)
- Welcome + role split: "Open a stand" → seller (`selMode='one'`) / "Shop the
  neighborhood" → buyer (`selMode='many'`).
- Buyer path: pick neighborhood(s) → feed, NO account gate. Account prompt only on
  an action (request/buy/save/follow), persisting `{name, contact, hoods[]}`.
- Chain: welcome → role → (buyer: neighborhood → feed) / (seller: neighborhood →
  builder). Rewire `geo-go` (currently just `go('home')`) and remove the temporary
  `#neighborhood` deep link once real nav exists.
- Persist account in localStorage (no backend yet).

## Then — Batch 3: neighborhood filter + role-aware home
- Tag each stand with its neighborhood id; feed filters to account's picked set.
- Top-bar place indicator reads account hoods (currently hardcoded "Country Club").
- Reseed Delaney in Country Club.

## Open / deferred
- **Text confirmations need real plumbing** (backend + Twilio-style SMS). v1 routes
  "request a lesson" off-platform (prefilled text/email to parent); auto two-way
  confirmation = when a backend exists. Decide when to cross that line.
- Per-week availability "copy to next 4 weeks" button (offered, not decided).
- Single profile slot → true multi-kid.
- "Too quiet" release valve if a neighborhood feels empty (adjacent-area opt-in).
