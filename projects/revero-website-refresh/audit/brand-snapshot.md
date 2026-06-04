# Brand Snapshot

## Fonts

- font_primary: Inter 400, 500, 600, 700 (rendered role: headings and UI)
- font_secondary: Open Sans 400, 500, 700 (rendered role: body / paragraphs)
- font_loading_method: Google Fonts via `fonts.googleapis.com/css?family=Inter:regular,bold,500,400,600|Open+Sans:regular,bold,500` plus four self-hosted ClickFunnels OTF files referenced as `font-6209/6210/6211/6212` (e.g. `https://s3.amazonaws.com/statics.myclickfunnels.com/font/6212/file/original-dde62ee312c1fc3677d64b4d69a84363.otf`). Falls back to `'Helvetica Neue', sans-serif`.

## Colors

- accent_brand: #02B3E2
- accent_role: Used on the word "health" in the hero headline "Take back your health", on the Revero logomark cross/swirl, on the secondary "Free Info Call" outline button, on the "Join Now" pill outline, on icon glyphs in the conditions/feature cards, and on the right-column check rows in the Traditional Care vs Revero comparison.
- neutral_dark: #1D283F (deep navy used for body copy, primary headings, the "Sign Up For Revero" / "Join Now" filled CTA, and the logo wordmark)
- base_background: #FFFFFF (page) with secondary tinted panels in #F5FAFF / #E6F8FD / #E8EBF1

## Identity-bearing assets

### asset_1

- filename: mockups/assets/revero-logo.png
- description: Revero logomark, a stylized cyan-and-navy four-petal cross/swirl mark to the left of the lowercase navy "revero" wordmark.
- why_identity: This is the brand mark itself. Removing or restyling it would make the client say "this isn't my site anymore" instantly.
- source_prominence: hero (top-left of header on every page)

### asset_2

- filename: mockups/assets/revero-care-preview.png
- description: Cluster of roughly twelve squircle-cropped real-person headshots (members and clinicians, mixed ages and ethnicities) arranged in an organic blob next to the homepage hero.
- why_identity: This is the homepage hero illustration. The "Real People Real Results" positioning is carried visually by these member faces, so swapping them out would gut the proof story.
- source_prominence: hero

### asset_3

- filename: mockups/assets/revero-hero-app.png
- description: Three angled iPhone mockups showing the Revero member app screens (nutrition tracker, biomarker dashboard, content feed) on a light cyan background.
- why_identity: This is how Revero shows it is a "digital clinic" rather than a clinic-and-website. The app screenshots are the product, so removing them would erase the smart-clinic-in-your-pocket claim.
- source_prominence: section-centerpiece (Smart clinic and care team in your pocket)

### asset_4

- filename: mockups/assets/revero-original-clinician.png
- description: Cut-out photo of a smiling clinician in scrubs and stethoscope, wearing a headset and gesturing to camera, suggesting a live virtual visit.
- why_identity: This image carries the "real clinical care team, not just an app" half of the brand. Without it the site reads as a pure nutrition app.
- source_prominence: section-centerpiece (Ongoing In-App Medical Care)

### asset_5

- filename: mockups/assets/revero-original-article-1.png
- type: image
- description: Before/after member portrait, same man, captioned "Before" and "After" inside a soft-rounded card frame.
- why_identity: Concrete proof of member transformation. This is the visual shorthand for the "Real People Real Results" tagline and the testimonial section depends on this kind of evidence.
- source_prominence: section-centerpiece (Our members say it best / testimonials)

### asset_6

- filename_or_pattern: CSS — cyan scoop / arc behind hero collage
- type: shape
- description: Large cyan arc occupying the top-right of the hero section, anchored behind the patient-headshot collage. Approximately 50% of viewport width, curving from top-right down and to the left. Color #02B3E2 at full opacity at center, fading to transparent at the edges, with a softer #E6F8FD wash behind it.
- why_identity: This shape is the recurring visual signature of the Revero hero across all marketing landing pages. The collage of patient faces sits inside it. Removing the scoop and showing just the headshots on a flat white background loses the immediate "this is Revero" read.
- source_prominence: hero

Catalogued but NOT identity-bearing. DO NOT USE these in the mockup:

- mockups/assets/revero-original-app-clinic.png — duplicate of asset_3 concept
- mockups/assets/revero-original-device.png — generic cyan glucose monitor icon
- mockups/assets/revero-original-feature-1.png — stock-style line illustration (woman with fruit)
- mockups/assets/revero-original-feature-2.png — stock-style line illustration (joint magnifier)
- mockups/assets/revero-original-feature-3.png — stock-style line illustration (brain-gut)
- mockups/assets/revero-original-feature-4.png — stock-style line illustration (celebrating couple)

