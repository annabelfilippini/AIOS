# instagram-carousel — quickstart

Annabel's instagram carousel builder. SKILL.md is the operating manual; this file is the 30-second how-to-run.

## Run

```text
"make an instagram carousel for [brand]"
"intro carousel for [brand]"
"carousel ad for [brand]"
```

Or any trigger phrase from SKILL.md.

## What happens

1. I confirm brand, carousel type, slide count.
2. I read the 3-layer style stack before drafting anything:
   - `references/style.md` (universal — your taste invariants)
   - `<project>/media/brand_context/voice-profile.md` + `visual-identity/tokens.json` (the brand's character)
   - `<project>/media/brand_context/carousel-direction.md` (your direction for THIS brand)
3. I pull 2–3 specific references from `inspiration/` and name them in the plan.
4. I draft copy + photo prompts, render the full carousel, run the pre-ship audit against every rule in the style stack, fix any failures, and only THEN show you the review HTML in your browser. You see a finished, audited carousel — not an in-progress draft.
5. Output lands in `<project>/media/<date>-<slug>/`.

## Where files go

Always: `<project_root>/media/<YYYY-MM-DD>-<slug>/`.
No project root → `~/Documents/AI-OS/projects/<brand-slug>/media/<date>-<slug>/`.

Enforced by the `enforce-media-folder.sh` hook. You can't put carousel files anywhere else.

## When you correct me

Say "I don't like X" / "change the Y" / "don't use Z" naturally — the `listen-for-corrections.sh` hook auto-saves the rule. Universal corrections land in `references/style.md`; corrections that name a specific brand ("for VH: …") land in that project's `media/brand_context/carousel-direction.md`. Next run, I read it before drafting.

## The folders

- `inspiration/` — brand-agnostic Meta/IG ads I've saved as visual references. Read every run.
- `references/style.md` — your universal taste. Hook-grown. (Layer 1 of 3)
- `scripts/` — the rendering engine. Don't edit unless something is genuinely broken.

## Cost

$0.50–$1.00 per carousel. 10–15 min wall time once inputs are confirmed.

## Lineage

Built from the Vital Health v1→v5 hand-built carousel (May 2026). The proven 6-slide intro arc lives in SKILL.md §8. Every correction Annabel made across those 5 versions is the seed of `style.md`.
