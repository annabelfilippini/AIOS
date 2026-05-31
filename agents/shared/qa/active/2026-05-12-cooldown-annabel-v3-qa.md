# Claude QA Review

## Target

- Project: Cooldown Shopify draft `Annabel v3`
- Theme ID: `180320076050` (unpublished)
- Preview: `https://cooldown-running.myshopify.com?preview_theme_id=180320076050`
- Editor: `https://cooldown-running.myshopify.com/admin/themes/180320076050/editor`
- Local source: `projects/consulting/prospects/cooldown/shopify-theme-annabel-v2`
- Requested by: Annabel
- Review date: 2026-05-12
- Prior pass: Codex structural QA (`session-checkpoint-2026-05-12-annabel-v3-draft.md`)

## Verdict

Pass. The add-to-cart flow is seamless end-to-end on both desktop (1440) and mobile (390). All previously fixed bugs (duplicate add, raw `.sale-badge` CSS leak, single-color auto-select) hold on v3. Remaining findings are minor and almost entirely inherited from prior reviews, not introduced by v3.

## Verified Live On v3 Preview

Confirmed `Shopify.theme.id === 180320076050`, `role === "unpublished"`, `name === "Annabel v3"` on every page tested, despite the storefront redirect from `cooldown-running.myshopify.com` to the canonical `cooldownrunning.com` domain (preview cookie survives the redirect).

## Add-To-Cart Flow (focused)

This was the lens for the whole review. Result: seamless.

Katherine Bra (multi-variant):

- Page loads with a default variant pre-selected (`lavender horizon / S`, variant ID present in `[name="id"]`); ATC is immediately clickable without manual selection.
- Switching color to `moon` and size to `M` updates the URL (`?variant=51145667576082`), the hidden variant input, and the visible option labels (`Color - moon`, `Size - M`) in lockstep.
- Clicking Add to cart fires exactly one `/cart/add` request (network-spy verified). Cart drawer auto-opens with `class="drawer animate active"`.
- Drawer shows: product image, product link, remove button, variant text `moon, M`, line price `$59.00`, qty controls, subtotal `$59.00 USD`, "Taxes and shipping calculated at checkout" caption, Check out CTA.
- Increasing quantity via the drawer `+` control updates the line from 1 → 2 (subtotal `$118.00`) without creating a duplicate line or firing extra `/cart/add`s.

Boulderthon Molly Short (single-color):

- The only color `skyway` is auto-selected on page load; ATC is enabled without manual swatch interaction. This is the regression the Bailey pass missed and the v2 fix introduced — it still holds.
- Adding `S / skyway` then `M / skyway` produces two separate cart lines, each qty 1, total `$136.00`. Single `/cart/add` per click in both cases.

Checkout reach:

- Cart drawer `Check out` button is a `type=submit` form button with `name=checkout` on a form posting to `/cart`.
- Clicking it navigates to `/checkouts/cn/hWNC...` (Shopify checkout) with `preview_theme_id=180320076050` preserved, so the v3 theme would render checkout-side previews of any storefront-injected blocks. Title becomes `Checkout - Cooldown`.

Mobile (390×844):

- Cart drawer opens full-width (left=0, right=390), Check out button visible at y≈571 of 844 viewport (mid-screen, comfortably above the fold), drawer inner is scrollable for taller carts.
- Single `/cart/add` fire on mobile, same as desktop. No regressions vs. the prior mobile QA.

## Other Verification

Homepage (desktop and mobile):

- Announcement: `buy 3 items • get 20% off` → `/pages/bundle-and-save`.
- Header: `shop` mega menu, search, the run club, start a cooldown, cart.
- Hero CTA: `shop apparel` and `our run club`.
- Featured product slider shows 8 products with correct price/colors and `Boulderthon Katherine Bra`, `Boulderthon Molly Short`, `Boulderthon Tank` cards from the Boulderthon pass.
- Run clubs preview section lists 10 cities with carousel arrows; full `/pages/run-clubs` page shows the full-bleed city tile grid (Denver, NYC, Minneapolis, Austin, Nashville, LA, Atlanta, Dallas, Chicago, Colorado Springs, Seattle, Toronto, DC).
- Footer: navigation, connect (Instagram, TikTok, General Inquiries), `be in the know` email subscribe.
- Console clean of theme-level errors; only app-injected logs (Easy Bundle, Globo, Timesact, Pop Convert, Grow) and one inherited Timesact 404 on PDPs.

Collection pages:

