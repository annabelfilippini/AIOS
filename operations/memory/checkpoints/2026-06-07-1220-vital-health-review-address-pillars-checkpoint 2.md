---
date: 2026-06-07
time: 12:20
project: vital-health-webflow-review
status: in-progress
next-session: Review the local Vital Health pages with Annabel, then translate approved address, copy, and pillar-order edits into Webflow staging only.
---

# Session: Vital Health review HTML address and pillar cleanup

## What we worked on

- Continued from `operations/memory/checkpoints/2026-06-07-1157-vital-health-webflow-review-meeting-updates.md`.
- Updated the local static review workspace at `projects/websites/vital-health-review/`.
- Edited:
  - `projects/websites/vital-health-review/home-review.html`
  - `projects/websites/vital-health-review/services-review.html`
  - `projects/websites/vital-health-review/about-review.html`
  - `projects/websites/vital-health-review/contact-review.html`
- Restarted the local preview server on port `8765` for browser verification.

## Decisions made

- Address is now `500 N Capital of Texas Hwy, Bldg 6, Suite 125, Austin, TX 78746`.
- Removed copy implying the clinic itself has been around for 50 years, including the homepage hero ticker.
- Homepage hero ticker now has only two items: `Austin, Texas · Whole-person care`.
- Service pillars should appear in this order everywhere:
  1. Hormone Optimization
  2. Weight Management
  3. Peptide Therapy
  4. Regenerative Medicine
  5. DNA Testing and Genomics
- Old service labels were normalized away from `Medical Weight Loss`, `Wellness & Rejuvenation`, and `Advanced Diagnostics & Early Detection` in the review pages.

## Open questions

- Whether `DNA Testing and Genomics` should remain the public-facing name even though that section still contains broader diagnostics content such as Galleri, GlycanAge, CognitiveView, carotid ultrasound, HRV, GI MAP, and full body MRI.
- Whether the address change should be pushed to all Webflow metadata, map URLs, structured data, and any platform/footer settings after Annabel approves the local review pages.
- Whether the homepage facts block should keep `Labs` as the replacement for the old `50+` stat or use a more polished metric/value.

## Next steps

- Have Annabel review the local preview at `http://127.0.0.1:8765/home-review.html`.
- If approved, prepare a Webflow staging update plan using known page IDs from the prior checkpoint.
- Push only to Webflow staging, not live, then QA desktop/mobile, anchors, map link, footer links, portal links, and metadata.
- Keep avoiding broad git staging because AI-OS has a large unrelated dirty tree.

## Context to preserve

- Fresh browser verification confirmed:
  - Homepage ticker: `Austin, Texas · Whole-person care`.
  - Homepage cards and Services page jump nav/sections match the requested pillar order.
  - Stale-copy search found no `50+ years`, `50 years`, `fifty years`, `7000 Bee Cave`, old address suite, or old pillar labels in `*-review.html`.
- HTML tag-balance check passed for all four review pages.
- The four review HTML files are currently untracked in AI-OS git status; `operations/annabel-press/usage/events.jsonl` is modified from capability-use logging.

## System refinement candidates

- Add a small static-review checklist for client factual corrections: address, headers, metadata, footers, map links, anchors, repeated service labels, and stale-copy search terms.
