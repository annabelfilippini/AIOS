---
date: 2026-06-28
time: 16:40
project: stoop
status: in-progress
next-session: Submit A2P 10DLC (Sole Proprietor) so real users — not just Annabel's
  whitelisted cell — can receive codes/texts. Gather Brand info (legal name, address,
  email), register Brand + Campaign on Messaging Service MGd416… via the Twilio API.
  Then optional Batch C: notify-order edge function reusing the same MS. Consider
  reassigning the owner=null demo seed stands (Delaney/Mateo/Priya) to Annabel's account.
---

# Session: Stoop — Batch 3 frontend (phone-OTP login) built + verified live

Picked up from the 15:56 checkpoint. Two asks: (1) build Batch 3, (2) does Annabel
need 10DLC as an individual. Answer to (2): **yes** — 10DLC is a carrier rule on all
A2P traffic over local numbers; "individual" only selects the Sole-Proprietor brand
type (no EIN, lighter), it is not an exemption. Error 30034 is that gate.

## What shipped (Batch 3 frontend — `projects/stoop/index.html`)
Reconciled the frontend with the Batch-1 DB migration (which had dropped the
`create_stand`/`update_stand` RPCs + `edit_token` and moved to `owner=auth.uid()` +
RLS — the frontend was still calling the dead RPCs).
- New `#view-login`: phone → 6-digit code, two steps, `e164()` normalization
  (formatted / bare-10 / 1-prefixed-11 all → `+1…`).
- Seller paths gate through `requireAuth()` (`chooseRole('seller')`, `startStand()`),
  resuming the intended action via `pendingAfterLogin`. Buyers stay account-free.
- `ownsCurrent()` now compares `profile.owner===user.id` (was `mine[id]` localStorage).
- Create → `from('stands').insert({...,owner:user.id}).select().single()`.
- Edit → `from('stands').update(payload).eq('id',id)` (RLS owner-gated); `fillOnboard`
  is now async and reads the owner's **own full row** (incl. phone, which the public
  view strips) to prefill.
- Session restored on load via `getSession()` + `onAuthStateChange`. **Sign out** added
  to the owner bar. All `MINE_KEY`/`mine`/`edit_token`/RPC logic removed.

## Test-OTP set (so login is testable pre-10DLC)
Supabase Auth config via Management API (PATCH `/v1/projects/{ref}/config/auth`):
- `sms_test_otp` = `13038593694=123456` — **format the API enforces: comma-separated
  `<phone>=<code>`, E.164 WITHOUT the leading `+`** (a `+`, a `:` separator, or an object
  all 400). Took several tries; the 400 body spells out the exact rule.
- `sms_test_otp_valid_until` = `2027-12-31T23:59:59Z` (else test OTPs may read expired).
- Test number short-circuits the SMS send entirely → no 30034 while testing.

## Verified live end-to-end (preview 8762, no console errors)
seller→login → `sendCode` (no SMS error) → `verifyCode('123456')` creates a session
(user f5caf946…, phone 13038593694) and resumes → neighborhood → create inserts with
owner=auth.uid() (RLS pass, owner bar + `?stand=` URL) → edit prefills phone from the
owner row + update lands in DB → owner-gated delete removes the row → sign-out clears
session → welcome. QA stand created+deleted; DB left clean.

## Context to preserve
- Supabase ref `pdovqkbejorncalnjqzv`. Auth config: PATCH `/v1/projects/{ref}/config/auth`
  (Bearer = Supabase personal access token, pasted in-session only, NOT in repo —
  rotate after 10DLC + edge-function work).
- Twilio: +1 720 575 8753 (sid PNf2e66e…) on Messaging Service MGd4166164b95b67e7188bd5ad1260a38b.
  Supabase phone provider already points at twilio + that MS.
- Anon key embedded in index.html (safe; RLS + phone-stripped public view protect data).
- Whitelisted test cell = +1 303 859 3694; fixed code 123456 (valid through 2027).

## System refinement candidates
- Proposed (pending Annabel's OK) adding to `~/.claude/CLAUDE.md` Tool & Stack
  Assumptions: `Claude_Preview` `preview_eval` shares one persistent JS scope across
  calls (wrap in an IIFE to avoid `const` redeclare errors); `preview_click` wants a CSS
  `selector`, not the numeric `ref` from `preview_snapshot`.
