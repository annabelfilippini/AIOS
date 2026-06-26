---
date: 2026-06-08
time: 12:00
project: websites / vital-health-review
status: complete
next-session: Filled-hummingbird Instagram carousel shipped live at https://vital-health-hormone-carousel.vercel.app/ (3 tabs, Intro Carousel / Hormone Optimization / Moving Announcement). Canonical assets media/vh-bird-white.png + vh-bird-forest.png; deploy folder client-share/vital-health-hormone-carousel/; rules in media/design.md.
---

# Vital Health Instagram — filled hummingbird shipped to Vercel

## Where to start next session

Live at <https://vital-health-hormone-carousel.vercel.app/> — three tabs (Intro Carousel / Hormone Optimization / Moving Announcement), all using the new filled hummingbird silhouette per `media/design.md`.

Source folders:

- `projects/websites/vital-health-review/client-share/vital-health-hormone-carousel/` — Vercel deploy folder. Holds slide-1.png through slide-4.png (hormone), we-are-moving.png (moving), and intro-carousel-review.html (intro, slides embedded as base64).
- `projects/websites/vital-health-review/media/vh-bird-white.png` and `vh-bird-forest.png` — canonical filled silhouette assets.
- `projects/websites/vital-health-review/media/2026-06-07-peptide-therapy-carousel/vh-bird-logo.png` — original outline PNG, kept only as source for re-generating tints.
- `projects/websites/vital-health-review/media/design.md` — the rulebook.

## Decisions

- The hummingbird mark is a **filled silhouette**, not an outline. Generated `vh-bird-white.png` and `vh-bird-forest.png` from the original outline PNG via flood-fill. Logo shape preserved exactly.
- **Default: one color per post**, chosen by the post's dominant background contrast. White on dark-dominated posts (hormone, moving). Forest on light-dominated posts (intro).
- **Per-slide override allowed** when the default color would blend in. Example: hormone slide 3 (Men) uses forest because its right panel is cream, even though the rest of the carousel uses white. Documented as a new clause in design.md.
- Position: top-right corner, 60/60 padding, 80px tall — for slides where this does not conflict with existing composition. Moving announcement preserved top-left because the right side holds the header text — flagged as a known exception.
- Live deploy uses pixel-level PNG editing (Python PIL): erase the old outline bird with sampled background color, composite the new filled bird. Original HTML source was overwritten earlier in the session and is gone, so this is the only path forward for these specific posts.

## Open Questions

- **Bird size mismatch across posts.** Hormone and moving use 80px. Intro uses ~56px (legacy, baked into base64-embedded photographic slides). Per the "same size on every post" rule, intro should be enlarged — but doing so cleanly requires either the source PNGs (lost) or destructive editing over photographic backgrounds.
- **Moving announcement bird position.** Currently top-left to preserve the header text composition. Per design.md the rule is top-right. Annabel chose to accept this as a documented exception rather than re-arrange the poster.
- **Instagram publishing.** These live previews on Vercel are not the actual Instagram posts. Whether to push these as the published versions is a separate handoff.

## Next Steps

- Decide whether to standardize intro carousel to 80px (would need a re-render of the original intro slides from source — verify if the source HTML/PNGs are still recoverable from any other folder before committing to destructive edits).
- Decide on moving announcement: keep top-left exception or rebuild with bird top-right.
- Promote `skills/instagram-carousel/references/style.md` with the filled-silhouette rule and per-slide override clause so future brands inherit them.
- Apply the same bird treatment to the peptides + regenerative test carousels in `media/2026-06-08-*/` so they're consistent with the new rule.

## Files Touched

- `projects/websites/vital-health-review/media/design.md` — added Hummingbird Mark rewrite (filled silhouette, post-level color with per-slide override, asset file paths).
- `projects/websites/vital-health-review/media/vh-bird-white.png` — new asset.
- `projects/websites/vital-health-review/media/vh-bird-forest.png` — new asset.
- `projects/websites/vital-health-review/client-share/vital-health-hormone-carousel/slide-{1..4}.png` — bird swapped to filled (white on 1, 2, 4; forest on 3).
- `projects/websites/vital-health-review/client-share/vital-health-hormone-carousel/we-are-moving.png` — bird swapped to filled white at top-left.
- Production Vercel deployment: `dpl_9iGzt1z6jNtdGTxqpdEDuubFWmjL`.

## Earlier Work This Session (still relevant)

- design.md got Slide Types (Cover vs Info), Topic Theme Kit, Slide-Level Conventions, Pre-ship Audit Checklist sections.
- Hormone carousel was re-rendered to match the new layout rules at `media/2026-06-07-hormone-optimization-carousel-fresh/` — but the published Vercel version is the ORIGINAL layout with only the bird swapped. The two are different versions of the same carousel. Annabel chose to keep the original layout and only update the bird.
- Two stress-test carousels exist at `media/2026-06-08-what-are-peptides-carousel/` and `media/2026-06-08-regenerative-medicine-carousel/` — they still use the old outline bird and need to be updated to the new filled assets when revisited.
- Earlier checkpoint: `operations/memory/checkpoints/2026-06-08-1130-vital-health-instagram-design-rules.md`. This one supersedes it for the bird work.
