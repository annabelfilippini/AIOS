# Session Checkpoint - Annabel v3 Draft

## Date

2026-05-12

## Shopify Theme Target

- Store: `cooldown-running.myshopify.com`
- New draft theme: `Annabel v3`
- Theme ID: `180320076050`
- Role: `unpublished`
- Local source folder: `projects/consulting/prospects/cooldown/shopify-theme-annabel-v2`
- Preview URL: `https://cooldown-running.myshopify.com?preview_theme_id=180320076050`
- Theme editor URL: `https://cooldown-running.myshopify.com/admin/themes/180320076050/editor`

## What Happened

- Created a new unpublished Shopify draft named `Annabel v3`.
- Uploaded the full local `shopify-theme-annabel-v2` folder to the new draft.
- Did not publish or modify the live theme.

## Verification

- `shopify theme check --path shopify-theme-annabel-v2 --fail-level crash` exited successfully.
- Confirmed `Annabel v3` appears in `shopify theme list` as unpublished with ID `180320076050`.
- Pulled selected files back from theme `180320076050` into `/private/tmp/cooldown-annabel-v3-verify`.
- Confirmed remote files contain the key current cart/PDP code:
  - `assets/pdp-polish.js` has `selectSingleColorOption`.
  - `snippets/cart-drawer.liquid` has inline cart line quantity controls and `CartDrawer-Checkout`.
  - `assets/component-cart-drawer.css` has the corrected `line-height:1.1`.
  - `sections/main-product.liquid` has the `metafield_accordion` and `Product callout` owner-editing blocks.

## Notes

- This was intentionally a full draft upload, not a narrow patch, because the task was to create a complete previewable v3 theme.
- Remaining full Theme Check output is inherited EComposer/translation/remote-asset debt and should not be treated as new Annabel v3 push fallout unless it touches the changed/QA surface.
