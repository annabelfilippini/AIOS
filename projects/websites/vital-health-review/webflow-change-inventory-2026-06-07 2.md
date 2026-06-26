# Vital Health Webflow Change Inventory

Date: 2026-06-07
Target: Webflow staging only, `https://vital-health-9bf311.webflow.io`
Local review source: `projects/websites/vital-health-review/*-review.html`

## Current Staging Baseline

- Verified staging Home, Services, About, and Contact return `200`.
- Verified staged HTML currently matches the local `*-source.html` captures.
- Verified `/shop` currently returns `404`.
- Therefore, the pending Webflow delta is the difference between `*-source.html`
  and `*-review.html`.

## Global Changes

- Add `Shop` to the main navigation and footer navigation if the Shop page is
  included in this review batch.
- Update all internal review-file links back to Webflow paths before publishing:
  - `home-review.html` -> `/`
  - `services-review.html` -> `/services`
  - `about-review.html` -> `/about`
  - `shop-review.html` -> `/shop`
  - `contact-review.html` -> `/contact`
- Update footer service links and order:
  - Hormone Optimization -> `/services#hormone`
  - Weight Management -> `/services#weight`
  - Peptide Therapy -> `/services#peptide`
  - Regenerative Medicine -> `/services#regenerative`
  - Advanced Diagnostics & Early Detection -> `/services#diagnostics`
- Update footer address everywhere:
  - `500 N Capital of Texas Hwy`
  - `Bldg 6, Suite 125`
  - `Austin, TX 78746`
- Update footer hours to `Monday to Friday · 8a to 5p`.
- Replace the old footer blurb with the new "You are more than a symptom..."
  whole-health positioning.
- Keep external Patient Portal links pointed at `https://vitalhealth.md-hq.com`.

## Home

- Update SEO/meta description to the new whole-person positioning:
  `You are more than a symptom. Our integrative, regenerative, and preventive
  approach draws on fifty years of clinical care to support your whole health,
  body, mind, and long-term vitality.`
- Update hero ticker from `Austin, Texas · Integrative Medicine · Since 1970`
  to `Austin, Texas · Whole-person care`.
- Replace hero lead with the new "You are more than a symptom..." copy.
- Replace the first fact from `50+ Years of clinical foundation...` to `Labs`
  with supporting copy: `Deeper testing and a full clinical picture guide each
  care plan.`
- Change first visit fact from `90 min` to `60 min`.
- Change Services preview from four pillars to five pillars.
- Replace old services intro, including `prescribed against your physiology`,
  with the new "Whatever brought you here..." copy.
- Reorder Home service cards:
  - Hormone Optimization
  - Weight Management
  - Peptide Therapy
  - Regenerative Medicine
  - Advanced Diagnostics & Early Detection
- Rename `Medical Weight Loss` to `Weight Management`.
- Replace `Wellness & Rejuvenation` as a pillar with `Regenerative Medicine`.
- Add the new Advanced Diagnostics & Early Detection card.
- Update founder/legacy philosophy copy so it does not imply the clinic itself
  has operated for fifty years.
- Replace testimonial placeholders with a Google-review rail concept:
  - Four native cards in the local mock.
  - Labels should communicate 5-star Google reviews only.
  - Do not publish fake patient testimonials.
- Update schedule section consultation copy from `Thirty minutes` to
  `Sixty minutes`.
- Update schedule section address and hours to the new address/hours.

## Services

- Update page meta description from the old four-pillar description to:
  `Hormone optimization, weight management, peptide therapy, regenerative
  medicine, and advanced diagnostics and early detection, guided by labs, goals,
  and the full clinical picture.`
- Change hero and intro from four pillars to five pillars.
- Use the five service anchors:
  - `#hormone`
  - `#weight`
  - `#peptide`
  - `#regenerative`
  - `#diagnostics`
- Hormone Optimization:
  - Soften and polish the intro.
  - Keep the women's testosterone decline claim only in softened form already
    present in the local review copy.
  - Add women's condition/support bullet groups.
  - Add men's low-testosterone symptom bullet group.
  - Change first visit from `ninety minutes` to `60 minutes`.
  - Replace `protocol written against the labs` with wording based on labs and
    clinical picture.
- Weight Management:
  - Rename from `Medical Weight Loss` to `Weight Management`.
  - Remove the semaglutide `18% bodyweight after 6 to 8 weeks` claim.
  - Soften GLP-1 copy around research support, risks, benefits, health history,
    labs, and expected timelines.
  - Replace `appetite suppressant` style wording with broader appetite/fullness
    regulation copy.
