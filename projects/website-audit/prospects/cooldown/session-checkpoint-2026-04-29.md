# Cooldown Redesign Session Checkpoint - 2026-04-29

## Context

Annabel is helping Bailey redo the Cooldown Running Shopify site. Bailey's core complaints from the meeting:

- Product page photos are too small.
- Color/size selection is confusing.
- Customers think items are sold out when they are not.
- Current agency-built theme/code makes simple edits hard.
- Bailey is interested in a fresh Shopify template or simpler Shopify setup.
- Announcement bar promo still points to the wrong page.

Current draft theme in Shopify:

- Theme name: `Annabel Design`
- Theme base: Dawn 7.0.1, with existing custom CSS and Globo swatch code.
- Work is being done in the Shopify theme customizer/code editor, not through a downloaded theme file.

## Files Created Locally

- `prospects/cooldown/redesign-brief.md`
- `prospects/cooldown/shopify-context-checklist.md`
- `prospects/cooldown/product-page-redesign-plan.md`
- `prospects/cooldown/session-checkpoint-2026-04-29.md`

## Current Findings

### Product Page

The product page is mostly native Dawn plus existing custom CSS and Globo Swatch behavior.

Important files/settings seen in Shopify:

- `assets/section-main-product.css`
- Product template: `Default product`
- Product information section:
  - Desktop media position: left
  - Desktop layout: thumbnail carousel
  - Desktop media size: medium during screenshots
  - Mobile layout: hide thumbnails
  - Sticky desktop content was visible as a setting

Product page blocks visible:

- Title
- Price
- Variant picker
- Quantity selector hidden
- Buy buttons
- Text - Why we made this hidden
- Description
- Collapsible rows: Materials, Care Instructions, Return Policy, Size Guide
- Share hidden
- Star Rating Widget

### Variant Problem

Katherine Bra product options are currently ordered:

1. Size
2. Color

This likely causes Bailey's customer confusion. Customers pick a size first, then many colors appear crossed out or unavailable. For apparel, the better shopping flow is:

1. Color
2. Size

Observed behavior:

- When selecting size `S`, most colors are available.
- When selecting `maroon` + `XL`, page correctly shows sold out.
- Some sizes/colors are genuinely sold out, but the current option order makes the whole product feel unavailable.
- Katherine Bra showed `XS` inventory at `-11`, which should be flagged to Bailey.

Recommended product-data fix:

1. Change product option order from `Size, Color` to `Color, Size` on Katherine Bra first.
2. Test the PDP.
3. If successful, repeat for the main products with color + size variants.
4. Review negative inventory and decide whether overselling is intentional.

This cannot be fully solved with CSS because option order and inventory are product data.

### Globo Swatch

Existing CSS confirms Globo Swatch is involved:

- `.globo-swatch-product-detail`
- `.globo-out-of-stock.globo-sold-out-cross-out`
- `.globo-style--button`

Need to inspect Globo settings for:

- auto-select first available variant
- hide sold-out variants
- cross out sold-out variants
- show unavailable combinations
- sold-out style

Ideal direction:

- Auto-select first available variant if possible.
- Do not hide unavailable variants entirely.
- Keep cross-outs on unavailable sizes after color is selected.
- Avoid making all colors look unavailable.

## CSS Work Done / In Progress

Annabel pasted a bottom CSS block into `assets/section-main-product.css`.

Purpose:

- Create a stronger two-column PDP.
- Make product image larger.
- Make product info column tighter.
- Make add-to-cart full-width/purple.
- Improve swatch spacing.
- Improve image crop.

Current intended bottom block:

