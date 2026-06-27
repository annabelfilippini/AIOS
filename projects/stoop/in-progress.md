# Stoop onboarding rebuild — in progress

Goal: full account/sign-in front door with **block-level** hyperlocal placement
(address + live map), built before showing Lainey. Anti-Nextdoor = strict block
filter, no radius.

Decisions (Annabel): block-level granularity; address + live map (Leaflet/OSM +
Nominatim geocode); block id = street + hundred-block; faked account (no backend).

## Batch 1 — Neighborhood capture ✅ DONE (2026-06-27)
- File touched: `projects/stoop/index.html` only.
- New `#view-neighborhood` view + `initGeo`/`geocode`/`reverseGeocode`/`blockFrom`/
  `showPin`. Leaflet+OSM in <head>. Block card + strict-filter promise copy.
- Verified: real address → pin + "Street · NNN block"; drag/tap map re-derives;
  Enter submits; error fallbacks. No console errors.

## Batch 2 — Account front door (NEXT)
- Welcome + role select (open a stand / shop the block), account basics, wire flow:
  welcome → role → account → neighborhood → (seller: builder / buyer: home).
- Persist account in localStorage. Open Q: real seed address for Delaney (town?).

## Batch 3 — Block filter + role-aware home
- Tag stands with block id; home/feed filters strictly to account.block.
- Top-bar place indicator reads account block (currently hardcoded "Country Club").
- Reseed Delaney with a real address/block.
