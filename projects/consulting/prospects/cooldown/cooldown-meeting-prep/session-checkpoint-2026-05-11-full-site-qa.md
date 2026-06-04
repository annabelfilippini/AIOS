# Session Checkpoint - Full Site QA

**Date:** 2026-05-11  
**Project:** Cooldown / Shopify full-site QA  
**Draft theme:** `Annabel Design` `#180287308050`  
**Live theme:** `Annabel v2` `#180306575634`

## QA Scope

Ran storefront QA on the current live site, with spot checks against the draft where code was pushed:

- Home
- All, women's, men's, and accessory collection paths
- Run clubs index and city pages
- About, returns, bundle, and start-a-cooldown pages
- Desktop and mobile core pages
- PDP add-to-cart path for `Katherine Bra`
- Previously verified one-color/cart paths for `Boulderthon Molly Short`

## Findings Fixed

### Duplicate Add-To-Cart Root Cause

The earlier cart guard stopped duplicate quantities, but full QA found the deeper cause in `layout/theme.liquid`:

- `product-form.js` handled the product form and posted to `/cart/add`.
- A body-level layout submit handler also posted the same form to `/cart/add.js`.
- This caused the duplicate add behavior and later a console error after the guard blocked the duplicate app-style request.

Fix:

- Added `if (event.defaultPrevented) return;` to the body-level submit handler in both theme copies.
- Re-tested `Katherine Bra` `lavender horizon / S`; only one `/cart/add` fired, cart quantity was `1`, drawer subtotal was `$59.00`, and there was no add-to-cart failure console error.

### Raw Final Sale CSS In Collection Text

Collection cards and PDP thumbnails used an inline `<style>` next to the `Final Sale` badge and wrapped the badge text in an `<h1>`.

Impact:

- Some collection pages exposed raw `.sale-badge { ... }` CSS in page text.
- The badge could be interpreted as the page heading.

Fix:

- Replaced badge `<h1>` with `<span>`.
- Moved badge CSS into theme CSS files.
- Re-tested women's and men's collection paths with cache-busted URLs; raw CSS no longer appears and the badge is no longer an `h1`.

## Files Pushed

Pushed narrow updates to both `Annabel Design` and live `Annabel v2`:

- `layout/theme.liquid`
- `snippets/card-product-collections.liquid`
- `snippets/product-thumbnail.liquid`
- `assets/component-card-collections.css`
- `assets/section-main-product.css`

Remote pulls confirmed the changed files are present on both themes.

## Passed QA Notes

- Desktop sampled pages returned 200s with no 404 body state.
- Mobile sampled pages had no horizontal overflow and no broken images in the checked set.
- Run club index and representative city pages loaded with expected content.
- Empty cart page renders normally.
- `Katherine Bra` add-to-cart works with selected color/size and no duplicate add.
- `Boulderthon Molly Short` was previously verified after the cart fix for one-color auto-selection and separate S/M variant lines.

## Remaining Non-Blocking Notes

- Bundle page loads, but the app still exposes only a small first-step product set (`Mikelle Bra`, `Swillz Tank`) before advancing. This remains an Easy Bundle Builder admin/app configuration area.
- Console still shows a Timesact config 404 on products (`/apps/timesact/config?...`). This appears tied to the preorder/notify app integration, not the cart fix.
- Shopify Theme Check still exits successfully at `--fail-level crash`, with known inherited EComposer/translation warnings/errors.
