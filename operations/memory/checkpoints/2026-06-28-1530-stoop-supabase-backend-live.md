---
date: 2026-06-28
time: 15:30
project: stoop
status: in-progress
next-session: Batch C — SMS confirmations (Supabase Edge Function + Twilio). Annabel must create a Twilio account + start A2P 10DLC registration; the Supabase token is still needed to deploy the function.
---

# Session: Stoop — real Supabase backend live (multi-user feed + persistence)

Annabel bought **stoopmarkets.com** and decided to move Stoop off the localStorage
demo onto a real backend. Decisions locked this session: **Supabase** backend, **SMS
now** for confirmations (so Twilio + 10DLC runs in parallel), edit-token identity (no
login). Parent-approval rail dropped from v1 — payments are off-platform, so requests
go straight to the parent's phone; there's no money/approval rail to build.

## What shipped (Batches A + B, both verified)
**A — Supabase backend.** Created/used project `stoop` (ref `pdovqkbejorncalnjqzv`,
Oregon, Stoopmarkets org), driven entirely via the Management API with Annabel's
personal access token. Schema in `projects/stoop/backend/schema.sql`, seed in
`backend/seed.sql`.
- `stands` + `orders` tables; `public_stands` view strips `phone` + `edit_token`;
  RPCs `create_stand` / `update_stand` / `submit_order`. RLS on, no direct table
  grants to anon — every write goes through an RPC. Edits gated by a per-stand
  `edit_token`.
- Seeded Delaney (service, avail next 4 wks via SQL), Mateo + Priya (products).

**B — Frontend cutover (`index.html`).** Replaced the whole localStorage data layer
with Supabase calls. Feed reads `public_stands` by hood; `openStand(id)` + `?stand=`
share links; create→`create_stand` (writes `?stand=` for a shareable URL); edit→
`update_stand`; order→`submit_order`. Owner bar shows only on owned stands (token in
`localStorage` `stoop-mine-v1`, which also caches the owner's full record so phone
prefills on edit without ever exposing it publicly). Deleted `DEFAULT`/`seedAvail`/
`NEIGHBORS`/`inFeed`/local `save`/`load`; `renderMoreKids` now queries real neighbors.

## Verification (live, port 8762)
Feed renders 3 DB stands; Hilltop buyer sees 0 (geo filter); create persisted to DB +
appeared in feed + owner bar shown; order row persisted server-side; edit persisted
with phone prefilled; **wrong `edit_token` rejected (RPC returns false, Delaney
untouched)**; `phone` absent from the public view; raw `stands` table is permission-
denied to anon. QA test stand deleted afterward.

## Open / next
- **Batch C — SMS.** Edge Function `notify-order` reads order + stand phone server-side,
  texts the parent via Twilio. Annabel: create Twilio + start A2P 10DLC (carrier approval
  takes days; until then, email fallback or test to verified numbers). Token still needed
  to deploy; revoke after.
- Hosting: deploy `index.html` (+ `delaney.jpg`) to stoopmarkets.com — static host
  (Cloudflare Pages / Netlify / Vercel). Not done yet.
- Hero photo is inline data-URL; move to Supabase Storage if rows get heavy.

## Context to preserve
- Management API + curl works for SQL (`/v1/projects/{ref}/database/query`); Cloudflare
  blocks Python urllib UA, so use curl with `--data-binary @file`.
- Anon key is embedded in `index.html` (safe by design; RLS protects data). Service_role
  key never used client-side.
- `description` column ↔ `.desc` in page code: `fromRow()` normalizes on load; payloads
  send `description`.

## System refinement candidates
- None this session.
