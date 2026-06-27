# Stoop onboarding rebuild — in progress

Goal: full account/sign-in front door with **block-level** hyperlocal placement
(address + live map), built before showing Lainey. Anti-Nextdoor = strict block
filter, no radius.

Decisions (Annabel, REVISED): named **neighborhoods**, not blocks (block was too
tight). City → curated Denver neighborhood list. **Sellers pick ONE** (stand is
physical), **buyers pick MANY** (own + friends' areas). Strict filter = exactly the
picked set, no radius. Map = display-only preview highlighting picks (no geocode).
Pilot city = Denver; Delaney's stand = Country Club. Faked account (no backend).

## Batch 1 — Neighborhood select ✅ DONE (2026-06-27, reworked from block version)
- File touched: `projects/stoop/index.html` only.
- `#view-neighborhood`: neighborhood chips + Leaflet/OSM map preview + summary card.
- `NEIGHBORHOODS` (10 Denver hoods w/ lat,lng), `selMode` 'one'|'many',
  `pickedHoods` Set, `toggleHood`/`renderHoods`/`paintMap`/`initGeo`.
- Dropped the address/geocode (Nominatim) machinery — list-based now.
- Verified: buyer multi-select (Country Club · Hilltop), seller single-select
  collapses to one, picks light up on map, copy adapts by mode. No console errors.
- **Map upgrade (2026-06-27):** dots → real neighborhood boundary polygons. Data is
  now a swappable `CITY` block (name/center/zoom/hoods/boundaries). Denver boundaries =
  official "statistical neighborhoods" (opendata-geospatialdenver), trimmed to the 9
  matching hoods, coords 5dp (~28KB inline). Selected hood fills its real shape in
  accent; unselected = faint outline; a hood with no official polygon (Crestmoor)
  falls back to a dashed bubble at its label point. Hardened initGeo invalidateSize
  (rAF re-invalidate) so tiles fill on first paint. Verified in preview, no errors.
  To add Chicago: swap the CITY block (its open-data neighborhood GeoJSON, same id keys).

## Batch 2 — Account front door (NEXT)
- Welcome + role select (open a stand → seller/selMode='one' / shop → buyer/'many'),
  account basics. Wire flow: welcome → role → account → neighborhood →
  (seller: builder / buyer: home). geo-go currently just go('home').
- Persist account {role, name, hoods:[...]} in localStorage.

## Batch 3 — Neighborhood filter + role-aware home
- Tag each stand with its neighborhood id; home/feed filters to account's picked set.
- Top-bar place indicator reads account hoods (currently hardcoded "Country Club").
- Reseed Delaney's stand in Country Club.
