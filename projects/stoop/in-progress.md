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

### Product gallery + description (2026-06-28, same file)
- `.prod-only` mirror of `.svc-only` (setKind toggles both). Product-only:
  - **Description** textarea (`f-desc`) in the "What you offer" card → `profile.desc`,
    shown as `#p-desc` in the book section above the pickup line.
  - **Photo gallery** card (`gal-file`, multi): `obPhotos[]`, reuses `downscale()`
    at 720px, capped at 6 (localStorage quota; comment notes upgrade path), thumb
    strip with remove → `profile.photos[]`, shown as `#p-gallery` grid between hero
    and book. Both render only for products with content; service shows neither.
  - Saved via ob-go (`desc`/`photos` cleared for services), loaded in fillOnboard.
- Verified: desc + 2 gallery imgs render on product profile, thumb remove works
  (2→1), service path hides both. No console errors.

## Batch 3 — Neighborhood filter + role-aware home ✅ DONE (2026-06-28)
- File touched: `projects/stoop/index.html` only.
- **Tag stands with a hood:** `profile.hood`. `DEFAULT.hood='country-club'` (reseeds
  Delaney in Country Club); a seller's new stand inherits `account.hoods[0]` at ob-go.
- **Feed filter:** `inFeed(p)` — buyer sees a stand only if `account.hoods` includes
  its hood; seller always sees their own; no account = no filter. renderHome guards
  the stand card with it (empty feed → just the CTA = the "too quiet" valve).
- **Top-bar `.place`:** `renderPlace()` (called from `go()`) — seller shows their one
  hood + "verified neighbor"; buyer shows the name (1 hood) or "N neighborhoods"; no
  account falls back to the demo default. Replaces the hardcoded "Country Club".
