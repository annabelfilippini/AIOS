# Session Checkpoint - Annabel Design, Annabel v2, And Bailey QA

**Date:** 2026-05-06  
**Project:** Cooldown / Shopify draft cleanup  
**Stable approved draft:** `Annabel Design`  
**Stable approved draft ID:** `180287308050`  
**Stable preview:** `https://cooldown-running.myshopify.com?preview_theme_id=180287308050`  
**V2 sandbox draft:** `Annabel v2`  
**V2 theme ID:** `180306575634`  
**V2 preview:** `https://cooldown-running.myshopify.com?preview_theme_id=180306575634`  
**V2 theme editor:** `https://cooldown-running.myshopify.com/admin/themes/180306575634/editor`  
**Stable local path:** `shopify-theme/`  
**V2 local path:** `shopify-theme-annabel-v2/`

## Session Summary

Annabel wanted to keep the current `Annabel Design` draft intact, fix the run club/header/footer issues there, QA against Bailey's notes, draft Bailey email language, then duplicate the stable draft into a separate `Annabel v2` sandbox to test a simpler Bailey editing surface.

## Annabel Design - Stable Draft Work

Pushed to Shopify theme:

```text
Annabel Design (#180287308050)
```

### Run Club Header Link

Updated:

- `shopify-theme/assets/megamenu.css`

What changed:

- Matched the `the run club` right-side header link treatment closer to the original live run-club page.
- Restored the plain white Athletics text link spacing:
  - `margin-right: 40px`
  - `margin-top: 7px`
  - inline-block link behavior
- Removed the newer flex gap spacing for those custom right-side links.

### Footer Links Scroll-To-Top Behavior

Updated:

- `shopify-theme/sections/footer.liquid`

What changed:

- Internal footer links now strip hash fragments in the rendered URL.
- Footer internal links get `data-footer-top-link`.
- Added a small script:
  - same-page footer clicks scroll to top instead of leaving the visitor at the bottom
  - cross-page internal footer clicks set a temporary session flag so the next page scrolls to top on load

### Push / Remote Verification

- Initial Shopify CLI push needed escalation because Shopify CLI writes to its preferences folder.
- Push to `Annabel Design` succeeded.
- Pulled remote files back into `/private/tmp/cooldown-remote-check`.
- Confirmed remote `Annabel Design` has:
  - `margin-right:40px`
  - `gap:0`
  - `data-footer-top-link`
  - `cooldownFooterScrollTop`

Annabel reviewed and said the result looked good. Keep this draft as-is.

## Bailey QA

Annabel asked to run QA against Bailey's notes and confirm whether everything discussed with Bailey was covered.

Created durable QA file:

- `agents/shared/qa/active/2026-05-06-cooldown-bailey-theme-qa.md`

Verdict:

```text
Pass With Follow-Ups
```

Covered Bailey asks:

- Product photos/layout polished around Katherine reference.
- Color/size selection clarified visually.
- Reviews restored with Loox rating and full review section.
- Product templates aligned around Katherine/default PDP structure.
- Announcement/bundle copy/link fixed.
- Header/menu cleanup completed.
- Latest run club/footer behavior completed on `Annabel Design`.

Retrospective QA gap captured on 2026-05-11:

- Visual option clarity was not enough. QA should have tested the actual add-to-cart path on representative PDPs.
- Specific missed scenario: products with only one color value, such as the Boulderthon Molly Short in `skyway`, should not require the customer to manually click the only color swatch before adding the selected size to cart.
- Future PDP QA must confirm selected option labels, actual checked inputs/variant ID, add-to-cart button state, and cart contents agree after app-injected swatches render.
- Add this to reusable Cooldown/Shopify QA: single-value option groups should auto-select or otherwise allow checkout without a redundant manual choice.

Remaining follow-ups:

- Easy Bundle Builder admin/app configuration.
- Product metafield definitions and filled values.
- Men/mens collection content or navigation decision.
- EComposer usage decision.
- SEO meta descriptions.
- Product image alt text.
- Duplicate/test pages and `-copy` product handles.
- Mobile QA across core pages.
- Final app ownership documentation.

## Bailey Email Draft

Annabel provided sponsor-outreach email copy and asked to include the AI workflows plus updated site info.

Drafted a concise email covering:

- Sponsor outreach workflows for college launches.
- No auto-send; drafts/research only.
- Example Ann Arbor sponsor map.
- Shopify draft updates:
  - cleaner product page structure
  - clearer color/size selection
  - reviews showing again
  - updated header/navigation behavior
  - easier Shopify/admin editing direction

Also clarified in conversation:

- The draft is easier for Bailey than before, especially for product edits.
- The theme is still agency/app-heavy overall.
- Best framing: customer-facing issues were cleaned up, but the next layer is simplifying admin/theme controls so Bailey and Anya are less dependent on brittle app/code surfaces.

## Annabel v2 Theme Creation

Annabel asked to duplicate the stable `Annabel Design` draft into a new Shopify theme called `Annabel v2`.

Created with:

```bash
shopify theme duplicate --store=cooldown-running --theme=180287308050 --name 'Annabel v2' --force --json
```

Shopify returned:

```json
{"theme":{"id":180306575634,"name":"Annabel v2","role":"unpublished","shop":"cooldown-running.myshopify.com"}}
```

Pulled v2 locally into:

```text
shopify-theme-annabel-v2/
```

Verification:

- `shopify-theme-annabel-v2/` matched `shopify-theme/` except for local-only `shopify-theme/docs/`.
- Confirmed v2 included stable approved changes:
  - run club link styling
  - footer top-link behavior
  - bundle announcement copy
  - PDP recommendations/reviews order

