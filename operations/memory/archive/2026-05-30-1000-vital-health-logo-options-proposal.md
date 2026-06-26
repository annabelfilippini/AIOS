---
date: 2026-05-30
time: 10:00
project: consulting / vital-health
status: logo branch options (removed + 3 repositions) built as HTML review page; phased proposal drafted. Awaiting client logo pick + Dr. Feste go-ahead + Zoom to lock content.
next-session: When client picks a logo direction, apply vector-clean version as site logo in Webflow. Then finish Phase 3 (Feste-as-owner tweaks) + Phase 4 (testimonials, medical-claim wording, founder story, custom-domain go-live). Scope Instagram automation (Phase 5) after launch.
---

# Session: Vital Health — Logo Branch Options + Phased Proposal

Supersedes nothing on the build side; complements
`2026-05-30-0930-vital-health-webflow-client-edits-round2.md`.

## Client feedback this round

- Rob + the doctor (via text): branch on hummingbird logo reads phallic; wants it
  repositioned or removed. Pricing "sounds appropriate." Owner becoming amenable.
- Rob: make proposal MORE specific — include hours to date + estimated ranges per
  phase (e.g. "phase 1 6-8 hrs, phase 2 4-5 hrs") with "final billable TBD with
  staff input" disclaimer. Wants to package + approve in one shot.
- Rob: tweak site so **Dr. Feste is reflected as owner and still present** during
  ownership transition ("right thing to do for now").
- Doctor: hopeful to stay **under $5,000** for the majority; flag if over so she
  can manage owner expectations. Also wants **Instagram weekly-posting help**
  (open to paying). Will confirm with Dr. Feste over weekend, reply Monday.

## Decisions / inputs from Annabel

- Rate = **$95/hour** (confirmed).
- Instagram = **automated weekly posting**, added as optional Phase 5 add-on
  after site launch, same $95/hr. Included in proposal so client sees it's on the
  radar, but priced/ scoped later.

## Logo work (done)

- `snapshot/vital-health-hummingbird.png` is ALREADY the branch-removed bird.
- `snapshot/vh-logo-transparent.png` is the current logo WITH the branch (olive
  sprig off lower-right body — the flagged one).
- Isolated the branch sprite by alpha-diffing region x>=212,y>=130 of the logo.
- Built 4 mockups (336x290) in /tmp then copied to project:
  `logo-options/out_removed.png`, `out_optA_beak.png` (sprig in beak),
  `out_optB_under.png` (sprig flat underneath), `out_optC_left.png` (sprig lower-
  left). Plus `out_current.png` for comparison.
- Review page: `logo-options/index.html` (opens in browser; branded cream/forest
  /gold). NOTHING changed on the live Webflow site yet — review only, per Annabel.
- NOTE: composites are quick raster repositions; once client picks, rebuild the
  chosen version vector-clean before uploading as the site logo asset.

## Proposal (done — CORRECTED structure)

- Drafted at `docs/proposal-vital-health-website.md`.
- IMPORTANT correction from Annabel: Cerbo/backend/retail/headshots are NOT
  excluded — they are the NEXT phase, done AFTER she meets the managers. The
  website is a FLAT $700 (one day at $95/hr), not an hourly phase.
- Based on Annabel's original message to Rob: site moved to Webflow so team can
  self-edit; Webflow hosting ~$40/mo ongoing (need Rob's ok); About page tells
  Dr. Joseph Feste's founding story, reworded as history — open question for
  JULIE on preferred phrasing; backend = connect Cerbo, retail in patient portal,
  staff add hormones/products to client cart for checkout, headshots, etc., all
  $95/hr; payment via Stripe, itemized invoice.
- Final phase structure: P1 Website (DONE, flat $700 + $40/mo hosting),
  P2 Small tweaks (logo branch + Feste-as-owner + About wording, 2-4h),
  P3 Backend after manager meeting (Cerbo/portal retail/checkout/headshots,
  ~19-32h table w/ line items), optional Instagram automation add-on later.
- Running total P1-3 ~$2,700-$3,940 incl. $700 site — under $5k. Explicit "flag
  before exceeding $5k" + "final billable TBD with Julie/staff input" disclaimers.

## Logo: FINAL clean+tilt direction (latest)

- Annabel marked a screenshot (Desktop) circling a leftover LEAF remnant on the
  bird's lower-right body. That remnant came from `out_removed.png` (traced out
  of the full logo). CORRECT clean base = `snapshot/vital-health-hummingbird.png`
  (no branch, no leaf, transparent, 223x187) — use THIS, not the traced version.
- Annabel wants the bird tilted "the other direction 35°" = CLOCKWISE / negative
  rotation (nose-down forward), opposite the earlier +15/25/35 CCW climb renders.
- Produced: `logo-options/hummingbird-clean-tilt-neg35.png` (transparent) +
  `-white.png`. Self-contained preview: `~/Desktop/vital-health-hummingbird-tilt.html`.
- AWAITING Annabel's confirm on this -35 direction. NOTE: source is only 223px
  wide — for final site logo/favicon, recreate chosen angle at higher res / vector.

## HTML logo page fix

- First HTML used external img src + stalled / wouldn't open for Annabel.
- Rebuilt SELF-CONTAINED with base64-embedded images (244KB, 5 imgs) and saved a
  copy to ~/Desktop/vital-health-logo-options.html. Opened fine.
- Captured as a global pref: CLAUDE.md ## Working Style now says visual-option
  review pages must embed images inline (base64) + drop a Desktop copy.

## Session instability gotcha

- This session repeatedly stalled: parallel Bash calls got cancelled, shell cwd
  kept resetting to project root, image Read previews intermittently failed then
  succeeded. Heredocs sometimes returned empty. Workarounds that worked:
  single-line python3 -c, retrying Reads, copying outputs to a real folder +
  building an HTML review page instead of relying on inline image rendering.

## Key paths

- Logo options + HTML: `projects/vital-health-webflow-migration/logo-options/`
- Proposal: `projects/vital-health-webflow-migration/docs/proposal-vital-health-website.md`
- Site IDs etc.: see `2026-05-30-0930-...-client-edits-round2.md`.
