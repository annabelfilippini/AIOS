# Vital Health Media Design

My (Claude's) rulebook for making Vital Health Instagram posts. Read this before drafting copy, choosing a layout, or rendering slides. The rules here are project-specific and override `skills/instagram-carousel/references/style.md` on conflict.

The point of this file is consistency: every Vital Health post should look like it came from the same practice, even when the topic changes. Cover slides may feel cinematic. Info slides should feel like a uniform system that carries the cover's theme.

## Brand Feeling

Vital Health should feel calm, clinical, warm, and quietly premium. The posts should read like they were made by a careful integrative medical practice, not a medspa, supplement brand, or wellness influencer.

The strongest direction so far:

- Cream paper, forest green, soft sage, and restrained gold.
- For Instagram, do not let it become too quiet. Use at least 3 image-led slides or rich visual texture moments in an 8-slide carousel.
- Add warmth with small terracotta, pale peach, or honey accents when the post needs more life.
- Big editorial serif headlines with a few italic moments.
- Inter or a similar clean sans for all body copy.
- Plenty of empty space. Do not fill every inch.
- Fine gold rules as structure, not decoration.
- Botanical and clinical cues, used lightly.
- Educational copy that sounds like a provider talking carefully to a patient.

## Visual System

Core colors:

- Forest: `#1f4d2a`
- Deep forest: `#12351e`
- Cream: `#f5efe0`
- Paper: `#fbf7ec`
- Sage: `#dce5d5`
- Gold: `#c9a04a`
- Warm terracotta accent: `#c77a4a`
- Pale peach accent: `#e9c8aa`
- Ink: `#2a2a26`
- Muted body text: `#676359`

Typography:

- Display serif: Fraunces.
- Alternate display serif: Cormorant Garamond italic, used on 2 or 3 slides per carousel.
- Body sans: Inter.
- Do not change the body font across slides.
- Do not use condensed stat fonts, script fonts, or trendy wellness typography.

Layout:

- 1080 by 1350 for portrait carousels. 1080 by 1080 for square posts.
- Vary slide architecture. Mix full-bleed color, split panels, grids, quote-like slides, and table-like slides.
- For educational carousels, treat the first slide like an Instagram cover, not a report cover. It needs an image or rich texture behind the main thesis.
- Use image bands, split image panels, or photographic proof moments to break up dense educational copy.
- Use one gold rule per slide.
- Avoid repeated mastheads.
- Small text should sit on solid cream, paper, or a dark veil. Do not place small text directly over a busy image.

## Hummingbird Mark

The hummingbird is the only Vital Health brand mark on a post. Do not use text wordmarks, fake VH lockups, or the practice name as a logo. The mark is locked in size, position, color, and style across every slide of a single post — and the same way of choosing color and size applies to every post Vital Health publishes, current and future.

### Asset

- **Filled silhouette, not an outline.** The hummingbird is a solid shape filled with one color. Outline / line-drawing versions of the bird are not used. The earlier `vh-bird-logo.png` in this repo is an outline and is the wrong asset.
- Two canonical PNG variants live at the root of `projects/websites/vital-health-review/media/`:
  - `vh-bird-white.png` — filled silhouette in cream/paper (`#fbf7ec`). Use on dark-dominated posts.
  - `vh-bird-forest.png` — filled silhouette in forest green (`#1f4d2a`). Use on light-dominated posts.
- Transparent background, square aspect, no halo, no circle, no chip.
- Both were derived from the original `vh-bird-logo.png` outline via flood-fill (interior enclosed region filled solid). Logo shape is preserved exactly. The outline PNG is retired for slide use; keep it only as the source for re-generating tinted variants.

### Color

- **Default: one color per post**, locked across all slides of that post. Pick the color at the post level based on what reads against the post's dominant backgrounds:
  - **White bird** when the post is dominated by dark forest, deep forest, ink, or any palette where a green bird would blend in. Example: the hormone optimization carousel (deep forest field on most slides) defaults to a white bird.
  - **Forest bird** when the post is dominated by cream, paper, sage, or any light palette where a white bird would disappear. Example: an intro carousel on cream defaults to a forest bird.
- **Per-slide override (added 2026-06-08).** If the post's default color would visibly blend into a specific slide's top-right corner (for example, a white bird on a cream right panel of a split-panel slide), switch to the other color on that slide alone. Readability beats color consistency. Example: hormone slide 3 (Men) flips to a forest bird because its right panel is cream, even though the rest of the carousel uses white.
- This is a contrast decision. Read the whole post before locking the default color; then check each slide and override only where needed.

### Size

- Bird height: 80 px on 1080 × 1080 and 1080 × 1350.
- **Same size on every slide AND every post.** A Vital Health feed scrolled top to bottom should show one consistent bird at one consistent size. Do not scale up on a cover, down on a dense info slide, or larger on an announcement. If the bird does not fit a slide composition, change the composition, not the bird.

### Position

- Anchor: always the **slide's outer top-right corner**. Never the corner of an inner panel or card. If a slide has a split-panel layout, the bird still sits in the slide's outer corner, even if that means crossing onto a different color block.
- Padding from top edge: 60 px.
- Padding from right edge: 60 px.
- Same anchor on 1080 × 1080 and 1080 × 1350.

### Frequency

- Every slide of a carousel gets the mark, in the same place, at the same size, in the same color.
- Single-post announcements (moving announcement, holiday hours, etc.) also use the mark, same rules.

### On photographic backgrounds

Because the bird is a solid filled silhouette, not an outline, a busy photographic corner is much less of a problem than it was for the outline version. The bird remains legible against light or dark photo regions when it is filled. Still, before shipping:

- Look at the **200 × 200 region under the bird** on each slide and confirm the bird's chosen color reads against it. If not, prefer cropping or repositioning the photo so the bird sits on uniform tone.
- Do not solve a contrast problem by adding a halo, circle, chip, or scrim behind the bird. The mark stands alone.

## Slide Types: Cover vs Info

A Vital Health carousel has two slide types. Treat them as different design systems that share a topic theme kit. Do not blur them.

**Cover slide (1 per carousel):**

- Cinematic. This is the slide that sets the topic mood and earns the swipe.
- Full-bleed background using the topic theme kit (palette + motif, see next section).
- The service or topic name is the large headline. Set it on a cream or paper card sitting on top of the themed background. The card is the structural anchor that all info slides will echo.
- One short patient-facing description sits under the headline inside the card. One short brand close ("Vital Health can help.") sits below the description, in forest serif.
- No bullets, no stats, no diagrams, no chips. Just the card and the supporting motif behind it.
- The cover is allowed to look different from info slides. It is the only slide that should.

**Info slides (every other slide):**

- Uniform. Info slides in the same carousel should feel like one rhythm. The reader should not feel like they walked into a different post halfway through.
- Use the topic theme kit's palette and motif on every info slide, even when the slide is mostly text. The motif may be small, faded, or cropped, but it must be present.
- Anchor every info slide on a single cream or paper text block, just like the cover card. This is the connective tissue between cover and info: the same block recurs slide to slide, holding the slide's headline + body.
- Allowed compositions for info slides (mix them, do not repeat the same composition twice in a row):
  - **Card on themed field** (cream card on the dark green / motif background, same family as the cover).
  - **Split panel** (cream/paper text block on one side, themed color block on the other; bird sits in the slide's outer top-right corner, color follows the panel beneath it).
  - **Quiet cream slide with a themed accent band** (cream background, but a slim band of the topic motif runs along one edge — top, bottom, or side — so the topic still reads).
- Do not introduce a new diagram language per slide. If the cover uses leaves, do not switch to circle arcs for one info slide and chips for another. Pick one supporting graphic motif per topic and stay in it.
- Do not use orbs, concentric circles, or abstract diagram clusters unless the topic's theme kit explicitly calls for them.

## Topic Theme Kit

Every Vital Health carousel has a topic theme kit. The kit defines a small palette slice and one supporting motif. The cover establishes the kit. Every info slide echoes it. The kit is what makes the carousel feel "on theme."

Pick the kit before drafting slides. Write it down at the top of the post's `post.md` or `caption.md`:

```
Topic theme kit
  Field color: <forest, deep forest, sage, paper, cream>
  Card color: <cream or paper, almost always one of these>
  Accent: <gold, terracotta, peach — pick ONE per carousel>
  Motif: <one supporting visual — see motif list>
```

Standing motif options (use one per carousel; do not mix):

- **Botanical leaves** — soft olive leaf shapes, partially behind the card. Use for hormones, women's health, longevity, lifestyle.
- **Amber glass and clean lab paper** — still-life crop in the corner or along a band. Use for peptides, labs, diagnostics, supplements.
- **Soft window light on cream linen** — diffuse warm glow as a background veil. Use for patient-journey, intake, complimentary consultation posts.
- **Botanical stem and brass pen** — for clinical-intake or care-plan topics.
- **Thin molecule line work** — only for genomics, DNA testing, biomarker explainers. Quiet, monoline, never neon.

Topic theme kit examples (the ones already used or proposed):

- **Hormone optimization** → field: deep forest. Card: paper. Accent: gold. Motif: botanical leaves. (The cover from 2026-06-07 is the canonical example.)
- **Peptides** → field: cream. Card: paper. Accent: terracotta. Motif: amber glass + lab paper.
- **Labs / biomarkers** → field: paper. Card: cream. Accent: gold. Motif: thin molecule lines on one edge.
- **Menopause / perimenopause** → field: sage. Card: paper. Accent: peach. Motif: botanical leaves.

If a future topic doesn't fit one of the above, define a new kit using the same four fields and add it here. Never ship a Vital Health post without a written-down kit.

Motif sharing across topics (added 2026-06-08 from peptides + regenerative stress test):

- The brand currently has one real still-life PNG (amber glass, lab paper, brass pen, botanical stem, cream linen). Two adjacent carousels may need to share it. That is fine, but the topics must read as different.
- When two topics share a photographic motif, differentiate them with the rest of the kit:
  - **Flip the field and card colors** between the two kits. If carousel A uses cream field + paper card, carousel B uses paper field + cream card.
  - **Use a different accent color.** Never give two adjacent topics the same accent. Hormones = gold. Peptides = terracotta. Regenerative = gold (cleaner / quieter than hormones). Menopause = peach.
  - **Crop and position the photo differently.** Cover the bottle on one carousel, foreground it on the other; full-bleed on one, accent band on the other; bottom edge on one, top band on the other.
  - **Use different composition rhythms.** If carousel A uses text-left split panels, carousel B uses text-right.
- If two carousels still feel too similar after applying the above, the gap is a missing photographic asset. Surface that to Annabel rather than reusing the same photo a third time.

## Hormone Carousel Lessons

These rules come from the 2026-06-07 hormone optimization carousel and should guide future Vital Health service posts.

- For a service cover, make the service itself the large headline. Do not lead with "Vital Health helps with..." as the headline. Use the practice name as the supporting close, for example "Vital Health can help."
- Remove small category kickers such as "For Women," "For Men," or "Hormone Care" when the main heading already says the topic. They made the slides feel more templated.
- Keep section left edges truly aligned, including the text inside a card or block. Do not align the container while leaving the inner text indented.
- Control important line breaks manually. Do not let phrases like "service supports," "Alzheimer's disease risk conversations," or a website URL break awkwardly if a small type adjustment or width change can fix it.
- Equalize bullet spacing across columns and rows before showing the design. Uneven bullet rhythm is one of the first things Annabel will notice.
- Avoid abstract filler panels that only contain leaves or vague circles. If the right side needs imagery, use a Vital Health-style still life: cream linen, amber glass, clean lab paper, brass pen, botanical stem, warm natural light, and no readable text.
- For public medical claims, keep the visual and copy careful. Prefer "supports care around," "risk conversations," "may be involved," and "can help" over guaranteed prevention or treatment language.
- When copy sounds technically true but awkward, rewrite it into plain patient-facing sentences. Example: "Women can spend a third to half of their lives after menopause. This phase is often undertreated, and it is one of Vital Health's specialties."

Photography and imagery:

- If using AI images, use documentary natural-light still life language.
- Good motifs: amber glass, cream linen, clean lab paper, botanical stems, brass pen, soft window light, patient hands, clinic table details.
- Bad motifs: generic stock doctors, happy medspa faces, syringes as drama, neon science, glowing molecules, fake labels.
- If using abstract graphics, keep them quiet: thin molecule lines, subtle grids, soft botanical silhouettes.

## Photography Direction (added 2026-06-08)

This section is the source of truth for what a Vital Health photograph should look like. It exists because earlier guidance was too vague ("amber glass, cream linen, soft window light") and image picks drifted. The two mood boards saved at `media/references/vh-moodboard-1.png` and `media/references/vh-moodboard-2.png` are the canonical reference. When choosing or generating a photo, it should be plausible as a 6th tile in either board.

### Palette and light

- **Surfaces:** white or pale grey marble (round trays, counters), cream linen drape, oatmeal cotton, raw paper, pale natural wood. No dark wood, no glossy black, no steel-grey clinical surfaces.
- **Light:** soft natural window light, mid-morning quality. Shadows are diffuse and warm, never hard or fluorescent. One direction of light per image; a faint shadow of leaves through the window is welcome.
- **Color cast:** warm-cream overall, with one accent — amber glass, honey capsule, lemon yellow, olive green, pale terracotta. Never blue, never magenta, never neon.

### Still life subjects (the ones we want to see)

Use these recurring objects. A good still-life slide picks 2–3 of them, not all of them.

- Amber pharmacy bottle (small, brushed silver cap, no readable label).
- Clear glass ampoule, often paired with the amber bottle.
- Ribbed lowball or rocks glass with water and a single lemon slice.
- Small cream or unglazed ceramic bowl, sometimes with eucalyptus or olive sprigs.
- Honey-gold gel capsules (2 to 4, loose on a tray), or 2 to 3 small white capsules in an open palm.
- Botanical sprigs: eucalyptus, olive branch, rosemary, fresh herbs. Never tropical leaves, never dried florals, never bouquets.
- Marble round tray as a staging surface.
- Cream linen napkin or throw, casually folded.
- Clipboard with cream paper and a slim pen, hands writing.
- Laptop with a calm dashboard or chart, closed books, eyeglasses on cream desk (the one "data" cue, used sparingly).

### Figures (when a person is in the frame)

- **Always cropped or turned away.** Back of head, hands only, or three-quarter from behind. No identifiable faces, no eye contact, no smiling-at-camera stock energy.
- **Wardrobe:** flowy natural-fiber cream, oatmeal, sand, or off-white. Linen pajama sets, linen button-downs, oatmeal sweatsuits. No logos, no prints, no color blocking, no scrubs, no white coats.
- **Hair:** loose low bun, messy bun, or low ponytail. Natural color. Not styled.
- **Setting:** at a sunlit kitchen window prepping greens, standing barefoot near a small indoor tree holding a glass of water, walking away on a dirt path through wildflowers with a city skyline far in the distance, or seated writing at a marble table. Pick one of these scenes per image.
- **Action:** quiet, single-task. Holding a glass, washing greens, writing, walking. Never exercising, never posing, never mid-gesture.

### Composition rules

- **One subject per frame.** Either a still life OR a figure-in-environment, not both fighting for attention.
- **Negative space on at least one side.** A photo we can crop into a square or portrait slide without losing the subject.
- **Top-right corner should be calm.** That is where the hummingbird lands. If the natural composition puts a busy element in that corner, recompose.
- **Tight, intimate crops for still life.** The amber bottle slide is shot from ~30 cm away, not across a room.
- **Wide, airy crops for figure scenes.** Lots of room above the head, plant or window framing on one side.

### What NOT to use

- Faces, smiles, eye contact with camera.
- White coats, scrubs, stethoscopes, exam tables, medical equipment.
- Visible brand labels on bottles, supplements, or devices.
- Syringes, needles, IV bags, drips.
- Glowing molecules, neon DNA, sci-fi science visuals.
- Dark moody backgrounds, black surfaces, hard rim light.
- Bouquets, tropical leaves, dried florals, candles.
- Group shots, multiple figures, anyone interacting with another person.
- Stock-photo posing (hand on chin, looking thoughtfully out window).
- Phones, branded laptops with visible Apple logos, social media UI on screens.

### When generating with AI

If prompting an AI image model (ChatGPT, Midjourney, etc.), the prompt should explicitly include:

- "documentary natural light, soft window light, mid-morning"
- "warm cream and oatmeal palette, marble surface, linen napkin"
- "back of head" or "hands only" if a figure is involved, "no face visible"
- "no logos, no readable text, no brand labels"
- "no white coat, no medical equipment, no syringes"
- aspect ratio matching the slide it will live in (1:1 for square posts, 4:5 for portrait carousels)

Generate 4 candidates and pick the one that could sit in the mood board without standing out. If none qualify, regenerate. Do not ship a "close enough" image.

## Informational Carousel Inspiration

Annabel reference batch from 2026-06-07: use the attached carousel screenshots as the main inspiration for Vital Health informational Instagram posts. Treat them as composition and rhythm references, not as templates to copy exactly.

What to borrow:

- **Editorial black and cream contrast:** oversized all-caps headlines, black/cream alternation, monochrome or muted photography, thin rules, and confident negative space. Translate this into Vital Health's forest, cream, paper, and ink palette rather than making the feed stark black-and-white.
- **Modular education slides:** numbered points, myth/fact pages, simple diagram arcs, checklist slides, and one-topic-per-slide layouts. These are useful for labs, peptides, diagnostics, genomics, menopause, cognitive health, longevity testing, and "when to ask your provider" topics.
- **Soft public-health color blocking:** approachable warm blocks, large numbered bursts, and easy-to-scan myth explainers. For Vital Health, use this sparingly with terracotta, pale peach, sage, and gold so it feels warmer without becoming pediatric or nonprofit-bright.
- **Minimal wellness templates:** cream backgrounds, fine borders, small photo panels, calm serif headings, and final slides that ask the reader to save, share, comment, or book a consultation. This is the closest direct lane for Vital Health.
- **Tall story-like carousels:** portrait-oriented slide sets with full-bleed image covers, split image/text panels, quiet line systems, tiny progress markers, and one elegant CTA slide. Use this when the topic is reflective or patient-journey oriented.
- **Type-led quote slides:** large serif or italic serif statements with a small supporting line. Use only when the statement is clinically grounded and not generic self-care content.

Vital Health translation:

- Start with a literal medical hook, but design it like a poster. Good cover examples: "What are peptides?", "Why labs matter before treatment", "Common misconceptions about functional medicine", "What is a full clinical picture?", "When should you ask about hormone testing?"
- Build 7 to 8 slide carousels with visible variety: cover, definition, one visual analogy, myth/fact or common misconception, checklist/table, clinical-context slide, patient question slide, final CTA.
- Use at least one high-contrast slide per carousel: deep forest or ink background, oversized type, and very little copy. This keeps educational posts from looking like a beige handout.
- Use at least two quiet cream/paper slides with fine rules and dense but readable education. These can carry the clinical substance.
- Use at least two image-led slides: full-bleed cover, vertical crop, ingredient/lab still life, patient hands, clinic table, or softly veiled image background.
- Numbering can be graphic and large, but keep it restrained. Do not make every slide a numbered lesson unless the post is explicitly a list.
- Use thin circular arcs, fine divider lines, small progress dots, or grid rules for structure. Avoid decorative blobs, bubble shapes, and trendy sticker-like graphics.
- Keep final CTA slides simple: "Ask Vital Health", "Book a complimentary 60 minute consultation", "Save this for your next appointment", or "Have questions about this topic?" Do not make the CTA feel like influencer engagement bait.

Avoid while using these references:

- Do not copy the business-coach look too literally: no "book now" energy, no fashion-studio attitude, no generic creator-brand phrasing.
- Do not overuse black. Vital Health can use ink or deep forest for contrast, but the feed should still feel clinical, warm, and premium.
- Do not let bright pink/yellow/orange public-health layouts override the Vital Health palette.
- Do not make quote slides vague or motivational. Every slide should teach, orient, or invite a specific provider conversation.
- Do not use tiny body copy over photographs. If a slide needs education, put the copy on solid paper or under a dark veil.

## Copy Voice

Vital Health copy should be specific, plain, and measured.

Instagram carousel headers should be literal and instantly scannable. Use clear questions such as "What are peptides?", "Why do labs matter?", "When are peptides considered?", and "How can Vital Health help?" Avoid clever editorial headers that make the reader decode the point before reading the slide.

Use:

- Simple question headers.
- "guided by your labs, goals, and full clinical picture"
- "may be considered"
- "when clinically appropriate"
- "history, testing, and care plan"
- "complimentary 60 minute consultation"
- "No cost. No commitment."
- "You are more than a symptom."

Avoid:

- Clever headers like "Tiny chains. Real signals.", "The same name can mean a different question.", or other poetic phrasing when the post is educational.
- Miracle, cure, guaranteed, reverse, melt, biohack.
- "Optimize your life" language.
- Outcome promises.
- Shopping-list framing for medical protocols.
- "Peptides for everyone" framing.
- Overly broad anti-aging claims.

## Peptide Content Guardrails

Peptide posts should be educational and careful.

- Do not present peptides as a menu.
- Do not imply that a peptide name equals a treatment recommendation.
- Explain that labs, history, medications, goals, risk factors, route, dose, source, and monitoring matter.
- If examples are listed, say they are examples patients may hear about, not recommendations.
- Include a soft medical disclaimer in the caption.
- Keep the CTA to a provider conversation, not a purchase.

## Informational Post Blueprint (added 2026-06-08, restructured 2026-06-08)

This is the canonical structure for any Vital Health informational Instagram post. The default is **3 slides** (positioning → definition → protocols + CTA). It was set after the peptide test run on 2026-06-08, when the 4-slide hormone structure proved overbuilt for topics that do not split cleanly by demographic. The hormone post's 4-slide structure is preserved as a **variant** (see Part E) for topics that genuinely have two lenses.

The blueprint has five parts:

- **A. Slide-by-slide template** — the 3-slide default.
- **B. Copy voice patterns** — the voice rules every slide's text obeys.
- **C. Research protocol** — how Claude (or the future Vital Health Cowork skill operator) gathers topic-specific info before drafting.
- **D. Per-topic operator input** — the minimum the human needs to provide.
- **E. 4-slide variant** — when the topic splits by demographic, phase, or clinical lens.

### A. Slide-by-slide template (3 slides)

The default informational post is 3 slides at 1080 × 1080. Topic theme kit (field, card, accent, motif) must be written down at the top of `post.md` before any slide is drafted. The hummingbird mark, gold rule, and paper-card pattern follow the global rules in this file.

**Slide 1 — Positioning.**

- Purpose: tell the reader how Vital Health thinks about this service. Not symptoms, not a hook, not a question. The practice's posture.
- Composition: card-on-themed-field. **The field is always deep forest with the leaf motif**, regardless of the topic's theme kit. This is a feed-level convention: every Vital Health informational post opens on the same cinematic forest cover so a reader scrolling the feed reads "Vital Health service" before reading the topic. The topic theme kit takes over on Slide 2 onward.
- Headline (Fraunces ~104 px in forest): the service or topic name, declarative, one or two words. Examples: "Peptides", "Hormone Optimization", "Lab-Guided Care", "Menopause Care". Do not phrase as a question.
- Support paragraph (Inter muted, ~28 px, 3 to 4 lines): leads with the practice. Pattern: "At Vital Health, [topic] is [posture word]. We [what we do first], then [what we decide based on]." Example: "At Vital Health, peptide therapy is personal. We start with your labs, your history, and your goals, then only consider peptides when that direction is clinically supported."
- No close line on the positioning slide. (The italic "Vital Health can help." close from the hormone post moves to the caption.)
- No eyebrow, no bullets, no stats, no chips.

**Slide 2 — Definition.**

- Purpose: explain what the topic actually is, in two careful sentences. Walk the reader from the physical definition to the clinical meaning.
- Composition: card-on-themed-field, **same field as Slide 1 (deep forest with leaves)** by default, so Slide 1 and Slide 2 read as a matched pair. The topic theme kit may optionally shift the field on this slide if the topic visually benefits (peptides may use the amber-glass still life behind a translucent veil instead of leaves) — note the choice in `post.md`.
- Headline (Fraunces ~64 px in forest): "What [topic] are" / "What [topic] is". Short, declarative. Examples: "What peptides are", "What hormone optimization is", "What lab-guided care is".
- Body paragraph (Fraunces ~26 px in ink, 4 to 6 lines): two sentences. First sentence is the physical/scientific definition in plain language. Second sentence explains the clinical relevance — why this thing matters for care. Pattern: "[Topic] are [physical definition]. [Clinical relevance — why selectivity, why precision, why this approach helps]." Example: "Peptides are short chains of amino acids your body already makes. They act as biological messengers, signaling specific cells and tissues. Targeting one pathway means the response can match a particular goal, like tissue repair, immune support, or sleep, rather than broadly affecting the body."
- No bullets, no stats, no chips. The body paragraph carries the whole slide.

**Slide 3 — Protocols / Options + CTA.**

- Purpose: name the specific things Vital Health considers in this service area, with one careful sentence each so the reader actually learns. Then the booking CTA.
- Composition: paper-dominant slide with a 200 px forest accent band on top, still-life or leaf motif inside the band. Body sits below on paper.
- Headline (Fraunces ~72 px in forest, max-width 700 px): "Protocols we may discuss", "Conditions we treat", "Labs we may run", "Approaches we use", etc. Verb chosen by epistemic level — "discuss" is the softest, "treat" the strongest.
- Optional gold rule (116 × 1 px) directly under the headline, left-aligned. Use only when there is no sub-paragraph between headline and chip grid.
- Optional sub (Fraunces ~24 px muted, max-width 760 px): one sentence philosophy line. Skip on Slide 3 by default — the chips themselves do the work. Add only if a posture caveat is needed.
- Chip grid: 8 chips in a 2-column grid. **Two-line chips** (this is the new default; the single-line version is deprecated):
  - Background: cream `#f5efe0`. Min-height 90 px. 16 × 22 px padding. 2 px gold left border. No number prefix — the protocol/condition name IS the label.
  - Line 1 (Fraunces ~26 px in forest): the protocol or condition name. Examples: "Ipamorelin", "BPC-157", "Low testosterone", "Thyroid panel".
  - Line 2 (Inter ~14 px in muted ink, 1.35 line-height): one careful sentence describing what it is considered, studied, or used for. Lead with an epistemic verb (see Part B). Examples: "Studied for tissue repair. Muscle, tendon, and ligament recovery, joint comfort, and gut health.", "Often part of conversations around sleep, recovery, body composition, energy, and joint comfort."
- CTA block: full-width gold rule (1 px), then "Book a consultation with Vital Health" (Inter 20 px, semibold, 0.08 em letter-spacing, uppercase, forest), with the site URL underneath (Inter 16 px in muted, mixed case, 0.04 em letter-spacing). The URL is `vitalhealthim.com`.

**Conventions that apply across all 3 slides.**

- Hummingbird mark: 80 px tall, 60/60 anchored to the slide outer corner. Pick the color by what is in the 200 × 200 region under the bird per the global rules.
- One gold rule per slide. Slide 1 has none visible (the field carries the role); Slide 2 has none visible; Slide 3 has the CTA rule (and optionally the headline rule).
- Botanical or still-life motif present on every slide. Same opacity family (~0.35 to 0.5) for visual rhythm.
- No em-dashes, en-dashes, or double hyphens in any copy.
- Caption (the Instagram body text, not on the slides): 3 short paragraphs plus a one-sentence medical note. Pattern: paragraph 1 is the same definition that opens Slide 2 (so the caption stands alone); paragraph 2 names Vital Health's full-clinical-picture posture; paragraph 3 lists the patient experiences this post speaks to and ends with "Vital Health can help." A final italic line is the medical note: "This content is educational and not a diagnosis or treatment recommendation. [Topic-specific] decisions should be made with a licensed clinician after individualized evaluation, labs, and risk review."

### B. Copy voice patterns

These patterns came from the 2026-06-08 peptide test run. Every line of slide and caption copy must obey them. They override the more general guidance in the older **Copy Voice** section when the two conflict.

- **Declarative headlines, not question headlines.** "Peptides" / "What peptides are" / "Protocols we may discuss" beats "What are peptides?" / "Patients ask about peptides for many reasons." The reader should hit the topic immediately, not decode a hook.
- **Slide 1 leads with the practice's posture, never with symptoms.** Open on "At Vital Health, [topic] is [posture word]…" Never open with "If you are struggling with…" That symptom-list pattern is banned from the positioning slide. It belongs in the caption, not on the slide.
- **Slide 2 is a definition slide, period.** Two sentences that walk from physical reality to clinical relevance. No claims about Vital Health, no calls to action, no questions. Just teach.
- **Epistemic verbs on Slide 3.** Every protocol description leads with one of these careful verbs, picked by claim strength:
  - "Studied for…" — strongest evidence base. Use for peptides with peer-reviewed clinical literature (BPC-157 for tissue repair, Thymosin Beta-4 for wound healing).
  - "Considered for…" — clinically appropriate in select patients. Use when the practice would consider it but the evidence base is moderate (PT-141 for sexual wellness).
  - "Discussed for…" — comes up in conversation, weaker evidence or off-label. Use for emerging applications (CJC-1295 for growth hormone signaling).
  - "Often part of conversations around…" — most common patient ask. Use when patients raise it, not when the practice initiates it (Ipamorelin for sleep, recovery, body composition).
  - "Used in… programs" — already part of a Vital Health offering. Use when the practice has standardized it (immune support programs, longevity programs).
  - "Tied to…" — physiological mechanism, not yet a recommendation. Use for mechanism-of-action descriptions (MOTS-c tied to metabolism and cellular performance).
- **Banned openings on the slide:** "Are you dealing with…" / "Struggling with…" / "Are you tired of…" / any infomercial framing. Banned even when the live Vital Health page uses them — the carousel is more careful than the page.
- **Caption keeps the italic close.** "Vital Health can help." moves off the positioning slide and into the caption as the close of paragraph 3.

### C. Research protocol

Before drafting any slide, Claude (or the operator using the Cowork skill) follows this order. Do not skip a step. If a step turns up nothing usable, note it and move on; do not invent.

1. **Vital Health site content first.** Read whatever the practice already says about the topic.
   - Check this repo for a services page or copy file (`services-delta-*.md`, `webflow-change-inventory-*.md`, `assets/`, prior post folders for the same topic).
   - If nothing local, scrape the live Vital Health page for the topic via Firecrawl (`firecrawl_scrape` on `https://www.vitalhealthaustin.com/<service>` or the equivalent URL). Use the voice and claim level from there as the ceiling for the post.
2. **Trusted medical sources.** For any claim not already grounded in Vital Health's own copy, draw from this allowlist only:
   - Mayo Clinic (`mayoclinic.org`)
   - Cleveland Clinic (`my.clevelandclinic.org`)
   - NIH / NIA / NHLBI / NIDDK (any `nih.gov` subdomain)
   - Endocrine Society (`endocrine.org`)
   - ACOG — American College of Obstetricians and Gynecologists (`acog.org`)
   - The Menopause Society / NAMS (`menopause.org`)
   - American Heart Association (`heart.org`) — for cardiovascular adjacencies
   - PubMed abstracts (`pubmed.ncbi.nlm.nih.gov`) for specific stats only, never primary citations on the slide
   - **Banned sources:** blogs, supplement-brand sites, telehealth marketing pages, influencer or "biohacker" content, Reddit, Quora, AI chatbot output, any source whose primary purpose is selling the substance being discussed.
3. **Voice and claim filter.** Run every drafted line through:
   - The **Copy Voice** section's banned vocabulary (miracle, cure, guaranteed, reverse, melt, biohack, optimize your life, outcome promises).
   - If the topic is peptides or any cosmetic/longevity adjacency, also run through **Peptide Content Guardrails** (no menu framing, no name-equals-treatment, soft disclaimer, provider-conversation CTA).
   - Any claim that cannot be sourced to step 1 or step 2 gets rewritten as "may be considered", "guided by labs and clinical picture", "when clinically appropriate", or dropped entirely.
4. **Stat sourcing.** The Slide 2 stat callout must trace to a specific source from the allowlist. Note the source in `post.md` for the record, even though it does not appear on the slide. If you cannot source a stat, swap the callout for a Fraunces sentence (see Slide 2 above).
5. **Chip sourcing.** The 8 chips on Slide 4 should be a mix of conditions, presentations, labs, or topic facets that Vital Health actually covers. Cross-check against the Vital Health site list before locking. Never invent a condition the practice does not treat.

### D. Per-topic operator input

When the eventual Vital Health Cowork skill runs, the operator (a non-technical Vital Health team member) should only need to provide:

1. **Topic name** — the words that will appear as the Slide 1 headline. E.g., "Peptides", "Hormone Optimization", "Lab-Guided Care", "Menopause Care".
2. **One-sentence positioning angle** (optional but encouraged) — how the practice thinks about this service, used to seed the Slide 1 support paragraph. E.g., "Peptides are personal. We start with labs, history, and goals before considering anything." Claude will turn this into the "At Vital Health, [topic] is [posture word]…" sentence.
3. **Vital Health page URL** (optional) — link to the practice's existing page for this topic, if one exists. Speeds up the research protocol.
4. **Variant choice** (optional) — if the topic clearly splits by demographic, phase, or clinical lens (like hormones did with Women/Men), the operator can request the 4-slide variant in Part E. Otherwise the 3-slide default applies.

Everything else — the definition paragraph, the protocol chip list with epistemic-verb descriptions, the caption, the medical note — Claude fills in by walking the research protocol and the slide-by-slide template.

### E. 4-slide variant (demographic, phase, or clinical-lens split)

Use the 4-slide variant when the topic genuinely splits into two complementary lenses that deserve their own slides. The original hormone optimization carousel (2026-06-07) is the canonical example. Do not use this variant just to make the post longer.

When to reach for it:

- **Demographic split** — the clinical conversation differs by who the patient is. Example: Hormones → "Women" / "Men". Menopause → "Perimenopause" / "Post-menopause".
- **Phase split** — the topic divides into two stages of a clinical journey that need distinctly different care. Example: Hormone therapy → "Starting therapy" / "Maintaining therapy".

The 4-slide variant inserts two **lens slides** between Slide 1 (Positioning) and the final Protocols + CTA slide. The new order is:

1. **Positioning** — same as the 3-slide default (Part A).
2. **Lens A** — card-on-themed-field. Topic theme kit takes over. Headline = lens label (Fraunces ~88 px in forest). Lede (Fraunces 30 px, 2 sentences). Optional gold-bordered stat callout, or Fraunces sentence in the same position if no stat is sourceable. Care-title (Fraunces 27 px in terracotta). 4-item 2-column bullet list with gold dot markers.
3. **Lens B** — split panel. Paper card on the left (~62%), themed field on the right with the topic theme kit's motif. Bird color picked per panel under it. Headline + gold rule + lede + sub-title + 6 to 8 item 2-column list. Italic Cormorant side caption in the right panel: "Guided by your labs, history, and full clinical picture."
4. **Protocols / Conditions + CTA** — same as Slide 3 of the 3-slide default (Part A), with the two-line chip format.

Do **not** drop the Definition slide when using the variant. If the topic needs both a definition and two lens slides, the post is now 5 slides (Positioning / Definition / Lens A / Lens B / Protocols + CTA), and that is acceptable. The hormone optimization carousel is the rare case where the Lens A slide carries the definition implicitly because "Women" and "Men" are already definitional. Most topics will need the explicit definition slide.

## Carousel Length Variants

The **4-slide Informational Post Blueprint** (above) is the default for every informational post. The 5-slide and 7–8 slide forms below are variants used only when the topic genuinely cannot fit the 4-slide structure. Pick the variant before drafting, write the choice into `post.md`, and explain why the default did not fit.

### 5-slide variant

When the topic needs a dedicated "how we decide" slide separated out from the lens panels, expand to 5 slides:

1. **Cover** with one calm thesis and a single supporting line. (Same as Slide 1 of the blueprint.)
2. **Definition** — what the topic actually is, in plain language.
3. **When it may be considered** OR **Why it is personal** — pick whichever lands harder for this topic.
4. **How Vital Health thinks through it** — a clinical decision frame: indication, history, labs, risk, outcomes, monitoring. A 3-column × 2-row grid of small frame-cells under a single headline reads well here.
5. **How to ask Vital Health** — complimentary 60 minute consultation, no cost, no commitment.

### 7–8 slide variant (deep educational)

For topics that genuinely need an examples slide AND a "why labs matter" callout in their own right (e.g., a foundational teach on labs, peptides, or genomics), expand to:

1. Cover with one calm thesis.
2. Plain-language definition.
3. Why the topic is personal.
4. When it may be considered.
5. Why labs and history matter.
6. Examples patients may hear about.
7. How Vital Health thinks through the decision.
8. How to ask Vital Health about it.

The post should get more useful as it goes. It should not just repeat the service page in prettier type. Use this variant sparingly — most service explainers fit the 4-slide blueprint, and a longer carousel without earned content reads as padded.

## Slide-Level Conventions (added 2026-06-08)

These are small patterns the peptide and regenerative stress test confirmed are worth standardizing.

**Eyebrow micro-kicker.** Each info slide may carry a small-caps eyebrow above its headline ("DEFINITION", "WHY PERSONAL", "WHEN IT MAY BE CONSIDERED", "HOW VITAL HEALTH THINKS THROUGH IT"). Inter, 14–16 px, 0.20 em letter-spacing, color = the kit's accent. One per slide, never on the cover, never longer than four words. These replace the older "category kicker" pattern (banned) — the difference is that eyebrows label the slide's *purpose*, not the topic.

**Italic offer line.** When a slide carries the consultation offer, set "Complimentary 60 minute consultation." in Cormorant Garamond italic at 30–34 px. Follow it with "No cost. No commitment." in Inter small-caps, 14–16 px, 0.10–0.12 em letter-spacing, in muted body color.

**Split-panel direction.** A carousel may use split-panel info slides in either direction (text-left / motif-right, or motif-left / text-right). Pick the direction per slide based on which side has the photo's natural focal point. Do not use the same direction on two split-panel slides in a row — alternate.

**Italic pull caption.** At most one slide per carousel may carry a small italic Cormorant Garamond pull line in a corner (e.g. "Guided by your labs, history, and full clinical picture."). It is decoration, not new information, so the rest of the slide must still teach without it. Put it on a solid scrim if it sits over a photo, so it stays legible.

**Frame-cell grid.** For "how we decide" slides, a 3-column × 2-row grid of small frame-cells (label in accent small-caps + one short Fraunces sentence) reads better than a bullet list. Top-border each cell with the gold-soft line, not a full box.

## Pre-ship Audit Checklist (added 2026-06-08)

Before exporting any Vital Health post, walk through these in order:

1. **Topic theme kit** is written down at the top of `post.md` (field, card, accent, motif).
2. **Hummingbird** is 80 px tall, 60/60 anchored, slide outer corner on every slide.
3. **Bird color** matches the 200 × 200 region directly under the bird on every slide. Photographs have been cropped or veiled so that region is uniform.
4. **Card pattern** is consistent — the same paper card (or same cream card) recurs as the anchor block across info slides.
5. **Cover is cinematic, info slides are uniform.** No info slide looks like a different post.
6. **Motif** appears on every info slide, even if small or faded.
7. **One gold rule per slide.** No more, no fewer.
8. **No two split-panel slides in a row with the same direction.**
9. **No banned vocabulary** — miracle, cure, guaranteed, reverse, melt, biohack, "optimize your life," outcome promises.
10. **No em-dashes, en-dashes, or double-hyphens** anywhere in the copy.
