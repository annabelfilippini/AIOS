# Revero Claims Matrix

Date: 2026-05-31

Purpose: prevent the redesign from making Revero's health, outcome, pricing, or
availability claims stronger than what has been approved.

Sources reviewed:

- `sources/home.html`
- `sources/about-us.html`
- `sources/membership.html`
- `sources/faq.html`
- Browser QA snapshots from `audit/`

Status legend:

- Keep: likely safe if client confirms wording and source.
- Soften: usable idea, but current wording is too broad or absolute.
- Attribute: keep only as a named testimonial or founder statement.
- Move: remove from hero/primary sales path and place in FAQ, footnote, or
  proof section.
- Hold: do not use in mockup until approved.

## High-Risk Health Claims

| ID | Current claim | Source | What it implies | Risk | Action | Preview-safe wording |
|---|---|---|---|---|---|---|
| H1 | "reverse autoimmune and other chronic diseases" | Home meta description | Disease reversal across broad chronic categories | High | Hold or soften | "care for chronic metabolic and inflammatory conditions" |
| H2 | "root cause treatment for your chronic conditions" | Home hero and site framing | Treats the cause, not just symptoms, across chronic disease | High | Soften | "care designed to address underlying metabolic and nutrition factors" |
| H3 | "Revero is a online medical clinic treating chronic health conditions with personalized medical treatments and precision nutrition" | About | Broad treatment claim | Medium | Keep after copy edit and condition scope confirmation | "Revero is a virtual medical clinic for select chronic conditions, combining medical care with precision nutrition." |
| H4 | "We treat metabolic conditions such as type 2 diabetes, prediabetes, hypertension, and obesity as well as autoimmune and inflammatory conditions" | About | Broad condition availability | High | Hold until current service list is confirmed | "Care for select metabolic conditions, with additional programs depending on eligibility and availability." |
| H5 | "personalized nutrition therapy and clinical protocols are designed to help reduce insulin resistance and inflammation" | About | Physiologic improvement claim | High | Keep only with clinical source/sign-off | "nutrition therapy and clinical protocols tailored to each patient's metabolic profile" |
| H6 | "reduce blood sugar" | Home lower-blood-sugar section | Direct biometric outcome | High | Keep with source/sign-off or soften | "support blood sugar management" |
| H7 | "reduce inflammation" | Home sections | Direct biological outcome across conditions | High | Soften unless sourced | "support a lower-inflammatory nutrition pattern" |
| H8 | "restore gut health" | Home sections | Restorative claim, broad digestive/autoimmune implication | High | Soften | "support digestive health" |
| H9 | "Our protocols are designed to limit the factors that disrupt the GI tract and cause chronic inflammatory and autoimmune responses in the body" | Home | Causal autoimmune mechanism claim | High | Hold | "personalized protocols account for digestive triggers and food tolerance" |
| H10 | "ketogenic nutritional therapy to treat chronic metabolic, autoimmune, and inflammatory conditions" | FAQ | Ketogenic diet as treatment for multiple disease categories | High | Hold or move to clinically reviewed FAQ | "ketogenic or low-carb nutrition therapy may be part of the care plan for eligible patients" |
| H11 | "Nutritional ketosis has been shown to improve inflammation, blood sugar stability, and weight loss" | FAQ | Evidence claim across outcomes | High | Keep only with citation/source | "some patients use nutritional ketosis under medical guidance as part of their care plan" |
| H12 | "A well-formulated ketogenic plan is safe and can improve metabolic health by reducing inflammation" | FAQ | Safety and efficacy claim | High | Hold unless clinician-approved | "a ketogenic plan may be appropriate for some patients under supervision" |

## Medication And Care Claims

| ID | Current claim | Source | What it implies | Risk | Action | Preview-safe wording |
|---|---|---|---|---|---|---|
| M1 | "reducing and often eliminating medications as a patient progresses" | FAQ | Medication discontinuation is common | High | Move to FAQ and approve clinically | "providers review medications and adjust care as clinically appropriate" |
| M2 | "Board-certified providers support, supervise and safely reduce medications" | FAQ | Safety and prescribing claim | High | Keep only if credentialing and protocol confirmed | "licensed providers monitor progress and medication needs" |
| M3 | "Revero providers will manage medications for Revero-treated conditions" | FAQ | Medication management scope | High | Keep with scope definition | "providers may manage medications that fall within Revero's treatment scope" |
| M4 | "Patients may see rapid changes, requiring the need to change medications in response" | FAQ | Rapid physiologic change | High | Move to clinical FAQ | "care plans and medications may need adjustment as progress is monitored" |
| M5 | "Revero's patients don't have to wait long for biomarker review like traditional care" | Membership | Speed guarantee versus traditional care | Medium | Soften | "patients receive ongoing biomarker review through the app and care team" |
| M6 | "Our system monitor daily biomarker data entered in the app by patients on an ongoing basis and alerts the clinicians as needed" | Membership | Real-time monitoring and alert workflow | Medium | Keep after workflow confirmation and copy edit | "the app helps the care team review patient-entered biomarker data between visits" |

## Patient Outcome Testimonials

