# Checkpoint: Annabel Site — Relocation + Jenna-style Redesign

Date: 2026-05-12 09:05
Project: `projects/site/`

## Direction

Annabel's personal site is being styled after `jennakutcher.com/`:
hero with confident centered portrait → giant editorial name behind → flow
down into an oversized about paragraph with highlighted words. Annabel
likes Jenna's editorial serif typography and the AF circle, but did **not**
want the rotating "Nice to meet you" ring around it.

The site is still moving toward the broader pivot captured in
`2026-05-12-0836-annabel-ai-site-audit-broker-pivot.md`:

> AI business auditor + implementation matchmaker.

This checkpoint only covers the design/relocation pass, not the offer
restructure.

## Project Relocation

Site moved from a Cooldown-nested path to a top-level project folder.

- Old: `projects/consulting/prospects/cooldown/annabel-ai-site/`
- New: `projects/site/`

The python preview server has been restarted from the new path and is
serving `http://127.0.0.1:4174/` (returns `200 OK`).

Restart command:

```bash
cd projects/site
python3 -m http.server 4174
```

## Files In `projects/site/`

- `index.html`, `website-audit.html`, `ai-systems.html`, `toolkit.html`,
  `lab.html`, `about.html`, `contact.html`
- `styles.css`, `script.js`
- `assets/img/annabel-headshot-cutout-web.png` (despilled, see below)
- `assets/img/annabel-headshot-cutout.png` (high-res cutout, unchanged)
- `assets/img/annabel-headshot-original.jpeg`
- `assets/img/annabel-headshot-web.jpg`

## What Changed Today (post-pivot checkpoint)

### Headshot — green halo fixed

`annabel-headshot-cutout-web.png` had a bright lime-green patch under the
hair on the left from an incomplete chroma cutout. Despilled with
ImageMagick by capping the green channel at `max(R,B)` per pixel:

```bash
magick input.png -channel G -fx "min(g, max(r, b))" +channel output.png
```

Lime halo is gone; hair edges read natural against the pink hero. A second
alpha-cleanup pass was attempted but washed the whole image out (the
formula keyed on green-dominant pixels caught warm hair tones too). That
attempt was reverted; the simple despill alone is what shipped.

### Badge — AF only, no rotating ring

Replaced the SVG `<textPath>` ring that said `NICE TO MEET YOU • …` with a
plain solid disc:

- HTML: `.meet-badge` → `.af-badge` (single child `<span>AF</span>`)
- CSS: removed SVG/circle/text/textPath rules and the `spinBadge` keyframe
- Removed the redundant `Nice to meet you` eyebrow above the about copy
- Mobile rule renamed from `.meet-badge` to `.af-badge`

### Typography — Fraunces + Public Sans

Added Google Fonts to every page `<head>`:

```html
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,300;9..144,400;9..144,500;9..144,600&family=Public+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet" />
```

Font picks based on inspecting `jennakutcher.com` in browser devtools:

- Jenna's display serif: **Reckless Neue Book** (commercial, Displaay)
  → free Google equivalent: **Fraunces** (similar wide editorial high-contrast feel)
- Jenna's body sans: **Circular Book / Public Sans**
  → use **Public Sans** (what Jenna's site also loads)
- Jenna's display sans: Moderat / Flecha — not used here

CSS variables updated:

```css
--serif: "Fraunces", "Reckless Neue", Georgia, "Times New Roman", serif;
--sans: "Public Sans", "Circular", "Helvetica Neue", Arial, ...;
```

### Font sizes — bumped site-wide

| Element            | Before                    | After                              |
|--------------------|---------------------------|------------------------------------|
| `body`             | (no size set), lh 1.55    | `1.08rem`, lh `1.6`               |
| `p, li`            | `0.98rem`                 | `1.13rem`                          |
| `.eyebrow`         | `0.78rem` / `0.13em` track | `0.92rem` / `0.18em` track        |
| `.about-lede`      | `clamp(2.15rem, 5vw, 5.25rem)` | `clamp(2.35rem, 5.4vw, 5.65rem)` |
| `.about-snapshot span` | `0.8rem`              | `0.98rem`                          |
| `.path-card p`     | inherits `0.98rem`        | `1.05rem`                          |
| `.proof-list strong/span` | inherits           | `1.12rem` / `1.05rem`              |
| `.page-heading p`  | `1.08rem`                 | `1.18rem`                          |
| `.hero-kicker`     | `clamp(0.9, 1.3vw, 1.1rem)` | `clamp(1, 1.4vw, 1.2rem)` w/ `0.22em` track |
| `h1/h2/h3`         | weight 500, lh 1.03       | weight 400, lh 1.05, `-0.01em` track |
| `.hero-name`       | weight 500                | weight 400, `-0.025em` track       |
| `.af-badge span`   | `clamp(2.1rem, 4vw, 3.5rem)` | `clamp(2.8rem, 5vw, 4.4rem)`    |

### About copy — professionalized

Old:

> I am a University of Michigan School of Information graduate who studied Information Analysis: the collaboration of technology, people, data, and design.
>
> Now I am starting at Okta, geeking out over AI, and helping small businesses use new tools to work more on the business, not only in it.

New:

> I am a University of Michigan School of Information graduate, trained in Information Analysis — the intersection of technology, people, data, and design.
>
> I am joining Okta as a Product Analyst, while advising small businesses on how to use AI and modern systems to work more on the business, not only in it.

Snapshot pills also professionalized:

- `University of Michigan, School of Information`
- `Product Analyst, Okta`
- `AI strategy & website audits for small business`

## Verification

- `http://127.0.0.1:4174/index.html` returns `200 OK` from new path.
- Playwright loaded the homepage at 1440×900; hero is clean (no green
  halo); AF disc renders; about lede renders in Fraunces at ~78px.
- Mobile media-query rule updated to `.af-badge` (was `.meet-badge`).

## Known follow-ups

1. There is still a *faint* gray/neutral edge where the original green
   was under the hair. It is not visible against the pink hero, but if it
   shows up against a different background section, the cutout may need
   a manual matte refinement (e.g. in Photoshop or remove.bg) rather
   than another despill pass.
2. Other pages (`about.html`, `ai-systems.html`, etc.) inherit the new
   typography but their content hasn't been rewritten in the new
   Jenna-style editorial voice yet. The home page is the only page
   updated for tone today.
3. The broader site pivot to "AI Audit + Agency Matchmaking" is still
   pending — see open questions in the prior checkpoint
   (`2026-05-12-0836-annabel-ai-site-audit-broker-pivot.md`).
4. The site is no longer git-ignored (`projects/site/` is a new
   top-level project folder, not nested under the consulting prospects
   path). Decide whether to commit it or keep it ignored.

## Next Best Steps

1. Decide on the final offer name and headline (audit product naming).
2. Rewrite the homepage architecture around the new business model.
3. Rewrite secondary pages (`about.html`, `website-audit.html`, etc.) in
   the same Jenna-style editorial voice and font scale.
4. Replace the headshot with a fully-clean cutout from the original
   `annabel-headshot-original.jpeg` (use remove.bg or a hand-masked
   export to eliminate the residual gray edge entirely).
