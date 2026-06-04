# Session Checkpoint - Technical Debt Audit Before Bailey Handoff

**Date:** 2026-05-05  
**Project:** Cool Down / Shopify draft cleanup  
**Draft theme:** `#180297498898`  
**Local theme path:** `shopify-theme/`  
**Local preview:** `http://127.0.0.1:9296/`  
**Reference PDP:** `http://127.0.0.1:9296/products/katherine-bra?pdp_cleanup=3`  
**Current browser URL during session:** `http://127.0.0.1:9296/products/katherine-bra?pdp_cleanup=3&guard=3`

## Session Goal

Annabel decided the next step should be a whole-site technical debt audit before handing the theme back to Bailey. The goal is not only to make Theme Check pass. The goal is to clean the site in a way that makes it safer, easier to maintain, and easier for Bailey to use through Shopify admin/theme editor instead of code.

North star:

- Katherine Bra remains the reference PDP.
- Product/page structures should be reusable, not one-off hacks.
- Bailey should manage product content through product fields, metafields, theme editor blocks, and app/admin settings.
- Code should be cleaned enough that remaining app-generated debt is understood and documented, not mysterious.

## Context From Earlier Same-Day Work

Earlier in this session, Katherine Bra was made the standard PDP reference and the product-specific templates were aligned to the same structure.

Files changed in the PDP system pass:

- `shopify-theme/templates/product.mikelle-bra.json`
- `shopify-theme/templates/product.swillz-tank.json`
- `shopify-theme/templates/product.emmy-short.json`
- `shopify-theme/templates/product.alkal-short.json`
- `shopify-theme/templates/product.cooldown-tee.json`
- `shopify-theme/assets/product-form.js`
- `shopify-theme/sections/main-product.liquid`
- `cooldown-meeting-prep/bailey-pdp-system-plan-2026-05-05.md`
- `cooldown-meeting-prep/bailey-product-editing-handoff-2026-05-05.md`
- `cooldown-meeting-prep/session-checkpoint-2026-05-05-bailey-pdp-system.md`

Key result:

- Existing product-specific templates now match `templates/product.json`.
- They share the Katherine/default PDP structure:
  - thumbnail-slider gallery
  - Loox rating near the price
  - variant picker before add-to-cart
  - metafield-driven Materials, Care Instructions, and Size Guide accordions
  - shared Return Policy accordion
  - Loox review section lower on page
  - `Others loved` recommendations
- `assets/product-form.js` now has defensive guards for missing forms/buttons.
- `sections/main-product.liquid` now cache-busts the PDP `product-form.js` include with `&pdp-system=1`.

Important verification from that pass:

- Product JSON templates parse.
- `node --check shopify-theme/assets/product-form.js` passed.
- `node --check shopify-theme/assets/pdp-polish.js` passed.
- Katherine, Mikelle, Emmy, and Alkal were checked in preview.
- Guessed handles `swillz-tank` and `cooldown-tee` returned 404, though their template files are aligned.
- Direct source check confirmed the PDP renders the guarded asset:
  - `/cdn/shop/t/15/assets/product-form.js?...&pdp-system=1`

## Technical Debt Audit Performed

Created:

- `cooldown-meeting-prep/technical-debt-audit-2026-05-05.md`

Audit command run:

```bash
shopify theme check --path shopify-theme
```

Theme Check result:

- 229 files inspected
- 136 total offenses
- 40 files affected
- 50 errors

Important interpretation:

- The theme does not need to be rebuilt from scratch before handoff.
- The current theme is a hybrid of:
  - Dawn-style theme files
  - EComposer-generated files
  - app-generated snippets/assets
  - custom Cool Down sections
- The scary Theme Check count is inflated by generated EComposer/app code.
- Still, several normal theme files have real issues and should be cleaned before handoff.

## Main Audit Findings

### P0 / First Cleanup Pass

Fix normal theme issues first:

