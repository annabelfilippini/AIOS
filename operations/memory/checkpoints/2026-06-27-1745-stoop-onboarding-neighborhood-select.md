---
date: 2026-06-27 17:45
project: stoop
status: in-progress
type: checkpoint
slug: stoop-onboarding-neighborhood-select
---

# Stoop — onboarding rebuild: hyperlocal neighborhood select (Batch 1 done)

Follows `2026-06-27-1700-stoop-per-week-availability.md`. All work in the single
file `projects/stoop/index.html`. Live progress tracker: `projects/stoop/in-progress.md`.

## Plan change this session
Annabel pivoted the roadmap: **build the whole platform before showing Lainey
(Delaney)**, starting with the account/sign-in front door and a genuinely tight
**hyperlocal neighborhood** model (the anti-Nextdoor foundation everything else
sits on). Deferred the earlier "ship one real page / stand up a backend" fork.

## Decisions locked (asked Annabel, two reversals as she saw it live)
1. First tried **block-level + address + live map** (built, worked: Nominatim
   geocode → "Street · NNN block" + Leaflet pin). Annabel felt block was **too
   tight** for what Stoop is.
2. **Revised + final model:** City → **named neighborhoods** (curated list).
   - **Sellers pick ONE** (a kid's stand is physical, pickup in person).
   - **Buyers pick MANY** (own neighborhood + friends' areas, e.g. Country Club +
     Hilltop, skip Cheesman).
   - **Strict filter = exactly the picked set, no radius.** This is still
     anti-Nextdoor because it's explicit opt-in, not algorithmic spillover.
     UI promise: "You'll only see the neighborhoods you pick. Just these."
   - **Map = display-only preview** (Leaflet+OSM) highlighting picks. Dropped the
     address/geocode machinery.
   - Pilot city = **Denver**; Delaney's stand = **Country Club**.
   - Faked account, **no backend** (localStorage). Real auth/verify = later.

## Batch 1 — Neighborhood select ✅ DONE & verified
- `#view-neighborhood`: neighborhood chips + map preview + summary/promise card +
  "Sounds good →".
- JS: `NEIGHBORHOODS` (10 Denver hoods w/ lat,lng: Country Club, Cheesman Park,
  Cherry Creek, Hilltop, Congress Park, Washington Park, Capitol Hill, Hale,
  Crestmoor, Belcaro), `selMode` ('one'|'many'), `pickedHoods` Set,
  `toggleHood`/`renderHoods`/`paintMap`/`initGeo`. Router: `go('neighborhood')`
  calls `initGeo()`. Leaflet+OSM CDN in `<head>`.
- Copy adapts by mode (seller: "Where's your stand?" single; buyer: "Which
  neighborhoods?" many).
- Verified in preview MCP `stoop` (port 8762), no console errors: buyer
  multi-select → "Country Club · Hilltop", picks light pink on map, fitBounds;
  seller single-select collapses to one.
- ponytail: removed the now-dead Nominatim geocode/reverse/blockFrom from the
  earlier block version rather than leaving it.

## Next — Batch 2: account front door (NOT started)
- Welcome + role select: "Open a stand" → seller (`selMode='one'`) / "Shop the
  neighborhood" → buyer (`selMode='many'`). Account basics (adult name, email stub).
- Chain the flow: welcome → role → account → neighborhood → (seller: builder /
  buyer: home). `geo-go` currently just `go('home')` — Batch 2 rewires it.
- Persist account `{role, name, hoods:[...]}` in localStorage.

## Then — Batch 3: neighborhood filter + role-aware home
- Tag each stand with its neighborhood id; home/feed filters to the account's
  picked set. Top-bar place indicator reads account hoods (currently hardcoded
  "Country Club neighborhood · verified neighbor"). Reseed Delaney in Country Club.

## Still open / deferred (unchanged)
- Per-week availability "copy to next 4 weeks" button (offered, not decided).
- Single profile slot → true multi-kid (profiles array + routing).
- Backend (unlocks real feed + parent dashboard + shareable persistence).
- "Too quiet" release valve if a neighborhood feels empty: adjacent-area opt-in.
