---
date: 2026-05-26
time: 18:39
project: consulting / vital-health
status: paused
next-session: Draft Vital Health proposal with Webflow public site + Cerbo/Fullscript backend coordination, using paid discovery or hybrid fixed-fee/hourly structure.
---

# Session: Vital Health Proposal And Backend Architecture

## What we worked on

- Recovered context for the Vital Health website project and live preview: `https://vital-health-deploy.vercel.app/`.
- Identified prior durable notes in Claude scratchpads:
  - `/Users/annabelfilippini/.claude/scratchpad/2026-04-22-1440-vital-health-mockups.md`
  - `/Users/annabelfilippini/.claude/scratchpad/2026-04-23-1104-vital-health-hybrid-mockups.md`
  - `/Users/annabelfilippini/.claude/scratchpad/2026-04-23-1235-vital-health-retry-direction-f.md`
  - `/Users/annabelfilippini/.claude/scratchpad/2026-04-23-1305-vital-health-feedback-pass.md`
  - `/Users/annabelfilippini/.claude/scratchpad/2026-04-23-1430-vital-health-logo-pass.md`
  - `/Users/annabelfilippini/.claude/scratchpad/2026-04-23-1508-vital-health-logo-fix-deploy.md`
- Discussed Annabel's meeting with Vital Health: they like the bones of the mockup and want help with the real website plus Cerbo/backend/product flow.
- Clarified likely architecture: public site is separate from Cerbo/Fullscript backend.
- Researched/confirmed Cerbo functions: EHR, practice management, patient portal, scheduling, forms, billing, supplements, inventory, patient records, integrations.
- Researched/confirmed Fullscript role: online supplement dispensary/check-out/fulfillment/promotions that can integrate with Cerbo.
- Clarified that Shopify is likely unnecessary unless Vital Health wants a public store.

## Decisions made

- Recommended public marketing site platform: **Webflow**.
- Reasoning: Vital Health needs editable pages, provider bios, service copy, announcements, and public promotion banners without needing custom-code maintenance.
- Recommended backend model:
  - Webflow = public site / services / trust / provider bios / patient resources / promo announcements.
  - Cerbo = patient portal, EHR, scheduling/forms/messages, billing/invoices, patient records, in-office inventory/refill requests.
  - Fullscript or WholeScripts = practitioner supplement recommendations, online checkout, shipping/fulfillment, discounts/promotions.
- Annabel should not position herself as “building Cerbo.” She is building the public website and coordinating/testing the patient-facing backend workflow.
- Pricing stance discussed:
  - Do not quote as a simple website.
  - Use hybrid pricing: fixed fee for website, hourly/capped block for Cerbo/backend coordination.
  - Suggested baseline: $95/hr for meetings/backend coordination, not below $85/hr.
  - Suggested structure: paid discovery/technical scope ($950-$1,500), website build around $6,500-$8,500, backend coordination hourly or 10-hour block.
- Proposal should explicitly exclude custom EHR development, HIPAA/legal compliance review, third-party subscription fees, and vendor implementation work unless separately scoped.

## Open questions

- Does Vital Health currently use Fullscript, WholeScripts/XYMOGEN, Shopify, Cerbo inventory only, or a mix?
- Are products fulfilled from the office, drop-shipped, or both?
- Do practitioners need to recommend products to specific patients, or should patients browse a public catalog?
- Should patients buy inside Cerbo, Fullscript, WholeScripts, or a separate store?
- Do promotions apply to all patients, specific patients, first orders, auto-refills, or specific products?
- How many products/SKUs exist now?
- Who manages inventory, pricing, promotions, and fulfillment today?
- Who is the Cerbo admin/support contact?
- Who will update the public site after launch?
- Are they expecting copywriting, migration, SEO, photography/headshots, testimonials, and product/pricing entry?

## Next steps

1. Draft a proposal outline with:
   - Project summary
   - Recommended architecture
   - Scope included
   - Scope excluded
   - Discovery/backend coordination block
   - Website build fixed fee
   - Hourly backend/vendor coordination terms
   - Timeline, revision rounds, client responsibilities
2. Draft a short technical discovery questionnaire specifically for Cerbo/product workflow.
3. Recommend Webflow for public site, with a CMS-backed promotions/patient resources area.
4. Keep backend commerce out of Webflow unless they explicitly request public shopping.
5. If needed, create a one-page diagram: Webflow public site -> Cerbo portal -> Fullscript/WholeScripts checkout.

## Context to preserve

- The final mockup direction was “Direction F / hybrid light,” using cream/forest/gold, Fraunces + Inter, square CTAs, and Vital Health hummingbird/logo lockup.
- Final deployed contact details in the preview: 7000 Bee Cave Road, Suite 310, Austin, TX 78746; (512) 559-4350; <info@vitalhealthim.com>; Mon-Fri 8-5.
- Early Cedar Park details in old scratchpads were superseded by Bee Cave Road details in final Direction F.
- Live preview exists, but local source folder recorded in old scratchpads (`~/Documents/Claude/scratch/designs/vital-health-*`) was not found after reorg.
- Useful explanation for client: website promotions are editable public announcements; checkout discounts live wherever checkout happens (Fullscript, WholeScripts, Cerbo, or Shopify).

## System refinement candidates

- Consider creating a reusable “medical/wellness website proposal” template under consulting framework after this project proposal is drafted.
