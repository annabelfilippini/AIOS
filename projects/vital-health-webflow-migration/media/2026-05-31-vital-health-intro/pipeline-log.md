# Pipeline Log — vh-intro-carousel — 2026-05-31

Runner: claude. Namespace: `claude/` (separate from Codex runs).

## Phase 0 — Inspo merge (mkt-visual-identity, Update mode)

- Read existing `brand_context/visual-identity/tokens.json` + `identity.md` + `moves.md`.
- Annabel provided 5 inspo refs in chat (Oura, Function, Bloom, Solawave, Plunge). Chose written-analysis path over file drop.
- Wrote structured analysis to `brand_context/visual-identity/_refs/inspo-notes.md`.
- Appended 8 new moves to `moves.md`: carousel-hero-human-touch, carousel-artifact-ui, carousel-patient-quote, carousel-credential-trust, carousel-loud-stat, carousel-signoff-cta, one-micro-rule-per-slide, carousel-layout-diversity.
- Appended 3 avoids to `tokens.json > style.avoid`: identical-layout, condensed-sans stat headlines, promo pricing chips.
- Updated `identity.md > Social Carousel Direction` with the 6-role rhythm.
- Wrote merge summary to `_analysis/2026-05-31-inspo-merge.md`.
- Locked fields not touched. Logos/fonts not regenerated. Brand-book PDF regen skipped (intentional, not blocking).
- **Reasoning**: targeted Update mode satisfies Rule "Manual user input always wins" — extracted signals from refs without overwriting brand decisions Annabel locked earlier.

## Phase 1 — Arc selection

- Drafted 3 arcs (Meet the practice / Integrative explained / First visit demystified).
- Annabel picked custom direction: "intro carousel about what to expect working with us. Generate new images, don't pull from website."
- Synthesized final 6-slide arc anchored to the 6-role rhythm. Hero + sign-off mirror each other.
- **Reasoning**: arc B/C educational angles were rejected because Vital Health has zero existing posts — the first ad must establish identity, not teach functional medicine concepts.

## Phase 2 — Pipeline blocker + pivot

- Loaded `00-social-content` skill, hit Phase 1 hard gate: `tokens.json` ✅ but `brand_context/templates/instagram-carousel/manifest.json` has 4 entries all `status: "pilot"` and ZERO `template.html` files on disk. `composition-primitives.json` missing.
- Decision tree: (a) run `mkt-visual-identity` Phase 4.95–5 to build real templates (30-60 min, multi-Agent flow), OR (b) pivot to direct image gen + hand-authored HTML composite.
- Annabel chose pivot; also asked for `claude/` namespace to isolate from Codex runs.
- Set up folder structure: `projects/00-social-content/claude/2026-05-31/vh-intro-carousel/{raw,slides,images,_workdir}/`.
- **Reasoning**: the pipeline's template factory is itself heavy. For a first artifact, hand-authoring 6 minimal templates from the locked tokens is faster and Annabel can iterate per-slide afterward.

## Phase 3 — Environment fixes

- `uv` not installed → created Python 3.14 venv at `_workdir/venv` + pip install openai, python-dotenv, playwright.
- First image-gen attempt: `python-dotenv` parse failed silently because line 2 of `.env` smashed `WEBFLOW_API_TOKEN="..."FIRECRAWL_API_KEY=` without a newline. All 13 API keys then read as empty.
- Surfaced blocker to Annabel; she fixed `.env` and confirmed go.
- Re-launched 6 image gens with explicit `--api-key` (not relying on dotenv path).

## Phase 4 — Image generation (gpt-image-1 via viz-image-gen)

- 6 parallel background processes, each 1024×1536 / quality high.
- All 6 returned successfully. File sizes 2.3–3.1 MB each.
- Spot-checked all 6 against the slide brief: no faces, no readable text, cream + forest + gold palette, documentary still-life mood.
- s4 (diagnostics) rendered slightly moodier/darker than briefed — kept (reads on-brand as a "diagnostic depth" cue, not a defect).
- **Reasoning**: parallel gen saves wall time. Slide-6 mirror composition validated against slide-1 by visual inspection; both share the leather-notebook + leafy shadow signature.

## Phase 5 — Slide compositing (Playwright HTML → PNG)

