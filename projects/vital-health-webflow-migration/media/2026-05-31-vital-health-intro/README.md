# Vital Health — Intro Carousel (Claude run)

Claude-namespaced output. Codex runs land elsewhere — do not mix.

- **Date**: 2026-05-31
- **Slug**: vh-intro-carousel
- **Format**: instagram-carousel, 6 slides, 1080×1350 (4:5)
- **Brand context**: `brand_context/visual-identity/` (tokens locked; 8 carousel moves merged today from 5 inspo refs)
- **Pipeline**: pivoted off `00-social-content` orchestrator because the template pool is stub-only (4 manifest entries, 0 `status: ready`, 0 `template.html` files on disk). The gate would have hard-blocked. Pivot path: generate 6 photos via `viz-image-gen/scripts/generate_image_gpt.py`, hand-author 6 slide HTMLs from tokens, composite via headless Chromium, build review HTML.

## Folder layout

```
vh-intro-carousel/
├── README.md             ← this file
├── plan.md               ← slide-by-slide content + image prompts
├── raw/                  ← AI-generated raw photos (1024×1536)
├── slides/               ← 6 self-contained slide HTMLs
├── images/               ← 6 final composited slide PNGs (1080×1350)
├── review.html           ← single-page review with all 6 slides embedded
├── post.yaml             ← caption + slide metadata
└── pipeline-log.md       ← phase log
```
