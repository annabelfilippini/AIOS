---
date: 2026-06-22
time: 16:11
project: cooldown
status: done
next-session: No open task. Fix is live on published v3. If Annabel wants very-tall images (e.g. Nicole) shown FULLY instead of cropped to the 128% portrait frame, that's a separate tweak (raise/remove the `min(128%, ...)` aspect cap on the media item) — she was offered it and did not ask for it. Edited file lives at projects/consulting/prospects/cooldown/v3-live/assets/section-main-product.css (pulled-fresh-from-live working copy; not committed to git).
---

# Session: Cooldown — PDP gallery thumbnails overlapping the product image (fixed live)

## Request
Annabel: on product pages the row of small thumbnails was sitting ON TOP of the
bottom of the large product image (clipping the model's skirt). Wanted thumbnails
moved BELOW the main image, "for all products." Asked for a draft mockup first
(approved), then said to edit live v3 directly since it was a small change.

## Connection (reusable)
- Store: `cooldown-running.myshopify.com` (primary domain redirects to
  `cooldownrunning.com`).
- Shopify CLI 3.94.3 at `/usr/local/bin/shopify`. Auth = browser device-code OAuth,
  creds cached in macOS keychain (no config file). First `shopify theme list
  --store=cooldown-running` triggers the login link; after that it's silent.
- Live published theme: **Annabel v3 = #180320076050**. (Other themes: Annabel v2
  #180306575634, Annabel Design #180287308050, plus Dawn/Ride/Sense backups.)
- Pulled a fresh narrow working copy to `v3-live/` via `shopify theme pull
  --theme=180320076050 --only ...` (don't trust the older stale `shopify-theme*`
  folders — live had moved on).

## Root cause (took real digging — box model lied at first)
- The thumbnails ALWAYS flow as a normal block AFTER the gallery viewer; they are
  NOT absolutely pinned. So at first every emulated width showed a 12–20px GAP and
  I could not reproduce the overlap. Annabel's first screenshot was ambiguous width.
- Her second screenshot was clearly DESKTOP two-column. Reproduced at 1728px.
- Real mechanism: the gallery viewer `slider-component` was capped at
  `max-height: 75vh` (= 810px at 1080 tall) with `overflow: visible`, but the
  product image renders in a taller **128% portrait frame** (`.product__media-item`
  ~927px via the theme's `min(128%, calc(100vh - 11rem))` rule). The image
  overflowed the bottom of its 810px viewer; the thumbnail row was placed right
  after the 810px viewer, so the image's overflow (~117px) rendered UNDER the
  thumbnails. Worse on bigger screens / taller images → hit ~all products.
- Source rules: `assets/section-main-product.css` lines ~229–240
  (`.slick-list`, `.product__media-item.slider__slide { max-height:75vh; overflow:hidden }`).
- MOBILE (<=749px) was already fine — image is object-fit-cropped to fit its slot,
  thumbnails 12px below, no overlap. So the fix is desktop-only.

## The fix (live)
Appended a desktop-only override block to the END of
`v3-live/assets/section-main-product.css`:
```css
@media screen and (min-width: 750px) {
  media-gallery slider-component:not(.thumbnail-slider) { height:auto !important; max-height:none !important; }
  .product__media-item.slider__slide { max-height:none !important; }
  .slick-list { max-height:none !important; }
}
```
Lets the viewer fit the 128% frame so thumbnails always land below it.

## Verified (pushed live, cache-busted, box-model measured)
- Pushed only that one asset: `shopify theme push --theme=180320076050 --path
  v3-live --only "assets/section-main-product.css" --nodelete --allow-live` (success).
- Katherine Bra: overlap -20 (20px gap), image fully shown (not clipped). ✓
- Nicole Bra (17 imgs, tall 150% image): overlap -20, framed to the standard 128%
  crop (same crop it had before — NOT a regression, just overlap gone). ✓
- Emmy Short: overlap -20. ✓
- Mobile unchanged.

## Notes / gotchas
- Verified everything via Playwright `browser_evaluate` box-model reads; Playwright
  MCP screenshots save to a sandbox the shell can't read (known) — don't hunt for them.
- Change went straight to the PUBLISHED theme (affects live store immediately) per
  Annabel's instruction. Not committed to git.
