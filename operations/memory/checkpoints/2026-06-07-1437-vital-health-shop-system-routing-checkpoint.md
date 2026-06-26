---
date: 2026-06-07
time: 14:37
project: vital-health-webflow-review
status: in-progress
next-session: Continue Vital Health Shop/Webflow implementation by connecting Shopify for public supplements and confirming HIPAAtizer notification settings for hormone refill submissions.
---

# Session: Vital Health shop and refill routing

## What we worked on

- Researched how Vital Health should route Webflow, Shopify, Clover, Cerbo, and reorder workflows.
- Reviewed the local Vital Health static review site at `projects/websites/vital-health-review/`.
- Added a new local review page:
  - `projects/websites/vital-health-review/shop-review.html`
- Updated nav/footer links on:
  - `projects/websites/vital-health-review/home-review.html`
  - `projects/websites/vital-health-review/services-review.html`
  - `projects/websites/vital-health-review/about-review.html`
  - `projects/websites/vital-health-review/contact-review.html`
- Inspected the current live Vital Health `/orders` page and identified its form implementation.

## Decisions made

- Webflow should remain the public front door and design layer.
- Shopify can be connected to Webflow for normal public supplement ecommerce.
- Hormone refills should not go through Shopify checkout.
- Hormone refill requests should stay on a secure form route because they are patient-specific and may include PHI.
- The current live `/orders` form uses HIPAAtizer, not a normal Webflow/Wix form.
- The local Shop page now embeds the same HIPAAtizer workflow directly instead of linking users back to the old Wix `/orders` page.
- Hero CTA routing on `shop-review.html`:
  - `Shop supplements` jumps to `#supplements`.
  - `Hormone refills` jumps to `#hormone-refills`.
- Lower reorder card routing:
  - `Open refill form` jumps to the embedded HIPAAtizer form section.

## Open questions

- Who has HIPAAtizer account access?
- Where are HIPAAtizer submissions currently stored and emailed?
- Should HIPAAtizer notification emails go to `jswett44@gmail.com`, or should Vital Health use a clinic-controlled Google Workspace address covered by its HIPAA/BAA setup?
- Does Vital Health want supplement products fully public, patient-only, or a mix?
- What exact Shopify store/products/collection IDs should be embedded next session?
- Should Clover remain payment-only, and if so, where should invoice/payment links live relative to Cerbo and Shopify?

## Next steps

- Connect Shopify Buy Button or collection embeds into the `#supplements` product area on `shop-review.html`.
- Replace static product cards with real Shopify products once store access/IDs are available.
- Log into HIPAAtizer and confirm the workflow `0baba513-3dc7-4a57-8459-1ea60e2a8a19` notification/submission settings.
- If approved, update HIPAAtizer recipient settings from inside HIPAAtizer, not from Webflow HTML.
- QA the published Webflow staging page after adding Shopify and the HIPAAtizer embed.

## Context to preserve

- HIPAAtizer iframe currently embedded:
  - `https://app.hipaatizer.com/workflow/0baba513-3dc7-4a57-8459-1ea60e2a8a19?initialValues=%5B%7B%22data%22%3A%7B%7D%2C%22formId%22%3A%222cb1113c-a7e1-4995-ad71-97f9d51ec657%22%7D%5D&size=desktop&isStartMultiWorkflow=false&overflowY=scroll`
- Headless QA confirmed the iframe loads the HIPAAtizer form text:
  - `Hormone Re-Order`
  - First Name, Last Name, Address, Email, Phone
  - Testosterone Cream, Testosterone Cypionate, Progesterone, Estradiol, NP Thyroid, CMP Thyroid, DHEA
  - Credit card on file, comments, reCAPTCHA, Submit
- The local `file://` screenshot can show the iframe area blank, but frame inspection confirmed the form content loads.
- Do not submit a test refill form without explicit approval because it would create a real patient-style request.
- Keep avoiding broad git staging because AI-OS has a large unrelated dirty tree.

## System refinement candidates

- Add a Vital Health backend-routing checklist: public ecommerce, patient-specific requests, payments, portal, form provider, notification recipients, HIPAA/BAA owner.
- Add a reusable Webflow healthcare form rule: embed HIPAA-capable providers for PHI and configure recipients inside the provider account, never via plain Webflow forms or ad hoc email scripts.
