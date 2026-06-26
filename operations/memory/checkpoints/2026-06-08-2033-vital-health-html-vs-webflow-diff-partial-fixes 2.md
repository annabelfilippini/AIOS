---
date: 2026-06-08
time: 20:33
project: vital-health-webflow-review
status: partial-shipped
next-session: Manual Designer work to land main-breakpoint fixes + CV button + address split. MCP bridge cannot modify existing main-breakpoint properties; only adds-to-empty-slots persist.
published-to: https://vital-health-9bf311.webflow.io (large-breakpoint overrides only)
---

# Session: HTML vs Webflow exhaustive diff + partial fixes via MCP

## What happened

- Annabel asked to compare the static review HTML preview (the design source of truth) against the live Webflow staging site and make sure they match exactly.
- Started with the most recent checkpoint scope (hormone bullets) and confirmed structure + CSS were byte-identical, then realized she also wanted the full site comparison.
- Took fullPage Playwright screenshots at 1280px of all five pages on both sides, with vh-reveal opacity forced visible. Pixel-diffed each pair, then text-diffed HTML to confirm content matches.
- Discovered five real deltas. Pushed three of them as partial fixes via Webflow MCP. Hit a bridge constraint that blocked the rest.

## Source of truth (re-confirmed)

- The `services-review.html`, `home-review.html`, `about-review.html`, `contact-review.html`, `shop-review.html` files in `projects/websites/vital-health-review/` are the design source. Webflow is supposed to match them.
- Direction of every fix: bring Webflow up to the HTML, never the reverse.

## Diff findings (Webflow is missing vs local HTML)

| # | Page | Delta | Local source |
|---|---|---|---|
| 1 | Home | Pillar cards render 4-up + 1 wrap on Webflow. Local is 5-up at ≥992px via `@media (min-width: 992px) .services-section .svc-grid { grid-template-columns: repeat(5, minmax(0, 1fr)) !important }`. | `home-review.html` |
| 2 | Services | Hormone-bullet rows are grid-aligned (ragged vertical spacing). Local was changed this session to CSS multi-column for clean rhythm. | `services-review.html` — switched from `display:grid; gap:6px 22px` to `column-count:2; column-gap:22px` with li `break-inside:avoid; margin-bottom:6px`. |
| 3 | About | "View Dr. Feste's CV" button missing on Webflow. Local has it between bio paragraph and blockquote, linking to `assets/cv/dr-joseph-feste-cv.pdf`. | `about-review.html` |
| 4 | Contact | LOCATION info card renders address as 2 lines (`Bldg 6, Suite 125, Austin, TX 78746` combined). Local is 3 lines. | `contact-review.html` |
| 5 | Shop | (a) Hero layout: live wraps paragraph below heading and stacks buttons; local is single-row heading-left + paragraph-and-buttons-right. (b) Product card images differ — local pills have white stripe + green band; live pills are plain brown silhouettes (different uploaded assets). | `shop-review.html` |

Footer matches across all pages. Nav has a few pixels of font-rendering noise, ignore. Services page text+structure was already byte-identical.

## What landed via MCP (large breakpoint, ≥1280px only)

| Style | Property added | Effect |
|---|---|---|
| `svc-grid` | `grid-template-columns: repeat(5, minmax(0, 1fr))` | Pillar cards 5-up on monitors ≥1280px |
| `hormone-bullets` | `display: block; column-count: 2; column-gap: 22px` | Multi-column bullets on monitors ≥1280px |
| `hormone-bullet-li` | `margin-bottom: 6px; break-inside: avoid` | Clean spacing + no item split across columns |
| `hormone-bullets` | (already shipped) `column-count: 1` at small breakpoint | Mobile single column |

Published to webflow.io subdomain at end of session.

## NEW Webflow MCP bridge constraint (worth preserving)

Webflow Designer MCP `style_tool > update_style` **only persists writes to empty property slots**. Confirmed with multiple diagnostic attempts:

- ADD a brand-new property on a brand-new breakpoint (e.g. `column-count: 1` on small for hormone-bullets) → ✅ persists
- ADD a brand-new property on a breakpoint that already has properties (e.g. `margin-bottom` on hormone-bullet-li main) → ❌ silently dropped
- MODIFY an existing property value (e.g. svc-grid main grid-template-columns) → ❌ silently dropped
- REMOVE an existing property (e.g. svc-grid main grid-template-columns) → ❌ silently dropped

