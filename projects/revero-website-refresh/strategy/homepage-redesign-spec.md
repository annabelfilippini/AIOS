# Revero Homepage Redesign Spec

Status: ready for Annabel review before HTML preview.

This spec is intentionally conservative because Revero is health care adjacent.
It should create a clearer, more trustworthy homepage without making stronger
medical claims than the current site.

Primary source: `audit/claims-matrix.md`

## Redesign Objective

Turn Revero's homepage from a dense funnel page into a credible virtual-clinic
homepage that explains:

- who Revero is for
- what kind of care model it offers
- how the enrollment path works
- why the model is clinically supervised
- what claims need approval before launch

## Audience

Primary visitor:

- Someone with a chronic metabolic, inflammatory, or related condition who has
  likely tried conventional care and wants a more hands-on, nutrition-centered
  option.

Secondary visitors:

- A family member helping someone compare options.
- A clinician or health care operator checking whether Revero is credible.
- A paid-search visitor deciding whether to enroll now or talk to a person.

## Brand Direction

Desired feel:

- modern virtual specialty clinic
- calm and clinical
- human, not sterile
- evidence-aware, not hype-driven
- technology-enabled, but care-team-led

Avoid:

- miracle-cure tone
- supplement funnel energy
- repeated CTA strips
- too many condition badges above the fold
- overclaiming root-cause language
- generic wellness gradients

## Page Architecture

### Section 1: Hero

Goal: establish Revero as a virtual clinic, not a diet program or generic funnel.

Layout:

- Left: headline, subhead, two CTAs, small eligibility note.
- Right: app/care-team visual, patient dashboard style crop, or calm clinician
  support image from approved assets.
- A slim trust row below the hero.

Draft copy:

Headline:

```text
Virtual care for chronic conditions, built around medical support and personalized nutrition.
```

Subhead:

```text
Revero pairs licensed medical providers, health coaches, remote monitoring, and a nutrition plan tailored to eligible patients.
```

Primary CTA:

```text
Get started
```

Secondary CTA:

```text
Book a free info call
```

Eligibility note:

```text
Eligibility, condition scope, labs, and device needs are confirmed during onboarding.
```

Do not use in hero:

- "reverse chronic disease"
- "heal autoimmune symptoms"
- "get off meds"
- specific weight loss or blood-pressure outcomes

### Section 2: Trust Strip

Goal: replace hype with concrete care-model signals.

Items:

- Licensed medical providers
- Health coaching
- Remote monitoring
- Personalized nutrition therapy
- Secure app-based care

Copy should remain factual and avoid outcome claims.

### Section 3: Who It Helps

Goal: show condition fit without overpromising treatment scope.

Layout:

- 2-column section with category cards.
- Categories are grouped, not a giant wall of conditions.

Draft structure:

- Metabolic health: type 2 diabetes, prediabetes, hypertension, obesity.
- Inflammatory and autoimmune support: use guarded language until condition list
  is approved.
- Digestive and skin concerns: only include if currently active and approved.

Required note:

```text
Program fit depends on medical history, current medications, state availability, and provider review.
```

### Section 4: How Care Works

Goal: make the model understandable and reduce anxiety.

Four steps:

1. Enroll and complete health forms.
2. Complete labs and provider onboarding.
3. Receive a personalized nutrition and care plan.
4. Use the app for monitoring, coaching, and provider support.

Draft copy must avoid claiming instant access or guaranteed outcomes.

CTA after section:

```text
See how it works
```

Destination: `/how-it-works`

### Section 5: Care Team And App

Goal: explain what "smart clinic in your pocket" means in a more trustworthy
way.

Content:

- Providers review health history, labs, biomarkers, and goals.
- Coaches support implementation and help patients stay consistent.
- Connected devices may be used for eligible patients.
- Medication needs may be reviewed within Revero's treatment scope.

Safe copy:

```text
The app gives patients a place to log progress, message the care team, and share biomarker data between visits.
```

Needs sign-off:

- real-time alert wording
- medication reduction language
- device eligibility and device pricing

### Section 6: Proof, Carefully

Goal: use testimonials without turning them into unsupported brand claims.

Recommended first preview:

- Use a proof section titled "Member experiences" or "What members say about
  the care team."
- Start with support/process testimonials, not the highest-risk outcome claims.
- Hold weight loss, medication, autoimmune, migraine, pain, and blood-pressure
  outcome testimonials until approved.

Preview-safe copy:

```text
Members often describe the value of having a care team that is responsive, encouraging, and familiar with their plan.
```

If using real testimonial cards:

- Use exact approved quotes only.
- Add "Individual results vary" if required by client/legal.
- Do not paraphrase results.

### Section 7: Membership Summary

Goal: answer cost questions without creating pricing liability on the homepage.

Include:

- Self-pay program.
- Medical care within Revero's defined treatment scope.
- Medications, labs in some states, and connected devices may be separate.
- HSA/FSA language only if current and approved.

Draft copy:

```text
Revero is a self-pay program. Membership details, device needs, lab requirements, and eligibility are confirmed during enrollment.
```

CTA:

```text
View membership details
```

Destination: `/membership`

### Section 8: Clinical Credibility

Goal: make the founder and clinical leadership credible without turning the
page into a personality brand.

Possible content:

- Short "Founded by..." card.
- Clinical leadership card.
- Link to Research or For Providers.

Do not overuse:

- "revolutionary treatment"
- founder personal healing story as proof of general patient outcomes

### Section 9: FAQ Preview

Goal: route sensitive details into an appropriate place.

Include 4 questions:

- Is Revero covered by insurance?
- Who is eligible?
- What happens after I enroll?
- How are medications handled?

Each answer should be short and link to FAQ for the full details.

### Section 10: Final CTA

Goal: restate the two-path conversion choice.

Headline:

```text
Ready to see if Revero is a fit?
```

Buttons:

- Get started
- Book a free info call

Support utility:

- Call `(415) 835-4151`

## Navigation

Recommended nav:

- How it works
- What we treat
- Membership
- Success stories
- FAQ
- Login
- Get started

Optional secondary/footer:

- About
- Research
- For providers
- Blog
- Support
- Careers
- Terms
- Privacy

Avoid:

- Duplicate nav sets with different labels.
- "Join Now," "Get Started," "Sign Up," and "Sign Up For Revero" all on the
  same page. Pick one primary label.

## Visual System

Use Revero's existing blue/white clinical base, but make it calmer:

- deep navy for text
- bright blue for primary actions
- pale blue and white surfaces
- one warm human accent if needed
- more whitespace
- fewer rounded pill clusters
- restrained cards
- clean icons only where they clarify the care model

Typography:

- one modern sans-serif system
- one H1 only
- section H2s with clear hierarchy
- no giant all-caps claims

## HTML Preview Requirements

Before building:

- Use only claims allowed by `audit/claims-matrix.md`.
- Keep testimonials generic or approved-only.
- Keep app/onboarding/support links external.
- Include desktop and mobile responsive layout.
- Include comments for placeholders requiring client approval.
- No audit annotations visible on the page.

Output path when built:

`projects/revero-website-refresh/mockups/homepage-preview.html`

## Open Questions Before Client Proposal

- Is the current funnel platform required for paid acquisition?
- Does Revero want Webflow, or does marketing need to stay in ClickFunnels?
- Which condition categories are live and actively enrollable?
- Which testimonials have documented consent and required disclaimers?
- Are HSA/FSA, device costs, refund rules, and lab-state rules current?
- What conversion path matters most from Google paid traffic?