- Hand-authored 6 slide HTML templates in `_workdir/render_slides.py` consuming brand tokens (Fraunces serif, cream/forest/gold, masthead, gold rules, hummingbird logo on slide 6).
- Layout diversity check: full-bleed-centered (1, 3, 6), split-left-text (2), split-with-vertical-rule (4), full-bleed-loud (5). No two slides share a layout — satisfies `carousel-layout-diversity` move.
- Embedded each AI photo as base64 data URI into the slide HTML so each `.html` is self-contained.
- Rendered to 6 × 1080×1350 PNGs via headless Chromium.
- All 6 verified at 1080×1350 via `sips`.

## Phase 6 — Review HTML + Desktop drop

- Generated `review.html` (12 MB self-contained, all 6 slides embedded base64).
- Layout: brand masthead, Fraunces headline, summary cards, 2-column grid of all 6 slides with per-slide move + note, suggested caption, footer.
- Copied to `~/Desktop/vh-intro-carousel-review.html`.

## Phase 7 — Output written

- `post.yaml` with caption + slide metadata.
- `pipeline-log.md` (this file).
- `plan.md` (slide-by-slide brief + image prompts) authored at Phase 1.

## Known issues (for next iteration)

- Slide 1 + slide 6: vertical gold micro-rule between the two headline lines renders thin against the dark photo veil. Consider widening to 2px or brightening accent.
- Slide 3: italic subline ("Long enough to actually hear your story") is small relative to canvas — could bump to 32–36px.
- s4 background is darker than the rest of the carousel — visually distinct but reads slightly differently. Could re-gen with brighter window light if Annabel prefers tighter color cohesion across all 6.
- Brand-book PDF (`mkt-visual-identity` Phase 6) not regenerated. Should be run if `moves.md` / `identity.md` changes are kept.

## Cost

- 6 × gpt-image-1 high quality at 1024×1536 ≈ $0.36–0.50 total.
- Playwright + venv install: free, one-time.

## Next steps Annabel can take

1. Open `~/Desktop/vh-intro-carousel-review.html` in browser → review all 6 slides.
2. Reply with per-slide edits (text changes, layout swap, regen one photo).
3. Approve → I'll write the actual `00-social-content` template pool from these slides so future posts can be generated through the real pipeline (not the pivot).

---

# Feedback Log — what worked, what didn't (live diary)

The purpose of this section is to be a per-version record of EXACTLY what Annabel
said worked and didn't, so the next session (and the eventual reusable skill for
peptide / health brands) can avoid re-learning the same corrections. Annabel's
words are quoted verbatim wherever possible.

## v1 — initial 6 slides (golden-hour, hands+notebook, paper on 4 slides)

**Approved:**
- The overall photographic style: cream + forest + gold, documentary still-life, brand chrome with masthead + gold rules + hummingbird.
- The 6-role arc structure (hero / philosophy / first visit / diagnostics / loud / signoff).
- The Claude-namespaced output folder (`projects/00-social-content/claude/...`) to keep separate from Codex runs.