Created checkpoint:

- `cooldown-meeting-prep/session-checkpoint-2026-05-06-annabel-v2-theme-created.md`

## Annabel v2 - Bailey Editing Surface Experiment

Annabel asked to try making Bailey's editing surface easier in v2.

Important:

- Worked only in `shopify-theme-annabel-v2/`.
- Pushed only to `Annabel v2 (#180306575634)`.
- Did **not** push these experiments to stable `Annabel Design`.

### New Product Metafield Accordion Block

Updated:

- `shopify-theme-annabel-v2/sections/main-product.liquid`

Added block type:

```text
metafield_accordion
```

Theme editor name:

```text
Metafield accordion
```

Purpose:

- Gives Bailey a dropdown-driven product accordion.
- Avoids putting Liquid code inside rich text settings.
- Supports:
  - Materials
  - Care instructions
  - Size guide
  - Fit notes
  - Product highlights
  - Final sale note
- Supports fallback rich text or fallback page.
- Can hide itself when selected metafield and fallback content are empty.

### New Product Callout Block

Updated:

- `shopify-theme-annabel-v2/sections/main-product.liquid`
- `shopify-theme-annabel-v2/assets/section-main-product.css`

Added block type:

```text
product_callout
```

Purpose:

- Gives Bailey a simple theme-editor product note block.
- Supports:
  - heading
  - rich text
  - optional link label
  - optional link
- Intended for temporary launch notes, final-sale notes, product notes, or small promo reminders.

### Product Template Updates

Updated product templates:

- `shopify-theme-annabel-v2/templates/product.json`
- `shopify-theme-annabel-v2/templates/product.alkal-short.json`
- `shopify-theme-annabel-v2/templates/product.cooldown-tee.json`
- `shopify-theme-annabel-v2/templates/product.emmy-short.json`
- `shopify-theme-annabel-v2/templates/product.mikelle-bra.json`
- `shopify-theme-annabel-v2/templates/product.swillz-tank.json`

What changed:

- Replaced Materials, Care Instructions, and Size Guide `collapsible_tab` blocks with `metafield_accordion` blocks.
- Added a disabled `bailey-product-callout` block after product description so Bailey can enable it from the theme editor.

### V2 Push Notes

First push attempts failed because Shopify has 25-character limits on block schema name/type and because Shopify validates templates against the remote schema during the same batch.

Fixes:

- Shortened display name to `Metafield accordion`.
- Shortened internal type from `product_metafield_accordion` to `metafield_accordion`.
- Pushed in two steps:
  1. `sections/main-product.liquid` and `assets/section-main-product.css`
  2. product JSON templates

Final push succeeded.

Remote verification:

- Pulled changed v2 files into `/private/tmp/annabel-v2-verify`.
- Confirmed remote v2 contains:
  - `metafield_accordion`
  - `product_callout`
  - `.product__bailey-callout`

Created checkpoint:

- `cooldown-meeting-prep/session-checkpoint-2026-05-06-annabel-v2-bailey-editing-surface.md`

## Validation

For stable and v2 work:

- JSON parse checks passed for touched product templates and key settings/templates.
- JS syntax checks passed for product/theme helper scripts during QA.
- Full `shopify theme check` still fails due to known generated/EComposer/app issues:
  - EComposer translation keys
  - parser-blocking/generated scripts
  - missing generated snippets such as `ecom-toast`
  - remote generated assets
  - inherited app/theme warnings

These failures are not new from the v2 Bailey-editing-surface pass.

## Current Theme State

### Annabel Design

Use this as the stable draft.

```text
Theme ID: 180287308050
Preview: https://cooldown-running.myshopify.com?preview_theme_id=180287308050
```

Contains:

- approved PDP/header/review/menu/footer work
- run club link styling
- footer top-of-page behavior

### Annabel v2

Use this as the sandbox.

```text
Theme ID: 180306575634
Preview: https://cooldown-running.myshopify.com?preview_theme_id=180306575634
Editor: https://cooldown-running.myshopify.com/admin/themes/180306575634/editor
```

Contains everything from `Annabel Design`, plus:

- product `Metafield accordion` block
- product `Product callout` block
- templates wired to easier metafield accordion blocks

## Next Best Steps

1. Open `Annabel v2` theme editor and inspect a product page:
   - confirm `Metafield accordion` blocks appear clearly
   - confirm disabled `Product callout` can be enabled and edited
2. Browser QA a representative product page on v2:
   - Katherine Bra
   - Mikelle Bra
   - Emmy Short
   - Alkal Short
   - One-color product such as Boulderthon Molly Short, verifying the single color auto-selects and add-to-cart works after choosing size
3. Decide whether the v2 editing model feels meaningfully easier.
4. If yes, next v2 experiments:
   - consolidate product templates toward one standard product template
   - create a Bailey-facing product metafield checklist
   - simplify homepage/run-club editable sections
   - inspect Easy Bundle Builder and EComposer admin usage before trying to simplify those surfaces
5. Do not push v2 experiments to `Annabel Design` unless Annabel explicitly asks.

## Watchouts

- Keep `Annabel Design` stable.
- Use `shopify-theme-annabel-v2/` for v2 experiments.
- Shopify may require section schema pushes before template pushes when introducing new block types.
- Do not treat Theme Check failures as new unless they appear in normal theme files touched by the current task.
- Easy Bundle Builder and EComposer remain admin/app decisions, not solved by the v2 product block experiment.
