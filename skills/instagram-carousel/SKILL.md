---
name: instagram-carousel
description: Build an Instagram carousel (intro, ad, educational, testimonial, list, story) for any brand. Reads inspiration/ for visual cues, a 3-layer style stack (universal style.md + brand_context character + per-brand carousel-direction.md) for taste, and renders 1080×1350 slides. Hooks save every "I don't like X" correction into the correct layer and force all artifacts into <project>/media/. Triggers on "instagram carousel", "carousel post", "carousel ad", "make a carousel", "intro carousel", "ig carousel", "instagram post for [brand]". Do NOT trigger for non-carousel posts, repurposing existing content (mkt-content-repurposing), or visual identity work (mkt-visual-identity).
---

# Instagram Carousel

Annabel's instagram carousel builder. Reads inspiration, applies her accumulated taste, ships 1080×1350 slides.

---

## How to use

### 0. Mark the skill active (so the correction-listener hook fires)

First thing, before any other work in this skill:

```bash
mkdir -p ~/.claude/state/active-skills && touch ~/.claude/state/active-skills/instagram-carousel.lock
```

When the run finishes (post-publish, or Annabel signals done), or if you abort early:

```bash
rm -f ~/.claude/state/active-skills/instagram-carousel.lock
```

The lockfile is the gate the global `listen-for-corrections.sh` hook checks. Outside an active run it's dormant; inside one it captures every "I don't like X" prompt and routes it to the correct file in the style stack (universal corrections → `references/style.md`; brand-specific → `<project>/media/brand_context/carousel-direction.md`). If you forget to remove the lockfile, the next session will keep listening — not fatal, but noisy.

### 1. Confirm scope before generating anything

Open the run by confirming three things in one short message:

- **Brand** — name, what they do, who they're for. Pull from `<project>/media/brand_context/` if the project has one. If not, ask.
- **Carousel type** — intro, ad, educational, testimonial, list, story, other. Each changes the arc.
- **Slide count** — default 6 for intros, 3–4 for ads, 5–8 for educational/list. Confirm before continuing.

If `<project>/media/brand_context/voice-profile.md`, `media/brand_context/positioning.md`, or `media/brand_context/visual-identity/tokens.json` exist, read them first. They override generic copy and styling. Missing voice → fine, ship in plain voice and offer to run `mkt-brand-voice` later. Missing visual identity → ask before guessing palette and type.

**Foundation-skill compatibility:** the foundation skills (`mkt-brand-voice`, `mkt-visual-identity`, etc.) still write to `<project>/brand_context/` (project root, the old convention — they are plugin-owned and not yet updated). If you find `<project>/brand_context/` but not `<project>/media/brand_context/`, that's the legacy location — read from there for this run AND tell Annabel so she can move the folder once.

### 2. Read the 3-layer style stack BEFORE drafting copy or photos

Before any copy, photo prompt, or layout decision, read all three layers in order:

1. **Universal style** — `references/style.md` end to end. Annabel's invariants. Apply to every carousel.
2. **Brand character** — `<project>/media/brand_context/voice-profile.md` + `visual-identity/tokens.json`. Who the brand IS. Use the brand's actual voice, palette, fonts, logo.
3. **Brand media guide** — `<project>/media/design.md`, if it exists. This is where project-specific social/media taste can live even when formal `brand_context/` files are missing.
4. **Brand direction** — `<project>/media/brand_context/carousel-direction.md`. Annabel's direction for THIS brand specifically. May not exist yet; if missing, the earlier layers are sufficient.

Layer 1 covers universal rules. Layer 1 also has a "Category modifiers" section — when the brand falls into a named category (preventive medicine, chronic care, etc.), that category's defaults activate. Layer 3 declares the brand's category and adds any brand-only direction.

Resolution order on conflicts: later layers override earlier. So a brand can override a category default; a category default can override a generic universal default; but Annabel's strict invariants (no em-dashes, no faces in AI photos) sit at the top of layer 1 and are never overridden.

If a rule conflicts with what the brand needs, surface the conflict instead of silently overriding.

### 3. Pull visual direction from inspiration/

Before generating photos, browse `inspiration/` for:

- External Meta/Instagram ads Annabel has saved (use these to inform composition, color, tone)
- The `ad-analyses-*.md` files (written analyses of ads with what to borrow / skip)

