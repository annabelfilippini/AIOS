# Codex QA Review

## Target

- Project: Cooldown Shopify draft cleanup
- Branch / PR / Diff: local `shopify-theme/`, pushed to Shopify theme `Annabel Design` `#180287308050`
- Requested by: Annabel
- Review date: 2026-05-06

## Verdict

Pass With Follow-Ups

The Annabel Design draft covers the major website issues Bailey raised: PDP photos/layout polish, confusing color/size selections, visible reviews, product template consistency, announcement/bundle copy, header/menu cleanup, and the new run club/footer behavior. The remaining work is mostly Shopify admin/app/content cleanup rather than more theme code before Bailey sees the draft.

## Scope Reviewed

- Bailey source notes:
  - `cooldown-meeting-prep/bailey-session-notes-2026-05-02.md`
  - `cooldown-meeting-prep/session-checkpoint-2026-05-02-shopify-redesign.md`
  - `cooldown-meeting-prep/bailey-pdp-system-plan-2026-05-05.md`
  - `cooldown-meeting-prep/bailey-product-editing-handoff-2026-05-05.md`
  - `cooldown-meeting-prep/session-checkpoint-2026-05-05-pdp-final-polish.md`
  - `cooldown-meeting-prep/session-checkpoint-2026-05-05-technical-debt-audit.md`
  - `cooldown-meeting-prep/session-checkpoint-2026-05-05-audit-reconciliation.md`
  - `cooldown-meeting-prep/session-checkpoint-2026-05-05-local-preview-mega-menu-bundle-qa.md`
  - `cooldown-meeting-prep/session-checkpoint-2026-05-06-annabel-design-header-collections-reviews.md`
- Current theme files most relevant to Bailey:
  - product JSON templates
  - `sections/main-product.liquid`
  - `assets/section-main-product.css`
  - `assets/product.js`
  - `assets/product-form.js`
  - `assets/pdp-polish.js`
  - `sections/loox-product-reviews.liquid`
  - `sections/product-recommendations.liquid`
  - `sections/header.liquid`
  - `assets/megamenu.css`
  - `sections/footer.liquid`
  - `config/settings_data.json`

## Verification Checked

- Shopify remote verification:
  - Pulled `assets/megamenu.css` and `sections/footer.liquid` back from theme `#180287308050`.
  - Confirmed remote files match local pushed files.
- JSON parse checks passed:
  - `config/settings_data.json`
  - `templates/index.json`
  - `templates/page.bundle-and-save.json`
  - `templates/page.json`
  - all standard/product-specific product templates
- JavaScript syntax checks passed:
  - `assets/product.js`
  - `assets/product-form.js`
  - `assets/pdp-polish.js`
  - `assets/collections.js`
  - `assets/global.js`
  - `assets/run-club-slider.js`
- Product template consistency:
  - `product.json`, `product.alkal-short.json`, `product.cooldown-tee.json`, `product.emmy-short.json`, `product.mikelle-bra.json`, and `product.swillz-tank.json` all use:
    - `main > product-recommendations > loox-product-reviews > 17049932609aaec97f`
    - Loox rating block near the product information
    - metafield-driven materials, care instructions, and size guide fields
    - recommendations before full Loox reviews
- Theme Check:
  - Full `shopify theme check --path . --fail-level error --no-color` still exits nonzero.
  - Current failures remain the previously documented EComposer/generated/app issues and translation keys, plus known remote asset warnings.

## Findings

### P1 - Must Fix

- None blocking Bailey review on the Annabel Design draft.

### P2 - Should Fix

- [ ] Easy Bundle Builder still needs admin/app configuration review. Theme-side copy and routing mitigations are present, but the bundle app itself previously showed bad variant/category state and redirected to an empty collection.
- [ ] Product metafields need Shopify admin verification. The templates reference `custom.materials`, `custom.care_instructions`, and `custom.size_guide`, but Bailey/admin still needs to confirm definitions and fill missing values.
- [ ] Men/mens collection state needs admin decision. Recent menu routing now exposes real mens routes; confirm collections are populated and not empty before live launch.
- [ ] EComposer usage needs a decision. Full Theme Check remains noisy because generated EComposer files still produce errors; do not spend time fixing generated code until confirming whether EComposer is still active.

### P3 - Nice To Fix

- [ ] SEO/admin cleanup: meta descriptions for homepage, collections, about, run clubs, and key products.
- [ ] Product image alt text cleanup in Shopify admin.
- [ ] Duplicate/test page cleanup or redirects, especially old run club/contact/city preview pages and `join-our-crew-1`.
- [ ] Product handle cleanup for `-copy` slugs with redirects.
- [ ] Blog/content strategy remains open from the original audit.
- [ ] Final app ownership note should explain Loox, Globo, Timesact/Growave, Easy Bundle Builder, EComposer, and Samita.

## Bailey Notes Coverage

- Product photos too small: Covered by PDP media/gallery polish using Katherine as the reference.
- Color/size selection confusing: Covered by selected option labels, clearer size pills, muted unavailable states, and app markup cleanup.
- Customers think items are sold out: Mostly covered visually; still needs live/manual testing across variants and app-generated unavailable states.
- Reviews missing: Covered by Loox rating near price and dedicated full reviews section.
- Agency-built code makes simple edits difficult: Partially covered through standardized product templates and Bailey editing handoff; remaining complexity exists in apps/generated files.
- Bailey wants fresher Shopify template approach/more control: Partially covered for PDPs and header/menu settings; larger theme-control layer remains a future proposal.
- Announcement promo wrong: Covered; announcement text/link point to `buy 3 items • get 20% off` and Bundle & Save.
- Bundle app hard to manage: Not fully covered; documented as admin/app configuration work.
- Run club/header/footer behavior from latest Annabel pass: Covered in Annabel Design draft only, not live production.

## Missing Verification

- Manual browser QA on the remote Annabel Design preview after today’s push:
  - homepage header
  - `/collections/all`
  - womens/mens category links
  - `/products/katherine-bra`
  - one sold-out/notify-me product state
  - `/pages/run-clubs`
  - footer links from bottom-of-page
  - `/pages/bundle-and-save`
- Mobile visual QA is still needed across homepage, collection page, representative PDPs, cart, search, run clubs, and bundle page.
- Shopify admin verification is still needed for metafields, product handles, image alt text, meta descriptions, duplicate pages, Easy Bundle Builder, and EComposer usage.

## Risks Accepted

- Full Theme Check is not clean because generated/app files still fail; this is documented and should not be treated as a surprise blocker.
- `pdp-polish.js` remains a pragmatic app-markup cleanup layer. It is acceptable for the draft, but the cleaner future path is fewer app/CSS overrides.
- The current work is intentionally kept on the unpublished Annabel Design theme.

## Suggested Fix Prompt For Claude Code

Do not fix theme code yet. Inspect Shopify admin/app configuration for Easy Bundle Builder, product metafields, product handles, SEO meta fields, duplicate pages, and EComposer usage. Produce a Bailey-ready admin cleanup checklist with exact decisions needed and any safe admin edits to make.

## Re-Review Notes

Re-review after remote browser QA and Shopify admin checks. The next review should focus less on Liquid/CSS and more on whether Bailey can safely maintain products/pages from admin without app surprises.
