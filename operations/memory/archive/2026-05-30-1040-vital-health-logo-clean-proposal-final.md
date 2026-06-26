---
date: 2026-05-30
time: 10:40
project: consulting / vital-health
status: Logo branch FULLY removed (clean source) + bird tilted -35° for flying read — awaiting Annabel's angle confirm. Proposal restructured to real plan (flat $700 site + hourly backend) with Annabel's exact Phase-3 hour numbers. Ready to package for Rob once logo angle confirmed.
next-session: (1) Confirm final logo angle with Annabel; rebuild chosen angle at higher res / vector before uploading to Webflow. (2) Optionally export proposal to PDF/Word for sending to Rob. (3) On client go-ahead: apply logo to site, do Phase 2 tweaks (Feste-as-owner), then schedule manager meeting to scope/start Phase 3 backend.
---

# Session: Vital Health — Clean Logo + Final Proposal

Supersedes `2026-05-30-1000-vital-health-logo-options-proposal.md` (which had a
duplicated line + stray backticks). Complements
`2026-05-30-0930-vital-health-webflow-client-edits-round2.md`.

## Client feedback driving this round (texts from Rob + the doctor)

- Logo branch reads phallic → reposition or remove. Pricing "sounds appropriate."
- Rob: make proposal MORE specific — hours-to-date + estimated ranges per phase,
  "final billable TBD with staff input" disclaimer, wants to approve in one shot.
- Rob: reflect **Dr. Feste as owner & still present** during ownership transition.
- Doctor: hopeful to stay **under $5k**; flag if over. Wants **Instagram weekly
  posting** help (open to paying). Confirms with Feste over weekend, replies Mon.

## Logo — FINAL direction (done; awaiting angle confirm)

- CLEAN base = `snapshot/vital-health-hummingbird.png` (223x187, transparent,
  NO branch, NO leaf). Use THIS. Do NOT use `out_removed.png` — it was traced
  from the full logo and left a leaf remnant on the lower-right body (Annabel
  circled this remnant in a Desktop screenshot).
- Earlier mockups (`logo-options/out_*.png` = removed/beak/under/left branch
  repositions) are now SUPERSEDED by "just remove it entirely."
- Annabel wants the bird tilted "the other direction 35°" = CLOCKWISE / negative
  rotation (nose-down, flying down-forward), opposite the earlier +15/25/35 CCW
  upward-climb renders.
- Delivered: `logo-options/hummingbird-clean-tilt-neg35.png` (transparent) +
  `-white.png`. Preview: `~/Desktop/vital-health-hummingbird-tilt.html`.
- OPEN: Annabel to confirm -35° angle. Source only 223px wide — recreate chosen
  angle at higher res / vector before using as site logo/favicon.

## Proposal — FINAL structure (done) at docs/proposal-vital-health-website.md

Two parts: website (done, flat fee) + backend (next, hourly after manager meeting).

- **P1 Website — flat $700** (~1 day @ $95/hr) + **Webflow hosting ~$40/mo** (confirm w/ Rob).
- **P2 Small tweaks (2–4h):** logo branch fix + Dr. Feste-as-owner. About founder
  story already reworded as history (Julie wording question REMOVED — already
  raised with her, per Annabel).
- **P3 Backend (after manager meeting)** — Annabel's exact hour numbers:
  - Manager meeting + plan: 2
  - Connect Cerbo: 5–7
  - Add-to-cart / checkout for staff: 3–5
  - Website touchups (headshots, bios, etc.): 2–4
  - Buffer: 2–4
  - **Subtotal 14–22 hrs ≈ $1,330–$2,090**
- **Running total P1–3 ≈ $2,030–$2,790** incl. $700 site — comfortably under $5k.
- **Instagram** = optional add-on after launch, automated weekly posting, $95/hr.
  ("Flagging it now so you know it's on my radar" line REMOVED per Annabel.)
- Terms: $95/hr backend, flat $700 site, Stripe + itemized invoice, hosting
  ~$40/mo, "flag before exceeding $5k" disclaimer.

## Global pref captured this session

- CLAUDE.md ## Working Style: when presenting multiple visual options, build ONE
  self-contained HTML page with base64-embedded images + drop a Desktop copy
  (external img src stalled / wouldn't open earlier).

## Session-instability gotchas (recurred all session)

- Parallel Bash/Read calls kept getting cancelled; shell cwd resets to project
  root each call; heredocs sometimes return empty; image Reads intermittently
  fail then succeed; guessed screenshot filenames were wrong (always `ls -t
  ~/Desktop` first). Workarounds: single sequential `python3 -c` calls, retry
  Reads, save outputs to real files + Desktop HTML instead of inline previews.

## Key paths

- Clean tilted logo: `logo-options/hummingbird-clean-tilt-neg35.png` (+ `-white.png`)
- Proposal: `docs/proposal-vital-health-website.md`
- Prior build state / Webflow IDs: `2026-05-30-0930-...-client-edits-round2.md`