`inspiration/` is brand-agnostic. To study a past shipped carousel for the brand you're building for now (or any past brand), look in `<that-project>/media/<date>-<slug>/` of the brand's project folder — NOT in this skill.

Name 2–3 specific references you're pulling from in your plan message so Annabel can sanity-check the direction.

### 4. Output location — HARD RULE (enforced by hook)

All generated artifacts MUST land in:

```text
<project_root>/media/<YYYY-MM-DD>-<slug>/
```

Where `<project_root>` is the project the skill is invoked from (e.g. `projects/vital-health-webflow-migration/`). If no project root is detected, create one at `~/Documents/AI-OS/projects/<brand-slug>/media/<YYYY-MM-DD>-<slug>/` and proceed.

`enforce-media-folder.sh` blocks any Write/Edit of `.png/.html/.yaml/.jsonl` outside this path. If the hook blocks you, fix the path — do not try to bypass it.

### 5. Render via the proven scripts

The `scripts/` folder is the rendering engine. Do not reinvent it inline.

```text
scripts/generate_photos.py   # gpt-image-1 calls, 1024×1536, ~$0.07/photo
scripts/render_slides.py     # HTML templates + Playwright → 1080×1350 PNG
scripts/build_review.py      # stitches a single-page review HTML
scripts/preship_audit.py     # lints against rules in the style stack
scripts/save_correction.py   # the hook calls this to append corrections
```

Each script accepts `--project-root` and derives the output path from it. Photos at 1024×1536 → base64-embedded in HTML → Chromium screenshots at 1080×1350. Typography stays vector-crisp; text is never baked into the AI image.

### 6. Pre-ship audit is blocking

`scripts/preship_audit.py` reads the full style stack (universal `style.md` + brand_context + per-brand carousel-direction.md) and lints the rendered slides against every rule. If it fails, surface the failures and offer fixes. Do not ship until it passes.

### 7. When Annabel corrects something, the hook saves it

When Annabel says "I don't like X", "don't use Y", "change the Z", etc., the `listen-for-corrections.sh` hook auto-appends a structured entry. Universal corrections land in `references/style.md`. Brand-specific corrections (those that name a brand or say "for VH" / "for this brand") land in `<project>/media/brand_context/carousel-direction.md`. You'll see a system reminder confirming where it was logged. Next run, you'll read both before generating anything.

You don't need to remember corrections in conversation. The hook is the memory.

### 8. The 6-slide intro arc — proven default

For intro carousels specifically, the v5 Vital Health build proved this arc. Use it as the default unless the brand needs a different shape.

| # | Role | Layout | Photo |
| --- | --- | --- | --- |
| 1 | **Hero** | Full-bleed photo + bottom-left headline | Person from behind, warm drink at window, morning light. No face. |
| 2 | **Why / origin** | Split right-photo + left text | Botanical still-life. Plants in window light. |
| 3 | **First visit / process** | Full-bleed + display word top-left | Top-down still-life: tea cup, paper card, brass pen, herb. |
| 4 | **Differentiator** | Split left-photo + right text | Marble surface, amber glass, capsules, single leaf. |
| 5 | **Philosophy pull quote** | Full-bleed + quote glyph + literary italic | Wide outdoor landscape. Person walking away. |
| 6 | **CTA** | Full-bleed + centered type + brand mark | Two hands meeting across linen table, hands only. |

**Slides 1, 2, 6 are non-negotiable for intro carousels.** Drop priority when reducing: 4 → 5 → 3.

For other carousel types (ad, educational, testimonial, list, story), infer the arc from inspiration/ + brand context. There is no hard-coded template for those yet — when one ships and Annabel approves it, add an arc note here.

### 8.1 The 4-slide health service arc — proven default

For short health service carousels, especially when Annabel asks for a 4-slide Instagram post, use this as the starting point:

| # | Role | Default move |
| --- | --- | --- |
| 1 | **Cover** | Service name as the large headline. One plain relevance paragraph. Brand can-help close. Real brand mark. |
| 2 | **Audience 1** | Direct audience heading, patient-facing context, one stat or care context line, and a concrete support list. |
| 3 | **Audience 2** | Direct audience heading, concise clinical approach copy, and evenly spaced symptom bullets. |
| 4 | **Scope / CTA** | "What we treat" or equivalent list, real website under the consultation CTA, and a brand-appropriate image or still life. |

