# Revero Website Refresh

Test project for the `client-website-refresh` harness.

## Source URL

- Live site: https://www.revero.com/
- Initial pages captured: Home, About, Membership, FAQ.

## Stack Reality

- Current public site appears to be built with ClickFunnels-style generated
  markup and assets.
- CTAs route to `onboarding.revero.com`, phone links, `free-info-call`, and
  Zendesk support.
- No client access, credentials, Webflow site, or approved redesign direction
  exists yet.

## Working Rules

- Treat this as an audit and process test until Annabel explicitly asks for a
  mockup or outreach/proposal.
- Because this is health care adjacent, flag medical claims, testimonials,
  state availability, pricing, privacy, and insurance statements for client or
  legal/clinical sign-off before any public use.
- Preserve the backend/platform boundary. A public-site redesign should not
  imply replacing onboarding, the app, medical workflow, payment, support, or
  clinical systems.
- Use `client-website-refresh` first, then `webflow-rebuild-qa` only if a
  Webflow rebuild becomes part of the test.
