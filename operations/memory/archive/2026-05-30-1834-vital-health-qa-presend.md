---
date: 2026-05-30
time: 18:34
project: vital-health-webflow-migration
status: complete
next-session: Decide on testimonial + headshot placeholders before sending review link to Rob/Julie; proposal PDF is send-ready
---

# Session: Vital Health pre-send QA (site + proposal)

## What we worked on
- QA'd the live site (https://vital-health-9bf311.webflow.io) across all 4 pages,
  desktop + mobile, ahead of sending to Rob and Julie.
- QA'd + finalized the proposal doc; scrubbed all remaining em/en-dashes per the
  no-dash rule and rebuilt both PDF copies.

## Site QA results
- Home, Services, About, Contact all render correctly on desktop (1440) and
  mobile (390). Nav, logo, all CTAs/Patient Portal point to Cerbo/MD-HQ
  (vitalhealth.md-hq.com); phone tel:5125594350; contact info consistent.
- Full-page screenshot shows blank sections — that's just Webflow scroll
  animations (opacity:0 until in view), NOT a bug. Content renders fine on real
  scroll. (Don't trust fullPage screenshots for this site; scroll + viewport shot.)
- TWO known placeholders still visible on the live site (both map to Phase 2):
  1. Home testimonials: 3 cards show "[Patient testimonial: drop in a real quote
     from a Google or patient review here.]" / "Patient name".
  2. About team photos: Dr. Feste has a real photo; Julie Swett (JS) and Kerri
     Thigpen (KT) show monogram placeholders awaiting headshots.

## Proposal QA results
- Math verified: 14h×$95=$1,330, 22h×$95=$2,090; +$700 = $2,030–$2,790, under $5k.
- Scrubbed dashes: title + phase headers now use colons ("Vital Health: ...",
  "Phase 1: Website (complete, flat fee)"); table ranges "5 to 7"..."14 to 22 hrs";
  "honest ranges, to be confirmed"; "Running total (Phases 1 and 2)". Verified
  zero em/en-dashes remain. Also fixed the hardcoded H1 in the build script.
- Rebuilt PDF -> docs/proposal-vital-health-website.pdf AND ~/Desktop/Vital Health
  Proposal.pdf (3 pages, branded).

## Open decision (for Annabel)
- Send review link as-is (placeholders explained by Phase 2), or hold testimonials/
  headshots until real content is in? Recommendation: send with a one-line note
  that testimonials + NP headshots are Phase 2 placeholders.

## Context to preserve
- Build pipeline: /tmp/build_proposal_pdf.py (writes /tmp/proposal-vital-health.html)
  then headless Chrome --print-to-pdf. Both still present this session.
- Proposal source of truth: docs/proposal-vital-health-website.md
