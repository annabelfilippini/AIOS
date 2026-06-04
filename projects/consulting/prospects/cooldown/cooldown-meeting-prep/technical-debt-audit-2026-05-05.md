# Cool Down Technical Debt Audit

**Date:** 2026-05-05  
**Theme path:** `shopify-theme/`  
**Draft theme:** `#180297498898`  
**Preview:** `http://127.0.0.1:9296/`  
**Audit command:** `shopify theme check --path shopify-theme`

## Executive Summary

The site does not need a brand-new custom theme before handoff, but the current draft theme should be cleaned in controlled passes. The theme is a hybrid of Dawn-style theme files, EComposer-generated files, app-generated snippets, and custom Cool Down sections. That mix is the source of most of the technical debt.

Theme Check inspected 229 files and reported 136 total offenses across 40 files, including 50 errors. The number sounds worse than the practical risk because many errors are concentrated in generated EComposer quickview/layout files. Still, several normal theme files have issues that should be cleaned before handing the theme back to Bailey.

The recommended approach is not to chase every warning equally. Fix the normal theme errors first, decide what to do with generated EComposer code second, then clean performance, SEO, and app overlap.

## Highest-Priority Fixes

### P0 - Fix normal theme syntax/schema/runtime issues

These are the items most likely to create real rendering, editor, or maintenance problems.

- `sections/header.liquid`
  - Theme Check reports `LiquidHTMLSyntaxError` at the dynamic tag:
    - `<{% if section.settings.enable_sticky_header %}sticky-header{% else %}div{% endif %} ...>`
  - Fix by assigning the tag name first, then rendering a normal tag open/close.
  - Also apply to `sections/header-original.liquid` or delete/archive `header-original` if it is truly unused.

- `sections/email-signup-banner.liquid`
  - Theme Check reports `ValidSchema`: `"templates"` is not allowed in section schema.
  - Fix by removing or relocating the invalid schema property.

- `sections/home-featured-collection.liquid`
  - Missing asset: `component-price-featured.css`.
  - Fix by either creating that asset, replacing it with `component-price.css`, or removing the reference if unused.

- `snippets/card-product-collections.liquid`
  - Theme Check reports an invalid close order: `</a>` before `</h3>`.
  - Fix HTML nesting in the placeholder/onboarding product card branch.

- `snippets/ecom_google_snippet.liquid`
  - Theme Check reports a Liquid tag close without matching open tag.
  - Because this is EComposer-generated schema/SEO code, decide whether it is actively used before editing. If used, fix. If unused, remove from render path.

- `snippets/ecom_theme_helper.liquid`
  - Missing snippet: `ecom-toast`.
  - Decide whether EComposer helper is still needed. If it is, either restore/add `snippets/ecom-toast.liquid` or remove that render call.

### P1 - Clean broken or fragile media/image markup

- `sections/location-detail.liquid`
  - `img` missing width/height.
  - Uses `{{ block.settings.image }}` directly, which should be reviewed for correct image object handling.

- `sections/runclubs-home.liquid`
  - Arrow images are remote Shopify file URLs with no width/height.
  - Fix dimensions and consider moving arrow SVGs into snippets/assets.

- `sections/ecom-default-template-quickview.liquid`
  - Multiple missing image width/height errors.
  - Generated file; should be handled only after deciding whether EComposer quickview is still active.

### P1 - Remove parser-blocking global scripts

`layout/theme.liquid` currently loads these as parser-blocking scripts:

- `https://unpkg.com/aos@2.3.1/dist/aos.js`
- `https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js`
- `https://cdnjs.cloudflare.com/ajax/libs/slick-carousel/1.8.1/slick.min.js`

Fix options:

- add `defer` if load order still works
- move scripts to Shopify theme assets and load via `asset_url`
- remove scripts if no active sections depend on them

This should be tested carefully because `product.js`, run club sliders, and older custom sections may depend on jQuery/Slick.

### P1 - Decide what to do with EComposer

EComposer files are responsible for a large chunk of Theme Check errors and warnings:

- `layout/ecom.liquid`
- `templates/index.ecomposer.liquid`
- `sections/ecom-default-template-quickview.liquid`
- `sections/ecom-predictive-search.liquid`
- `sections/ecom_filters.liquid`
- `snippets/ecom_*`

Main issues:

- missing translation keys
- remote EComposer assets
- parser-blocking or malformed `asyc` script attributes
- missing image dimensions
- missing `ecom-toast` snippet
- orphaned snippets
- deprecated filters

Before fixing generated EComposer code, answer:

1. Is EComposer still installed and actively editing any live pages?
2. Is the EComposer homepage/template still assigned anywhere?
3. Is EComposer quickview used on collection/product cards?
4. Can EComposer-generated files be removed after replacing those pages with native theme sections?

If EComposer is no longer actively needed, the cleanest path is to remove or quarantine generated EComposer templates/snippets from the active theme. If it is needed, fixes should be made cautiously because EComposer may overwrite generated files.

## Medium-Priority Fixes

### Translation keys

Missing translation keys appear in:

- `layout/ecom.liquid`
- `sections/ecom-default-template-quickview.liquid`

These are mostly EComposer-generated. Fix by either:

- adding missing keys to `locales/en.default.json`
- replacing translation calls with literal text if the file is not meant to be translated
- removing generated files from the active theme path if unused

### Deprecated filters

