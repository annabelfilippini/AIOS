# Revero Current Site Audit

Date: 2026-05-31

Sources:

- Live home page: https://www.revero.com/
- About: https://www.revero.com/about-us
- Membership: https://www.revero.com/membership
- FAQ: https://www.revero.com/faq
- Local captures: `sources/home.html`, `sources/about-us.html`,
  `sources/membership.html`, `sources/faq.html`
- Browser QA screenshots: `audit/revero-home-desktop.png`,
  `audit/revero-home-mobile.png`

## Executive Read

Revero has a compelling underlying product: a virtual clinic combining medical
care, nutrition therapy, coaching, remote monitoring, and an app for chronic
conditions. The website's main problem is not lack of content. It is that too
much content is repeated, too many claims are doing heavy legal/clinical work,
and the page structure feels like a funnel builder rather than a trustworthy
medical brand.

The highest-leverage refresh is a trust and conversion cleanup:

1. Rebuild the homepage around one clear story.
2. Reduce duplicate page sections and competing CTAs.
3. Clean medical copy and grammar.
4. Move claims into a clinically defensible proof system.
5. Preserve onboarding, app, support, and phone workflows as external systems.

## What Is Working

- Clear core promise: root-cause treatment for chronic conditions.
- Specific care model: medical providers, health coaches, nutrition therapy,
  remote monitoring, app-based support, and medication management.
- Strong founder/advisor material on About.
- Strong testimonial raw material.
- Multiple conversion paths: join, free info call, phone, login, support.
- FAQ contains substantial education content that could support SEO and sales.

## Priority Findings

### 1. The first impression is blocked by consent UI

Browser QA shows the accessibility tree begins with "Cookie and Tracking
Consent" before the page content. On both desktop and mobile, the consent layer
is the first announced region.

Why it matters: the first experience should establish clinical trust and the
care model. Right now, the first interaction is compliance UI.

Recommendation: keep consent compliant, but reduce its first-impression weight
and test whether it blocks key CTAs or mobile header visibility.

### 2. The page structure is overloaded and repetitive

Browser QA found:

- 53 total H1 elements on the home page.
- 23 visible H1 elements on desktop.
- Four visible "Join Now" instances and four visible "Free Info Call" instances
  in the desktop crawl.
- Multiple repeated content blocks across desktop/mobile variants.

Why it matters: this hurts accessibility, scanability, SEO hierarchy, and the
feeling of editorial control.

Recommendation: use one H1, a restrained section hierarchy, and one primary CTA
system. Keep "Join Now" and "Free Info Call," but define when each appears.

### 3. There are visible or source-level builder artifacts

The source capture includes a modal with "All Right! You're Ready!" and "Submit
your info down below and we'll get in contact - ASAP!" in `sources/home.html`.
Web extraction also surfaces "CUSTOM JAVASCRIPT / HTML" blocks and "Working..."
on some pages.

Why it matters: even when some artifacts are hidden, search engines, assistive
tech, previews, QA tools, and future editors may encounter them. It signals a
site that has accumulated patches.

Recommendation: rebuild with clean native sections and remove old hidden funnel
fragments.

### 4. Medical trust is being undercut by grammar and polish issues

Examples found in the live extracted pages:

- About: "Revero is a online medical clinic."
- About: "remote medical support in a personalized based on each patients
  unique profile."
- Membership: "The traditional healthcare model often reply on treating the
  symptoms."
- Membership: "Our nutrition therapy helps patients lose weight by eat healthy
  foods."
- FAQ: "Which locations is Reveroavailable in?"
- Membership: "4-month packageS."

Why it matters: small copy errors are more damaging on a medical site than on a
normal marketing site. They make the clinical claims feel less controlled.

Recommendation: full copy QA before design polish. Use a medical-trust voice:
plain, careful, specific, no hype.

### 5. Claims and testimonials need a defensibility pass

Current extracted claims include:

- "root cause treatment for your chronic conditions."
- "reverse autoimmune and other chronic diseases" in the meta description.
- Testimonials such as "lost 80 pounds, reversed my blood pressure, eliminated
  chronic pain" and "healed my autoimmune symptoms, got me off meds."
- Membership copy says the monthly subscription covers medical care, excluding
  medications, and that Revero is not covered by insurance.

Why it matters: these are not just marketing claims. They are health claims,
pricing claims, and patient outcome claims. A redesign should not amplify them
without clinical/legal approval.

Recommendation: create a claims matrix before mockup copy:

- keep as-is with source/sign-off
- soften
- move to testimonial with clear attribution
- remove from primary conversion path

### 6. Conversion hierarchy is muddled

Visible CTAs include Join Now, Sign Up, Sign Up For Revero, Get Started, Free
Info Call, Book a Free Call, Call Now, Schedule a Call, Login, Contact us now,
and Support.

Why it matters: the funnel has two good paths, join and talk to someone, but the
labels change too often. That makes the decision feel noisy.

Recommendation:

- Primary CTA: Join Revero or Get Started.
- Secondary CTA: Book a Free Info Call.
- Utility: Login, phone, support.
- Avoid new labels unless the destination genuinely changes.

### 7. The public site and backend systems should stay separate

Observed destinations:

- Join and login route to `onboarding.revero.com`.
- Support routes to Zendesk.
- Phone links use `(415) 835-4151`.
- Free info call is a separate Revero page.

Why it matters: this is like the Vital Health lesson. The public site should not
pretend to replace onboarding, the app, clinical workflows, support, or payment.

Recommendation: public-site refresh plus enrollment workflow coordination. If
rebuilt in Webflow, keep onboarding and support external and test all handoffs.

## Suggested Redesign Direction

Positioning: "A virtual clinic for chronic conditions, built around medical care
and personalized nutrition."

Homepage story:

1. Hero: who it is for, what Revero does, two CTAs.
2. Trust strip: licensed clinical care, remote monitoring, coaching, app,
   HSA/FSA if confirmed.
3. Conditions: metabolic first, then autoimmune/inflammatory with careful
   wording if availability varies.
4. How care works: labs/devices, clinician review, nutrition plan, coaching,
   medication management, app support.
5. Proof: outcomes with attribution and clinical/legal sign-off.
6. Membership: what is included, what costs extra, insurance/HSA/FSA note.
7. Founder/clinical credibility: short founder story plus medical leadership.
8. FAQ preview.
9. Final CTA: join or book a free info call.

## Discovery Questions

- Which conditions are currently available, and which are "coming soon"?
- Are autoimmune and inflammatory conditions live for all patients or limited?
- Which state availability limits apply?
- What claims and testimonials are approved for use in ads and on the public
  website?
- What does "Join Now" start inside onboarding?
- What is the conversion goal from paid search: immediate enrollment or info
  call?
- Who owns site updates now?
- Would Revero want a public-site rebuild in Webflow, or is the current funnel
  platform required for marketing ops?

## Process Harness Notes

The new process worked well for this first pass because it forced:

- Client/Annabel/reality separation before design.
- Backend boundary check before recommending Webflow.
- Medical-claim blockers before mockup copy.
- Browser QA evidence, not just subjective design critique.

Gap noticed: for health/digital clinic sites, the harness should probably add a
mandatory "claims matrix" reference before any HTML preview.
