# Correct And Incorrect Patterns From Cooldown

## Draft Targeting

Good:

- Duplicate or identify the safe working draft before experiments.
- Push only to the named draft theme ID.
- Treat `Annabel v2` as the sandbox for redesign experiments.
- Pull remote files after pushing to confirm the exact draft has the changes.

Bad:

- Pushing to live because the user mentions the regular site while discussing redesign work.
- Assuming a local folder or previous draft is the intended Shopify admin target.
- Pushing broad changes without `--only`.

Rule:

```text
For redesign/site iteration work, draft-only is the default. Live requires explicit current-turn approval.
```

## Theme IDs And Preview Source Of Truth

Good:

- Record theme name, ID, preview URL, editor URL, and local path in checkpoints.
- Use the Shopify admin screenshot or user confirmation to correct theme targeting.
- Use store-domain previews for Loox/review/app surfaces.

Bad:

- Trusting stale localhost previews after preview tokens expire.
- Verifying app-rendered content only on localhost.
- Treating full theme check as a blocker when failures are inherited generated app code.

## Owner Editing Model

Good:

- Move product accordion content into product metafields selectable by theme-editor dropdowns.
- Add disabled-by-default theme blocks for temporary product callouts.
- Use page metafields for run club city/state/time/location/leaders/cover image.
- Add theme-editor guidance that tells the owner where to edit the content.

Bad:

- Storing Liquid-looking metafield snippets inside JSON template settings.
- Making the theme editor look editable while the real workflow depends on preserving developer-written snippets.
- Solving recurring product/page content with one-off CSS or copied template blocks.

## Shopify Images And URLs

Good:

- Use `image_url` only for Shopify image objects.
- Guard mixed image inputs:

```liquid
{%- if image_value.width != blank -%}
  {{ image_value | image_url: width: 1500 | image_tag }}
{%- else -%}
  <img src="{{ image_value | escape }}" alt="{{ title | escape }}">
{%- endif -%}
```

Bad:

- Calling `image_url` on a plain URL or metafield URL. This can render `Liquid error: invalid url input`.
- Using a `url` schema setting for an image when an `image_picker` would make the editor safer.

## Layout And Spacing

Good:

- Check global layout CSS before changing section CSS.
- Add focused body/template-class overrides for known page templates.
- Preserve the original site’s proven visual behavior when the user provides a reference screenshot.

Bad:

- Tweaking section padding when the actual gap comes from global `main` padding.
- Applying a broad site-wide layout change to fix one template.

## App And Generated Code Debt

Good:

- Separate inherited EComposer/generated translation errors from touched-file defects.
- Document app/admin decisions for Easy Bundle Builder, EComposer, Loox, subscription/notify-me apps, preorder apps, and reviews.
- Inspect app admin before attempting theme-side cleanup.

Bad:

- Chasing generated EComposer translation keys during a focused redesign pass.
- Calling a redesign complete when the owner still cannot manage app/admin surfaces.

## QA And Handoff

Good:

- Create a Bailey/client-facing checklist for admin tasks: metafields, SEO meta descriptions, image alt text, duplicate pages, redirects, product handles, menu links, bundle app state.
- State residual risk plainly.
- Save checkpoints after important decisions, especially theme IDs and mistakes.

Bad:

- Reporting “fixed” without remote pullback verification.
- Omitting known manual/admin work from the final summary.
