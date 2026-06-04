# inspiration/

Visual reference library for instagram carousels. **Read every run** before generating photos or picking a layout.

This folder is brand-agnostic. It holds **external ads Annabel has saved** and **written ad analyses** that apply across any brand. Past brand-specific work (Vital Health, dentist, derm, etc.) does NOT live here — it lives in that brand's `projects/<brand>/media/<date>-<slug>/`. To study a past shipped carousel, look in the brand's project folder, not in the skill.

Bad work doesn't archive here either. Lessons from bad work live in `references/style.md` as rules, not as images.

## Folder shape

```text
inspiration/
├── README.md                        ← this file
├── ad-analyses-<niche>.md           ← written analysis of saved ads (no image files)
└── <ad-or-source-name>/             ← one folder per saved ad
    ├── <image-files>.jpg/.png
    └── note.md                      ← one-paragraph: brand, format, what to borrow, what to skip
```

A bare image file in `inspiration/` (no folder, no note) is allowed but discouraged — without a note, future runs can't tell why it's there.

## Naming

- Per-ad folders: `<brand-or-source>-<short-descriptor>/`, e.g. `function-health-gift-time/`, `bloom-nutrition-glow-up/`, `ag1-erica-testimonial/`.

## How the skill uses this

Before drafting photo prompts or picking layouts:

1. Browse this folder.
2. Pick 2–3 specific references that fit the current brand + carousel type.
3. Name them explicitly in the plan message so Annabel can sanity-check the direction.
4. Pull from the `ad-analyses-*.md` files for written breakdowns (what move each ref contributes).

If `inspiration/` is empty for a niche, ask Annabel what to use OR draft from `references/style.md` rules alone and flag that there's no visual reference seed.

## Current contents

- `ad-analyses-health.md` — analysis of 5 ads (Oura, Function Health, Bloom Nutrition, Solawave, Plunge). Useful for any health/wellness/preventive-medicine carousel. No image files — written analysis only.

(More refs land here as Annabel saves ads.)
