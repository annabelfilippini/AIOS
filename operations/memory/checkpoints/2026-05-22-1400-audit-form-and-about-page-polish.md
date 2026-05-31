---
date: 2026-05-22
time: 14:00
project: agency-audit-network
status: in-progress
next-session: Push the latest paid Tally form changes with a rotated TALLY_TOKEN, add/launch the 8-question free preview audit, and visually QA the newer `projects/site/about.html` About page.
---

# Session: Audit form and About page polish

## What we worked on

Annabel wanted to use her Skool CLI / Mansel audit material to judge whether every section of the paid Tally audit form was necessary. We reviewed the Mansel-spined audit logic, the existing `rjJo05` form builder, and iterated the form from exhaustive consultant worksheet toward a still-rigorous agency-ready scoping experience.

Also refined the newer personal site About page to include a more engaging bio layer: Michigan SI, Okta Product Analyst, small-business AI audit work, agencies, running, kitesurfing, travel, and making room for both work and play.

## Decisions made

- Keep the paid audit substantial; do not cut 40-50%. Target was roughly a 25% reduction while preserving agency-ready depth.
- Keep the 13-section paid audit shape, but tighten repeated leadership/operator/deep-dive questions.
- Section 6 is necessary, but it must clearly be the structured Step Cards artifact, not another narrative workflow prompt.
- The old Section 6 Google Sheets TODO is not required for launch. A spreadsheet template can be added later, but Tally can collect Step Cards directly.
- Replace jargon/confusing labels:
  - "Money Slide" -> "ROI + Cost of Inaction"
  - "DRI" -> "Internal owner"
  - "Kill / Pivot" removed as separate prompt and folded into success criteria
  - "oh shit moment" -> "serious incident or near-miss"
- The free audit should be an 8-question preview that tells users where to look, not a replacement for paid Step Cards / QDOAA / ROI / agency handoff.
- The About page should feel credible and human: professional proof plus a little personality/movement/travel, not a stiff resume block.

## Open questions

- Tally conditional logic for 5A/5B still needs to be confirmed in the UI: Acquisition should route to 5A; Delivery/Support/Operations should route to 5B.
- Decide whether to create the free preview audit in Tally, on the website, or both.
- Decide whether `projects/site/` has superseded `projects/agency-audit-network/site-draft/` as the canonical AnnabelFilippini.com source.
- Visual QA of `projects/site/about.html` still needs a browser screenshot because Playwright was locked by another browser profile during this session.

## Next steps

1. Rerun the Tally update command with a fresh rotated token:
   `TALLY_TOKEN='...' TALLY_FORM_ID='rjJo05' node /Users/annabelfilippini/Documents/AI-OS/projects/agency-audit-network/scripts/build-tally-audit.mjs`
2. Open `https://tally.so/forms/rjJo05/edit` and verify:
   - no "Kill / Pivot"
   - Section 6 says "Turn the workflow into Step Cards"
   - Section 10 says "ROI + Cost of Inaction"
   - 5A/5B conditional logic is configured
3. Build the free preview audit from `projects/agency-audit-network/research/templates/free-audit.md`.
4. Open `projects/site/about.html` locally and visually inspect the new identity mosaic on desktop/mobile.

## Context to preserve

- Paid audit builder: `projects/agency-audit-network/scripts/build-tally-audit.mjs`
- Paid audit source spec: `projects/agency-audit-network/research/templates/self-serve-audit.md`
- Free audit source spec: `projects/agency-audit-network/research/templates/free-audit.md`
- Updated About page: `projects/site/about.html`
- Updated About styles: `projects/site/styles.css`
- Skool CLI local mirror was usable for stats, but live Skool access had auth/session issues. Mansel source material remains in `projects/agency-audit-network/research/sources/mansel-ainative-2026-05-14/`.

## System refinement candidates

- If Tally work continues, promote the update/create script pattern into a reusable Tally form skill or CLI connection.
- If `projects/site/` is now canonical, archive or clearly label `projects/agency-audit-network/site-draft/` to avoid editing the wrong website copy.