Before showing the first pass, check the details Annabel had to correct on the Vital Health hormone carousel:

- The cover headline should be the service, not "Brand helps with..."
- Remove tiny redundant kickers like "For Women," "For Men," or "Hormone Care" when the main heading already does the job.
- Use the real brand mark, keep it the same size on every slide, and place it consistently.
- Align the actual text edges, not just the container edges.
- Pre-control line breaks for medical phrases, disease names, and URLs.
- Equalize bullet spacing across rows and columns.
- Avoid abstract decorative filler. Use a fresh editorial still life for image panels when the brand needs warmth.

### 9. Voice rules — apply to every line

These are Annabel's standing rules. They also live in `references/style.md` and the audit enforces them.

- **No em-dashes, en-dashes, or double-hyphens** in any copy. Use commas, periods, separate sentences.
- No claim words: miracle, cure, guaranteed, reverse, melt, biohack.
- Quiet confidence > hype. Short sentences. Plain words.
- Always end on a soft, real next step. Use the brand's actual low-friction offer, not generic "book a consult."

### 10. AI image prompt rules — apply to every photo prompt

Borrowed from `00-social-content` Rule 12 (proven across many runs):

- Open prompts with **documentary-photography keywords**: natural light, editorial, candid, real-world, slice-of-life.
- NEVER use: cinematic, epic, 8k, masterpiece, hyper-realistic, ultra-detailed, award-winning.
- Always end with the negative prompt: **"no faces, no readable text, no logos, no watermarks."**
- Pull palette vocabulary from the brand's `tokens.json` (cream/forest/gold, or whatever the brand actually uses).
- When mentioning a company/product/tool by name, render the real brand logo (Simple Icons, Lobehub, Devicon, or user upload). Never a generic icon, never "[Brand]" text. Escalate to Annabel if you can't resolve a real logo.

---

## What's in this skill

```text
instagram-carousel/
├── SKILL.md                  ← this file
├── README.md                 ← quickstart for a new run
├── inspiration/              ← visual reference library (read every run)
│   ├── README.md
│   ├── ad-analyses-*.md      ← written analyses of saved ads (Oura/Function/etc)
│   └── <ad-or-post>/         ← image files of saved ads + posts Annabel likes
├── references/
│   ├── README.md
│   └── style.md              ← Annabel's universal taste (auto-grown by hook). Layer 1 of 3.
└── scripts/
    ├── render_slides.py      ← HTML templates → 1080×1350 PNGs
    ├── generate_photos.py    ← gpt-image-1 photo gen
    ├── build_review.py       ← single-page review HTML
    ├── preship_audit.py      ← lints against the full style stack (blocking)
    ├── save_correction.py    ← hook entry point: routes corrections to style.md or carousel-direction.md
    └── photo-prompts.yaml    ← base prompts per slide role
```

### inspiration/

Brand-agnostic visual reference library. One source:

- **External ads** — Meta and Instagram ads Annabel saves. Drop the image into `inspiration/<ad-name>/` with a one-line note.

Plus `ad-analyses-*.md` files: written breakdowns of refs with "what to borrow / what to skip" notes. The first one, `ad-analyses-health.md`, covers 5 ads (Oura, Function Health, Bloom Nutrition, Solawave, Plunge). Brand-specific past work (past Vital Health builds, past dentist builds, etc.) lives in that brand's project folder under `media/<date>-<slug>/`, never here.

**Read this folder every run.** Inform composition, color, tone from what's actually here. Name 2–3 specific references in your plan message.

### references/

`style.md` is the universal layer of Annabel's 3-layer style stack. Hook-grown — every "I don't like X" comment that's universal becomes a structured entry. Brand-specific corrections go to `<project>/media/brand_context/carousel-direction.md` instead. Categories: Typography, Photography, Copy, Layout, Composition, Voice, Don't do this, Category modifiers, Working principles, Health-brand playbook, Uncategorized. **Read all three layers before drafting any copy or photos.**

`README.md` explains the format, the 3-layer stack, and the hook flow.

### scripts/