Deprecated filters appear in:

- `layout/ecom.liquid`
- `snippets/ecom_google_snippet.liquid`

Examples:

- `img_url`
- `product_img_url`

Replace with `image_url` where these files are retained.

### Undefined objects and minor Liquid warnings

Normal-theme examples:

- `sections/contact-form.liquid`: `sizes` unknown
- `sections/image-divider.liquid`: `sizes` unknown
- `sections/main-collection-product-grid.liquid`: `sizes` unknown
- `sections/main-product.liquid`: `media` unknown in a featured-media srcset line
- `sections/main-product.liquid`: `continue` warning inside recommendation loop
- `sections/run-club-grid.liquid`: `sizes` unknown
- `sections/runclubs-home.liquid`: `sizes` unknown

These likely do not break the site, but they should be cleaned after P0/P1 items.

### Hardcoded routes

- `sections/main-collection-product-grid.liquid`
  - hardcoded `/collections/all`
  - replace with `{{ routes.all_products_collection_url }}`

### Console logs and debugging leftovers

Remove from first-party scripts:

- `assets/product.js`
  - `console.log('fire')`
- `assets/collections.js`
  - `console.log(imgHeight)`
- `assets/global.js`
  - `console.log(pagePos)`
  - `console.log('shop')`

Do not blindly edit `assets/timesact.js` yet. It appears to be app/vendor code and contains many logs tied to the pre-order/notify behavior.

## App And Integration Audit

Current app/integration surfaces visible in the theme:

- Loox Reviews
  - product templates now use Loox rating and review blocks.

- Easy Bundle Builder
  - present in `templates/page.bundle-and-save.json`.

- EComposer
  - present across layouts, sections, snippets, and `templates/index.ecomposer.liquid`.

- Timesact
  - `assets/timesact.js` loaded globally from `layout/theme.liquid`.
  - Appears related to preorder/back-in-stock behavior.

- Globo swatches
  - product page cleanup references `.globo-swatch-product-detail`.

- Samita lock/search
  - `templates/search.samitaLockSearch.liquid` paginates by 1000, which Theme Check flags.

Audit question for Bailey/Katherine:

- Which apps are still intentionally installed and actively used?
- Which apps are legacy or replaced?
- Which app owns reviews, swatches, notify-me, bundles, locked search, and page builder content?

Cleaning app overlap is as important as lint cleanup because it affects Bailey's ability to maintain the site.

## Template And Content Cleanup

Templates include several likely legacy/test/page-builder templates:

- `templates/index.ecomposer.liquid`
- `templates/page.homepage-typeform-test.json`
- `templates/page.typeform-test.json`
- `templates/search.preorder-now-search.liquid`
- `templates/search.samitaLockSearch.liquid`
- product-specific templates now aligned to the standard PDP:
  - `product.mikelle-bra.json`
  - `product.swillz-tank.json`
  - `product.emmy-short.json`
  - `product.alkal-short.json`
  - `product.cooldown-tee.json`

Recommended cleanup:

- identify which templates are assigned to live pages/products
- remove or archive unassigned test templates before handoff
- keep product-specific templates only if products are actively assigned to them
- otherwise migrate assigned products to the default product template and remove the extras

## Recommended Cleanup Order

### Pass 1 - Safe normal-theme fixes

Fix these first:

1. Header dynamic tag syntax in `header.liquid`.
2. Invalid `templates` schema property in `email-signup-banner.liquid`.
3. Missing `component-price-featured.css` reference.
4. Broken card HTML nesting in `card-product-collections.liquid`.
5. Image width/height errors in `location-detail.liquid` and `runclubs-home.liquid`.
6. First-party console logs in `product.js`, `collections.js`, and `global.js`.
7. Hardcoded `/collections/all` route.

Then run Theme Check and browser QA:

- homepage
- collection page
- Katherine PDP
- cart drawer/cart page
- run club page
- bundle page
- search page

### Pass 2 - Global performance cleanup

Focus on `layout/theme.liquid`:

1. Defer or localize AOS.
2. Defer or localize jQuery/Slick.
3. Confirm old sliders still work.
4. Replace font preloads with `preload_tag` where appropriate.
5. Review remote CSS/image assets used in global CSS.

### Pass 3 - EComposer decision

Do not spend hours fixing generated EComposer code until deciding whether it remains part of the active site.

If EComposer is unused:

- remove/disable EComposer layout/template/snippets from active theme paths
- verify homepage/page assignments are native theme templates

If EComposer is used:

- restore missing `ecom-toast`
- add missing translation keys or replace generated translation calls
- fix generated script attributes
- add missing image dimensions where possible
- accept some remote asset warnings as app-generated unless replacing the app

### Pass 4 - SEO/content/admin audit

This is outside Theme Check but important before handoff:

- product image alt text
- meta titles/descriptions
- empty blog/posts/pages
- indexed test pages
- `-copy` product slugs
- product descriptions
- app duplication in reviews/notify/bundles
- product metafield completeness

## Handoff Standard

Before handing back to Bailey, the theme should meet this bar:

- no normal-theme Liquid syntax errors
- no missing local assets
- no obvious runtime console errors on core flows
- product pages use the Katherine PDP system
- Bailey has a clear product-editing handoff
- legacy/test templates are identified or removed
- active app ownership is documented
- remaining generated-app warnings are explained rather than mysterious