- Peptide Therapy:
  - Move to the third pillar.
  - Use the PDF-approved/patient-approved personal intro:
    `Peptide therapy works best when it's personal...`
  - Replace epigenetic/longevity-promotion claims with clinical-picture,
    labs/goals/history language.
  - Add `How peptide therapy is considered`.
  - Include reviewed peptide protocol cards:
    Ipamorelin, Sermorelin, BPC-157, CJC-1295, MOTS-c, Thymosin-alpha1,
    PT-141, Semax / Selank.
  - Include the note that this is not a complete peptide list and additional
    options may be discussed during the 60 minute consultation.
- Regenerative Medicine:
  - Replace old `Wellness & Rejuvenation` pillar.
  - Include exosomes, IV nutrient protocols, ozone, NAD+ and glutathione, and
    young plasma discussion copy.
  - Remove the old numeric exosome/stem-cell concentration claim.
  - Use cautious language around exosomes as cellular messengers studied for
    inflammation signaling and tissue repair pathways.
- Advanced Diagnostics & Early Detection:
  - Add a new fifth service section at `#diagnostics`.
  - Include draft testing cards for DNA testing, Galleri, GlycanAge, NexGen,
    Cognivue, carotid ultrasound, HRV and body composition, heavy metal
    testing, GI MAP, full body MRI offering, and related advanced diagnostics
    from the local review page.
  - Keep this marked as draft pending final clinic PDF/list approval.
- Schedule section:
  - Change consultation copy to `Sixty minutes`.

## About

- Update SEO/meta description away from "four practitioners" and "fifty years
  of clinical foundation" wording.
- Update hero/body copy to:
  - One coordinated record.
  - Whole-person care.
  - The team continuing Dr. Feste's model.
- Update founder philosophy so it does not overstate current role or clinic age.
- Change first visit reference from `ninety minutes` to `60 minutes`.
- Update Dr. Feste bio:
  - Remove `50+ Years / Of clinical practice` stat.
  - Use `Clinical / Practice foundation`.
  - Add a placeholder `Download Dr. Feste's CV` link only after replacing the
    local placeholder with the actual CV asset or hiding it until the file is
    available.
- Update schedule section consultation copy to `Sixty minutes`.
- Update footer services, address, hours, and blurb.

## Contact

- Update SEO/meta description and visible contact copy to the new address:
  `500 N Capital of Texas Hwy, Bldg 6, Suite 125, Austin, TX 78746`.
- Update schedule CTA copy from `Thirty minutes` to `Sixty minutes`.
- Update visible address block:
  - `500 N Capital of Texas Hwy`
  - `Bldg 6, Suite 125`
  - `Austin, TX 78746`
- Update hours to:
  - `Monday to Friday`
  - `8am to 5pm`
- Update map/directions copy to the new West Austin address.
- Update Google Maps URL query to:
  `500+N+Capital+of+Texas+Hwy+Bldg+6+Suite+125+Austin+TX+78746`
- Update footer services, address, hours, and blurb.

## Shop

- Local review page exists at `shop-review.html`.
- Staging `/shop` currently returns `404`.
- Treat Shop as a separate Webflow page decision unless Annabel wants it in this
  client review push.
- Local concept includes:
  - Supplement cards with pricing and stock labels.
  - Supplement reorder path.
  - Hormone refill/care request path.
  - Secure form placeholder.
- Blockers before a real Shop launch:
  - Decide Shopify/Webflow/Clover/public-products architecture.
  - Confirm refill form URL or HIPAAtizer replacement.
  - Confirm compliance posture for hormone refill/care request flows.
  - Confirm fulfillment, payment, private-label, and inventory ownership.

## Blockers Before Custom-Domain Live Publish

- Do not publish to the custom domain in this batch.
- Replace or hide all review-only testimonial/review placeholders.
- Confirm Advanced Diagnostics names and descriptions with the final clinic PDF.
- Get clinician sign-off/citations before adding or strengthening sensitive
  claims around testosterone, stem-cell/exosome statistics, GLP-1 timelines,
  cancer screening, peptides, young plasma, or regenerative outcomes.
- Replace the Dr. Feste CV placeholder with the actual CV asset or hide the link.
- Confirm Julie/Kerri headshots and final team imagery if the client expects
  those live.
- Resolve policy links if `Privacy · HIPAA` should become actual links.

## QA After Webflow Staging Push

- Publish to `.webflow.io` staging only.
- Check Home, Services, About, Contact, and optionally Shop at desktop ~1440px
  and mobile ~390px.
- Verify mobile nav includes all intended links and does not overflow.
- Verify anchors: `#hormone`, `#weight`, `#peptide`, `#regenerative`,
  `#diagnostics`, `#schedule`, and `#google-reviews` if used.
- Search published HTML for stale copy:
  `Since 1970`, `Thirty minutes`, `90 minutes`, `ninety`, `7000 Bee Cave`,
  `Suite 310`, `prescribed against your physiology`, `Medical Weight Loss`,
  `Wellness & Rejuvenation`, and `DNA Testing and Genomics`.
- Verify Google Maps, Patient Portal, phone, email, and contact links.
- Check console errors and horizontal overflow.
