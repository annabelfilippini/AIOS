# Bailey Editing Guide - Annabel v2

Use this for the next round of Cooldown site edits. The goal is to keep routine content changes in Shopify admin instead of editing Liquid, JSON templates, or app-generated code.

## Product Pages

Edit product-specific copy in **Products > product > Metafields**.

Use these product metafields:

- `custom.materials`: Materials accordion.
- `custom.care_instructions`: Care Instructions accordion.
- `custom.size_guide`: Size Guide accordion. This can point to a page.
- `custom.fit_notes`: Optional fit notes accordion.
- `custom.product_highlights`: Optional highlights accordion.
- `custom.final_sale_note`: Optional final sale note accordion.

In **Online Store > Themes > Customize > Products**, the Annabel v2 product template includes:

- `Metafield accordion`: choose which product metafield should show.
- `Product callout`: turn on for temporary launch notes, final-sale notes, or small promos.
- `Return Policy`: shared copy that should usually stay the same across products.

Avoid putting Liquid code like `{{ product.metafields... }}` into rich text fields. Use the metafield dropdown block instead.

## Run Club Pages

For each run club location page, edit the page metafields:

- `custom.cover_image`
- `custom.city`
- `custom.state`
- `custom.time`
- `custom.where`
- `custom.what`
- `custom.leader_1` through `custom.leader_8`

The `Run club location` section now reads those page metafields directly. Keep **Use page metafields** turned on unless you need a one-off manual fallback.

## Run Club Grid

Edit the run club cards in **Online Store > Themes > Customize > Run Clubs page > Run club grid**.

Each card has:

- Card image
- City
- State
- Run club page link

Leave the page link blank for coming-soon clubs. The card will show without sending shoppers to a blank or broken page.

## Homepage

Most homepage content is already in theme-editor sections:

- Hero video URL, headline, and buttons live in `Video Banner`.
- Product collection modules live in featured collection sections.
- Image/text bands live in image or rich text sections.

The homepage still has a few developer-facing custom Liquid slots for embeds. Use those only for app embeds like Typeform.

## App-Owned Areas

These are not fully controlled by the theme:

- Easy Bundle Builder: bundle page products, bundle rules, discounts, and bundle app layout.
- Loox: review widgets and review content.
- EComposer: generated page/quickview/search sections.
- Popups, preorder, swatches, and upsell app embeds.

For these, edit the app admin first. Theme code should only be touched if the app placement or surrounding layout breaks.
