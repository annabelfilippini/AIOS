# Vital Health — Carousel Inspo Refs

Five ads Annabel pulled as visual reference for the Vital Health Instagram intro carousel.
Written analysis (not pixel input) — Annabel chose this path over file drop.

The goal is **variety across slide types**, not "borrow one look five times." Each ref
contributes a different *move* the carousel can borrow once.

---

## Ref 1 — Oura Ring (Amazon.in placement)

- **Format**: 9:16 vertical, product-in-hand hero against soft watery blue background.
- **Type**: Sans-serif headline left-aligned, "Starting ₹28,900" as a green-fill pill — tight, retail.
- **Composition**: Big phone screenshot floating in the center with UI dashboard visible. Top-left brand wordmark, top-right partner logo (Amazon).
- **What we borrow**: The "show the actual interface / report / form" move. Vital Health carousels should not be all metaphor + stock — one slide should show a real artifact (intake form, lab snippet, schedule). Anchors credibility.
- **What we skip**: Retailer-banner co-brand row; promo-grade pricing chips.

## Ref 2 — Function Health

- **Format**: 9:16 vertical, candid family-touch photo (child hand on adult arm, warm orange + cream sweaters).
- **Type**: Sans-serif clean small wordmark + dot logo dead center, **two-line stacked serif italic** under a thin white vertical rule: *"Gift the only thing that matters: / more time with the people you love most."*
- **Composition**: Soft full-bleed photo, type centered with vertical micro-rule, single muted-white subline at bottom.
- **What we borrow**: This is the closest visual cousin to Vital Health's existing identity — cream/forest/gold + serif + micro-rule rhythm. We borrow the **emotional human-touch photo** + **center-stacked serif over a thin rule** as the carousel's HERO (slide 1) and CTA (final slide) template. White rule → translate to gold rule for Vital Health.
- **What we skip**: Nothing — this is the spiritual anchor.

## Ref 3 — Bloom Nutrition

- **Format**: 1:1 square feed ad, bright pink ground with green serif italic display "glow-up", customer quote, product render.
- **Type**: Big sans display "30-DAY" + italic script "glow-up" + smaller sans body quote + signature "— Nicolle B."
- **Composition**: Bottom-right product render, top-left lifestyle prop (spoon of powder, glass with strawberry/matcha layers), tight grid feel.
- **What we borrow**: The **quote-with-attribution slide** as a carousel format — a real patient/practitioner sentence in italic serif, signed. Vital Health version: forest green ground, cream serif italic, gold thin signature line.
- **What we skip**: The bright pink consumerist intensity, the "30-DAY" claim format, the product-render-as-hero composition (Vital Health is a service, not a SKU).

## Ref 4 — Solawave LED Mask

- **Format**: 1:1 feed ad, soft pink-glow product hero with press pull-quote and Vogue logo.
- **Type**: Sans wordmark top, large serif-ish quote *"Best LED Face Mask for Glowing Skin"* with **Vogue** wordmark stacked underneath as authority.
- **Composition**: Single object floating against gradient glow background — extreme product worship. Bottom carries URL + CTA.
- **What we borrow**: The **press-quote / credential slide** treatment — pull one credential or quote (e.g. "Board-certified Integrative MD" / "15 years in practice" / a real patient sentence), set it large in serif, attribute under a thin rule. Use as the trust slide.
- **What we skip**: Glowing-object hero (no equivalent product to worship); over-promise claim copy.

## Ref 5 — Plunge (cold plunge)

- **Format**: 1:1 feed ad, lifestyle photo (man in cold tub, laughing) with massive overlay headline.
- **Type**: All-caps condensed sans **"INCREASE YOUR DOPAMINE LEVELS UP TO 250%"** burned into the photo, tiny disclaimer underneath, brand wordmark top.
- **Composition**: Single dramatic full-bleed photo, big stat headline, soft caption strip below.
- **What we borrow**: The **stat-on-photo** move for ONE slide max — a real Vital Health-relevant fact, set in cream/gold serif (not condensed sans) over a botanical / clinical still-life photo. The lesson is "one slide is allowed to be loud."
- **What we skip**: The dopamine-percentage claim format (regulatory risk for a medical practice), the condensed-bro typography, the over-saturated lifestyle photo.

---

## Synthesis — moves the carousel must include

Diversity audit pulled from the 5 refs above:

1. **Hero / cover** → human-touch photo + center-stacked serif over gold micro-rule (Function-style, translated to forest+cream+gold)
2. **Artifact / proof** → real Vital Health UI element (intake form excerpt, scheduling calendar, sample report) (Oura-style)
3. **Patient quote** → italic serif sentence + signature line on cream or forest ground (Bloom-style, restrained)
4. **Credential / trust** → single big serif stat or credential under thin rule (Solawave-style)
5. **One loud slide** → stat or single bold claim on botanical/clinical still-life photo (Plunge-style, dialed way down)
6. **CTA / sign-off** → mirror of slide 1: human moment + serif + gold rule + "Book a consult / Visit us in Austin"

Goal: no two slides share a layout template. That is what kept the paused pilot from feeling alive.

---

## Tokens to confirm or update

Existing tokens (`tokens.json`) already cover this — no override needed:

- primary `#1F4D2A` (forest)
- accent `#C9A04A` (gold) → use as **micro-rule** color throughout
- cream `#F5EFE0` / paper `#FBF7EC` → alternate ground colors
- Fraunces serif for headlines, Inter for body

**New move to add to `moves.md`**:

- "One micro-rule per slide" — gold horizontal or vertical, 1–2px, centered or under signature. Never decorative pattern — always structural.

**New avoid to add to `style.avoid`**:

- "Identical layout repeated across slides" (the paused-pilot failure mode)
- "Condensed-sans stat headlines" (Plunge mistake — not on-brand)
- "Promo pricing chips / retailer co-brand rows" (Oura mistake — not service-appropriate)
