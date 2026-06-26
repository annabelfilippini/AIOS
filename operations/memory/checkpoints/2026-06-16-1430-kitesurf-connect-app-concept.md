---
date: 2026-06-16
time: 14:30
project: ideas / kitesurf-connect-app
status: CONCEPT LOCKED — scope agreed, no build started. Waiting on Phase 0 (friend + supply signal) before any code.
---

# Session: Kitesurf-connect app — concept shaping

Brainstorm only. No files created, no prototype built. A semi-pro kitesurfer
friend floated the idea; Annabel is doing this for love of the game, not a
business.

## Locked concept
A way to connect kitesurfers at a spot. Two sides:
- **Find people to ride with** (riding buddy / downwinder partner), AND
- **Find or offer coaching** (one mode inside the broader app, not the whole app).

Decided design:
- **Onboarding role**: ride / coach / get coached.
- **Profiles**: experience, home spot, level, discipline (foil, wave,
  freestyle, big air, wing), optional price for coaches.
- **Matching** by discipline + location.
- **Travel mode**: "I'm in Dakhla for 2 weeks in March" → see who's around.
- **Mutual-match (Hinge-style)** before anyone can DM. DECIDED yes (cuts spam +
  creepy DMs, fits free-community vibe).
- **In-app DM** for connecting. Off-platform contact is fine (not a business).
- **Disclaimer**: Annabel does not facilitate, book, or vet anyone. No booking
  calendar. Disclaimer shown clearly at signup.

## Key reframes that shaped it
- It's a passion project, not a business → disintermediation and liability stop
  mattering; scope shrinks a lot (no booking calendar).
- The strongest wedge is NOT beginner lessons (kite schools own that, plus
  gear/insurance/IKO). It's intermediate+ riders + the **riding-buddy** angle,
  which is the stickier, retention-driving use (you shouldn't kite alone).
- Geography is an advantage, not just a filter: kitesurfing is spot-concentrated,
  so launch ONE spot densely (Tarifa) and beat the cold-start problem.

## Accepted risks (Annabel's calls)
- **Fake/inflated credentials**: leave as-is. Optional later: Instagram link +
  cert/video badge for signal, not enforcement.
- **DM safety / creepiness**: accept, mitigated by mutual-match + disclaimer.
  (Suggested but not decided: show spot not exact pin.)

## Artifact ready to use
A paste-ready, plain-voice (no-dash) concept description for the friend is
written in the chat transcript — includes ride/coach onboarding, discipline,
travel mode, riding-buddy framing, mutual-match, disclaimer, and ends with the
two supply questions ("Would you use this? Do you know coaches who'd list?").
Re-generate from this checkpoint if needed.

## Build plan (agreed, from Annabel's side)
- **Phase 0 — Validate (no code, GATE)**: send description; real signal = named
  coaches who'd list, not "cool idea." Pick launch spot (Tarifa).
- **Phase 1 — Clickable prototype (Claude builds, fast, no backend)**: fake data,
  no login/persistence; purpose = feel the flow + recruiting tool for supply.
- **Phase 2 — Real MVP (the actual project)**: web app / PWA (skip App Store).
  Needs accounts, photo upload, discovery feed w/ filters, mutual-match logic,
  **real-time DMs (biggest eng chunk)**. Proposed stack: **Supabase**
  (auth + postgres + realtime + storage). NOT set up — needs Annabel's go-ahead
  before assuming it.
- **Phase 3 — Seed + soft-launch (mostly Annabel)**: manually onboard ~15-20
  Tarifa people before opening; friend helps recruit.

## Next step
Waiting on friend's response (Phase 0). Do nothing technical until there's a real
supply signal. When Annabel wants something to show people, build the Phase 1
prototype (onboarding → profile → swipe → match, fake data).