1. `sections/header.liquid`
   - `LiquidHTMLSyntaxError` from dynamic tag:
     - `<{% if section.settings.enable_sticky_header %}sticky-header{% else %}div{% endif %} ...>`
   - Fix by assigning tag name first or splitting the markup into explicit branches.
   - Also decide what to do with `sections/header-original.liquid`, which has the same issue.

2. `sections/email-signup-banner.liquid`
   - `ValidSchema`: `"templates"` is not allowed in section schema.
   - Remove or relocate invalid schema property.

3. `sections/home-featured-collection.liquid`
   - Missing asset:
     - `component-price-featured.css`
   - Either create asset, switch to `component-price.css`, or remove reference if unused.

4. `snippets/card-product-collections.liquid`
   - Broken HTML nesting:
     - Theme Check says `</a>` closes before `</h3>`.
   - Fix the placeholder/onboarding product card branch.

5. `sections/location-detail.liquid`
   - `img` missing width/height.
   - Also uses `{{ block.settings.image }}` directly and should be reviewed for proper image object output.

6. `sections/runclubs-home.liquid`
   - Remote arrow images missing width/height.
   - Consider moving arrows to assets/snippets later.

7. First-party debug logs:
   - `assets/product.js`: `console.log('fire')`
   - `assets/collections.js`: `console.log(imgHeight)`
   - `assets/global.js`: `console.log(pagePos)` and `console.log('shop')`
   - Do not blindly edit `assets/timesact.js`; it appears app/vendor-owned.

8. `sections/main-collection-product-grid.liquid`
   - hardcoded `/collections/all`
   - replace with `{{ routes.all_products_collection_url }}`

### P1 / Global Performance Cleanup

Focus on `layout/theme.liquid`:

- parser-blocking AOS script:
  - `https://unpkg.com/aos@2.3.1/dist/aos.js`
- parser-blocking jQuery:
  - `https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js`
- parser-blocking Slick:
  - `https://cdnjs.cloudflare.com/ajax/libs/slick-carousel/1.8.1/slick.min.js`
- remote CSS assets:
  - Slick CSS
  - AOS CSS
- font preloads that Theme Check wants changed to `preload_tag`

Must test carefully because old custom sections and `product.js` may depend on jQuery/Slick.

### P1 / EComposer Decision

EComposer files produce many Theme Check errors/warnings:

- `layout/ecom.liquid`
- `templates/index.ecomposer.liquid`
- `sections/ecom-default-template-quickview.liquid`
- `sections/ecom-predictive-search.liquid`
- `sections/ecom_filters.liquid`
- `snippets/ecom_*`

Issues include:

- missing translation keys
- remote EComposer assets
- malformed `asyc` attributes on scripts
- parser-blocking scripts
- missing image width/height
- missing `snippets/ecom-toast.liquid`
- orphaned snippets
- deprecated filters

Do not spend hours fixing generated EComposer code until deciding whether EComposer is still active. Need to answer:

1. Is EComposer still installed and actively editing live pages?
2. Is `templates/index.ecomposer.liquid` assigned anywhere?
3. Is EComposer quickview used on collection/product cards?
4. Can generated EComposer files be removed/quarantined after replacing pages with native theme sections?

If EComposer is unused, best path is to remove or quarantine generated files from active theme paths.

If EComposer is used, fix carefully because generated files may be overwritten by the app.

### SEO / Content / Admin Audit Still Needed

Outside Theme Check but important before Bailey handoff:

- product image alt text
- meta titles/descriptions
- empty blog/posts/pages
- indexed test pages
- `-copy` product slugs
- product descriptions
- product metafield completeness
- app duplication in reviews/swatches/notify/bundles
- assigned template cleanup

## App / Integration Surfaces Identified

- Loox Reviews
  - now used in standard product templates
- Easy Bundle Builder
  - used in `templates/page.bundle-and-save.json`
- EComposer
  - widespread generated files
