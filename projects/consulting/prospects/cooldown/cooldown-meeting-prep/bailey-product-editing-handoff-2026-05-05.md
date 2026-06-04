# Bailey Product Editing Handoff

**Date:** 2026-05-05  
**Reference product:** Katherine Bra  
**Theme path:** `shopify-theme/`

## What Changed

The Katherine Bra product page is now the standard product-page structure for the draft theme. The existing one-off product templates were aligned to the same structure:

- `product.mikelle-bra.json`
- `product.swillz-tank.json`
- `product.emmy-short.json`
- `product.alkal-short.json`
- `product.cooldown-tee.json`

This means those products should use the same product-page layout, review placement, media layout, option area, accordions, and related-products pattern as Katherine.

## Where Bailey Should Edit Products

Use Shopify product admin for product-specific content:

- product title
- price
- variants
- product images and alt text
- product description
- product status and inventory

Use product metafields for repeatable PDP details:

- `custom.materials`
- `custom.care_instructions`
- `custom.size_guide`

Those metafields feed the product accordions, so Bailey can update Materials, Care Instructions, and Size Guide without editing the theme template.

## What The Theme Controls

The product template controls the shared PDP structure:

- image gallery position and thumbnail behavior
- product title, price, reviews, variants, add-to-cart, and description order
- accordions for Materials, Care Instructions, Return Policy, and Size Guide
- related products section

If Bailey wants the same layout for a new product, assign it to the default product template or one of the existing product templates now aligned to the Katherine structure.

## App Ownership

Reviews should use the Loox blocks in the product template:

- rating near the price
- review section lower on the page

Swatches and notify-me behavior still come from the installed apps and are styled by the theme. If those apps change their generated markup, the theme polish may need another pass.

Bundles/promos should stay in the bundle app or Shopify admin unless the product page needs a visible reusable message block later.

## What Bailey Should Avoid

Bailey should not need to edit:

- Liquid files
- CSS files
- JavaScript files
- custom Liquid blocks
- app-generated HTML

If a product page needs a new reusable content area, create it as a theme block or product metafield instead of hardcoding it into one product template.

## New Product Checklist

1. Add the product in Shopify admin.
2. Add product images with useful alt text.
3. Add variants and inventory.
4. Write a clean product description without emoji-heavy formatting.
5. Fill in Materials, Care Instructions, and Size Guide metafields.
6. Assign the standard product template.
7. Confirm color/size options, reviews, add-to-cart, sold-out, and notify-me states.
8. Preview on desktop and mobile before publishing.

