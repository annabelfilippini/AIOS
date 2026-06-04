# Admin / Content Cleanup Map

Use this as the working checklist before deleting, renaming, or redirecting Shopify admin content. The theme references below were found locally, but final decisions should be made against live Shopify admin URLs and analytics.

## Redirect + Handle Map

| Current URL / handle | Local evidence | Recommended action | Redirect target | Notes |
| --- | --- | --- | --- | --- |
| `/pages/typeform-test` | `templates/page.typeform-test.json` duplicates run club grid and Typeform embed behavior. | Delete or unassign after confirming no live nav/search/ads use it. | `/pages/run-clubs` | This looks like an old run club application/test page. Preserve Typeform embed only if still needed elsewhere. |
| `/pages/homepage-typeform-test` | `templates/page.homepage-typeform-test.json`; old CSS dependency removed from `assets/base.css`. | Delete or unassign after confirming no live traffic. | `/` | Looks like a homepage experiment with embedded Typeform. |
| `/pages/runclubs2024` | `templates/page.runclubs2024.json`; CSS still supports `.page-runclubs2024`. | Rename/migrate to canonical `run-clubs`, then remove old template once content is merged. | `/pages/run-clubs` | Compare city list against current `run-clubs` page before deleting. |
| `/pages/contact2024` | `templates/page.contact2024.json`. | Rename to canonical `/pages/contact` if still current, or delete if duplicate. | `/pages/contact` | Confirm contact forms and footer/nav references first. |
| `/pages/join-our-crew-1` | Header links in `config/settings_data.json`. | Rename to a clean handle if this is the active franchise/start page. | Suggested: `/pages/start-a-cooldown` | Header text says `start a cooldown`, so the handle should match. Update header links after rename. |
| `/pages/copy-of-chicago` | Linked inside `templates/page.runclubs2024.json`. | Rename to clean city handle if active, otherwise redirect. | Suggested: `/pages/chicago` | Check whether `/pages/chicago-1` or `/pages/chicago` is the live canonical page. |
| `/pages/tampa-1` | Linked inside `templates/page.runclubs2024.json`. | Rename if active. | Suggested: `/pages/tampa` | Add redirect from old suffix handle. |
| `/pages/boston-1` | Linked inside `templates/page.runclubs2024.json`. | Rename if active. | Suggested: `/pages/boston` | Add redirect from old suffix handle. |
| `/search?view=preorder-now-search` or `search.preorder-now-search` | `templates/search.preorder-now-search.liquid`. | Confirm app dependency before deletion. | `/search` | Likely app-generated or legacy. Do not remove if an app still calls this view. |
| `/search?view=samitaLockSearch` or `search.samitaLockSearch` | `templates/search.samitaLockSearch.liquid`. | Confirm app dependency before deletion. | `/search` | Likely app-generated lock/search template. Do not remove if an app still calls this view. |

## Product Content Consistency

For every active apparel product:

| Field | Standard |
| --- | --- |
| Product title | Clean customer-facing name, no variant/color suffix unless the product is color-specific. |
| Product description | 1 short brand paragraph, then fit/function details, then any final-sale or care caveats. |
| SEO title | Product name plus category and brand, ideally under 60 characters. |
| Meta description | Specific, benefit-led sentence under 155 characters. |
| Image alt text | Product name + color/style + visible angle/detail. Avoid raw filenames. |
| Materials metafield | Filled consistently, since templates render `product.metafields.custom.materials.value`. |
| Care instructions metafield | Filled consistently, since templates render `product.metafields.custom.care_instructions`. |
| Size guide metafield | Points to the correct product/category size guide page. |

## Page SEO Pass

Prioritize:

| Page | SEO / content action |
| --- | --- |
| Home | Confirm title/meta describe Cooldown as run club + apparel brand. |
| Run Clubs | Canonicalize to one page/handle; remove 2024/test duplicates. |
| Start a Cooldown | Rename handle from `join-our-crew-1` if active; align page title, H1, nav, and SEO. |
| Bundle and Save | Remove disabled placeholder blocks in admin if they are visible in editor clutter; confirm live copy is not placeholder. |
| Contact | Canonicalize `contact2024` vs `contact`. |
| Returns | Confirm policy copy matches PDP return accordion. |
| City pages | Normalize city handles, title format, meta descriptions, and redirects from suffix handles. |

## Admin Execution Order

1. Export or review live Shopify pages/products/collections.
2. Move questionable pages into the Bailey archive queue instead of deleting immediately.
3. Mark each duplicate/test page as `keep`, `merge`, `rename`, `archive`, or `delete`.
4. Create redirects before deleting or renaming live handles.
5. Update navigation/header/footer links after handle changes.
6. Fill page and product SEO title/meta fields.
7. Add product and page image alt text in Shopify admin.
8. Re-test: homepage, run clubs, city pages, start page, bundle page, collection pages, PDPs, search, header/footer nav.

## Bailey Archive Queue

Shopify Pages does not support true folders, so use this lightweight archive process:

1. Set the page visibility to hidden.
2. Rename the page title with an archive prefix, for example `[Archive Review] Run Clubs 2024 - Preview Version`.
3. Keep the page content intact until Bailey reviews it.
4. Add the page to this queue with the proposed redirect.
5. After Bailey approves, create the redirect and delete or permanently unassign the old page/template.

| Page title in Shopify | Current status | Proposed decision | Proposed redirect | Bailey decision |
| --- | --- | --- | --- | --- |
| Run Clubs - Typeform Test | Visible | Archive for review | `/pages/run-clubs` | Pending |
| Run Clubs 2024 - Preview Version | Hidden | Archive for review | `/pages/run-clubs` | Pending |
| Contact 2024 - Preview Version | Hidden | Archive for review | `/pages/contact` | Pending |
| About Us 2024 - Preview Version | Hidden | Archive for review | Current About page | Pending |
| Tampa old | Visible | Archive for review | Current Tampa page | Pending |

## Theme Follow-Up Candidates

These are optional code cleanup items after admin cleanup:

| File | Candidate cleanup |
| --- | --- |
| `assets/base.css` | Remove `.page-runclubs2024` styles after the old run club page is retired. |
| `assets/megamenu.css` | Remove `.page-runclubs2024` selectors after canonicalizing run clubs. |
| `templates/page.typeform-test.json` | Delete after admin confirms page is unused and redirects exist. |
| `templates/page.homepage-typeform-test.json` | Delete after admin confirms page is unused and redirects exist. |
| `templates/page.runclubs2024.json` | Delete after content has been merged to canonical run club page. |
| `templates/search.preorder-now-search.liquid` | Delete only after confirming no app routes require it. |
| `templates/search.samitaLockSearch.liquid` | Delete only after confirming no app routes require it. |
