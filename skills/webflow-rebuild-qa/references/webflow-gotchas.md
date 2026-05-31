# Webflow Gotchas

These are preserved from the Vital Health rebuild.

## Static Preview To Webflow

Good path:

1. Use the static/Vercel preview as visual and content reference.
2. Recreate the global style system in Webflow.
3. Rebuild pages natively: Home, Services, About, Contact, or the approved page
   set.
4. Convert repeatable sections to CMS where helpful.
5. Wire booking, portal, checkout, phone, email, and location links.
6. Publish to staging and QA the published site.

Bad path:

- Trying to import HTML/CSS into Webflow and expecting Designer-editable pages.
- Leaving the site as custom HTML when the client asked to make changes later.

## Designer Reliability

- Designer element/style calls can timeout after a few operations.
- Keep the Designer tab foregrounded.
- Retry idempotent style/text batches after a timeout.
- Use Data API for pages, site scripts, CMS, settings, and publishing when it
  covers the job.

## Scripts

- Published output is the source of truth for scripts, fonts, current nav state,
  and scroll animations.
- After changing a script, publish and cache-bust the staging URL.
- If `update_registered_script` fails, register a new inline script version and
  attach that version to the site.
- Keep scripts small and purposeful. Mobile nav and scroll reveal are acceptable
  polish; page copy and client-owned content should remain native.

## Staging Versus Live

- `.webflow.io` staging is public but no-index and acceptable for client review.
- Custom domain publish is a separate launch decision.
- Staging can carry clearly documented placeholders for review.
- Live should not carry review-only placeholders, unverified claims, or fake
  policy links.
