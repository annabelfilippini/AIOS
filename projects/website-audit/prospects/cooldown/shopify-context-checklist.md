# Cooldown Shopify Context Checklist

Use this when Annabel is inside Shopify and Codex cannot directly log in.

## Helpful Screenshots

### Theme / Setup
- Theme name and version.
- Draft theme name.
- Theme actions menu showing available options.
- Shopify apps list filtered for product, swatch, reviews, bundle, popup, and page builder apps.

### Announcement Bar
- Announcement bar settings panel.
- Current announcement text.
- Current announcement link.
- Available link picker result for the intended bundle page.

### Product Page
Open a product that causes variant confusion, ideally Katherine Bra or Molly Short.

Capture:
- Product page on desktop preview.
- Product page on mobile preview.
- Left sidebar section list for the product template.
- Expanded product information section settings.
- Variant picker settings.
- Media/gallery settings.
- Buy buttons settings.
- Any custom liquid blocks in the product template.
- Product admin variants table for the same product.
- Product admin media section.

### Collection Page
- Women's collection page desktop preview.
- Collection template section list.
- Product card settings.
- Filtering/sorting settings.

### Navigation
- Header settings panel.
- Main menu links.
- Announcement, shop, run club, and bundle-related links.

## Useful Code Snippets

Only if needed, use `...` > `Edit code`, then copy/paste these files or screenshots of their top-level structure:

- `sections/announcement-bar.liquid`
- `sections/header.liquid`
- `sections/main-product.liquid`
- `snippets/product-variant-picker.liquid`
- `snippets/product-media-gallery.liquid`
- `snippets/card-product.liquid`
- `templates/product.json`
- `templates/index.json`
- `config/settings_data.json` if Shopify allows viewing it

Do not paste secrets or customer data.

## First Diagnosis Questions

- Is the draft theme still Dawn 7.0.1?
- Is the product page using Shopify's native variant picker or an app-controlled swatch picker?
- Which app controls color swatches, if any?
- Does the product have separate variants for every color/size combination?
- Are unavailable variants hidden, crossed out, greyed out, or shown as sold out?
- Does the issue happen more on mobile or desktop?
- Does Loox have reviews available but not displayed, or are there no reviews yet?

## First Fix Sequence

1. Fix announcement bar link.
2. Diagnose whether variant confusion is theme-level or app-level.
3. Increase product media prominence on one draft product template.
4. Improve variant picker labels and selected state.
5. Test mobile add-to-cart flow.
6. Only after product page clarity is improved, move to homepage redesign.