- **Role-aware home:** add-stand CTA reads "Open your own stand" for buyers (not "Add
  your stand", which framed Delaney's seeded demo as theirs); seller keeps "Add your stand".
- Also cleaned up product reqbar: lone "Request this" now centers (was shoved right by
  the leftover service `justify-content:space-between`).
- Verified in preview (8762): buyer country-club+hilltop → sees Delaney, place "2
  neighborhoods", CTA "Open your own stand"; buyer washington-park → empty feed + CTA,
  place "Washington Park neighborhood"; seller hilltop → own stand, place "Hilltop
  neighborhood · verified neighbor", CTA "Add your stand"; product profile reqbar
  centered. Fresh visitor lands on welcome. No console errors.

## Neighbor stubs in the feed + coming-soon + site-wide bunting ✅ DONE (2026-06-28)
- File touched: `projects/stoop/index.html` only.
- **Stubs in the feed:** `NEIGHBORS` (Mateo/Priya) hood-tagged `country-club` so they
  survive `inFeed`, and rendered in `renderHome` so the feed reads as a populated block
  instead of one stand + CTA. Factored the card markup into one `standCard(p, onclick)`
  helper shared by the real stand and the stubs (no duplication).
- **Coming-soon:** stubs have no page yet, so a tap fires a lightweight `toast()`
  ("<name>'s stand is coming soon") instead of a dead click. New fixed toast pill
  (CSS + 4-line helper, 1.9s auto-dismiss). Real stand still opens its page.
- **Site-wide bunting:** removed the `view==='home'` toggle in `go()` so the flag strip
  shows on every view (Annabel liked it up top and wanted it carried through).
- Verified in preview (8762): feed shows Delaney + Mateo + Priya; Hilltop buyer sees 0
  stubs, Country-Club buyer sees both (geo filter intact); stub tap toasts correct name;
  bunting `display:flex` on welcome/home/profile/onboard/neighborhood. No console errors.

## Backend: real multi-user feed + persistence ✅ DONE (2026-06-28) — Batches A+B
Domain bought (stoopmarkets.com). Went from localStorage demo to a real shared backend.
- **Supabase** project `stoop` (ref `pdovqkbejorncalnjqzv`, Oregon, in the Stoopmarkets
  org). Driven entirely via the Management API. SQL lives in `backend/schema.sql` +
  `backend/seed.sql`.
- **Schema:** `stands` + `orders` tables, a `public_stands` view that strips `phone`
  and `edit_token`, and 3 RPCs (`create_stand`, `update_stand`, `submit_order`). RLS on,
  zero direct table grants to anon — all writes go through the RPCs. Edit gated by a
  per-stand `edit_token` (no login; token cached in `localStorage` `stoop-mine-v1`).
- **Seeded** Delaney (service, avail computed for next 4 wks), Mateo + Priya (products)
  as real rows so every visitor's Country-Club feed has content.
- **Frontend (`index.html`):** added supabase-js; feed reads `public_stands` filtered by
  hood; tapping a card / `?stand=<id>` opens that stand (`openStand`); create→`create_stand`
  (sets `?stand=` for a shareable link); edit→`update_stand`; order→`submit_order`. Owner
  bar only shows on owned stands. Phone never reaches the browser. Removed the old
  `DEFAULT`/`seedAvail`/`NEIGHBORS`/`inFeed`/local `save`/`load`.
- **Verified live (8762):** feed renders 3 DB stands; Hilltop buyer sees 0 (geo filter);
  create persisted to DB + appeared in feed + owner bar shown; order row persisted;
  edit persisted with phone prefilled from owner-cache; **wrong edit_token rejected
  (returns false, Delaney untouched)**; phone absent from public view. QA stand cleaned up.
- Token note: Annabel's Supabase personal access token still needed for Batch C
  (edge-function deploy + Twilio secret); revoke after SMS is wired.

## Login refactor (phone OTP) — IN PROGRESS (2026-06-28)
Decision: real accounts via **Supabase Auth phone OTP**. Sellers log in; stands
tie to the account (any device). Buyers stay account-free.

- **Batch 1 ✅ backend ownership migration** (`backend/migrate-auth.sql`, applied +
  verified). `stands.owner` → `auth.users`; dropped `edit_token` + the token RPCs
  (`create_stand`/`update_stand`); RLS so a seller touches only their own stands;
  `public_stands` view now exposes `owner` (no phone). `submit_order` kept for buyers.
  `backend/schema.sql` re-synced to canonical.
- **Batch 2 ✅ Twilio↔Supabase wiring** (verified). Bought number **+1 720 575 8753**
  (sid PNf2e66e…, FriendlyName "Stoop"). Messaging Service **MGd416…** created, number
  attached. Supabase Auth phone provider PATCHed → twilio + that MS, 6-digit OTP, 10min.
  Live test OTP to Annabel's cell returned HTTP 200; Twilio logged **error 30034
  (unregistered 10DLC)** → pipe is correct, only 10DLC gates real delivery.
- **Batch 3 ✅ frontend** (`index.html`, 2026-06-28): new `#view-login` (phone → 6-digit
  code) with `e164()` normalization. Seller paths (`chooseRole('seller')`, `startStand()`)
  now gate through `requireAuth()`; buyers stay account-free. `ownsCurrent()` compares
  `profile.owner===user.id`. Create → `from('stands').insert({...,owner:user.id}).select()`;
  edit → `from('stands').update(...).eq('id',…)` (RLS-gated), prefilled from the owner's
  own full row (phone included, since the public view strips it). Session restored on load
  via `getSession()` + `onAuthStateChange`; **Sign out** added to the owner bar. All
  `stoop-mine`/`edit_token`/`create_stand`/`update_stand` logic removed.
  - **Verified in preview (8762):** welcome renders; seller→login (phone step shown, code
    hidden, top-bar place hidden); `e164` collapses formatted/bare/1-prefixed → `+1…`;
    buyer→neighborhood with no gate; no console errors. NOT yet verified end-to-end: the
    live OTP round-trip (send code / verify / create+edit as owner) needs the Supabase
    **test-OTP** set first — see GATE below.

### GATE (Annabel's action): A2P 10DLC registration
Real users can't receive codes/texts until this clears (days). Needs your business
info for the Brand: legal name, address, email; sole-proprietor is the light path.
Twilio number + Messaging Service already exist to attach the campaign to.

## (superseded) NEXT — Batch C: SMS confirmations
- Supabase Edge Function `notify-order` that reads the order + stand phone server-side
  and texts the parent via Twilio. Trigger: client calls it after `submit_order` (or a
  DB webhook on insert). Annabel: create Twilio account + start A2P 10DLC registration
  (days of carrier approval). Until approved, email fallback or testing to verified numbers.

## Deferred
- Single profile slot → multi-kid/multi-stand: now possible (backend exists); add a
  "my stands" switcher when a seller owns more than one.
- Per-week "copy to next 4 weeks"; richer empty-feed state.
- Hero photo stored inline as data-URL; move to Supabase Storage if rows get heavy.
- Parent approval rail dropped from v1 (payments off-platform; requests go straight to
  the parent's phone).