```css
/* Annabel PDP redesign pass - Cooldown */
@media screen and (min-width: 990px) {
  main section .product.grid {
    display: grid !important;
    grid-template-columns: minmax(0, 1.35fr) minmax(36rem, 0.85fr);
    column-gap: 5rem !important;
    row-gap: 0 !important;
    align-items: start;
  }

  .product--large:not(.product--no-media) .product__media-wrapper,
  .product__media-wrapper {
    width: 100% !important;
    max-width: 100% !important;
  }

  .product--large:not(.product--no-media) .product__info-wrapper,
  .product__info-wrapper {
    width: 100% !important;
    max-width: 100% !important;
    padding: 2rem 0 0 0 !important;
  }

  .product__info-container {
    position: sticky;
    top: 9rem;
    max-width: 52rem;
  }
}

.product-form__buttons {
  max-width: 100% !important;
}

.product-form__buttons .button,
.product-form__submit {
  width: 100% !important;
  min-height: 5.6rem;
  border-radius: 999px !important;
  background: #b292e7 !important;
  color: #ffffff !important;
  border: 0 !important;
  font-weight: 700;
  text-transform: lowercase;
  letter-spacing: 0;
  padding: 1.5rem 2.5rem !important;
  margin: 2rem 0 1rem !important;
}

.product-form__buttons .button:hover,
.product-form__submit:hover {
  background: #9f82dc !important;
}

.product-form__submit:before,
.product-form__submit:after,
.product-form__buttons .button:before,
.product-form__buttons .button:after {
  box-shadow: none !important;
  border-radius: 999px !important;
}

.product__info-container .product-form {
  margin-top: 1rem;
  margin-bottom: 1.5rem;
}

body .swatch--gl .name-option {
  font-size: 1.6rem;
  margin-top: 1.8rem;
  margin-bottom: 1.2rem;
}

body .globo-swatch-product-detail .swatch--gl li .globo-style--button {
  min-width: 4.6rem;
  min-height: 4.6rem;
}

body .globo-swatch-product-detail ul.value.g-variant-color-detail.active {
  display: flex;
  gap: 1rem;
  align-items: center;
}

body .globo-swatch-product-detail ul.value li.select-option input:checked + .globo-style--button,
body .globo-product-groups-detail .gsw-item-product-group a.is-gsw-active .globo-style--button,
body .globo-swatch-product-detail .swatch--gl li .globo-style--button:hover,
body .globo-swatch-product-detail .swatch--gl li:first-of-type .globo-style--button.default {
  background: #191919 !important;
  color: #ffffff !important;
}

@media screen and (max-width: 989px) {
  main section .product.grid {
    display: block !important;
  }

  .product__media-wrapper,
  .product__info-wrapper {
    width: 100% !important;
    max-width: 100% !important;
  }
}

@media screen and (max-width: 749px) {
  .product-form__buttons .button,
  .product-form__submit {
    min-height: 5.2rem;
    font-size: 1.8rem;
    background: #b292e7 !important;
  }
}

@media screen and (min-width: 990px) {
  .global-media-settings.product__media {
    padding-top: 100% !important;
  }

  .global-media-settings.product__media img {
    height: 100% !important;
    object-fit: cover;
    object-position: center top;
  }
}
```

Important: in one pasted version, the `.globo-style--button` selector was accidentally line-broken as `.globo- style--button`. That must be corrected if still present.

## Announcement Bar

Live site check on 2026-04-29 showed the announcement still linked to:

- `/pages/run-clubs`

In the draft theme, Annabel confirmed the announcement block still showed `Run Clubs`.

Correct destination appears to be the `Bundle and Save` page/template:

- Template/page name: `bundle-and-save`
- Page shows bundle builder UI.

Issue to flag:

- Announcement says: `buy 4+ items • get 20% off`
- Bundle page says: `Add 3 product(s) to get 10% discount!`

The link should point to Bundle and Save, but the discount mismatch needs Bailey's clarification.

## Estimated Scope

Recommended tight Phase 1:

- 10-15 hours
- Fix announcement bar.
- Fix Katherine Bra product flow.
- Apply product page pattern to top 5-8 products.
- Clean homepage hero/CTA flow.
- QA mobile.

Full current-theme redo:

- 20-35 hours.

Fresh Shopify template/theme migration:

- 40-70 hours.

## Next Steps

1. Fix announcement bar link in draft:
   - Click nested announcement block.
   - Change link from `Run Clubs` to `Bundle and Save`.
   - Save.
2. Ask Bailey whether promo should be:
   - 4+ items / 20% off, or
   - 3 products / 10% off.
3. On Katherine Bra:
   - Reorder product options from `Size, Color` to `Color, Size`.
   - Save.
   - Preview page.
4. If Katherine Bra improves, audit other key products for same issue:
   - Molly Short
   - Nicole Bra
   - Meg Tank
   - Any bestseller Bailey prioritizes
5. Inspect Globo Swatch settings for unavailable variant behavior.
6. Continue CSS polish only after variant flow is fixed.

## Important Boundary

Codex cannot directly control Annabel's browser or log into Shopify with Bailey's credentials. Best workflow is:

- Annabel stays logged in.
- Codex provides exact click/code steps.
- Annabel sends screenshots.
- Codex adjusts code/instructions.