**Asked to change** (Annabel's words):
- *"i like the card/paper idea but it is brought up in too many slides, just keep it to one slide"*
- *"maybe include people in an image or two?"*
- *"the notebook - hand idea doesnt make a lot of sense"*
- *"this overall vibe is kind of sad. vital ehalth is preventative so i want this to have more of a positive, uplifitng vibe"*

**Interpretation → action for v2:**
- Paper/card kept on slide 3 only (the intake/first-consult slide where it makes narrative sense).
- Notebook dropped from all 6 slides.
- People (back-only, no faces — confirmed via popup) added to slides 1, 5, 6.
- Shifted tone from intimate golden-hour to bright morning light. Cut sprigs → growing plants. Static still-life → movement and outdoor space on the lifestyle slides.

## v2 — bright preventive tone, people back-only

**Approved:**
- *"this looks good"*
- The bright/uplifting tone shift across the whole carousel.
- People framed from behind, no faces (the "no identifying faces" rule).
- The growing-herbs-on-a-windowsill move for slide 2 (vs the v1 cut eucalyptus + journal).

**Asked to change** (Annabel's words):
- *"make sure you include men too, maybe replace one of the girls for a boy a little bit older"*
- *"the words dont make much sense. id like you to pay a bit more attention to the story outlined on the website a bit more"*
- *"vital health is more functional medicine and it is preventative so its more like about catching illness before it becomes a big issue. julie is an x er doctor so she saw a lot of ppl come in to the er because something went wrong that could have been prevented so i want to make sure we share that a bit more accurately. this is outlined in the website so you should already know that."*

**Interpretation → action for v3:**
- Read `snapshot/about.html`, `brand_context/positioning.md`, `brand_context/voice-profile.md` BEFORE drafting any new copy.
- Rewrote all 6 headlines + sublines anchored to the actual website language: Dr. Swett's ER → prevention origin, 90-min first visit, four-sets-of-eyes diagnostics, free 30-min call as the CTA.
- Replaced slide 5 woman with an older man (early 60s, salt-and-pepper) walking through Austin wildflowers toward the downtown skyline.

**Generalized rule learned**: never draft carousel copy from generic "functional medicine" / "wellness" vocabulary. Always pull the brand's actual website + positioning + voice samples first. The brand's real founder story + real numbers + real CTA language outperforms any generic copy.

## v3 — website-anchored copy, older man added

**Approved:**
- *"that looks good"*
- The new copy across all 6 slides (Dr. Swett's ER story → preventable framing → 90 min → measurement-takes-weeks → relationship → free 30-min call).
- The older man on slide 5.

**Asked to change** (Annabel's words):
- *"the austin tex. intregative medicine header and tag line is twice on the first and last post"* — the duplicate-masthead bug on slides 1 and 6 (top "AUSTIN, TEXAS · INTEGRATIVE MEDICINE · EST. 2010" and bottom subline "VITAL HEALTH · INTEGRATIVE MEDICINE · AUSTIN" were saying nearly the same thing).
- *"i also want you to switch up word sizing and placement on the pictures"*
- *"there are a lot of headers with subheaders and i really want you to be whimsical and make it look like vital health curated each post indivisually"*

**Interpretation → action for v4:**
- Dropped the top masthead AND the bottom duplicate subline on slides 1 and 6. Replaced with single non-redundant chrome elements.
- Rewrote each of the 6 slide HTMLs with a different layout architecture:
  - Slide 1: bottom-left anchored 3-line headline, italic "catches it" for whimsy
  - Slide 2: magazine "01 · Why Vital Health" kicker + italic gold numeral + oversized italic display "preventable."
  - Slide 3: oversized italic display "Ninety." upper-left + smaller serif coda + bottom sub-block
  - Slide 4: photo flipped to LEFT (asymmetry vs slide 2's photo-right) + "03" kicker + italic display "weeks."
  - Slide 5: pull-quote treatment — italic gold quotation mark + italic forest quote + gold rule + "THE HOUSE STYLE OF VITAL HEALTH" attribution. No masthead.
  - Slide 6: italic salute "Begin here." + kicker + huge italic "Free." + URL only (stripped "· Austin, TX" duplicate). Hummingbird stays.

**Generalized rule learned**: same chrome rhythm + same header+subheader formula on every slide reads as templated. "Whimsical and individually curated" = vary chapter kickers, oversized display words (one per slide), pull-quote treatments, asymmetric photo placement, mixed alignment. Do not duplicate brand identifier strings across chrome and subline.

## v4 — varied architecture, magazine treatment (current)

**Pending Annabel's review.** This is the version on Desktop now.

Hypotheses to validate at v4 review:
- Does the layout variation feel "whimsical and individually curated" without losing visual cohesion?
- Is the oversized italic display word move (preventable. / Ninety. / weeks. / Free.) carrying its weight on all 4 slides, or does one of them feel forced?
- Is the pull-quote on slide 5 strong enough to be the carousel's emotional peak?
- Is the new arc legible: hero → why → first visit → measurement → relationship → CTA?

## Working principles to carry into the next health-brand carousel

1. **Read the website FIRST.** Borrow the founder's actual story, real numbers, real CTA language. Generic functional-medicine talk loses every time.
2. **Preventive brand → bright, growing, moving.** Reserve intimate-stillness for chronic/therapy brands.
3. **One motif per carousel.** If the brand has an intake form / supplement / device, use it on ONE slide as proof, never as repeated decoration.
4. **Mix patient gender and age.** At least one older patient (50s+) is mandatory for any preventive-medicine brand because the ICP skews older.
5. **No duplicate identifier strings.** If the masthead carries brand + city, the subline doesn't say brand + city again.
6. **Vary the chrome architecture per slide.** Same formula on every slide = dead. Use numbered chapters, oversized display words, pull-quote treatments, asymmetric layouts.
7. **Whimsy = italic Fraunces + asymmetric placement + gold accents.** Not hand-drawn, not playful illustration. The brand's serif italic IS the whimsy.
8. **Real CTA, not generic CTA.** "Book your first consult" loses to "Start with a free thirty-minute call" because the second is the brand's real low-friction first step.
