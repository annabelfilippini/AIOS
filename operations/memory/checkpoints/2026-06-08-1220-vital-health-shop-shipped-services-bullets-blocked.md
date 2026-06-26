---
date: 2026-06-08
time: 12:20
project: vital-health-webflow-review
status: paused
next-session: Shop page is shipped and matches source. Services hormone bullets are blocked — `bullets hormone-bullets` classes ARE applied to all 4 lists, a site-wide CSS-injector script is registered and loaded, but the visual output still does not match the source (no golden dots, wrong spacing/font). Investigate why the script's injected CSS is not taking effect on staging.
published-to: https://vital-health-9bf311.webflow.io (Shop now live at /shop)
---

# Session: Vital Health — Shop page shipped, Services bullets still broken

## What we worked on

- Built and shipped the entire Shop page from scratch in Webflow against `projects/websites/vital-health-review/shop-review.html`. ~8 MCP calls, no bridge drops after initial reactivation.
- Confirmed the home page Services block already matches `home-review.html` exactly (no edits needed).
- Tried to fix the Services page hormone-section bullet lists, which Annabel flagged as wrong font, spacing, size, and bullet style versus `services-review.html`.

## What landed

### Shop page (DONE)

- Page ID `6a2692963ea5da7eb9c1134a`, slug `/shop`, SEO title + meta description match source.
- Sections: `shop-ab-hero` (SHOP h1 + intro + 2 anchor buttons), `#supplements` (4 product cards with prices and Add to cart / Out of stock states), `#hormone-refills` (Hipaatizer iframe).
- Shared Site Nav prepended and Site Footer appended via `de_component_tool > insert_component_instance` — the previously broken Shop nav link now resolves.
- All custom styles (`.shop-*`, `.product-*`, `.hormone-form-*`, brand overrides, 991/767 breakpoints) were attached on the first `whtml_builder` call and survived.
- Text diff vs source: identical for all 3 sections.

### Services bullets (BLOCKED, visually wrong)

- Identified 4 `<ul>` lists in the hormone block: For-women-4-items, For-women-8-items, For-men-11-items, What-we-treat-8-items.
- Created `hormone-bullets` style via `style_tool > create_style` (grid 2-col, 22px/6px gaps, 8px/14px margin, no list-style).
- Applied `set_style ["bullets", "hormone-bullets"]` to all 4 lists — confirmed live HTML now reads `class="bullets hormone-bullets"`.
- Tried adding font/color/dot rules via `whtml_builder` CSS sink: rules were rejected because compound selectors like `.svc-body .hormone-bullets li::before` don't map to Webflow's class-based Style system. Only the standalone `.hormone-bullets {}` rule survived.
- Workaround: registered inline script `VHHormoneBulletsCSS` (id `vhhormonebulletscss`, v0.0.1) that injects a `<style>` tag at runtime; attached to the site footer scope.
- Confirmed `vhhormonebulletscss-0.0.1.js` is loaded on `/services`. Annabel reports the visual output is still wrong.

## Decisions made

- Use site-wide script injection as the fallback for CSS rules Webflow's Style system can't express (pseudo-element descendant rules like `li::before`). Confirmed loadable; effect still TBD.
- Keep the Webflow Style entities (`bullets`, `hormone-bullets`) as the source of truth for grid + list-style — they survive publish cleanly.
- Do not attempt to fix the bullets via Designer manual edits before debugging the script — the script approach should work and is replicable.

## Open questions

- Why doesn't the injected CSS visibly take effect? Hypotheses to test next session:
  - Cloudflare cache served stale HTML before the script was added; need a hard refresh after waiting longer or invalidate cache.
  - The injected `<style>` element appends after Webflow's CSS but the selectors don't actually win specificity over a Webflow class rule. Try moving the script to header location, or raise specificity (e.g. `ul.bullets.hormone-bullets li`).
  - The script may be loading but blocked by a CSP or executing in an unexpected document context.
  - Webflow strips `<style>` injection from third-party scripts? Unlikely but possible.
- Whether to skip the script entirely and instead apply per-`<li>` styles via `set_style` with a new `hormone-bullet-item` style that has `padding-left`, `position: relative`, and pseudo `before` properties — Webflow update_style accepts `pseudo: "before"`. Tedious (31 li elements across 4 lists) but more robust.

## Next steps

1. Hard refresh `/services` and inspect with devtools: confirm the script ran, the injected `<style>` is in `<head>`, and which rules are losing specificity battles.
2. If specificity loss: bump the script's selectors to `ul.bullets.hormone-bullets li::before` etc. Update script via `data_scripts_tool > update_registered_script` and republish.
3. If the script never executed: switch attach location from footer to header, or move to per-page attach on Services only.
4. Backup plan: per-li styling via Webflow Style entities with `pseudo: "before"`. Apply `hormone-bullet-item` style to all 31 list items via batched `set_style` calls.
5. Once bullets render correctly, do a full curl-diff vs source and update the previous-session deferred list (CV PDF, 3-line address, regenerative chip href).

## Context to preserve

### Site

- Site ID: `6a15e6f364922623e13946da`
- Webflow staging URL: `https://vital-health-9bf311.webflow.io`
- Designer activation link: `https://vital-health-9bf311.design.webflow.com?app=dc8209c65e3ec02254d15275ca056539c89f6d15741893a0adf29ad6f381eb99`

### Page IDs

- Home: `6a15e6f464922623e139470e`
- Services: `6a15f430cbd0f7ef0469e27f`
- About: `6a19b8b56de372b248e55901`
- Contact: `6a19bf5c98546d4f3a53d97a`
- Shop: `6a2692963ea5da7eb9c1134a` (NEW, /shop)

### Services hormone bullet list IDs (component `6a15f430cbd0f7ef0469e27f`)

- For-women 4-items: `c4ddd0ca-5a22-13e1-bafb-0439351f57d5`
- For-women 8-items: `da7b2e31-1ba7-1c4f-8908-2bf0c628f8c1`
- For-men 11-items: `c399d66e-ff34-e943-53f1-396e9da6caf7`
- What-we-treat 8-items: `121e6788-5f34-b85b-dfc5-6783dace8eac`

### Style entities

- `bullets` (id `9557fa1d-85a2-9e4d-9661-6c7d1aab85ae`) — pre-existing, 2-col grid with 30/10 gap
- `hormone-bullets` (id `e9ae9556-a59a-1047-d983-65c07d7a9f9a`) — NEW, 2-col grid with 22/6 gap, source-matching

### Script

- ID `vhhormonebulletscss`, v0.0.1, attached to site footer.
- Hosted at `https://cdn.prod.website-files.com/6a15e6f364922623e13946da%2F689e5ba67671442434f3ca35%2F6a2696b331523d92ed6f0c6e%2Fvhhormonebulletscss-0.0.1.js`

### Carry-over from previous session (still deferred)

- About: "View Dr. Feste's CV" link needs PDF upload to Webflow assets.
- Home + Contact: address renders as 2 lines instead of source's 3 (missing `<br>` between Suite 125 and Austin TX).
- Regenerative chip href: verify after publish; may still read `#wellness` instead of `#regenerative`.

## System refinement candidates

- `whtml_builder` silently drops compound CSS selectors. Worth noting in the Webflow MCP usage memory so future sessions reach straight for `style_tool` or `register_inline_script` for anything beyond single-class rules.
- Page-level `add_page_script` returned 404 immediately after `register_inline_script`; site-level apply worked. May need a short delay between register and page-attach, or the page-attach endpoint expects a different lookup.