These were the assets Codex's v0 used as the "Conditions We Treat" tiles, which was a key part of the v0 failure. The Builder must not reach for them.

## Vibe

- vibe: clinical
- evidence: Cool cyan-on-navy palette, clean Inter/Open Sans typography, scrubbed clinician photo, app-dashboard screenshots, and a Traditional-Care-vs-Revero comparison table all project a digital-medical-clinic register rather than a wellness or lifestyle one.

## Latitude

- latitude: redirect

### Latitude notes for this project

- Cap the mockup at 10 distinct sections (header + 8 content sections + footer).
- Merge the two duplicate testimonial blocks (source sections 11 and 12) into one.
- Treat the footer call band + footer + regulatory note as a single footer block.
- The condition list in source section 3 can stay as ~6 condition tiles, but
  use the identity-bearing assets only — NOT the stock line illustrations.
  If no real photo exists for a condition, use a typographic tile (large
  condition name, restrained label) rather than a stock icon.

## Voice samples

1. "Take back your health"
2. "Get root cause treatment for your chronic conditions today"
3. "What if medicine treated the Cause, not the symptoms?"
4. "Smart clinic and care team in your pocket"
5. "Our members say it best"

## Source structure

1. Top utility nav + header — logo, How It Works, Testimonials, Organizations, Resources (Diabetes / Inflammatory conditions / Obesity & hypertension / Research), Membership, For Providers, "Call us: (415) 835-4151", Join Now CTA.
2. Hero — H1 "Take back your health" with cyan accent on "health", subhead "Get root cause treatment for your chronic conditions today", two CTAs ("Join Now" filled navy, "Free Info Call" cyan outline), member-headshot cluster illustration on right.
3. Conditions We Treat — intro line "Revero combines nutrition therapy with clinical expertise and technology to deliver personalized treatments for chronic conditions", six condition tiles (Type II Diabetes, Prediabetes, Primary Hypertension, Autoimmune Disease, Digestive Issues, Skin Conditions), "Learn more about the Revero Treatment" link.
4. How Revero Works — "Targeting The Root Causes Of Chronic Disease" with two paired blocks: "Ongoing In-App Medical Care" (clinician cut-out) and "Personalized Nutrition Therapy".
5. Smart clinic and care team in your pocket — app screenshots, supporting copy "We treat the root cause with personalized medical care and nutrition", three benefit columns (Lower blood sugar, Reduce inflammation, Restore gut health).
6. Member testimonial pull-quotes — "Working with my care team..." and "My care team is fabulous..." with phone number "(415) 835-4151".
7. Conditions detail strip — "Our clinical care and nutrition therapy can help with" Metabolic Conditions, Autoimmune (Rheumatoid Arthritis, Psoriasis, Crohn's, Ulcerative colitis), Inflammatory / Joint Conditions (Fibromyalgia, Rosacea, Eczema, IBS, Joint Pain, Osteoarthritis).
8. Free info call CTA band — "Call us at (415) 835-4151 for a free info call" with "Schedule a Call" button.
9. Membership pricing teaser — "Start your journey with an incredible first month", bulleted inclusions (comprehensive labs, medical supervision, remote monitoring devices, biomarker tracking, medication adjustments, health-coach check-ins, video learning modules), "Sign Up For Revero" CTA.
10. Traditional Care vs Revero comparison — H1 "What if medicine treated the Cause, not the symptoms?" + "Here's how Revero is different.", two-column table (Traditional Care: more symptoms → more prescriptions, long waits, acute-problem focus, manage side effects; Revero: personalized nutritional plan, ongoing care-team and community support, designed for chronic conditions, sustainable habits), CTAs "Get Started" and "Book a Free Call".
11. Featured member testimonials — "Our members say it best" with three long-form quotes from Kevin, Rob, and Kiska, plus "See more success stories" link to /testimonials.
12. Secondary "What Our Members Say" testimonial block — repeats the two short care-team quotes.
13. Footer call band — "Call us at (415) 835-4151 for a free info call", "Call Now: (415) 835-4151" button, regulatory note "*Due to state regulations, patients who have labs drawn in NJ, NY, and RI must self-pay for labs or contact their insurance provider for possible coverage."
14. Footer — About Us, News & press, Healthcare Providers, Contact us now, Terms of Service, Privacy Policy, Privacy Practice, Site map, "Copyright © 2026 Revero Inc".
15. Cookie consent overlay — "Cookie and Tracking Consent" modal with Accept All / Necessary / Show Preferences.
