---
date: 2026-06-07
time: 21:15
project: freeride-tarifa-website
status: in-progress
next-session: Review the Freeride hero collage visually, clean unused failed capture assets, and continue homepage refinement from the live local preview.
---

# Session: Freeride Hero Instagram Collage

## What we worked on

- Iterated on the Freeride Tarifa static preview in `/Users/annabelfilippini/Documents/AI-OS/projects/websites/freeride-tarifa/index.html`.
- User disliked the first collage direction and asked for a packed, no-gap collage next to the “Freeride Tarifa” hero copy.
- Built a full-height hero collage grid that runs from the top of the hero to the bottom on desktop.
- Pulled/captured Instagram post imagery from `https://www.instagram.com/freeridetarifa/` for use in the hero.
- Removed brittle direct Instagram CDN hotlinks from the hero markup and replaced them with local assets.
- User then asked to remove a proof strip under the hero copy and replace a bad tile showing Instagram likes/comments.

## Decisions made

- Hero collage should be a dense image wall with no visible gaps between tiles.
- The collage should sit directly beside the hero copy on desktop, not under/behind it.
- On mobile, the collage can move below the copy as an edge-to-edge image block.
- The hero should not include the three proof boxes:
  - “Beginner to independent rider”
  - “French, English and Spanish”
  - “Kite camp, yoga and Tarifa days”
- The Instagram tile with baked-in likes/comments should be replaced with a clean actual photo, not a duplicate or screenshot.

## Open questions

- Need confirm final visual taste with Annabel after the latest cleanup.
- Need decide whether to keep or delete unused failed capture files:
  - `assets/instagram-collage/ig-profile-*.png`
  - `assets/instagram-collage/profile-captures.json`
  - `assets/instagram-collage/ig-post-06-clean.png`
- Need confirm Freeride has usage rights / comfort with Instagram assets before production.

## Next steps

- Open `http://127.0.0.1:8097/` if the local server is still running, or restart it from `/Users/annabelfilippini/Documents/AI-OS/projects/websites/freeride-tarifa`.
- Visually inspect the hero after the proof strip removal.
- Remove unused failed capture files only if safe to clean generated assets.
- Continue refining the homepage design and asset choices.

## Context to preserve

- Current changed site file:
  - `/Users/annabelfilippini/Documents/AI-OS/projects/websites/freeride-tarifa/index.html`
- New local Instagram asset folder:
  - `/Users/annabelfilippini/Documents/AI-OS/projects/websites/freeride-tarifa/assets/instagram-collage/`
- Clean downloaded replacement for the bad likes/comments tile:
  - `assets/instagram-collage/ig-post-06-direct.jpg`
- The bad baked-in screenshot tile was originally `ig-post-06.png`.
- Browser QA already confirmed after the latest patch:
  - `.hero-proof` no longer exists.
  - `m11` uses `assets/instagram-collage/ig-post-06-direct.jpg`.
  - No hero collage images were broken.

## System refinement candidates

- For Instagram-derived website assets, prefer downloading the image source directly when available. Browser element screenshots can accidentally include hover states, cookie dialogs, or login modal overlays.
- When replacing a disliked collage tile, verify the exact tile class and image source before patching so the asset is replaced rather than visually shuffled.
