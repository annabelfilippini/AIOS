# Checkpoint - Annabel v3 QA + Polish QA Gaps Found

Date: 2026-05-12 09:50
Project: `projects/consulting/prospects/cooldown/`

## Theme Target

- Store: `cooldown-running.myshopify.com`
- Draft: `Annabel v3` `#180320076050` (unpublished)
- Local source: `projects/consulting/prospects/cooldown/shopify-theme-annabel-v2/`
- Preview: `https://cooldown-running.myshopify.com?preview_theme_id=180320076050`
- Editor: `https://cooldown-running.myshopify.com/admin/themes/180320076050/editor`

## Verdict

Functional pass — add-to-cart flow is seamless end-to-end on desktop and mobile.
All v2-era fixes hold on v3 (duplicate-add guard, raw `.sale-badge` CSS leak,
single-color auto-select). Full QA report saved at
`agents/shared/qa/active/2026-05-12-cooldown-annabel-v3-qa.md`.

## Add-To-Cart Flow Verified

- Default variant pre-selected on PDP load; variant input populated immediately.
- Switching color/size updates URL, hidden `name=id`, and selected option labels in lockstep.
- ATC fires exactly one `/cart/add` per click (network-spy confirmed) on desktop and mobile.
- Different variants of same product create separate cart lines.
- Single-color products (`Boulderthon Molly Short` → `skyway`) auto-select.
- Drawer auto-opens with image, title, variant, line price, qty controls, remove, subtotal.
- Qty `+` updates the line without spawning duplicate; cart total tracks correctly.
- `Check out` reaches `/checkouts/cn/...` with `preview_theme_id=180320076050` preserved.
- Mobile drawer fits 100% width at 390px; checkout visible mid-viewport; inner is scrollable.

## Polish / Alignment Gaps Found (NEW)

Visual QA surfaced items that Codex's structural pass and earlier QA passes missed. These are documented as patterns to catch next time in the skill's
`workflow.md` (Polish & Alignment QA) and `good-bad-examples.md` (Visual Polish QA).

Site header (`sections/header.liquid`):

- Duplicate search icon: search appears on the LEFT (next to `shop`) AND on the RIGHT (just before `the run club`). Should be a single instance.
- Right-side nav text is 3-4 px below icon center: `the run club` / `start a cooldown` have visual-center y=58 while the search/cart icons sit at y=54. Caused by missing `display: flex; align-items: center; line-height: 1` on `.nav-links`.
- Right search hugs `the run club` with 0 px gap (after dedupe, gap can rebalance).
- Asymmetric edge padding: 20 px on the left, 30 px on the right.

Home featured-products section:

- Product card title `Boulderthon Katherine Bra` wraps to 2 lines while neighbors are 1 line. Without `min-height` (or reserved space via `line-clamp: 2`), the price row drops on that card, breaking horizontal alignment across the row.

Home run-clubs section:

- Carousel arrows float at the top-right in dead space, not vertically aligned with either the heading row or the card row.

Collection pages:

- `/collections/womens-collection` and `/collections/mens-collection` have no visible H1 — only a tiny breadcrumb. Page identity is missing for both users and SEO.

3rd-party popup (Mailchimp Forms — NOT theme):

- `mcforms-wrapper` close button is 27×27 px with a 13×13 SVG icon. Below WCAG 24×24 minimum (well below Apple HIG 44×44 for touch). Click works but feels unresponsive due to ~1 s fade-out animation.
- Popup renders inside a Shadow DOM (`#mcforms-...` host). Theme CSS cannot override it. Fix is in the **Mailchimp Forms app dashboard** (popup builder for form ID `55954-72384`), not v3 code.

## Inherited / Not New In v3

- `/apps/timesact/config` 404 on every PDP (carried over from v2; app config or removal).
- `srcset` `w`-descriptor parse warnings on a Katherine Bra image (content upload issue).
- `1 colors` (plural) on single-color collection cards.
- `/collections/womens` and `/collections/mens` 404 (only the `-collection`-suffixed handles work).
- Easy Bundle Builder first-step product set is narrow (admin/app, not theme).

## Deployment Readiness

No blockers for publishing v3. Purchase path is verified.
Polish items above are recommended but non-blocking.

## Files Created/Updated

- QA report: `agents/shared/qa/active/2026-05-12-cooldown-annabel-v3-qa.md`
- Skill: `agents/shared/skills/small-business-shopify-redesign/references/workflow.md` (added Polish & Alignment QA subsection)
- Skill: `agents/shared/skills/small-business-shopify-redesign/references/good-bad-examples.md` (added Visual Polish QA section)
- Screenshots in cooldown project root: `v3-home-desktop.png`, `v3-home-mobile.png`, `v3-header-1440.png`, `v3-home-section-products.png`, `v3-home-section-runclubs-full.png`, `v3-pdp-header.png`, `v3-pdp-mobile.png`, `v3-coll-header.png`, `v3-mens-collection.png`, `v3-popup-state-2.png`, `v3-popup-after-x-click.png`, `v3-run-clubs-desktop.png`.

## Next Best Step

If Annabel decides to publish v3 to live: have Codex first fix the four header/section items above (duplicate search icon, nav text vertical alignment, card title `min-height`, run-clubs carousel arrow placement) as a narrow `--only` push. Pop-up close-button sizing is an app-config task in the Mailchimp Forms dashboard, not a theme push.
