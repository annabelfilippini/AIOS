---
date: 2026-06-07
time: 11:57
project: vital-health-webflow-review
status: in-progress
next-session: Review local Vital Health pages with Annabel, collect missing assets/citations, then translate approved edits into Webflow staging only.
---

# Session: Vital Health Webflow review from Zoom and Granola notes

## What we worked on

- Read prior Vital Health Webflow checkpoints and Webflow rebuild QA guidance.
- Transcribed the June 5 Vital Health Zoom audio with local Whisper after downloading the model with approval.
- Created a local static review workspace at `projects/websites/vital-health-review/`.
- Built local review pages before pushing anything to Webflow:
  - `projects/websites/vital-health-review/home-review.html`
  - `projects/websites/vital-health-review/services-review.html`
  - `projects/websites/vital-health-review/about-review.html`
  - `projects/websites/vital-health-review/contact-review.html`
- Wrote implementation notes at `projects/websites/vital-health-review/meeting-2026-06-05/services-change-notes.md`.
- Restarted the local preview server on port `8765`; current review URL is `http://127.0.0.1:8765/home-review.html`.

## Decisions made

- Keep all edits as local review HTML first, then push to Webflow staging only after Annabel reviews.
- Use “50+ years of clinical care” instead of “Since 1970” because the clinic itself is not 56 years old.
- Use “long term vitality” rather than dash-heavy copy in client-facing page text.
- Change visible consultation references from 30 or 90 minutes to 60 minutes.
- Expand Services from four pillars to five pillars by adding Advanced Diagnostics and Early Detection.
- Add the Dr. Feste CV download as a placeholder link only because the actual 55-page CV file was not provided.
- Do not publish unsupported medical absolutes or statistics without clinician sign-off and citations.

## Implemented review copy

- Homepage hero tagline changed to the “You are more than a symptom” language.
- Header logo and Vital Health wordmark enlarged with local CSS overrides.
- Services page updated with the fifth diagnostics pillar, including DNA testing, Galleri, GlycanAge, Next Gen cognitive testing, CognitiveView, carotid ultrasound, HRV and body composition, heavy metal testing, GI MAP, and full body MRI offering.
- Peptide section now includes the personal/labs/goals intro and a note that more peptides may be available.
- Hormone section expanded with women’s and men’s symptom lists.
- Wellness section now emphasizes IV therapy, ozone protocols, young plasma discussions, and softened exosome language.
- Contact and footer hours changed to Monday to Friday, 8am to 5pm.

## Open questions

- Need the actual Dr. Feste 55-page CV file and desired filename before replacing the placeholder link.
- Need Dr. Feste’s citation before adding the “stem cells drop 90% by age 30” claim.
- Need clinician approval or citation before using the “100% of postmenopausal women lack testosterone” claim.
- Need supplement/shop decisions: public products, portal products, or both; Shopify/Webflow/Clover approach; fulfillment; private-label details.
- Need the hormone reorder form URL or implementation direction before placing it next to the patient portal.
- Need headshots for Julie/Kerri and any final team imagery.
- Need exact diagnostics/supplement PDF content before finalizing the Advanced Diagnostics descriptions.
- Need testimonial/review-feed source and implementation choice for the 85+ reviews idea.

## Next steps

- Annabel reviews the four local pages in the in-app browser.
- If copy/layout direction is approved, prepare a Webflow staging update plan using the existing page IDs from prior checkpoints.
- Replace local-only placeholders with real assets and URLs.
- Push only to Webflow staging, then QA desktop/mobile, links, console, and form/portal paths before any client handoff.

## Context to preserve

- Webflow site ID from previous checkpoint: `6a15e6f364922623e13946da`.
- Services page ID: `6a15f430cbd0f7ef0469e27f`.
- About page ID: `6a19b8b56de372b248e55901`.
- Contact page ID: `6a19bf5c98546d4f3a53d97a`.
- Static preview server command: `python3 -m http.server 8765` from `projects/websites/vital-health-review/`.
- QA already passed locally: HTML parser checks, stale-copy search, Playwright desktop/mobile snapshots, mobile menu check, no console errors, and no mobile horizontal overflow on Services.
- Current AI-OS git worktree has many unrelated pre-existing deletions/changes; do not stage or revert them casually.

## System refinement candidates

- A Webflow static-review workflow should preserve page-specific local CSS overrides separately from content changes so Webflow Designer implementation is less manual.
- Vital Health medical claims need a small citation/sign-off tracker before push, especially for hormone, exosome, stem-cell, cancer-screening, and GLP-1 copy.