Every call returns `{status: "success", message: "Style X updated"}`. The `data` field shows the OLD state. A fresh `query_styles` call is the only way to detect the silent drop.

Workaround pattern that worked this session: add the same property to a higher breakpoint that doesn't yet have it (e.g. `large` for svc-grid where only `main` had `grid-template-columns`). Covers ≥1280px only.

Also confirmed: even when Designer is in `design` mode on the correct page, foreground tab, the constraint holds. Not a focus issue. The bridge times out after ~3 calls if the tab idles, which is a separate (focus) issue.

→ saving as a new memory: `feedback_webflow_bridge_empty_slots_only`.

## Decisions

- Switched local hormone-bullets from CSS grid to CSS multi-column to fix ragged vertical row spacing that Annabel flagged from a viewport screenshot. The grid behavior was identical between local and live; the spacing was a layout choice, not a Webflow-vs-local mismatch.
- Did not push to Webflow for shop (#5) — Annabel didn't pick those in the fix scope question; reserved for a later pass that needs new image uploads.
- Published the partial large-breakpoint fixes to staging rather than letting them sit as unpublished drafts.

## Open questions

- For svc-grid 5-col and hormone-bullets multi-column on Webflow: do we accept the ≥1280-only landing, or is it worth Annabel manually changing main breakpoint in Designer? Most desktop traffic is ≥1280px, but 13" MacBooks and similar at default zoom land at 1280 exactly or 1440 logical, so the partial fix covers them. The 992-1279 band is rare on modern hardware.
- About CV button and Contact address split — both will likely hit the same MCP constraint (element_tool write to existing structures). Best path is probably manual Designer click-through, with click-by-click instructions from this session's findings.
- Whether to ALSO add the xl/xxl breakpoints with same overrides for consistency, or leave only `large`.

## Next steps

- Annabel does manual Designer work for the four still-open items:
  1. `svc-grid` main breakpoint: change `grid-template-columns` from `repeat(4, 1fr)` to `repeat(5, minmax(0, 1fr))`.
  2. `hormone-bullets` main breakpoint: change `display: grid` → `display: block`, remove `grid-template-columns`/`grid-column-gap`/`grid-row-gap`, add `column-count: 2` and `column-gap: 22px`.
  3. `hormone-bullet-li` main breakpoint: add `margin-bottom: 6px` and `break-inside: avoid`.
  4. About page Joseph Feste section: upload `projects/websites/vital-health-review/assets/cv/dr-joseph-feste-cv.pdf` as a Webflow asset, then insert an outline-style link button labeled "View Dr. Feste's CV" between the bio paragraph and the blockquote, linking to that asset.
  5. Contact page LOCATION info card: split the line "Bldg 6, Suite 125, Austin, TX 78746" so it renders as two separate lines: `Bldg 6, Suite 125` and `Austin, TX 78746`.
- After her edits, re-publish to staging and re-run the local-vs-live diff with Playwright + Python ImageChops to confirm pixel-clean match.
- Skip Shop fixes for now; flagged for a separate pass that needs new product image uploads and hero layout adjustment.

## Context to preserve

- Site ID: `6a15e6f364922623e13946da`
- Services page ID: `6a15f430cbd0f7ef0469e27f`
- Home page ID: `6a15f464_64922623e139470e` (slug `/`)
- Style IDs:
  - `svc-grid`: `84c0e81f-327c-8245-28af-e6e18c24d84d`
  - `svc-card`: `84c0e81f-327c-8245-28af-e6e18c24d84e`
  - `hormone-bullets`: `e9ae9556-a59a-1047-d983-65c07d7a9f9a`
  - `hormone-bullet-li`: `5efefa87-c636-3f35-e68e-a0ed3f497acc`
- Local review pages: `projects/websites/vital-health-review/*-review.html`
- Local source pages: `projects/websites/vital-health-review/*-source.html`
- CV PDF: `projects/websites/vital-health-review/assets/cv/dr-joseph-feste-cv.pdf`
- Diff scratch: `.playwright-mcp/vh-diff/` (local-*and live-* PNGs per page, plus diff-*.png composites)
- Local preview server: `python3 -m http.server 8765` in `projects/websites/vital-health-review/`
- Webflow Designer launch: <https://vital-health-9bf311.design.webflow.com?app=dc8209c65e3ec02254d15275ca056539c89f6d15741893a0adf29ad6f381eb99>
