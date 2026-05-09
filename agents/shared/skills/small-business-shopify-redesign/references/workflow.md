# Small Business Shopify Redesign Workflow

## Purpose

Use this workflow when a small business site needs a practical redesign or cleanup, not a theoretical rebuild. The goal is a better storefront and a safer editing model for the owner.

## 1. Establish The Safe Work Lane

- Identify store handle/domain.
- Identify all theme folders in the repo.
- Identify all known remote theme IDs from checkpoints, docs, or admin screenshots.
- Confirm the target draft theme.
- Treat live theme edits as forbidden unless explicitly requested.
- Record target state in updates and final notes.

Example target record:

```text
Store: cooldown-running.myshopify.com
Target theme: Annabel v2
Theme ID: 180306575634
Local folder: shopify-theme-annabel-v2/
Preview: https://cooldown-running.myshopify.com?preview_theme_id=180306575634
```

## 2. Classify The Work

Before coding, classify each task:

- **Theme code:** Liquid, CSS, JS, JSON templates, sections.
- **Shopify admin/content:** pages, products, metafields, collections, redirects, SEO, alt text.
- **App configuration:** Loox, EComposer, Easy Bundle Builder, subscription/notify-me apps, preorder apps, reviews.
- **Hybrid:** theme code displays fields controlled by admin or apps.

Do not solve app/admin configuration problems with theme code until the app/admin surface has been inspected or the user explicitly wants a theme workaround.

## 3. Owner-Editable Design Test

For every proposed implementation, ask:

- Can the owner change this from Shopify admin or the theme editor?
- Is this content product/page-specific, global, or temporary?
- Does this belong in a metafield, product field, page metafield, section setting, theme block, menu, app admin, or code?
- Would the owner have to preserve Liquid snippets in rich text or JSON settings? If yes, redesign the pattern.
- Would a future product/page require copying hidden code? If yes, build a reusable block/section/metafield pattern.

## 4. Code Change Rules

- Keep changes narrow.
- Use existing theme patterns.
- Prefer native Shopify image pickers for theme settings and page/product file references for admin-managed content.
- If a value may be either a Shopify image object or a plain URL, guard before applying `image_url`.
- Avoid relying on class names derived from unescaped human text. Use `handleize` for CSS classes.
- Do not edit app-generated files unless the app file is truly the product surface and the user accepts the maintenance risk.

## 5. Push Rules

- Use `--only` for every push unless there is a deliberate reason to push the whole theme.
- Use `--theme <id>` for drafts.
- Avoid `--live` and `--allow-live` by default.
- Use `--nodelete` for narrow pushes.
- If a JSON template depends on a changed section schema, push the section first, then the JSON templates.

## 6. Verification Rules

- Pull back changed files from the remote target into `/private/tmp/<project>-verify`.
- Grep/read for the actual patch in the pulled files.
- Open or fetch the preview URL when possible.
- For app-rendered surfaces, verify on the store-domain preview, not only localhost.
- Mention inherited full-theme-check failures separately from touched-file risks.

## 7. Deliverable Rules

For the user, keep the final answer brief but precise:

- What changed.
- Where it was pushed.
- How it was verified.
- What remains admin/app work.
- Links to changed local files and preview/editor URL if useful.
