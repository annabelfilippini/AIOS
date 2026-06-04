# Session Checkpoint - Annabel v2 Theme Created

**Date:** 2026-05-06  
**Project:** Cooldown / Shopify draft cleanup  
**Original approved draft:** `Annabel Design`  
**Original theme ID:** `180287308050`  
**New sandbox draft:** `Annabel v2`  
**New theme ID:** `180306575634`  
**New preview URL:** `https://cooldown-running.myshopify.com?preview_theme_id=180306575634`  
**New theme editor:** `https://cooldown-running.myshopify.com/admin/themes/180306575634/editor`  
**Original local path:** `shopify-theme/`  
**Annabel v2 local path:** `shopify-theme-annabel-v2/`

## What Happened

Annabel asked whether we could preserve the current approved `Annabel Design` draft and create a separate Shopify theme called `Annabel v2` for experimenting with a simpler Bailey editing surface.

Created the duplicate with:

```bash
shopify theme duplicate --store=cooldown-running --theme=180287308050 --name 'Annabel v2' --force --json
```

Then pulled the new theme into its own local folder:

```bash
shopify theme pull --store=cooldown-running --theme=180306575634 --path shopify-theme-annabel-v2 --force
```

## Verification

- Shopify returned new unpublished theme:
  - `Annabel v2`
  - `#180306575634`
- Compared local folders:
  - `shopify-theme-annabel-v2/` matches `shopify-theme/`
  - only difference is the local-only `shopify-theme/docs/` folder
- Confirmed the new v2 copy includes the recent approved changes:
  - `the run club` styling in `assets/megamenu.css`
  - footer top-of-page link behavior in `sections/footer.liquid`
  - `buy 3 items • get 20% off` announcement copy in `config/settings_data.json`
  - `product-recommendations` before `loox-product-reviews` in product templates

## Intended Use

Keep `Annabel Design` as the stable approved draft.

Use `Annabel v2` as the sandbox for making Bailey's editing surface easier:

- consolidate one-off product templates
- move product/page content into metafields and theme editor settings
- add cleaner editable sections for recurring page content
- document app ownership and reduce app-generated clutter where safe
- simplify Shopify admin/template choices without changing the live theme

## Important Reminder

Do not push Bailey-editing-surface experiments to `Annabel Design` unless Annabel explicitly asks.
