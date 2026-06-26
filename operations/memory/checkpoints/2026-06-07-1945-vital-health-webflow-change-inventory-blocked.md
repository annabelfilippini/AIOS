---
date: 2026-06-07
time: 19:45
project: vital-health-webflow-review
status: in-progress
next-session: Use Webflow Designer/native element tooling to apply the local review deltas, then publish staging only and run QA.
---

# Session: Vital Health Webflow change inventory and push check

## What we worked on

- Used `webflow-rebuild-qa` to map the local Vital Health review HTML against the current Webflow staging site.
- Verified current staging pages return `200` and match local `*-source.html`:
  - `https://vital-health-9bf311.webflow.io/`
  - `/services`
  - `/about`
  - `/contact`
- Verified staging `/shop` currently returns `404`.
- Created `projects/websites/vital-health-review/webflow-change-inventory-2026-06-07.md`.
- Restarted local preview server at `http://127.0.0.1:8765/home-review.html`.
- Opened the local Home review page in Playwright and confirmed expected updated content renders.
- Confirmed Webflow CLI auth can access site `6a15e6f364922623e13946da` and that staging was last published May 30, 2026.

## Decisions made

- Treat the pending delta as `*-source.html` -> `*-review.html`, because staging exactly matches the source captures.
- Do not run `webflow sites publish` yet, because no native Webflow content changes have been applied in this session.
- Do not use injected custom code to swap body copy/content for review, because Vital Health should remain editable in Webflow.
- Treat Shop as a separate decision unless Annabel explicitly wants a review-only `/shop` page created now.

## Open questions

- Which Webflow editing path should be used next: Designer MCP/native element tooling, Annabel logging into Webflow Designer in the active browser, or manual Designer edits using the inventory?
- Whether the Shop page should be included in this client review batch or parked for the Shopify/Clover/HIPAAtizer compliance pass.
- Whether the Google reviews rail should stay a mock for client discussion or wait for a CMS/API implementation.

## Next steps

1. Open Webflow Designer with authenticated editing access or restore the Designer element tooling used in prior sessions.
2. Apply Home, Services, About, and Contact changes from `webflow-change-inventory-2026-06-07.md` as native Webflow elements.
3. Convert local review links back to production paths before publish.
4. Publish to `.webflow.io` staging only.
5. QA desktop/mobile, anchors, stale-copy search, map link, patient portal, console, and horizontal overflow.

## Context to preserve

- Webflow site ID: `6a15e6f364922623e13946da`.
- Page IDs:
  - Home: `6a15e6f464922623e139470e`
  - Services: `6a15f430cbd0f7ef0469e27f`
  - About: `6a19b8b56de372b248e55901`
  - Contact: `6a19bf5c98546d4f3a53d97a`
- Designer URL redirected to Webflow login in this Playwright session, so there is no active Designer browser auth.
- CLI supports `sites publish`, CMS, assets, and forms, but not native static page DOM editing.

## System refinement candidates

- Add a Webflow Designer-access preflight to the static-review workflow before promising a staging push.
- Preserve Webflow-native element IDs or Designer edit maps next to future local review HTML so pushes are less manual.
