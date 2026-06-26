---
date: 2026-06-07
time: 16:18
project: vital-health-webflow-review
status: in-progress
next-session: Review the local Vital Health HTML at http://127.0.0.1:8765/home-review.html with Annabel, then prepare a Webflow staging-only update plan if approved.
---

# Session: Vital Health PDF and transcript HTML review pass

## What we worked on

- Read `~/Downloads/vital_health_website_copy (2).pdf`.
- Cross-checked the PDF against the June 5 Zoom transcript at `projects/websites/vital-health-review/meeting-2026-06-05/audio1562734014.txt`.
- Updated only the local static review HTML, not Webflow:
  - `projects/websites/vital-health-review/home-review.html`
  - `projects/websites/vital-health-review/services-review.html`
  - `projects/websites/vital-health-review/about-review.html`
  - `projects/websites/vital-health-review/contact-review.html`
  - `projects/websites/vital-health-review/shop-review.html`
- Kept the local preview server running on port `8765`.

## Decisions made

- Homepage hero uses PDF Option B because the transcript has Dr. Feste choosing the second option.
- Services intro uses a hybrid: the PDF's "path forward" direction plus the meeting-approved five-pillar structure.
- Consultation length stays at 60 minutes because the Zoom transcript explicitly corrected 30/90 minute references to 60 minutes.
- Removed old `prescribed against your physiology` language from review HTML.
- Fifth service pillar is `Advanced Diagnostics & Early Detection`, with local anchor `#diagnostics`.
- Diagnostics content reflects the PDF while preserving meeting-mentioned tests such as GI MAP, heavy metals, gene testing, and full body MRI.
- Peptide intro now uses the PDF-approved personal/labs/goals/full-clinical-picture language.
- Hormone Optimization section now reflects the PDF in the current website layout, including women, men, and What We Treat lists.
- Hormone bullet lists were styled into polished two-column groups on desktop and one-column groups on mobile.

## Open questions

- Whether the current Advanced Diagnostics list is final enough for Webflow, or whether Vital Health will send a cleaner official PDF/list with exact final names.
- Whether unsupported medical claims such as absolute post-menopausal testosterone language or stem-cell statistics should remain omitted until clinician citation/sign-off.
- Whether the local review should keep the Shop page in this batch or separate shop into its own backend/compliance pass.
- Whether Webflow should use `Advanced Diagnostics & Early Detection` everywhere, including metadata and CMS/navigation labels.

## Next steps

- Annabel reviews the local pages, especially Hormone Optimization and Advanced Diagnostics.
- If approved, prepare a Webflow staging-only update plan for Home, Services, About, Contact, and Shop footer labels.
- Push to Webflow staging only, not live.
- QA staging desktop/mobile, anchors, old-copy search, footer links, patient portal, map/address, and console errors before client handoff.

## Context to preserve

- Local review URL: `http://127.0.0.1:8765/home-review.html`.
- Verified stale-copy search clean for `prescribed against`, `DNA Testing and Genomics`, `#genomics`, `ninety`, `90 minutes`, and `30 minutes`.
- Browser checks confirmed Home and Services rendered expected copy and anchors.
- Mobile-width check on Services found no horizontal overflow after the longer hormone and diagnostics copy.
- `operations/annabel-press/usage/events.jsonl` was updated because `client-website-refresh` and `webflow-rebuild-qa` were materially used.
- AI-OS worktree still has a large unrelated dirty state. Do not broad-stage or revert casually.

## System refinement candidates

- Add a reusable Vital Health/Webflow review checklist for PDF-vs-transcript conflicts: option selection, consultation length, service labels, claim sign-off, anchors, metadata, and stale-copy search.
