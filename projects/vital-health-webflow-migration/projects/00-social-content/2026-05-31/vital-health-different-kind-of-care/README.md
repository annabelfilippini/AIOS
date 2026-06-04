# Vital Health Carousel Pilot

This is a Codex-assisted dry run of the Scrapes `00-social-content` output shape.

## What Is Real

- Brand context has been seeded in `brand_context/`.
- Caption, metadata, HTML preview, and 5 rendered PNG slides are saved here.
- The output uses Vital Health's existing logo, colors, and homepage still-life image.

## What Is Not Yet A Full Native Scrapes Run

- Claude Code's `/00-social-content` slash pipeline was not executed from Codex.
- The full `mkt-visual-identity` Template Factory has not generated native Scrapes template files.
- `brand_context/templates/instagram-carousel/manifest.json` is marked `pilot`, not `ready`, so Claude does not mistake this for a completed template pool.

## Next Best Test

Open this folder's `index.html` or the PNG slides and judge whether the visual/content direction is good enough. If yes, run the Scrapes visual identity/template setup in Claude Code using these files as references.
