# Annabel's Carousel Style — Universal Rules

Layer 1 of 3 in the carousel style stack. **Read top to bottom before any copy, photo prompt, or layout decision.**

The three layers:

| Layer | File | Holds |
| --- | --- | --- |
| **1. Universal style** (this file) | `skills/instagram-carousel/references/style.md` | Annabel's invariants — apply to every brand, every carousel type |
| 2. Brand character | `<project>/media/brand_context/voice-profile.md` + `visual-identity/tokens.json` | Who the brand IS — voice, palette, fonts, logo. Produced by foundation skills or auto-discovery. |
| 3. Brand direction | `<project>/media/brand_context/carousel-direction.md` | What Annabel wants THIS brand's carousels to do, beyond what brand_context already says |

The renderer merges in that order; later layers override earlier on conflicts. So your universal "no em-dashes" never gets overridden by a brand, but a brand's "use chiaroscuro" overrides the default preventive=bright modifier.

Every entry below is something Annabel corrected on a past run. The `listen-for-corrections.sh` hook auto-appends new entries here (or to layer 3 if the correction names a specific brand).

**Entry format:**

```text
- [YYYY-MM-DD] <rule, one sentence, imperative>
  Source: <where it came from>
  Quote: "<verbatim words, if captured>"
  Applies to: <all | intro carousels | health brands | etc.>
```

---

## Typography

- **[2026-05-31] Vary the display serif on ~2 of 6 slides with a close cousin.** Pair Fraunces with Cormorant Garamond italic. Default: alt serif on slides 3 and 5. Same brand, different register. Never radically different faces.
  Source: v4→v5 correction
  Quote: "the font is the same on each slide. I think we should change that on a few slides. similar font just not the exact same."
  Applies to: all

- **[2026-05-31] Body sans stays constant across all slides.** Inter on every slide. The utility font is connective tissue, not a place to play.
  Source: derived from v4→v5 font variety correction
  Applies to: all

- **[2026-05-31] No em-dashes, en-dashes, or double-hyphens in any copy.** Use commas, periods, or separate sentences.
  Source: Annabel's global voice rule (`~/.claude/CLAUDE.md`)
  Applies to: all

- **[2026-05-31] Whimsy = italic serif + asymmetric placement + accent color.** NOT hand-drawn, NOT playful illustration. The brand's serif italic IS the whimsy.
  Source: v3→v4 correction
  Quote: "i really want you to be whimsical and make it look like vital health curated each post indivisually"
  Applies to: all

## Photography

- **[2026-05-31] Documentary still-life vocabulary.** Real materials in natural light. Reads editorial, not stock. Specific materials adapt to the brand's palette (see `<project>/media/brand_context/visual-identity/tokens.json`).
  Source: v3 worked-well baseline
  Applies to: all

- **[2026-05-31] ONE motif per carousel.** If the brand has an intake form, supplement, or device, show it on ONE slide as proof. Never as repeated decoration.
  Source: v1→v2 correction
  Quote: "i like the card/paper idea but it is brought up in too many slides, just keep it to one slide"
  Applies to: all

- **[2026-05-31] AI photo prompts ALWAYS include "no faces, no readable text, no logos, no watermarks."** gpt-image-1 will invent gibberish labels and generic faces otherwise.
  Source: every version
  Applies to: all

- **[2026-05-31] AI prompt vocabulary: documentary-photography keywords only.** Open with: natural light, editorial, candid, real-world, slice-of-life. NEVER use: cinematic, epic, 8k, masterpiece, hyper-realistic, ultra-detailed, award-winning.
  Source: 00-social-content Rule 12 (proven across many runs)
  Applies to: all

- **[2026-06-03] can you delete this part and just put vital health instagram as the header with a hummingbird - Medicine that catches it before it catches you.**
  Source: hook (UserPromptSubmit) — cwd: /Users/annabelfilippini/Documents/AI-OS/projects/vital-health-webflow-migration
  Quote: "can you delete this part and just put vital health instagram as the header with a hummingbird - Medicine that catches it before it catches you. Six slides for the first Instagram intro carousel — Vital Health’s preventive thesis, Dr. Swett’s ER-to-prevention story, the…"
  Applies to: all (recategorize next run if wrong)

## Copy

- **[2026-05-31] NEVER draft copy from generic vocabulary.** Read the brand's actual website, `snapshot/about.html`, `positioning.md`, and `voice-profile.md` BEFORE writing a single headline. Borrow founder story, real numbers, real CTA language verbatim.
  Source: v2→v3 correction
  Quote: "the words dont make much sense. id like you to pay a bit more attention to the story outlined on the website a bit more"
  Applies to: all

- **[2026-05-31] If the brand website is missing, STOP and ask for the founder origin story before continuing.** Generic copy loses every time.
  Source: derived from v2→v3
  Applies to: all

- **[2026-05-31] No claim words.** Banned: miracle, cure, guaranteed, reverse, melt, biohack, optimize-your-X.
  Source: v3 worked-well baseline + global voice
  Applies to: all (especially regulated categories: medical, supplements, financial, legal)

