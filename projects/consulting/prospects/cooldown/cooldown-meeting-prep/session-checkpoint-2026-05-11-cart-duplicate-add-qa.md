# Session Checkpoint - Cart Duplicate Add QA

**Date:** 2026-05-11  
**Project:** Cooldown / Shopify cart QA  
**Draft theme:** `Annabel Design` `#180287308050`  
**Live theme:** `Annabel v2` `#180306575634`  
**Stable local path:** `shopify-theme/`  
**Live local path:** `shopify-theme-annabel-v2/`

## Issue

Annabel reported that adding one item to cart was automatically adding two.

Live QA reproduced the issue on `Boulderthon Molly Short` (`/products/molly-short-copy`):

- One click on `S / skyway` sent the theme add request to `/cart/add`.
- The app layer immediately sent a second request to `/cart/add.js` for the same variant.
- Cart quantity became `2` and subtotal became `$136.00` instead of one `$68.00` line.

## Fix

Updated both theme copies:

- `shopify-theme/assets/product-form.js`
- `shopify-theme-annabel-v2/assets/product-form.js`

Added `window.CooldownCartAddGuard`, which records the theme add-to-cart request fingerprint and suppresses only an immediate duplicate app `/cart/add.js` request for the same variant/options inside a short window.

This keeps the theme cart drawer as the source of truth while preventing the app's duplicate add from increasing quantity.

## Pushes

Pushed only `assets/product-form.js`:

- `Annabel Design` `#180287308050`
- `Annabel v2` `#180306575634` with `--allow-live`

Pulled the remote asset back from both themes and confirmed Shopify contains:

- `CooldownCartAddGuard`
- `isDuplicateAppAdd`
- `record(formData)`

## Verification

- `node --check` passed for both `product-form.js` files.
- `shopify theme check --fail-level crash` exited successfully for both theme folders, with the known inherited EComposer/translation noise still present.
- Live storefront QA after push:
  - Added `Boulderthon Molly Short` `S / skyway`.
  - Cart stayed at quantity `1`.
  - Drawer subtotal was `$68.00`, not `$136.00`.
  - Added `M / skyway` afterward.
  - Cart showed two separate lines, `M / Skyway` quantity `1` and `S / Skyway` quantity `1`.
  - Test cart was cleared after QA.

## Next QA Note

For cart regressions involving apps, instrument network requests and compare `/cart/add`, `/cart/add.js`, and `/cart.js` alongside the visible drawer. Visual cart QA alone can miss duplicate add sources.
