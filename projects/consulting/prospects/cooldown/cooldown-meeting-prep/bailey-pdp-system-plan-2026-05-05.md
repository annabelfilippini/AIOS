# Bailey PDP System Plan

**Date:** 2026-05-05  
**Project:** Cool Down Shopify draft theme  
**Reference product:** Katherine Bra  
**Draft theme:** `#180297498898`  
**Theme path:** `shopify-theme/`

## Core Decision

Use the Katherine Bra PDP as the reference pattern for the rest of the product catalog, but do not leave that pattern as a one-off polish patch. The goal is to turn the Katherine page into an editable product-page system Bailey can use when she changes products, launches new products, updates callouts, changes imagery, or cleans up descriptions.

The client-facing recommendation is only useful if Bailey/Katherine need to understand why this is worth doing. Its point is not to sound formal. Its point is to explain that the issue is not just visual design: the current theme depends on scattered app output, product-description formatting, and CSS/JS overrides. A reusable PDP system saves Bailey from needing a developer every time she changes a product page.

## What Katherine Bra Should Define

Katherine Bra should become the product-page standard for:

- desktop image proportions and thumbnail placement
- product title, price, review, variant, and add-to-cart order
- selected option labels, such as `Color - lavender horizon` and `Size - S`
- clearer swatches and size pills
- visible sold-out and notify-me states
- calmer product description formatting
- product accordion order: materials, care, returns, size guide
- related products section behavior

This does not mean every product needs identical content. It means every product should use the same editable structure.

## Bailey-Friendly Editing Model

Bailey should be able to manage product pages mostly through Shopify admin and theme editor fields:

- Product admin:
  - title
  - price
  - variants
  - product media
  - product description
  - product metafields for materials, care instructions, size guide, and product-specific notes

- Theme editor:
  - global PDP layout
  - promo/final-sale callouts
  - accordion order and default copy
  - whether to show reviews near the price
  - related products display
  - reusable trust/returns messaging

- Apps/admin:
  - reviews source and placement
  - notify-me behavior
  - bundles/promos

Bailey should not need to edit theme code, custom Liquid, app-generated HTML, or hidden CSS selectors.

## Implementation Plan

### 1. Freeze Katherine as the visual reference

- Keep the current Katherine Bra PDP as the reference state.
- Take screenshots of the reference page for desktop and mobile.
- Use those screenshots as QA comparison when testing other products.
- Avoid further Katherine-specific tweaks unless they reveal a reusable system need.

### 2. Audit the current PDP dependencies

Map which parts of the current Katherine page are controlled by:

- `sections/main-product.liquid`
- `templates/product.json`
- product metafields
- product descriptions
- Globo swatches
- Growave notify-me markup
- Loox reviews
- `assets/pdp-polish.js`
- `assets/section-main-product.css`

The key question for each part: can Bailey edit this safely herself?

### 3. Convert one-off polish into theme-level controls

Add product section settings or blocks for the pieces Bailey may need to change:

- optional product notice/callout block
- optional final sale message block
- optional short product highlight block
- editable return/shipping reassurance copy
- review placement toggle if needed
- description cleanup rules only if they are safe globally

Keep global styling in CSS. Keep product-specific content in product fields/metafields. Avoid hardcoding Katherine-specific copy into the section.

### 4. Standardize metafields

Confirm or create a simple product metafield map:

- `custom.materials`
- `custom.care_instructions`
- `custom.size_guide`
- optional `custom.fit_notes`
- optional `custom.product_highlights`
- optional `custom.final_sale_note`

Use these fields in the product template so new products can inherit the Katherine-style layout without new code.

### 5. Create a reusable product template

Use the default product template as the main Cool Down PDP template if this design should apply catalog-wide.

If some products need different layouts, create clearly named templates instead:

- `product.cooldown-standard.json`
- `product.bundle.json`
- `product.archive-sale.json`

Avoid many tiny one-off templates.

### 6. Test against a small product set

Pick 3-5 representative products:

- Katherine Bra as the reference
- one product with many color variants
- one product with sold-out variants
- one product with sparse content
- one product that participates in a bundle or promo

For each product, check:

- media layout
- color and size controls
- selected option labels
- add-to-cart or notify-me state
- reviews placement
- description formatting
- accordions
- mobile layout

### 7. Reduce app overlap and fragile patches

Decide which app owns each concern:

- reviews: preferably one source/placement
- swatches: Globo or native theme controls, not both fighting
- notify me: Growave or theme/app block, with consistent styling
- bundles: Easy Bundle Builder/admin configuration unless theme code must display a message

Keep `pdp-polish.js` only for unavoidable third-party cleanup. Any behavior that can be moved into Liquid, metafields, theme settings, or app configuration should move there.

### 8. Fix the known console error

Investigate the pre-existing `product-form.js` error:

`Cannot read properties of null (reading 'setAttribute')`

This matters because Bailey-friendly product pages still need reliable variant and add-to-cart behavior. The error did not block visible Katherine testing, but it should be resolved before calling the PDP system production-clean.

### 9. Write Bailey handoff

Create a short handoff that explains:

- which product fields Bailey edits
- which theme editor controls affect all PDPs
- which app/admin areas control reviews, notify-me, and bundles
- how to add a new product using the Katherine structure
- what not to touch without help

This should be practical, not polished for show.

## Proposed Next Work Session

1. Capture Katherine reference screenshots.
2. Inspect 3-5 other product pages against the Katherine standard.
3. Identify which differences come from missing content versus theme limitations.
4. Add the smallest set of theme controls/metafields needed.
5. Test changes on Katherine plus the selected product set.
6. Draft Bailey's product editing handoff.

## Success Criteria

- New products can use the Katherine-style PDP without custom code.
- Bailey can update product content without touching Liquid, CSS, or JavaScript.
- Product-specific information lives in product fields or metafields.
- Global PDP design choices live in the theme editor.
- Third-party apps have clear ownership and do not create confusing duplicate UI.
- The PDP is consistent across representative products on desktop and mobile.

