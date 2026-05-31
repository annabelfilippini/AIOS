---
date: 2026-05-26
time: 20:38
project: consulting / vital-health
status: in-progress
next-session: Continue rebuilding the Vercel preview inside Webflow Designer, using uploaded assets and CMS collections already created through Webflow CLI.
---

# Session: Vital Health Webflow CLI Connected

## What we worked on

- Authenticated Webflow CLI on Annabel's machine.
- Confirmed official Webflow CLI version `1.23.0`.
- Listed Webflow sites and found `Vital Health`.
- Created local migration workbench at `projects/vital-health-webflow-migration/`.
- Downloaded the current Vercel preview snapshot and core assets into `projects/vital-health-webflow-migration/snapshot/`.

## Decisions made

- Use Webflow CLI where it helps: assets, CMS collections/fields, site listing, publish support.
- Do not treat Webflow like Shopify CLI. Webflow CLI cannot import the Vercel HTML/CSS into editable Designer pages.
- The rebuild still needs Webflow Designer for layout/page construction, using the Vercel snapshot as the reference.

## Open questions

- Whether Annabel wants Codex to use browser automation to perform the Designer rebuild step visually.
- Whether Vital Health wants CMS collections connected to visible pages immediately or after static page layout is rebuilt.
- Whether promotions should be public-site announcements only, backend checkout discounts, or both.

## Next steps

1. Open the Vital Health Webflow site in Designer.
2. Rebuild Home, Services, About, and Contact using the Vercel snapshot.
3. Connect editable repeatable sections to CMS where appropriate.
4. Wire Cerbo patient portal links to `https://vitalhealth.md-hq.com`.
5. QA mobile/desktop and publish when ready.

## Context to preserve

- Webflow site ID: `6a15e6f364922623e13946da`.
- Assets uploaded to Webflow and documented in `projects/vital-health-webflow-migration/docs/webflow-assets.md`.
- CMS collections and fields created in Webflow and documented in `projects/vital-health-webflow-migration/docs/webflow-cms.md`.
- Webflow CLI credentials were saved by the CLI at `/Users/annabelfilippini/.config/webflow/auth.json`; do not commit credentials.

## System refinement candidates

- If this workflow works, create a reusable "Vercel/static preview to Webflow rebuild" checklist under consulting or small-business website skills.
