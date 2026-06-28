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

## Batch 2 — Account front door ✅ DONE (2026-06-28)
- File touched: `projects/stoop/index.html` only.
- New `#view-welcome` front door: role split — "Open a stand" (seller, selMode='one')
  / "Shop the neighborhood" (buyer, selMode='many'). `chooseRole()` sets mode +
  `pendingRole`, routes to neighborhood.
- `geo-go` rewired: writes `account {role, hoods:[...]}` to localStorage
  (`stoop-account-v1`), then routes seller→onboard(builder), buyer→home(feed).
- **Account-free browse:** welcome/neighborhood need no account; the account record
  only gains `contact`/`name` when the user acts (request modal prefills + persists).
- Startup: account on file → restore selMode/hoods, skip to home; else land on welcome.
  Removed the temp `#neighborhood` deep link. geo-back → welcome.
- `.place` top-bar indicator hidden on welcome (still hardcoded "Country Club" — Batch 3).
- Verified in preview (8762): buyer path (multi-pick → account → home), seller path
  (single-select collapse → account → builder), returning visitor skips welcome +
  restores hoods, request flow persists contact, fresh load prefill empty. No errors.

## Builder branches by offer type ✅ DONE (2026-06-28)
- File touched: `projects/stoop/index.html` only.
- New first builder question "What are you offering?" → `service` | `product`
  (`obKind`, `setKind()`, `.kind` picker reusing the role-card look).
- **Service** (Delaney): keeps how-long/where/what-to-bring + the availability
  calendar → profile shows "Pick a time" + "Request a lesson".
- **Product** (honey/bracelets): those fields wrapped `.svc-only` and hidden;
  no availability saved (`avail:{}`); profile hides the calendar, shows "Get one"
  + "Local pickup" fact + an always-enabled "Request this".
- Request modal + SMS body + done screen adapt by kind; confirmation copy made
  gender-neutral ("They'll reach out"), dropped lacrosse-only "See you on the field".
- `profile.kind` persisted; missing kind treated as service (back-compat for old saves).
  DEFAULT (Delaney) seeded `kind:'service'`.
- Verified in preview (8762): product builder hides svc fields + adapts unit
  label/placeholder; product profile no calendar, request enabled, sends with
  pickup copy; service path (Delaney) calendar intact. No console errors.

## Batch 3 — Neighborhood filter + role-aware home
- Tag each stand with its neighborhood id; home/feed filters to account's picked set.
- Top-bar place indicator reads account hoods (currently hardcoded "Country Club").
- Reseed Delaney's stand in Country Club.
