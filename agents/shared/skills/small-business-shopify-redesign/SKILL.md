---
name: small-business-shopify-redesign
description: Draft-only Shopify redesign workflow for small business sites. Use when Codex is asked to improve, redesign, QA, simplify, push, or document a Shopify theme for a small business, especially when there are multiple draft/live themes, app-generated code, owner-editability goals, product/page templates, metafields, theme previews, or requests to replicate lessons from the Cooldown redesign.
---

# Small Business Shopify Redesign

Use this skill to redesign or clean up a Shopify site without creating live-site risk, while making the result easier for a non-developer owner to maintain.

## Non-Negotiables

- Work on the explicitly approved draft theme only.
- Never edit or push to the live theme unless the user explicitly asks for live production changes in the current turn.
- Before pushing, identify the store, target theme name, target theme ID, local folder, preview URL, and whether the change is code, Shopify admin/content, app configuration, or a mix.
- Keep pushes narrow with `shopify theme push --only ...`.
- Pull the changed remote files back after pushing and verify the exact remote theme contains the patch.
- Treat full `shopify theme check` failures from app/generated legacy code as contextual debt unless they touch changed files or block the requested work.
- Prioritize owner-editable Shopify fields, metafields, theme blocks/settings, and app admin surfaces over brittle custom CSS/JS/Liquid patches.

## First Pass

1. Read project-specific docs and checkpoints before broad searches.
2. Locate all local Shopify theme folders and decide which folder maps to the approved draft.
3. Search memory/checkpoints for prior target theme IDs and mistakes.
4. Ask only if the target draft is ambiguous; otherwise proceed on the documented draft.
5. Do not assume a folder named like the client, “redesign,” or “draft” is the correct remote theme. Verify.

## Implementation Pattern

- Reproduce the issue in the draft preview when feasible.
- Inspect the relevant template, section, asset, and app/metafield dependency.
- Make the smallest code change that solves the user-facing issue without making owner editing harder.
- If a pattern appears in multiple templates, convert it into an owner-editable section/block/metafield pattern instead of duplicating code.
- Avoid editing generated app files unless the user specifically approves that app-layer work.
- For visual changes, preserve the existing design language unless the user requests a new direction.

## Verification Pattern

- Run targeted checks when full theme check is noisy.
- Use store-domain previews for app-rendered features such as reviews, bundles, subscriptions, notify-me widgets, and embedded app blocks; localhost can mislead.
- Verify generated HTML or screenshots for the exact page when possible.
- Push only changed files to the target draft.
- Pull only changed files into `/private/tmp/...` and grep/read them to confirm remote state.
- Give the user the preview/editor URLs and state clearly what was not verified.

## Handoff Pattern

End with:

- Theme name and ID changed.
- Files changed.
- Preview URL.
- Verification performed.
- Remaining admin/app decisions.
- Any theme-check failures that are pre-existing and unrelated.

## References

- For the reusable workflow checklist, read [workflow.md](references/workflow.md).
- For correct and incorrect examples from the Cooldown project, read [good-bad-examples.md](references/good-bad-examples.md).
- For Shopify command and verification guardrails, read [shopify-guardrails.md](references/shopify-guardrails.md).
