---
date: 2026-05-31
time: 10:02
project: vital-health-webflow-migration
status: complete
next-session: Proposal is send-ready (2 pages); decide on testimonial + NP-headshot placeholders before sending the live review link to Rob/Julie
---

# Session: Vital Health proposal final edits + 2-page fit

## What we worked on
- Re-QA'd site + proposal, applied a round of client-requested proposal edits,
  and compressed the PDF layout to fit on 2 pages (signature was orphaned on p3).

## Site QA (unchanged from prior session, re-confirmed)
- Home, Services, About, Contact all render correctly desktop (1440) + mobile (390).
- Nav/logo/CTAs/Patient Portal -> vitalhealth.md-hq.com; phone tel:5125594350;
  contact info consistent across pages.
- Webflow scroll animations make fullPage screenshots look blank — NOT a bug;
  scroll + viewport-shot to QA this site.
- TWO known placeholders still live (both = Phase 2 scope):
  1. Home testimonials: 3 cards "[Patient testimonial: drop in a real quote...]".
  2. About: Feste has real photo; Julie (JS) + Kerri (KT) are monogram placeholders.

## Proposal edits made this session
- Scrubbed ALL em/en-dashes per no-dash rule: title + phase headers use colons
  ("Vital Health: ...", "Phase 1: Website"); table ranges "5 to 7"..."14 to 22 hrs";
  "honest ranges, to be confirmed"; "Running total (Phases 1 and 2)". Verified 0 dashes.
- Removed "(complete, flat fee)" from Phase 1 header.
- Removed "(after we meet with managers)" from Phase 2 header.
- Removed "(final billable TBD with Dr. Feste, Julie, and staff)" from Phase 2
  estimate bullet — now ends "at $95/hr."
- Unbolded "automated weekly posting workflow" and "$95/hr" in Instagram section.
- Compressed CSS to fit 2 pages: @page margin 0.8->0.6in; body 11.5->10pt,
  line-height 1.55->1.4; h1 16->14pt; h2 14->12pt; h3 12->10.5pt; table 10.5->9.5pt;
  p/li/ul margins reduced; signature margin-top 26->16px. Result: clean 2 pages,
  signature sits on p2 after "A note on the estimates". Math still verified
  ($2,030-$2,790, under $5k).

## Open decision (carried)
- Terms + "A note on the estimates" still say "final billable confirmed with
  Dr. Feste, Julie, and staff input" — Annabel may want these stripped too for
  consistency (offered; not yet actioned).
- Send review link as-is (placeholders = Phase 2) vs hold for real testimonials/
  headshots. Recommendation: send with one line noting they're Phase 2 placeholders.

## Context to preserve
- Source of truth: docs/proposal-vital-health-website.md
- Build pipeline: /tmp/build_proposal_pdf.py -> /tmp/proposal-vital-health.html ->
  headless Chrome --print-to-pdf (Google Chrome). H1 + CSS live in the script,
  not the markdown (script strips the md H1). Recreate /tmp script if cleared.
- Output (both copies): docs/proposal-vital-health-website.pdf AND
  ~/Desktop/Vital Health Proposal.pdf
- Live review link: https://vital-health-9bf311.webflow.io

## System refinement candidate
- PDF build pipeline (markdown -> styled HTML -> Chrome print) is reusable and
  worth promoting from /tmp to a project skill or skills/ script.
