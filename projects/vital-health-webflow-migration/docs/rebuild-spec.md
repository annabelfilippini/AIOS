# Vital Health Webflow Rebuild Spec

## Visual System

- Fonts: Fraunces for headings, Inter for body/UI.
- Palette:
  - Cream: `#F5EFE0`
  - Paper: `#FBF7EC`
  - Forest: `#1F4D2A`
  - Deep forest: `#163820`
  - Gold: `#C9A04A`
  - Ink: `#2A2A26`
  - Muted: `#7A776B`
- Style notes: square CTAs, refined editorial spacing, cream/forest/gold medical-wellness feel, hummingbird/logo lockup.

## Pages

### Home

- Hero with editorial still-life background, Vital Health headline, consultation CTA, services link.
- Practice facts.
- Four service cards.
- Philosophy section.
- Reviews/testimonials placeholder.
- Schedule/contact CTA.

### Services

- Service navigation anchors.
- Core services:
  - Peptide Therapy
  - Hormone Optimization
  - Medical Weight Loss
  - Wellness & Rejuvenation
- Each service should be CMS-ready if Vital Health wants ongoing edits.

### About

- Founder/legacy positioning.
- Provider/team content should become CMS if bios will change.
- Preserve Bee Cave Road details.

### Contact

- Phone, email, address, hours.
- Cerbo patient portal / scheduling links.
- Google Maps link.

## CMS Collections

### Services

- Name
- Slug
- Short summary
- Long description
- Icon label or asset
- Display order
- CTA label
- CTA URL

### Providers

- Name
- Credentials/title
- Bio
- Photo
- Specialty tags
- Display order

### Promotions

- Title
- Summary
- Start date
- End date
- CTA label
- CTA URL
- Active flag
- Disclaimer text

### Patient Resources

- Title
- Category
- Summary
- Body
- File/link
- Display order

## External Systems

- Cerbo remains the patient portal and patient records system.
- All patient portal CTAs link to `https://vitalhealth.md-hq.com`.
- Product/hormone commerce flow still needs discovery: Cerbo, Fullscript, WholeScripts, Xymogen, Shopify, or mixed workflow.

