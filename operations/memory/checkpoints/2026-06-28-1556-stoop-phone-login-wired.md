---
date: 2026-06-28
time: 15:56
project: stoop
status: in-progress
next-session: Build Batch 3 (frontend login UI + owner-based create/edit in index.html). Set a Supabase test-OTP for Annabel's number so the flow is testable pre-10DLC. In parallel, collect Annabel's 10DLC Brand details (legal name, address, email; Sole-Prop path) and submit registration.
---

# Session: Stoop — phone-OTP login chosen + backend/Twilio fully wired

Annabel decided to add **real accounts** (was token-edit-link model). Chose **phone
OTP** login. Also asked: (1) admin way to remove markets, (2) how to connect texts,
(3) will everyone have profiles. Answers: sellers log in via phone, stands tie to the
account; buyers stay account-free; admin-delete deferred (use Supabase dashboard for now,
or a `?admin=` build later). She set up Twilio this session and handed over creds.

## Decisions made
- Login = **Supabase Auth phone OTP**, sellers only; buyers account-free (no signup tax).
- Stands own-by-`auth.uid()` (dropped the `edit_token`/`stoop-mine` secret-link model).
- 10DLC recommended path = **Sole Proprietor** (no EIN) for the pilot.
- Login + order-texts share one Twilio Messaging Service → both light up when 10DLC clears.

## What shipped + verified (Batches 1 & 2)
- **Backend migration** `backend/migrate-auth.sql` (applied via Management API, verified):
  `stands.owner`→`auth.users`; dropped `edit_token`, `create_stand`, `update_stand`; 4
  RLS owner policies; `public_stands` view exposes `owner` (still no phone); `submit_order`
  kept for buyers. `backend/schema.sql` re-synced to canonical.
- **Twilio** (via REST API, curl): account is **Full** (not trial), owned **0** numbers.
  Bought **+1 720 575 8753** (Denver; sid PNf2e66e…, FriendlyName "Stoop"). Created
  Messaging Service **MGd416…**, attached the number.
- **Supabase Auth** phone provider PATCHed → twilio + MGd416…, 6-digit OTP, 600s expiry.
- **Live test:** OTP to Annabel's cell → HTTP 200; Twilio logged **error 30034
  (unregistered 10DLC)**. Pipe is fully correct; only 10DLC gates real delivery.

## Open questions
- 10DLC: register as Sole Proprietor (recommended) or business w/ EIN?
- Admin-remove-markets: dashboard-only for now, or build the in-app `?admin=` delete?
- Should the seeded demo stands (Delaney/Mateo/Priya, owner=null) be reassigned to
  Annabel's account once she logs in, so she can edit Delaney for the Lainey demo?

## Next steps
1. **Batch 3 frontend** (`index.html`): phone→code login screens; `chooseRole('seller')`
   gates on auth; create→`from('stands').insert({...,owner:user.id})`; edit→`update`
   (RLS-gated); `ownsCurrent()` compares `owner===user.id`; remove `MINE_KEY`/`edit_token`
   logic; add sign-out + restore session on load. Verify in preview (test-OTP).
2. Set Supabase **test-OTP** for Annabel's number (fixed code, no SMS) to test pre-10DLC.
3. **10DLC**: gather Annabel's Brand info, submit Brand+Campaign on MGd416… via API.
4. Later: order-notification edge function (`notify-order`) reusing the same MS.

## Context to preserve
- Supabase ref `pdovqkbejorncalnjqzv`. SQL via Management API: POST
  `/v1/projects/{ref}/database/query` with `{"query":...}`, curl `--data-binary @file`
  (Cloudflare blocks Python urllib UA). Auth config via PATCH `/v1/projects/{ref}/config/auth`.
- Twilio driven by REST API + curl basic-auth (SID:AuthToken); no CLI installed/needed.
- Anon key embedded in `index.html` (safe; RLS protects data). Personal access tokens
  (Supabase + Twilio creds) were pasted in-session only — NOT written to repo. Revoke/rotate
  the Supabase token after 10DLC + edge-function work is done.
- Error 30034 = the 10DLC gate; expect it on every send until registration clears.

## System refinement candidates
- None this session.
