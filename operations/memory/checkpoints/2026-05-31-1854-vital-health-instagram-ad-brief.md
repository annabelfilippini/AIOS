---
date: 2026-05-31
time: 18:54
project: vital-health-webflow-migration
status: in-progress
next-session: Continue by collecting Annabel's functional health ad references, then build a Vital Health intro carousel creative brief before generating images.
---

# Session: Vital Health Instagram ad brief

## What we worked on

- Slowed down after the rushed Scrapes pilot carousel and clarified the actual ad goal.
- Annabel chose Vital Health as the first test case for a repeatable company-to-Instagram-carousel process.
- Live brand source: `https://vital-health-9bf311.webflow.io/`
- Existing Scrapes/social pipeline remains installed at `projects/vital-health-webflow-migration/.claude/skills/00-social-content`.
- Built a visual HTML concept brief at `projects/vital-health-webflow-migration/projects/00-social-content/2026-05-31/vital-health-intro-carousel-brief/index.html`.
- Revised the same HTML to v2 after Annabel's critique, adding generated images under `projects/vital-health-webflow-migration/projects/00-social-content/2026-05-31/vital-health-intro-carousel-brief/assets/`.
- Revised the HTML to v3 after Annabel's copy critique: preventive/functional medicine framing, Julie's ER-to-prevention lens, and varied copy hierarchy.

## Decisions made

- Use Codex for the image-generation and visual-judgment layer because Vital Health currently lacks enough real imagery.
- Use Scrapes/Claude-style structure as the production pipeline, but only after Codex/Annabel define the creative brief.
- Simone/Scrapes carousel advice to preserve: the carousel should include variety across image types, not six near-identical branded panels.
- First Vital Health carousel is an introduction to the company, not a service-specific hard sell.
- Tone: welcome, warm, calm, credible, "we are glad you are here; here is how we can help."
- Format: Instagram ad carousel, soft-sell enough to feel like organic brand introduction.
- Audience: people who care about internal health, especially middle-aged moms and dads, broadly adults 20-70.
- Visual relationship to site: inspired by and clearly recognizably Vital Health, not an exact website clone.
- Desired CTA: viewer should want to book a consultation.
- Functional health ad references should guide image style, composition, and content rhythm, but Vital Health must avoid miracle/cure/guaranteed outcome language.

## Reference ad learnings

- Function Health-style emotional lifestyle ad: close human crop, warm overlay, sparse centered serif copy, gift/time-with-family emotional frame.
- Bloom-style product still-life ad: bright product color, oversized hook, testimonial proof, food/product props. Useful for energy and composition, but too playful/pink for Vital Health.
- Solawave-style authority ad: single product/device hero with publication quote. Useful proof structure, but Vital Health should avoid borrowed-publication claims unless real.
- Plunge-style bold benefit ad: outdoor product/lifestyle scene with huge block text. Useful for confidence and variety, but medical claims need softer language and disclaimers.
- Natural Cycles/Oura-style interface/object ad: device + app UI, dark premium background, simple benefit. Useful pattern if Vital Health later has lab dashboards or patient portal screenshots.
- RYZE-style offer/product layout: clear product arrangement and price/CTA hierarchy. Park for offers; not right for this welcome intro.
- Oura/Amazon-style hand-held device lifestyle: human touch + technology object + atmospheric background. Useful for making health data feel personal.
- Vital Health carousel should vary image archetypes: emotional family/lifestyle, botanical clinical still-life, consultation/lab notebook scene, service-pillar visual, soft CTA/logo slide.

## Annabel feedback on v1 HTML

- Overall issue: too many slides used the same bordered card treatment and small top labels. Future versions need stronger variation between slides.
- Do not reuse images directly from the Vital Health website. Generate new imagery that matches the Vital Health vibe without copying site assets.
- Slide 1: direction was good, but the hook and image were not strong enough to make someone keep scrolling.
- Slide 2: worst slide. Website image reuse, cut-off words, and generic repeated frame made it look terrible.
- Slide 3: better direction. Annabel liked the notebook concept and copy matching the notebook vibe, but text alignment needs correction.
- Slide 4: liked the concept, but too much white space. Use icons or visual symbols for the services instead of mostly words.
- Slide 5: liked.
- Slide 6: liked, but used the old hummingbird logo. Use the newer logo mark instead.

## Annabel feedback on v2 HTML

- Overall: v2 looks much better visually.
- Copy issue: "Your body has been asking for a longer conversation" is close emotionally but not accurate enough.
- More accurate strategic frame: Vital Health is functional/preventive medicine. The intro carousel should be about catching issues before they become big problems.
- Julie's ER background matters: she saw many people arrive in emergency medicine after something went wrong that could have been prevented. The carousel should reflect this without becoming fear-based.
- "Not a protocol pulled off a shelf" also did not make enough sense as a slide headline.
- Do not make every slide follow header + subheader. Mix copy hierarchy: sometimes big words only, sometimes smaller explanatory text, sometimes one headline, sometimes headline + body.
- Slides should feel individually curated by Vital Health, not like one template repeated six times.

## Open questions

- What specific functional health ads or websites should inspire the imagery?
- Should the carousel lead with the practice identity, patient concern, or consultation experience?
- How many slides should the first intro ad use?
- Should generated imagery be botanical/clinical still-life only, human lifestyle scenes, practitioner/patient scenes, or a mix?
- Does Annabel want a reusable intake form/brief for future companies before any generation begins?
- Which exact mix of image archetypes should the first carousel use?

## Next steps

1. Annabel reviews the HTML concept brief.
2. Build v2 HTML using generated imagery, not website screenshots.
3. Increase slide-to-slide visual variety by changing composition systems, not just copy.
4. Replace the old hummingbird with `logo-options/bird-final-transparent.png` or the newest approved mark.
5. Promote the usable Instagram templates from pilot to ready or create a Scrapes-ready template handoff after Annabel approves a direction.

## Context to preserve

- Brand voice files already exist in `projects/vital-health-webflow-migration/brand_context/`.
- Current brand direction: forest green, cream paper, gold accents, Fraunces + Inter, hummingbird mark, botanical clinical still-life, refined editorial spacing.
- Core copy frame from the site: "Your journey to optimal vitality," "A different kind of integrative care," "Integrative, regenerative, and preventive medicine," "complimentary consultation."
- Best ad posture: relationship-first and invitation-first, not urgency-first or funnel-first.

## System refinement candidates

- For future company-to-social-ad work, require a pre-generation brief (source, objective, audience, CTA, refs, brand + medical constraints, approval boundary).
- Keep the reusable workflow stages: brand extraction → ad strategy → image direction → carousel production.
- What worked in this pass: converting reference ads into image archetypes made the carousel feel varied without losing brand coherence.
- What did not happen yet: the HTML is a concept brief with CSS/brand assets, not final generated ad art.
- V1 mistake to avoid permanently: a carousel brief can still feel generic if every slide shares the same border/header treatment. Variety must be structural.
- V2 changes made: stronger slide 1 hook, generated non-website images for slides 1/2/3/5, denser icon-led service slide, newer bird mark on CTA.
- V2 remaining review need: Annabel should judge whether the generated image style and hook feel scroll-worthy enough before this becomes a Scrapes-ready template direction.
- V3 copy direction: preventive/functional medicine, "upstream" care, quiet signals before urgent problems, Julie's emergency medicine lens, no fear bait.
- V3 design changes: vary copy hierarchy; avoid default header+subheader; slides 1–6 now use the updated preventive copy set.
