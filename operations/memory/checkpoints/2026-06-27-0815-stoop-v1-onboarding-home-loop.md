---
date: 2026-06-27 08:15
project: stoop
status: in-progress
type: checkpoint
slug: stoop-v1-onboarding-home-loop
---

# Stoop — V1 closed: onboarding → live profile → neighborhood home (one real loop)

Follows `2026-06-27-0736-stoop-hero-calendar-qa-fixes.md`. Turned the hardcoded
Delaney mock into a real first-user flow. New single file
`projects/stoop/index.html` is now the app entry; `cousin-lacrosse.html` and
`preview.html` are superseded (left in place as reference, not deleted).

## What V1 now is (the loop)
1. **Onboarding** (`#view-onboard`) — one-screen form: name+age, about, page
   title, price/unit, duration, location, one-thing-to-bring, **phone**, pick
   free days-of-week + per-day times, theme swatch. Saves to `localStorage`
   key `stoop-profile`.
2. **Profile** (`#view-profile`) — the approved Delaney page, now rendered from
   the saved object instead of hardcoded HTML. Calendar built from `avail`
   (dow → [times]). Owner bar (hidden from visitors conceptually): Edit / Copy
   link / Start fresh.
3. **Home** (`#view-home`) — the neighborhood. Shows Delaney's stand card built
   from her saved page → tap → her profile. Plus a dashed "Add your stand" slot
   → onboarding. One real kid, the 8 fake stands from preview.html are gone.

## Home restyled to preview.html's craft-fair design (Annabel preferred it)
Annabel saw the old `preview.html` market page and liked it more than the first
plainer home. Ported its design into `#view-home`: top **bunting** strip (fixed
rainbow, home-only — toggled in `go()`, hidden on profile), big underlined
Fredoka hero + coral underline + grass "Start my own stand" CTA, and tilted
craft-fair stand cards (tape corner, kid's theme gradient/accent inlined per
card, pickup tag, heart). Stoop logo is now fixed **sun yellow** everywhere
(brand mark, matches preview) instead of the kid's accent.
The card's photo now **fills the whole card top** (object-fit cover) since kids
have real photos — not a small circle.

## Photo upload added to onboarding ("Your photo" card)
File input → `downscale()` (canvas, 480px cap, jpeg 0.82) → base64 data URL in
`profile.photo`, persisted to localStorage. ponytail: the downscale is the
guard — a raw multi-MB phone photo would blow the ~5MB quota and silently fail
to save. Delaney's default stays `delaney.jpg` (a path, not a data URL — img
src handles both). Replaced the old name===Delaney photo hack with `obPhoto`.

Router: `go(view)`. First-ever visit (no saved profile) → onboarding; returning
→ home. Onboarding prefills from saved profile, or from `DEFAULT` (Delaney's
real answers) on first run, so the cold-start demo lands on the approved page in
one tap.

## The two threads that merged
- Last session's blocker was "Request a lesson goes nowhere — need a
  destination." Onboarding's **phone field IS the destination.** The request
  modal's Send now builds a real prefilled `sms:<phone>?&body=...` (lesson +
  kid + contact + note) and fires `window.location.href`. Verified the link
  builds: `sms:5551234567?&body=Hi%20Delaney!...`. That's checkpoint Option A
  done, for free, via onboarding. ponytail: sms link, no backend.

## Lazy calls (ponytail)
- `localStorage`, not a backend — the honest way to make "save → see it live"
  real for one user. Shared origin works because preview serves over
  http://localhost:8762.
- One file, not three — so saved data is reliably shared and the QA'd profile
  CSS came along verbatim (ported, not redesigned).
- Availability editor = check days + comma-separated times applied per day.
  No per-slot booked/strikethrough state on a brand-new page (dropped the fake
  BOOKED set). ponytail-commented.

## Verified (preview MCP `stoop`, port 8762, index.html)
First-run → onboarding prefilled (name Delaney, back hidden, 7 day chips, 6
swatches). Open my page → profile (title/price/facts/about/photo all from saved
data, 2 open days correct for late June, owner bar shows). Home → Delaney card +
add-stand. Request flow: day→slot enables button, modal opens, sms link builds.
Mobile 375 single-column clean. No console errors (favicon 404 only).

## Open / next
- Annabel hasn't reviewed in her real browser yet — left on home view.
- `delaney.jpg` is auto-kept as the photo only when name === "Delaney"; a true
  new user has no photo upload yet (avatar falls back to first initial). Photo
  upload is the obvious next onboarding field if a second kid is added.
- Avatar is still the full-motion action crop (tighter re-crop still offered,
  undecided — carried from prior checkpoint).
- Deferred unchanged: hyperlocal feed, parent dashboard, builder polish.