- **[2026-05-31] Quiet confidence > hype.** Short sentences. Plain words. No taglines, no marketing-speak.
  Source: Annabel's global voice rule
  Applies to: all

- **[2026-05-31] CTA uses the brand's real low-friction offer, NOT generic "book your first consult."** Pull the actual language from the brand's website. ("Free thirty-minute call" beats "Book your appointment" because it's the brand's actual on-ramp.)
  Source: v3 worked-well + Working principles
  Applies to: all

- **[2026-05-31] No chapter-kicker meta-labels** ("01 · Why X", "02 · How we measure"). They make a short carousel feel like a brochure TOC.
  Source: v4→v5 correction
  Quote: "I don't love the 1. why vital health, 2. etc etc."
  Applies to: intro carousels

- **[2026-05-31] No fake pull-quote attributions** ("The house style of X", "The X way"). Either attribute to the founder by name (if it's truly her voice) or drop the attribution entirely.
  Source: v4→v5 correction
  Quote: "the house of vital health on slide 5 doesn't make much sense"
  Applies to: all

## Layout / Composition

- **[2026-05-31] No two slides share the same layout.** Mix full-bleed, split-left, split-right, pull-quote, oversized-display. Carousel diversity is the difference between magazine-feel and brochure-feel.
  Source: v3→v4 correction + Working principles
  Quote: "i also want you to switch up word sizing and placement on the pictures"
  Applies to: all

- **[2026-05-31] One accent micro-rule per slide.** Brand accent color, 1–2px horizontal or vertical line. Centered or under signature. Never decorative pattern — always structural.
  Source: Vital Health visual identity + inspo-notes synthesis
  Applies to: all (when brand has a rule-accent move)

- **[2026-05-31] Brand mark appears on slide 6 ONLY.** Restraint reads as curated; repetition reads as templated.
  Source: v3 worked-well
  Applies to: intro carousels

- **[2026-05-31] No duplicate identifier strings.** If a masthead says brand + city, the subline does NOT say brand + city again. The bottom slot is the URL alone, a salute, or nothing.
  Source: v3→v4 correction
  Quote: "the austin tex. intregative medicine header and tag line is twice on the first and last post"
  Applies to: all

- **[2026-05-31] No masthead string appears on >1 slide.** Identifier strings stay in one place per carousel.
  Source: v3→v4 generalization
  Applies to: all

- **[2026-05-31] Vary photo placement per slide.** Photo-left on one slide, photo-right on another, full-bleed on a third. Same composition rhythm on every slide = templated and dead.
  Source: v3→v4 correction
  Applies to: all

- **[2026-05-31] 1080×1350 (4:5) canvas.** Optimal Instagram carousel aspect. Render at 1024×1536 → composite at 1080×1350.
  Source: v3 worked-well baseline
  Applies to: all

## TEXT-ON-PHOTO LEGIBILITY (highest priority — caught TWICE)

- **[2026-05-31] Any text element <24px on a photographic background WITHOUT a solid plate, dark veil, or guaranteed dark region behind it WILL fail.** Before shipping any slide, audit every text element <24px. If on photo with no plate/veil/dark region: give it one OR delete it. **Default to deletion for secondary copy.**
  Source: v4→v5 correction (caught twice: slide 3 bottom sub AND slide 1 top kicker — same failure mode)
  Quote: "the words on slide 3 at the bottom arent super visable" + "the words at the top of slide 1 also arent super visable so maybe remove them as well and make note that this has been an issue twice in this development"
  Applies to: all
  Enforcement: `scripts/preship_audit.py` blocks ship if any text <24px sits on raw photo

## Voice

- **[2026-05-31] No softening for fluent readers.** Don't paraphrase product names, technical terms, or vocabulary the brand uses natively. The reader knows the words.
  Source: global memory (`feedback_no_softening_for_fluent_readers.md`)
  Applies to: all

- **[2026-05-31] Match Annabel's plainer, direct voice.** Avoid taglines, marketing-speak, overly polished phrasing.
  Source: global CLAUDE.md voice rule
  Applies to: all caption + copy drafting

## Don't do this

- **[2026-05-31] Don't reorder the intro arc.** Hero → Why → First visit → Differentiator → Philosophy → CTA. Drop priority when reducing: 4 → 5 → 3. Slides 1, 2, 6 are non-negotiable.
  Source: v3 worked-well + intro arc lock
  Applies to: intro carousels

- **[2026-05-31] Don't show un-humanized copy.** Always run `tool-humanizer` silently before showing a draft. Carousel humanizer runs inside Phase 5.5 (before slide plan); single/text runs in Phase 6.
  Source: 00-social-content Rule 4 + Rule 5
  Applies to: all

- **[2026-05-31] Don't use generic icons when a real brand logo exists.** If a slide mentions a company, tool, or product (OpenAI, Cursor, Notion, GitHub, Anthropic), render the REAL brand logo. Resolution chain: local commons → Simple Icons → Lobehub → Devicon → user upload. Escalate to Annabel before falling through to a text label.
  Source: 00-social-content Rule 15 (human-feel principle)
  Applies to: all

- **[2026-05-31] Don't write to anywhere except `<project>/media/<date>-<slug>/`.** Enforced by `enforce-media-folder.sh` hook.
  Source: project-wide convention (this skill)
  Applies to: all

- **[2026-06-01] Don't keep brand-specific work in the skill folder.** Past carousels for a specific brand live in that brand's project under `media/<date>-<slug>/`, never in `skills/instagram-carousel/inspiration/`. Inspiration is brand-agnostic only (saved ads + ad-analyses files).
  Source: 2026-06-01 cleanup pass
  Applies to: all

## Category modifiers

These apply when the brand falls into a named category. Layer 3 (brand-direction.md) names the category; this section names the defaults.

- **[Preventive medicine / wellness / longevity brands → BRIGHT.** Default to morning light, growing plants, movement/outdoors, openness. Reserve intimate/moody stillness for chronic-care, hospice, therapy brands.
  Source: v1→v2 correction
  Quote: "this overall vibe is kind of sad. vital ehalth is preventative so i want this to have more of a positive, uplifitng vibe"
  Applies to: preventive medicine, wellness, longevity

- **Preventive-medicine ICP skews older — mix patient gender AND age.** At least one older patient (50s+) is MANDATORY for preventive-medicine brands.
  Source: v2→v3 correction
  Quote: "make sure you include men too, maybe replace one of the girls for a boy a little bit older"
  Applies to: preventive medicine, wellness, longevity

## Working principles (carry across every carousel)

These are the meta-rules — bake them into how the skill operates, not into per-slide checks.

1. **Read the brand website FIRST.** Founder's actual story, real numbers, real CTA. Generic vocabulary loses every time.
2. **Match category mood.** Preventive → bright, growing, moving. Chronic / therapy → intimate stillness. Look up the brand's category before picking a mood.
3. **One motif per carousel.** If there's an intake form / supplement / device, use it on ONE slide as proof, never repeated decoration.
4. **Match ICP demographics.** Older patient (50s+) mandatory for preventive-medicine brands. Adjust for the brand's actual audience.
5. **No duplicate identifier strings.** Masthead carries brand + city → subline doesn't say it again.
6. **Vary chrome architecture per slide.** Numbered chapters, oversized display words, pull-quotes, asymmetric layouts. Same formula every slide = dead.
7. **Whimsy = italic serif + asymmetric placement + accent.** Not hand-drawn.
8. **Real CTA, not generic CTA.** Brand's actual low-friction first step beats "Book your first consult" every time.

## Health-brand category playbook

For brands in health / wellness / preventive medicine, the 5 ads in `inspiration/ad-analyses-health.md` (Oura, Function, Bloom, Solawave, Plunge) yielded six required "moves" that any health intro carousel should hit at least once. Don't repeat any single move twice in the same carousel.

1. **Hero / cover** → human-touch photo + center-stacked serif over micro-rule (Function-style)
2. **Artifact / proof** → real brand UI element (intake form, calendar, sample report) (Oura-style)
3. **Patient quote** → italic serif sentence + signature line on cream or brand-color ground (Bloom-style, restrained)
4. **Credential / trust** → single big serif stat or credential under thin rule (Solawave-style)
5. **One loud slide** → stat or single bold claim on botanical/clinical still-life (Plunge-style, dialed way down)
6. **CTA / sign-off** → mirror of slide 1: human moment + serif + rule + brand's real low-friction offer

Goal: no two slides share a layout template.

---

## Uncategorized

(Hook drops here when keyword match fails. Recategorize next run.)

---

- **[2026-06-03] ok criteria needs to be 3br only please change that everywhere**
  Source: hook (UserPromptSubmit) — cwd: /Users/annabelfilippini/Documents/AI-OS/projects/vital-health-webflow-migration
  Quote: "ok criteria needs to be 3br only please change that everywhere"
  Applies to: all (recategorize next run if wrong)

- **[2026-06-03] ok criteria needs to be 3br only please change that everywhere and re run yesterdays scrape.**
  Source: hook (UserPromptSubmit) — cwd: /Users/annabelfilippini/Documents/AI-OS/projects/vital-health-webflow-migration
  Quote: "ok criteria needs to be 3br only please change that everywhere and re run yesterdays scrape. i want a fully new assessment"
  Applies to: all (recategorize next run if wrong)

## Edit log

- **2026-06-01** — Renamed from `preferences.md` and split into 3-layer architecture (universal style.md + brand_context character + brand carousel-direction.md). Brand-direction entries for Vital Health moved to `projects/vital-health-webflow-migration/media/brand_context/carousel-direction.md`. Hook-noise entries pruned.
- **2026-06-01** — File seeded from Vital Health v1→v5 corrections. Every rule traceable to a verbatim Annabel quote or a generalization explicitly derived from one.
