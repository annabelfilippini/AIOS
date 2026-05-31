# Webflow QA Checklist

Run this on the published staging URL, not only inside Designer.

## Page And Link Checks

- All intended pages return 200.
- Nav links go to the right pages and show the correct current state.
- Logo link works.
- Primary CTAs go to the correct booking, portal, checkout, phone, email, or
  form destination.
- External links open as intended and use `rel="noopener noreferrer"` where
  applicable.
- Phone numbers, emails, address, hours, and footer details are consistent.
- CMS template slugs do not collide with static pages.

## Visual And Responsive Checks

- Desktop QA at around 1440px.
- Mobile QA at around 390px.
- Mobile nav opens, closes, contains all required links, and does not overflow.
- Section spacing is intentional, not accidental giant voids.
- Cards, buttons, labels, and images do not overlap.
- Font weights match the approved preview or design direction.
- Images load, crop correctly, and are not substituted into the wrong semantic
  slot, especially headshots or founder portraits.
- Animations work on published staging and fail gracefully if JavaScript is off.

## Copy And Claims

- No em dashes, en dashes, or double hyphens in Annabel/client-facing copy.
- Current people are described in their current role.
- Redundant clauses are removed when the layout already shows the fact.
- Testimonials are real or clearly flagged as placeholders.
- Medical, legal, financial, or regulated claims have client/expert sign-off or
  are softened.
- SEO titles and meta descriptions are set and do not regress to old punctuation.

## Editability

- Client-owned body copy, images, bios, stats, services, contact details, and
  announcements are native editable elements or CMS content.
- Custom code is limited to polish or behavior that should not need normal
  client editing.
- Any non-editable tradeoff is documented in the handoff.

## Launch Blockers

Do not call the site live-ready if any of these remain:

- Review-only testimonial placeholders.
- Missing headshots or bios that the client expects on live.
- Unsigned sensitive claims.
- Broken portal, checkout, booking, phone, or email CTA.
- Unresolved custom-domain decision.
- Privacy, HIPAA, terms, refund, or policy links shown as links but not created.

## Reporting

End with:

- Staging URL.
- Pages checked.
- Desktop and mobile viewports checked.
- Known blockers before custom-domain live publish.
- What the client can edit in Webflow.
- What remains custom code or admin/vendor work.