The rendering engine. Do not reinvent inline.

- `render_slides.py` — reads `inputs.yaml` + photos, emits self-contained HTML per slide, screenshots at 1080×1350.
- `generate_photos.py` — calls gpt-image-1 with templated prompts. Brand palette substituted into style suffix.
- `build_review.py` — single-page review HTML with all slides embedded, copied to `<project>/media/<slug>/review.html`.
- `preship_audit.py` — runs every rule from the full style stack against rendered slides. Blocking.
- `save_correction.py` — `--project-root <path> --feedback "<message>"` classifies the correction (universal vs brand-specific) and appends to the right file.
- `photo-prompts.yaml` — base prompt per slide role with `{palette}`, `{vocabulary}` placeholders.

---

## Hooks (the listening + the fence)

Two hooks live in `~/.claude/hooks/` and are registered in `~/.claude/settings.json`:

### `listen-for-corrections.sh` (UserPromptSubmit)

Fires on every user message during a skill run. Pattern-matches negative feedback:

- "I don't like…" / "I don't want…"
- "don't use…" / "stop using…" / "never use…"
- "change the…" / "that's wrong" / "no, the…"
- "make it less…" / "make it more…"
- "the [X] is too [Y]"

When matched, runs `scripts/save_correction.py --feedback "<message>"` which classifies the correction (universal vs brand-specific) and appends a structured, dated entry to either `references/style.md` or `<project>/media/brand_context/carousel-direction.md`. Then injects a system reminder so I confirm where the rule was logged before continuing.

### `enforce-media-folder.sh` (PreToolUse on Write/Edit/Bash)

Blocks any write of `.png/.html/.yaml/.jsonl` outside `<project_root>/media/<date>-<slug>/`. If no project root, auto-creates `~/Documents/AI-OS/projects/<brand-slug>/media/<date>-<slug>/`. If you hit a block, the path is wrong — fix it.

Both hooks are dormant outside instagram-carousel skill runs.

---

## Relationship to other skills

- **`00-social-content`** — was the parent orchestrator. Its proven conventions (post.yaml shape, image-source priority, real-logos rule, humanizer placement, AI prompt vocabulary) are now baked into this SKILL.md. The original skill is archived at `~/Documents/AI-OS/_archive/skills/00-social-content/`.
- **`mkt-brand-voice` / `mkt-positioning` / `mkt-visual-identity`** — foundation skills that produce brand_context content. They currently write to `<project>/brand_context/` (legacy location, plugin-owned). This skill prefers `<project>/media/brand_context/` (new convention); if it finds the legacy folder, move it once.
- **`mkt-content-repurposing`** — for turning an existing post into Instagram. This skill is for original carousels.
- **`tool-humanizer`** — run silently on any drafted caption before showing it to Annabel.
- **`tool-publisher`** — takes the finished `post.yaml` and publishes via Zernio.

---

## Cost + time

- ~$0.40 for 6 photos at 1024×1536 via gpt-image-1
- ~$0.30 typical iteration cost for 2–3 photo regens during review
- **Total per carousel: $0.50–$1.00**
- Wall time: 10–15 min for a clean first pass once inputs are confirmed

---

## When something goes wrong

| Symptom | Most likely cause | Fix |
| --- | --- | --- |
| Photos look generic / stock | Style suffix in `photo-prompts.yaml` lacks brand-specific palette vocab | Add palette words from brand tokens to the suffix |
| Copy reads generic | Brand `snapshot/about.html` not read | Stop, read it, redraft anchored to real founder words |
| Text not legible on a slide | Text < 24px sitting on photo with no plate/veil | Audit should catch this; if not, add veil in `render_slides.py` or delete the text |
| Brand feels templated | Same display face across all 6 slides | Set 2 of 6 to alt serif (close cousin, not radical departure) |
| Hook didn't fire on a clear correction | Trigger phrase missed the pattern list | Tell me the verbatim feedback; I'll log it manually + add the phrase to the listener |
| Files writing to wrong folder | `--project-root` not passed to script | Re-run with `--project-root <path>`; hook should have blocked already |
| `.env` `KEY=` exists but API call fails | Template stub matching, value not set | Read the actual value (length, prefix) — global rule from `~/.claude/CLAUDE.md` |
