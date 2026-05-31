---
date: 2026-05-26
time: 20:16
project: consulting / vital-health
status: paused
next-session: Use these manager questions in the Vital Health proposal/follow-up, then scope the Vercel mockup rebuild into Webflow.
---

# Session: Vital Health Proposal Questions And Webflow Transfer

## What we worked on

- Preserved Annabel's additional Rob-call notes for the Vital Health website proposal.
- Recalled the current preview URL: `https://vital-health-deploy.vercel.app/`.
- Confirmed the existing mockup is a static HTML/CSS/JS site hosted on Vercel, with links to the Cerbo patient portal at `https://vitalhealth.md-hq.com`.
- Clarified that the real client-manageable site should be rebuilt in Webflow rather than connected to Vercel by API.

## Decisions made

- Keep the patient portal. The proposal should not imply replacing Cerbo.
- Position the work as `Website Refresh + Patient Store Workflow Coordination`, not a simple brochure-site redesign.
- Webflow is the recommended public-site platform; Vercel is only the current preview/mockup host.
- No API is needed to transfer the Vercel mockup into Webflow. The practical path is to rebuild the design in Webflow using the current site as visual/content reference, then point buttons/links to Cerbo or the relevant dispensary/store.
- Use CMS-backed Webflow areas for editable public content such as provider bios, services, patient resources, announcements, and promotion banners.

## Open questions

- Do they use Cerbo only, Fullscript, WholeScripts, Xymogen, Shopify, or a mix for supplements/hormones?
- Where do providers add product/hormone recommendations for patients: Cerbo, Fullscript, WholeScripts/Xymogen, or another system?
- Who fulfills products: the office, a third-party dispensary, drop-shipping, or both?
- Should products be patient-portal-only, public retail, or a hybrid?
- Where do promotions actually happen: public website announcement, checkout discount, patient-specific discount, or backend coupon?
- Who needs backend/admin access for promotions and product updates?

## Next steps

1. Include a short discovery section in the proposal before final backend scope/pricing.
2. Ask the manager:
   - You use Cerbo for patient records, notes, labs, billing, and the patient portal. For supplements/hormones, are you also using Fullscript, WholeScripts, Xymogen, Cerbo inventory, Shopify, or something else?
   - When a provider recommends supplements or hormones, where does that recommendation get added?
   - Who fulfills the order: your office, a third-party dispensary, or both?
   - Should products be available only to logged-in patients through the patient portal, or do you also want any public retail shopping on the website?
   - When you run promotions, do those discounts happen inside Cerbo/Fullscript/checkout, or do you just need the public website to advertise the promotion?
3. Scope Webflow rebuild as a manual rebuild/migration from the Vercel preview:
   - Audit current pages and assets.
   - Recreate global style system in Webflow.
   - Rebuild Home, Services, About, Contact.
   - Convert repeatable areas into CMS where useful.
   - Wire patient portal and booking links.
   - QA responsive layout and links before launch.

## Context to preserve

- Rob's needs: refresh site; ensure accuracy of patient store; providers need access to put hormones/products into patient portal; promotions require backend access; keep patient portal.
- Current site style: cream/forest/gold, Fraunces + Inter, square CTAs, Vital Health logo/hummingbird, editorial integrative-medicine feel.
- Existing preview content includes Bee Cave Road contact details and Cerbo portal links.

## System refinement candidates

- Create a reusable wellness/medical Webflow proposal template after this proposal is drafted.