- Timesact
  - `assets/timesact.js` loaded globally from `layout/theme.liquid`
  - likely preorder/back-in-stock behavior
- Globo swatches
  - referenced by `assets/product.js` and `assets/pdp-polish.js`
- Samita lock/search
  - `templates/search.samitaLockSearch.liquid` paginates by 1000 and is flagged

Need to document which app owns what before handoff:

- reviews
- swatches
- notify-me/back-in-stock
- bundles
- locked search
- page builder content

## Current Files Added This Session

- `cooldown-meeting-prep/bailey-pdp-system-plan-2026-05-05.md`
- `cooldown-meeting-prep/bailey-product-editing-handoff-2026-05-05.md`
- `cooldown-meeting-prep/session-checkpoint-2026-05-05-bailey-pdp-system.md`
- `cooldown-meeting-prep/technical-debt-audit-2026-05-05.md`
- this checkpoint:
  - `cooldown-meeting-prep/session-checkpoint-2026-05-05-technical-debt-audit.md`

## Current Local Server State

Shopify dev server was running at:

```text
http://127.0.0.1:9296/
```

If resuming later and preview is stale or dead, restart with:

```bash
shopify theme dev --path shopify-theme --host 127.0.0.1 --port 9296
```

If port is occupied/stale, use a fresh port:

```bash
shopify theme dev --path shopify-theme --host 127.0.0.1 --port 9297
```

## Suggested Next Session Plan

### Step 1 - Re-establish baseline

1. Read this checkpoint.
2. Read `technical-debt-audit-2026-05-05.md`.
3. Start or confirm Shopify preview.
4. Run:

```bash
shopify theme check --path shopify-theme
```

5. Save/compare output mentally against this checkpoint.

### Step 2 - Implement safe normal-theme cleanup

Start with the first cleanup pass:

1. Fix header dynamic tag syntax in `sections/header.liquid`.
2. Decide whether to fix or remove/archive `sections/header-original.liquid`.
3. Fix invalid schema in `sections/email-signup-banner.liquid`.
4. Fix missing `component-price-featured.css` reference.
5. Fix HTML nesting in `snippets/card-product-collections.liquid`.
6. Fix image dimensions/object output in `sections/location-detail.liquid`.
7. Fix arrow image dimensions in `sections/runclubs-home.liquid`.
8. Remove first-party debug logs.
9. Replace hardcoded `/collections/all`.

### Step 3 - Verify after pass 1

Run:

```bash
shopify theme check --path shopify-theme
node --check shopify-theme/assets/product.js
node --check shopify-theme/assets/collections.js
node --check shopify-theme/assets/global.js
```

Browser QA:

- homepage
- collection page
- Katherine PDP
- Mikelle / Emmy / Alkal PDP
- cart drawer/cart page
- run club page
- bundle page
- search page

### Step 4 - Decide EComposer path

Before editing generated EComposer files, determine if EComposer is still active.

Possible approaches:

- inspect template assignments / JSON references
- ask Bailey/Katherine whether EComposer is still used
- inspect whether `index.ecomposer.liquid` or EComposer quickview appears in active pages

Then choose:

- remove/quarantine EComposer generated code if unused
- or fix/accept generated EComposer warnings if active

### Step 5 - Bailey usability cleanup

After code safety:

- reduce unnecessary one-off templates
- document assigned templates
- verify product metafields exist and are filled
- create final Bailey handoff:
  - where to edit product content
  - where to edit page sections
  - what apps control each area
  - what not to touch

## Definition Of Done Before Bailey Handoff

- No normal-theme Liquid syntax errors.
- No missing local assets.
- No obvious runtime console errors on core flows.
- Product pages use the Katherine PDP system.
- Bailey has a practical product/page editing guide.
- Legacy/test templates are identified or removed.
- App ownership is documented.
- Remaining generated-app warnings are explained and not treated as mysterious unfinished work.

