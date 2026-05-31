# Checkpoint: Annabel AI Personal Site Prototype

Date: 2026-05-11
Project: `projects/consulting/prospects/cooldown/annabel-ai-site`

## Current Direction

Annabel is building a personal professional site that is part LinkedIn, part services page, part living lab. The site should position her as a human-first AI tinkerer who helps small businesses use AI to work on the business, not just in it.

Core message:

> Use AI to work on the business, not just in it.

Human-first framing:

> AI should not replace the parts of work people love. It should take pressure off repetitive work so owners can get back to creativity, strategy, customers, community, and the reason they started.

## Visual Direction

Annabel likes Jenna Kutcher-style layout: large name behind the person, cutout portrait in front, short supporting phrases on the left/right of the body, bold simple top navigation.

Color direction comes from Annabel's reference images but the images should not appear on the site. Palette should stay earthy, warm, feminine-but-not-cheesy: rose, clay red, warm ivory, muted pink, deep green accents.

Current hero is more Jenna-inspired:

- Top nav on rose background
- Oversized `Annabel / Filippini` behind portrait
- Cutout headshot in front
- Left/right supporting phrases
- CTAs near the bottom

## Built Files

- `annabel-ai-site/index.html`
- `annabel-ai-site/styles.css`
- `annabel-ai-site/script.js`
- `annabel-ai-site/assets/img/annabel-headshot-original.jpeg`
- `annabel-ai-site/assets/img/annabel-headshot-cutout.png`
- `annabel-ai-site/assets/img/annabel-headshot-cutout-web.png`
- `annabel-ai-site/scripts/make_cutout.swift`
- `service-offer/personal-ai-site-plan.md`

Local preview is running at:

- `http://127.0.0.1:4174`

## Headshot Work

Annabel provided `/Users/annabelfilippini/Desktop/DSC_3746.JPEG`.

A local macOS Vision cutout was generated using `scripts/make_cutout.swift`. It required escalated execution because Vision inference was blocked by sandbox entitlements.

The cutout is usable for prototype but has visible edge artifacts around hair and a little remaining green from the original background. A final launch version should use either:

- a cleaner manual cutout pass, or
- a headshot taken against a simpler background.

Do not over-clean the cutout with aggressive green removal; one attempt damaged face/hair areas and was reverted.

## Business Review Notes

Garry reviewed the prototype and said the direction is strong, especially:

- AI tinkerer + website-first entry point
- Human-first AI message
- Toolkit and Lab as differentiators
- Warm visual direction

Main critique: the site risked feeling too broad. Tighten toward:

> Sharp AI tinkerer who can help my small business get clearer, save time, and move faster.

Changes already applied from review:

- Added clearer `best for` language on Website Audit
- Added Week 1 / Week 2+ first-project framing
- Simplified AI Automation into four useful starting points
- Softened Comfrt into a learning example, not a credibility centerpiece
- Made Lab cards ask for specific feedback
- Translated Toolkit jargon into business outcomes

## Site Structure

Navigation:

- Home
- Website Audit
- AI Automation
- Toolkit
- Lab
- About
- Contact

Pages/sections currently exist in one static page with anchors.

## Important User Preferences

- The site should feel professional, not too AI-generated.
- The words were previously too large; keep typography proportional and readable.
- Do not show the tone reference images as content.
- Use reference images only to inform palette.
- Annabel likes Jenna Kutcher and Gemma-style personal hero layouts.
- She likes the person centered, looking at camera, making the visitor feel like they are talking to her.
- Keep earthy reds/pinks, but not harsh colors.
- Flowery/botanical influence is okay, but not cheesy.

## Next Best Steps

1. Refine hero spacing and hierarchy after Annabel reacts to the Jenna-inspired version.
2. Decide whether to keep current rose/yellow combo or shift yellow toward softer cream/ivory for a less literal Jenna feel.
3. Improve cutout quality or replace with a cleaner headshot.
4. Tune nav labels to match final site architecture.
5. Add real contact email to `script.js` mailto.
6. Add more concrete copy for Wayloft and Spent.
7. Consider separating the one-page prototype into real pages once content direction is approved.

## Current Caveats

- `annabel-ai-site/` is ignored by root `.gitignore` via `projects/*`, so git status from this repo may not show these files unless force-added or moved.
- Local preview server was started with `python3 -m http.server 4174` from `annabel-ai-site` because port 4173 was occupied.
- Browser QA found no console errors after latest checks.
