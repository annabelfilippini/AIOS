# Session Checkpoint — Cool Down Shopify Redesign

**Date:** 2026-05-02, 4:25 PM EDT  
**Project:** Cool Down / Shopify draft redesign  
**Draft theme:** Annabel Design, `#180287308050`  
**Local theme path:** `shopify-theme/`  
**Local preview:** `http://127.0.0.1:9292/`

## What happened

- Shopify CLI was installed and verified at version `3.94.3`.
- The `Annabel Design` draft theme was pulled locally into `shopify-theme/`.
- Shopify local preview server was started successfully.
- Bailey/Annabel Granola notes were saved into `cooldown-meeting-prep/bailey-session-notes-2026-05-02.md`.

## Site changes made

- Updated the global announcement bar copy from `buy 4+ items • get 20% off` to `buy 3 items • get 20% off`.
- Confirmed the announcement bar links to `shopify://pages/bundle-and-save`.
- Updated homepage promo copy from `save 20% when you buy 4+ items` to `save 20% when you build a 3-item bundle`.
- Updated homepage promo buttons to point to `shopify://pages/bundle-and-save`.
- Added `assets/bundle-page-copy-fix.js` to patch stale Easy Bundle Builder app copy on the bundle page.
- Updated `layout/theme.liquid` so the bundle copy patch loads only on `/pages/bundle-and-save`.
- Verified the rendered bundle page now shows `Add 3 product(s) to get 20% discount!` and no longer shows `10% discount`.

## Important caveat

The bundle-page discount sentence is injected by the Easy Bundle Builder app, not by normal Shopify theme JSON/Liquid. The theme-side patch fixes the customer-facing copy, but the clean permanent fix is to update the source configuration inside the Easy Bundle Builder app admin so its own rule/text is set to 20%.

## Bailey's key website complaints

- Product page photos feel too small.
- Color/size selection is confusing; customers think products are sold out.
- The current agency-built Shopify code is too complex for simple edits.
- Bailey wants a fresher Shopify template approach and more control.
- The bundle app is hard for Bailey to change herself.

## Come back to this

Explore whether Annabel should build Bailey a simpler custom theme/control layer with only the sections and settings Cool Down actually needs:

- Homepage hero and announcement bar controls.
- Simple bundle promo section.
- Product page with larger media and clearer variant picker.
- Run club/city page templates.
- Launch-friendly sections for college campuses, expos, apparel drops, and sponsor activations.
- Cleaner theme settings so Bailey/Anya can change common copy, images, and promos without digging through brittle app or agency code.

## Next likely work session

1. Inspect product template files: `sections/main-product.liquid`, `assets/section-main-product.css`, product-related snippets/assets.
2. Improve product page image sizing.
3. Make variant selection clearer, especially color/size and unavailable/sold-out states.
4. Decide whether bundle app should stay, be reconfigured in admin, or be replaced by a simpler custom bundle experience.
5. Document a “Bailey-editable theme” recommendation for the case study and next proposal.
