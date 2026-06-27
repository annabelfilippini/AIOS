---
date: 2026-06-26 20:45
project: stoop
status: in-progress
type: checkpoint
slug: stoop-deeper-lacrosse-theming
---

# Stoop — deeper lacrosse theming on cousin-lacrosse.html

Follows `2026-06-26-2017-stoop-project-folder-and-cousin-lacrosse-page.md`.
Annabel picked "deeper lacrosse theming" (her photo as hero, stick motifs,
custom title font) over the availability editor / builder flow this session.

## Key design call: sport layer is color-agnostic
Lacrosse identity lives in the SPORT layer (motifs, avatar, title font); color
stays the MOOD layer (the 6 swatch themes). They're orthogonal, so pink-default
+ crossed sticks = pink crossed sticks. Verified the motif tints correctly under
both pink and lacrosse-green. This resolves the earlier tension (cousin wants
pink AND "true lacrosse themed").

## What changed (all in cousin-lacrosse.html)
- **Hero avatar:** dropped the "M" monogram. Now JS-rendered from a `PHOTO`
  const — `const PHOTO=''` → falls back to a crossed-lacrosse-sticks-and-ball
  SVG (accent-tinted). Drop Maddie's real photo URL/path into PHOTO and it
  shows her photo (object-fit cover). This IS the "her photo as hero" slot,
  ready, just no real photo on disk yet (references/ is empty).
- **Hero motif:** faint crossed-stick watermark (top-right) + a field
  center-line with midfield circle, both tinted by `--heroText` so they follow
  the theme. `.hero` is now position:relative/overflow:hidden; content sits at
  z-index 1.
- **Athletic title font:** added Anton (jersey/varsity condensed), applied to
  the hero `h1` only (uppercase). Fredoka stays for section headers, Nunito for
  body. Dropped Caveat already gone from prior session.
- **Mobile:** watermark scaled down (140px, opacity .09) in the <=680px query so
  it stays texture, not a scissor-ish focal shape.

## Verified (playwright, localhost http.server)
Desktop + 390px mobile, pink + green themes. Anton title wraps cleanly 2 lines
on mobile, avatar reads as crossed sticks, motif tints per theme. Only console
error is favicon 404 (harmless). Shots in `projects/stoop/shots/`:
lacrosse-themed-hero/full/green/mobile2.png.

## NEXT (unchanged options, minus this one)
- **Real photo:** drop Maddie's photo into the `PHOTO` const (needs the actual
  image first — ask Annabel).
- **Availability editor** — kid sets her own open times (pattern still hardcoded
  Tue/Thu 4-5:30 / Sat am). The real next build.
- **Builder flow** — the 4-5 questions that generate a page from nothing.
- **The feed** — pages collect, hyperlocal scoping rule (feed-era only).

Still no code committed (concept/preview stage). Working tree has uncommitted
edits to cousin-lacrosse.html.
