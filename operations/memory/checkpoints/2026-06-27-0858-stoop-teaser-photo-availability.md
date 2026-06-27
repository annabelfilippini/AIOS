---
date: 2026-06-27 08:58
project: stoop
status: in-progress
type: checkpoint
slug: stoop-teaser-photo-availability
---

# Stoop — sign-up teaser + photo-for-any-kid + tap-to-pick availability (30-min)

Follows `2026-06-27-0815-stoop-v1-onboarding-home-loop.md`. Four changes this
session, all in the single-file app `projects/stoop/index.html`. V1 loop
(onboarding → profile → home) was already done; this hardened the new-user flow
and made availability easy to set.

## 1. "More kids near Delaney" teaser (growth bait)
New `#more-kids` block at the bottom of `#view-profile` (between `.about` and
`.foot-note`), rendered by `renderMoreKids()`. Shows 2 hardcoded stub neighbors
(`const NEIGHBORS`: Mateo/backyard honey $7/sun, Priya/friendship bracelets
$4/purple) + a dashed "Set up your stand" CTA. Stub cards → `go('home')`, CTA →
`go('onboard')`. Horizontal scroll row, compact `.mk-card` styling (not the big
`.stand` card). ponytail: stubs are hardcoded — no feed/geo exists yet, fakeness
is the point (link-first → feed-second loop made visible).

## 2. Photo upload works for any kid (was Delaney-only leak)
`delaney.jpg` is sample data for the one-tap demo. Before: a new kid who skipped
upload inherited Delaney's face because the form prefilled her photo. Fix = one
`effectivePhoto()` helper (single source of truth, used by both the onboarding
preview AND save): returns the sample photo only when name === Delaney, else ''
→ initial-letter avatar. `f-name` now fires `setPhotoPreview` on input so the
preview drops to the initial live as you type your name. Real uploads (data URLs)
are never === `DEFAULT.photo`, so they're always kept.

## 3. New-stand onboarding starts BLANK (was autofilled with Delaney)
Annabel's report: "Start my own stand" opened prefilled with Delaney's answers.
Root cause: `fillOnboard()` prefilled from `profile || DEFAULT` on every path.
Fix: `DEFAULT` is now a **seed, not a form prefill**.
- `fillOnboard(mode)` — `mode==='edit'` prefills the saved profile; anything else
  → blank form.
- `go(view, mode)` threads `mode`; only the owner-bar **Edit** button passes
  `'edit'`. Start my own / Add your stand / Set up your stand / Start fresh all
  pass nothing → blank.
- Boot changed: `if(!profile){ profile=clone(DEFAULT); save() } go('home')` — seeds
  Delaney so the neighborhood home always has one real stand, and always lands on
  home (no more cold-start-into-prefilled-onboarding).
- `ob-back` now always shown (home always exists once seeded).

## 4. Availability editor: tap-to-pick chips, now 30-min slots
Replaced the per-day comma-separated **text input** with tappable time chips
(Annabel disliked typing times). `renderDayTimes()` now renders a chip grid per
selected day. Data shape unchanged (`obDays[dow] = [label strings]`) so the
booking calendar/profile read it verbatim — backward compatible with Delaney's
saved hour-times.
- `const SLOTS` = 9:00am→8:00pm in 30-min steps (minutes 540→1200, 23 chips);
  `slotLabel(m)` formats. Was hourly (`HOURS`/`hourLabel`) first, upgraded to
  half-hour on Annabel's request (e.g. 3:30–4:30).
- Toggling recomputes `obDays[i]=SLOTS.map(slotLabel).filter(selected)` to keep
  chronological order. Default on first day-select still `['4:00 pm','5:00 pm']`.
- CSS: `.hchip`/`.hchip.on` (reuses accent), `.trow`/`.hchips` replace `.row`+input.

## Verified (preview MCP `stoop`, port 8762, index.html) — no console errors
- Teaser: 2 cards + dashed CTA, "More kids near Delaney", mobile screenshot clean.
- Photo: Delaney demo keeps `delaney.jpg`; new kid no-upload → "T" initial; new kid
  with real upload → data URL kept and shown on profile.
- Blank onboarding: boot → home with Delaney card; "Start my own stand" → empty
  form, "?" avatar; Edit → Delaney's data intact.
- Chips: 23 half-hour chips 9am–8pm; 3:30/4:00/4:30 pm select in chronological
  order; save → calendar shows "open" day with exact slot times; Edit lights up
  Delaney's saved hours (backward compat).

## Open / next
- Annabel still hasn't done a full pass in her own browser.
- **Single profile slot** is the next real limit: building a new stand overwrites
  Delaney (seeded). True multi-kid needs a profiles array + per-page routing —
  the obvious step whenever a 2nd real kid exists.
- Teaser neighbors are stubs; they tap through to home, not real pages.
- Deferred unchanged: hyperlocal feed, parent dashboard, builder polish.
