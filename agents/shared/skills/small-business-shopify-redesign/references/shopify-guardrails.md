# Shopify Guardrails

## Common Commands

Use exact theme IDs for remote draft work:

```bash
shopify theme push --store <store>.myshopify.com --theme <theme-id> --nodelete --only <path>
shopify theme pull --store <store>.myshopify.com --theme <theme-id> --nodelete --only <path> --path /private/tmp/<verify-folder>
```

Use live only when explicitly approved:

```bash
shopify theme push --store <store>.myshopify.com --live --allow-live --nodelete --only <path>
```

Run local preview on a fresh port if the old preview breaks:

```bash
shopify theme dev --store <store>.myshopify.com --path <theme-folder> --host 127.0.0.1 --port <fresh-port>
```

## Theme Check

- `shopify theme check --fail-level crash` can be useful when full check is noisy.
- Full theme check may fail because of inherited generated/app files.
- Treat failures as blocking only when they touch changed files, indicate syntax errors, or affect the requested surface.
- Report inherited failures as technical debt, not as new regressions.

## Remote Verification

After every push:

1. Pull the same file(s) from the same target theme into `/private/tmp/...`.
2. Search the pulled file(s) for the patch.
3. Open/fetch the preview page when practical.
4. For app-rendered features, verify on the store-domain preview because localhost can omit or misrepresent app behavior.

## Push Sequencing

If adding section schema that templates reference:

1. Push section/snippet/assets first.
2. Push JSON templates after Shopify has the new schema.
3. Pull back both groups.

## Red Flags

- User mentions “regular site” during redesign work: clarify whether they mean live or reference behavior. Default to draft-only changes.
- Multiple themes with similar names: do not push until theme ID is confirmed.
- App-generated Liquid is noisy: inspect before editing; avoid unless explicitly in scope.
- Admin content can overwrite JSON templates: note that theme editor/admin may regenerate templates.
