# Cooldown Product Page Redesign Plan

## What Bailey Liked From The Audit Concept

The audit product-page concept made the Katherine Bra feel more complete and easier to shop. The useful parts to carry into Shopify are:

- Large product photography, roughly half the page width.
- Sticky, focused product info on the right.
- Clear color swatches with an obvious selected state.
- Size buttons that feel like choices, not tiny form controls.
- A full-width, high-contrast add-to-cart button.
- Product confidence content near the buying controls:
  - rating/reviews
  - bundle promo
  - shipping/returns/payment notes
  - final sale note if relevant
- Rich below-the-fold content:
  - "why we made this"
  - features/fabric
  - pairs well with / complete the kit
  - size guide
  - reviews

## Current Draft Product Page Diagnosis

From the Shopify customizer screenshot:

- Product media is better than the live site, but still not strong enough for the goal.
- The current layout is visually imbalanced: the image is large, but the product info column is very wide and sparse.
- The add-to-cart button sits in a huge empty buy-buttons block, making the page feel unfinished.
- Color swatches are too small and do not show the selected color name clearly enough.
- Size is selected before color visually, which may contribute to customer confusion when combinations are unavailable.
- There is no helper text explaining the color/size sequence.
- The product copy starts immediately under the buy controls, but the buying area lacks trust signals and promo context.

## Customizer Findings From Annabel's Draft

- Theme: duplicated Dawn draft named `Annabel Design`.
- Product template: `Default product`.
- Product information settings:
  - Sticky desktop content is currently off.
  - Desktop media position is left.
  - Desktop layout is `Thumbnail carousel`.
  - Desktop media size is currently `Medium`.
  - Mobile layout hides thumbnails.
  - Section padding is 0 top / 0 bottom.
- Product blocks visible:
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
- Variant picker:
  - Type is `Pills`.
  - Color swatches are present, likely controlled by the current theme/custom swatch setup.
- Buy buttons:
  - Dynamic checkout buttons are off.
  - Add-to-cart button is small and outline-style.

## First Shopify Settings Pass

Do these before editing theme code:

1. In `Product information`, enable sticky content on desktop.
2. Change `Desktop media size` from `Medium` to `Large`.
3. Keep `Desktop layout` as `Thumbnail carousel` for now.
4. Keep `Mobile layout` as `Hide thumbnails`.
5. Drag `Star Rating Widget` directly under `Price`.
6. Add a text block directly under `Variant picker`:
   - `choose a color first, then select your size. unavailable sizes update by color.`
7. Keep `Quantity selector` hidden.
8. Keep dynamic checkout buttons off until the base add-to-cart UI is fixed.
9. Move long product content below the buy controls:
   - Description
   - Materials
   - Care Instructions
   - Return Policy
   - Size Guide

## Target Layout

### Desktop

- Two-column layout.
- Left column: 55-60% width product gallery.
- Right column: 40-45% width product info.
- Product info should stay visually compact, with less dead space around the buy button.
- Product gallery should support large inspection of fit/color.

### Mobile

- Product gallery first.
- Product title/price/variants/add-to-cart immediately after.
- Add-to-cart should stay easy to reach.
- Variant labels must remain visible, not only swatches.

## Product Info Order

Use this order in the Shopify product template:

1. Title
2. Price
3. Reviews/rating block, if Loox can be displayed
4. Color picker
   - Label should show selected color, e.g. `Color: Sky`
5. Size picker
   - Label should show selected size, e.g. `Size: XS`
6. Helper text
   - `choose a color first, then select your size. unavailable sizes will update by color.`
7. Add to cart
8. Bundle promo
   - `buy 4+ items, get 20% off`
   - Link to bundle page
9. Shipping/returns note
10. Product description/accordions

## Shopify Customizer Changes To Try First

Before editing code, check whether Dawn settings can do this:

- Product information section:
  - Set media size to large.
  - Set desktop media layout to stacked or thumbnails, whichever gives the largest first image.
  - Enable sticky product information if available.
  - Move buy buttons directly under variant pickers.
  - Remove unnecessary empty spacing blocks.
- Variant picker:
  - Use buttons/pills for size.
  - Use swatches for color.
  - Confirm selected option names are visible.
- Product description:
  - Move long description below the main product area if the top becomes too text-heavy.

## Code Changes Likely Needed

If customizer settings are not enough, edit the draft theme only.

Likely files:

- `sections/main-product.liquid`
- `snippets/product-variant-picker.liquid`
- `snippets/product-media-gallery.liquid`
- `assets/section-main-product.css`
- `assets/component-product-variant-picker.css`

Possible CSS goals:

- Increase desktop media column width.
- Reduce empty padding in buy-buttons area.
- Make add-to-cart full width.
- Increase color swatch size.
- Improve selected swatch outline.
- Add spacing between variant groups.
- Make product info sticky on desktop.

## Variant UX Rules

- Color should be a real named choice, not only a dot.
- Selected color name must be visible.
- Disabled sizes should be clearly disabled, but not make the whole product feel sold out.
- If a selected color/size combo is unavailable, the page should explain that combination is unavailable.
- Avoid hiding unavailable variants entirely; hidden options make customers think the site is broken.

## Bailey Variant Complaint Diagnosis

The current Katherine Bra page loads with `Size` above `Color`. That likely means the Shopify product option order is:

1. Size
2. Color

For apparel with many colorways, this is the wrong shopping sequence. It encourages the shopper to pick a size first, then makes many colors appear sold out or crossed out based on that size. Bailey's complaint that customers think items are sold out likely comes from this exact interaction.

Recommended default option order:

1. Color
2. Size

The product page should first let the customer choose the color they visually want, then show which sizes are available for that selected color.

Second likely issue: the product may be loading the first variant by default, and that first variant may be sold out. If the first variant is unavailable, the page opens with `Sold out` beside the price and a disabled/sold-out add-to-cart state, making the whole product look unavailable.

Checks needed in Shopify admin:

- Open Katherine Bra in Products.
- Check whether option order is `Size` then `Color`.
- Check whether the first variant in the variants table is sold out.
- Check whether Globo Swatch has a setting for:
  - auto-select first available variant
  - hide sold-out variants
  - cross out sold-out variants
  - show unavailable combinations
  - unavailable style

Best fix:

1. Reorder product options to `Color` first and `Size` second.
2. Ensure the default selected variant is available, or configure the product page/app to avoid loading a sold-out variant by default.
3. Use visual styling to soften unavailable combinations so the whole product does not feel sold out.

## Announcement Bar Note

The screenshot shows the Announcement bar section settings, not the individual announcement block settings. To edit the promo link:

1. In the left sidebar, click the nested `Announcement - buy 4+ items...` block.
2. Look for the link field inside that block.
3. Change the link to the correct bundle page.
4. Save in the draft theme first unless Bailey approved a live change.

## Next Screenshots Needed

To decide whether this can be solved in settings or needs code, capture:

- Product page left sidebar with all sections/blocks visible.
- Product information section expanded.
- Variant picker block expanded.
- Buy buttons block expanded.
- Product media/gallery settings.
- Mobile product page preview.
- Product admin variants table for Katherine Bra.