| ID | Current claim | Source | What it implies | Risk | Action | Preview-safe wording |
|---|---|---|---|---|---|---|
| T1 | "I lost 80 pounds, reversed my blood pressure, eliminated chronic pain, and all I did was follow the food list." | Home testimonial extract | Large weight loss, blood pressure reversal, pain elimination | High | Attribute only with testimonial approval and disclaimer | Use as approved testimonial only. Do not paraphrase into brand claim. |
| T2 | "After years of prescriptions with no relief, Revero healed my autoimmune symptoms, got me off meds, and even stopped my migraines." | Home testimonial extract | Autoimmune healing, medication discontinuation, migraine cessation | High | Attribute only with approval or omit from preview | Use softer proof category until approved. |
| T3 | "I love this program, and any challenges I have, I am able to work through with my care team." | Home hidden/testimonial section | Care team support | Low | Keep if approved | "members describe the care team as responsive and supportive" |
| T4 | "My care team is fabulous! Very responsive and encouraging." | Home hidden/testimonial section | Service quality | Low | Keep if approved | Can be used in proof section if testimonial permissions are confirmed. |

## Pricing, Insurance, Refunds, And Devices

| ID | Current claim | Source | What it implies | Risk | Action | Preview-safe wording |
|---|---|---|---|---|---|---|
| P1 | "Our monthly subscription covers all costs of medical care (excluding medications) within the scope of our treatment with no add-on fees" | Membership | No hidden fees inside medical scope | High | Keep only with current pricing approval | "membership includes medical care within Revero's defined treatment scope. Medications and some outside costs are separate." |
| P2 | "Revero is not covered by insurance" | Membership | Insurance status | Medium | Keep if current | "Revero is a self-pay program." |
| P3 | "accepts FSA/HSA cards" | FAQ | Payment eligibility | Medium | Keep if current | "FSA/HSA cards may be accepted, subject to eligibility." |
| P4 | "Patients with hypertension or diabetes will also be required to purchase a Revero connected blood pressure or blood glucose device ($100 each)" | Membership | Required device cost | High | Keep after pricing confirmation | "some patients may need a connected device. Pricing should be confirmed before launch." |
| P5 | "If ... ineligible for the program, everything paid will be refunded with the exception of $125" | FAQ | Refund policy and provider-time fee | High | Keep exactly only after legal approval | Move to FAQ or checkout flow, not homepage. |
| P6 | "patients who have labs drawn in NJ, NY, and RI must self-pay for labs or contact their insurance provider for possible coverage" | Site footer/FAQ | State-specific lab cost limitation | High | Keep as footnote if current | Keep in legal/FAQ area. Do not hide if pricing is discussed. |

## Availability, Eligibility, And Scope

| ID | Current claim | Source | What it implies | Risk | Action | Preview-safe wording |
|---|---|---|---|---|---|---|
| A1 | "licensed in all 50 states" | About physician bio | Nationwide clinician coverage | Medium | Keep only if current and role-specific | "medical leadership includes clinicians with broad state licensure" |
| A2 | "Revero does not serve patients residing outside the United States" | FAQ | Geographic limitation | Medium | Keep | "available to eligible patients in the United States" |
| A3 | Exclusion list includes type 1 diabetes/LADA, pregnancy, dialysis, advanced heart/liver disease, transplants, and medication limitations | FAQ | Eligibility restrictions | High | Keep in eligibility/FAQ, not homepage | "eligibility depends on medical history and provider review" |
| A4 | Revero does not provide hormone replacement therapy, thyroid medication management, complex psychiatric care, neurological disease management, cardiovascular risk/lipid management, or gout/kidney stone treatment | FAQ | Scope exclusions | High | Keep in FAQ | "some conditions and medication categories remain outside Revero's scope" |
| A5 | "conditions Revero treats" includes metabolic, autoimmune, digestive, skin, musculoskeletal, and other categories in source scripts | Home source metadata | Search and page title claims across many condition pages | High | Audit before SEO rebuild | Use only confirmed active condition list in navigation and homepage. |

## Structural And Schema Claims

| ID | Current claim or artifact | Source | What it implies | Risk | Action | Preview-safe wording |
|---|---|---|---|---|---|---|
| S1 | `MedicalBusiness`, `MedicalTherapy`, and `MedicalProcedure` schema appear on pages | Source structured data | Search engines receive explicit medical entity claims | High | Review schema as part of SEO cleanup | Align schema with actual entity, services, and approved claims. |
| S2 | Recipe schema appears on unrelated public pages | Source structured data | Off-topic schema may confuse search engines | Medium | Remove or scope correctly | Not applicable to homepage preview. |
| S3 | Page meta scripts define many condition resource titles and descriptions | Home source scripts | Dynamic SEO claims across condition pages | High | Audit condition-page SEO before launch | Keep homepage condition language broad until condition list is approved. |

## Mockup Rules From This Matrix

For the first homepage preview:

1. Do not use "reverse disease" language.
2. Do not state that Revero heals, cures, eliminates, or reverses symptoms.
3. Do not use patient outcome numbers in the hero.
4. Do not paraphrase testimonials into brand claims.
5. Use "support," "help manage," "clinician-supervised," and "eligible patients"
   where exact clinical scope is unconfirmed.
6. Keep pricing simple and guarded. Link detailed pricing to Membership.
7. Include an eligibility and sign-off note in the internal handoff.
8. Keep onboarding, app, support, payment, lab, and device workflows as external
   systems unless Revero explicitly asks for those to change.