- `/collections/all`, `/collections/womens-collection`, `/collections/mens-collection` all return 200, render product grids (47 / 17 / 10 products respectively).
- No raw `.sale-badge` CSS leaked into page text on any collection. Final Sale badges render as `<div class="sale-badge">` (no longer `<h1>`).
- No nested `<a>` inside product cards.
- No horizontal overflow at 1440 on collection pages.
- Note: `/collections/womens` and `/collections/mens` 404 — only the `-collection`-suffixed handles work. The shop menu and footer use the working handles, so this is only a problem for hand-typed URLs.

PDP (Katherine Bra):

- `<h1>Katherine Bra</h1>`, price `$59.00`, Loox rating (4.5 stars, 63 reviews).
- Selected option label visible: `Color - lavender horizon`, `Size - S`. Updates live with selection.
- 32-image gallery, with the `Why We Made This` editorial block, `Materials`, `Care Instructions`, `Return Policy`, `Size Guide` accordion buttons, and `Others loved` recommendations section.

Bundle:

- `/pages/bundle-and-save` redirects to `?source=pageEmbed&page=addProductsPage1&currentFlow=byob` and renders the Easy Bundle Builder steps (`Add a top`, `Add bottoms`, `Add an accessory`, Tops/Mikelle... grid). The first-step product set is still narrow, consistent with the documented app-admin debt — not a v3 regression.

## Findings

### P1 - Must Fix

None.

### P2 - Should Fix

- [ ] Mobile PDP shows `document.scrollWidth = 400` at viewport 390 (10px excess). The visible ATC button has `rect.right = 400`. No unclipped descendant exceeds the viewport, so the source is likely a near-edge padding/margin in the product form container. Not user-perceptible; worth trimming before pushing to live.
- [ ] Run clubs page shows `scrollWidth = 1454` at viewport 1440 (14px excess). Same shape as above — invisible but real. Both deserve a single CSS pass to find and remove the offending margin/padding.
- [ ] PDP request to `/apps/timesact/config?productId=...` still 404s on every PDP. Carried over from 2026-05-11 full-site QA. Either configure Timesact correctly in admin or remove the integration from PDPs to clean the console.

### P3 - Nice To Fix

- [ ] Single-color products show `1 colors` (plural) on collection card subtitle. Theme-string pluralization edge case; affects `Boulderthon Katherine Bra`, `Boulderthon Molly Short`, `Boulderthon Tank`.
- [ ] Women's and Men's collection pages have no visible H1 title (the document `<h1>` is the logo wordmark). Add a real collection title H1 for accessibility/SEO.
- [ ] `Katherine Bra` gallery image emits `srcset` `w` descriptor parse warnings (3 dropped candidates for `15_5531720f-…png`). Looks like a content upload with a bad `w` descriptor — fixable by re-uploading the image in Shopify admin.
- [ ] `/collections/womens` and `/collections/mens` 404 (the live handles are `-collection`-suffixed). Add Shopify redirects so hand-typed URLs resolve.

## Risks Accepted

- Easy Bundle Builder first-step product set remains narrow — documented admin/app-side work, not a v3 theme issue.
- Theme Check has known inherited EComposer/translation noise; v3's `shopify theme check --fail-level crash` is documented as passing in the v3 draft checkpoint.

## Files Of Interest (no changes recommended in this pass)

- `assets/product-form.js` — `CooldownCartAddGuard` confirmed firing on v3.
- `layout/theme.liquid` — `if (event.defaultPrevented) return;` confirmed via single `/cart/add` per click.
- `snippets/cart-drawer.liquid` — qty/remove/checkout reachable from drawer on both desktop and mobile.
- `assets/component-cart-drawer.css` — mobile drawer fits 100% width, checkout visible mid-viewport at 844px height.

## Suggested Fix Prompt For Claude Code

Trim the residual 10–14px right-edge overflow on the mobile PDP (`/products/*`) and the desktop run-clubs page (`/pages/run-clubs`). The body `scrollWidth` exceeds `clientWidth` but no unclipped descendant is offending — start by inspecting the outermost product form container on PDP and the run-clubs section container; the culprit is most likely a `margin-right`/`padding-right` or a negative-margin row that escapes its parent. Verify with `document.documentElement.scrollWidth === document.documentElement.clientWidth` after the fix.

## Re-Review Notes

If Annabel wants to publish v3 to live, the gating items are the two `scrollWidth` excesses (visual polish) and the Timesact 404 (console hygiene). Functional shopping path is ready.
