---
date: 2026-06-08
time: 21:08
project: vital-health-instagram-design
status: shipped
next-session: Use the 3-slide blueprint and the v2 voice patterns to draft the next informational post (likely Labs, Menopause, or Regenerative). When ready, also build a Vital Health Cowork skill that wraps the blueprint + research protocol so the practice team can run it themselves.
published-to: https://vital-health-hormone-carousel.vercel.app/ (Peptides tab added live)
---

# Session: Informational post blueprint + peptide v2 carousel

## What happened

- Annabel asked for more specific guidelines for Vital Health informational Instagram posts, modeled on the 2026-06-07 hormone optimization carousel. Goal: make the design system tight enough to drive a future Vital Health Cowork skill.
- Reverse-engineered the hormone post's structure into a written blueprint, ran the peptide post as the first test of it, found the v1 wording was awkward, rewrote with voice patterns Annabel approved, deployed live.
- Two real artifacts landed: (1) a much stronger `media/design.md` section that the future skill can lean on; (2) a peptide carousel live on the existing tabbed review site.

## Decisions

- **The 3-slide structure is the default for informational posts**, not the 4-slide hormone structure. Order: Positioning → Definition → Protocols + CTA. The 4-slide form (with Lens A / Lens B middle slides) is preserved as a variant for topics that genuinely split by demographic or phase, e.g. hormones (Women / Men) or menopause (Perimenopause / Post-menopause).
- **Slide 1 always opens on the deep forest leaf field**, regardless of the topic's theme kit. This is a feed-level convention so a scroller reads "Vital Health service" before they read the topic. Topic theme kit takes over on Slide 2 onward.
- **Slide 1 leads with the practice's posture, not symptoms.** Pattern: "At Vital Health, [topic] is [posture word]. We [what we do first], then [what we decide based on]." The old "If you are struggling with…" pattern is banned from the positioning slide and lives only in the caption.
- **Slide 2 is a definition slide, period.** Two careful sentences that walk from physical definition to clinical relevance. No claims about Vital Health, no CTA, no questions.
- **Slide 3 chips are two-line** (protocol name in Fraunces + one careful sentence in Inter underneath). The previous single-line chips with terracotta number prefixes are deprecated. Each description leads with an epistemic verb chosen by claim strength.
- **Epistemic verb ladder** (strongest to softest):
  - "Studied for…" — peer-reviewed evidence.
  - "Considered for…" — clinically appropriate in select patients.
  - "Discussed for…" — comes up in conversation, off-label or emerging.
  - "Often part of conversations around…" — patient-initiated.
  - "Used in… programs" — already part of a Vital Health offering.
  - "Tied to…" — mechanism only, not yet a recommendation.
- **"Vital Health can help." moved off the slide and into the caption.** It was previously the italic close line on the cover; it now closes paragraph 3 of the caption.
- **Research protocol order:** Vital Health's own page first via Firecrawl, then the trusted-source allowlist (Mayo, Cleveland Clinic, NIH/NIA, Endocrine Society, ACOG, Menopause Society, AHA, PubMed for stats only). Any claim not traceable to those gets rewritten as "may be considered" / "guided by labs and clinical picture" / "when clinically appropriate" or dropped.
- **The live Vital Health page voice is the floor, not the ceiling.** The page uses "Are you dealing with…" infomercial framing. The carousel does not. Any claim or framing the live page makes that wouldn't survive the brand carousel voice gets softened.

## Files touched

- `projects/websites/vital-health-review/media/design.md` — Informational Post Blueprint restructured into five parts (A. 3-slide template / B. copy voice patterns / C. research protocol / D. operator input / E. 4-slide variant). Hormone post moved to Part E. Voice patterns (declarative headlines, practice-first opener, epistemic verbs, banned openings) added as Part B. The older "Proven Carousel Pattern" section was relabeled "Carousel Length Variants" so the 5-slide and 7–8 slide arcs are clearly secondary to the 3-slide default. A "Photography Direction" section was added earlier in the session, capturing the mood-board reference Annabel shared.
- `projects/websites/vital-health-review/media/2026-06-08-peptide-therapy-blueprint/` — new folder, contains `post.md` (v2), `index.html` (v2), `render.mjs` (3-slide loop), `slide-1.png` through `slide-3.png`, plus `node_modules/playwright` for the renderer.
- `projects/websites/vital-health-review/client-share/vital-health-hormone-carousel/index.html` — Peptides tab added between Hormone Optimization and Moving Announcement. Header copy updated.
- `projects/websites/vital-health-review/client-share/vital-health-hormone-carousel/peptides/` — slide-1.png, slide-2.png, slide-3.png copies for the tabbed site.

## Deployments

- `vercel --prod --yes` from `client-share/vital-health-hormone-carousel/`.
- Production URL: <https://vital-health-hormone-carousel.vercel.app/> (Peptides tab now live).
- Deployment ID: `dpl_EjkoBFdMFZDUDL4m1neTxpYGSDRV`.

## Open questions

- Should the Slide 2 definition slide stay on the same forest field as Slide 1, or shift to the topic theme kit's field (e.g. cream + amber-glass for peptides)? Currently both are forest so Slides 1 and 2 read as a pair. Annabel approved this look but flagged that "Slide 2 could look a little bit different." Worth A/B-ing on the next post.
- Optional gold rule under the Slide 3 headline: marked optional in design.md. Was used on the peptide v2. Should it be mandatory? Defer until two more posts ship.
- The eventual Vital Health Cowork skill: what is the operator's input surface? Today it's topic name + positioning angle + URL + variant choice. After two more posts that input list should be stress-tested by handing it to someone who isn't Annabel.

## Next steps

- Use the blueprint to draft the next informational post (Annabel to pick the topic, likely Labs / Menopause / Regenerative).
- After 2 to 3 more posts, package the blueprint + research protocol + render harness as a Vital Health Cowork skill. The skill should accept the operator input from Part D of the blueprint and walk the research protocol automatically.
- Revisit the Slide 2 field question once another topic has been built — peptides alone is not enough signal.

## Sources surfaced this session

- Vital Health live peptides page: <https://www.vitalhealthim.com/peptides> — used for practice voice and peptide coverage list. Read but softened.
- NIH StatPearls "Biochemistry, Peptide": <https://www.ncbi.nlm.nih.gov/books/NBK562260/> — definition source.
- NIH NHGRI Genome glossary: <https://www.genome.gov/genetics-glossary/Peptide> — corroborating definition.
- PMC8844085 "Therapeutic Peptides: Current Applications and Future Directions" — selectivity framing on Slide 2.
- FDA Human Drug Compounding pages — regulatory backdrop, informs "only considered when clinically supported" framing.
- Cleveland Clinic and Mayo Clinic searched but had no generic peptide-therapy explainer pages; logged in `post.md` so future drafts skip them for this topic.
