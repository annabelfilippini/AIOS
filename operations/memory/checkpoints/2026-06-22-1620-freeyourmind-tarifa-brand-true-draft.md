---
date: 2026-06-22
time: 16:20
project: websites / freeyourmind-tarifa
status: DONE this session — brand-true homepage approved ("this is epic") + DEPLOYED to https://freeyourmind-tarifa.vercel.app/ (public). NEXT: build the inner pages in the brand-true system, then resolve confirm-before-launch items before any custom domain.
next-session: Build inner pages (Lessons, Camps, Stay, Contact) in the brand-true system (cyan/yellow/Urbanist, plain noun titles, "Message us on WhatsApp"/"Offerings" buttons), matching the homepage. Then resolve the confirm-before-launch list (review permission, full team roster, current email, prices to WhatsApp) before pointing a custom domain. Live homepage = index.html (brand); espresso preserved at index-espresso.html.
supersedes: 2026-06-21-1540-freeyourmind-tarifa-polish-qa-outreach.md
---

# Session: Free Your Mind — brand-true redraft (start from THEIR side)

## The pivot (Annabel's idea)

On a walk Annabel realised she has been building generic-to-her sites for
businesses full of their own personality. The existing FyM site uses their real
photos + copy but is still HER house lane (Fraunces serif / warm espresso /
sunset coral). It is their content in her mould — the old brief even contemplated
recolouring their own logo so it stopped "fighting the palette." New method: full
audit + scrape of all their channels, then build FROM their identity (colours,
type, founders, story, voice), not her preferences. She wanted to try it on FyM.

## What I did

1. **Grounded in prior work** (3 sites: legacy Jimdo EN/DE + the real WordPress
   freeyourmindexperience.com; IG already pulled; espresso draft fully built/QA'd).
2. **Brand audit** via Firecrawl `branding` extract + their logo + About page:
   - Real palette: yellow `#F8EC1E`, cyan `#4DC0E2`, magenta `#CC3366`, white/black.
   - Type: Urbanist + Barlow (rounded geometric sans). Rounded pill buttons.
     Logo = cyan/yellow paint-splatter, playful/street-beach.
   - Their own site self-describes: playful, high energy, young & adventurous.
   - Voice surprise: mindful/conscious ("feel the wind, listen to your body, let
     go of the noise", "part of the family", conscious tourism).
   - = a **duality**: loud playful surface over a calm soulful core.
   - Founder: Tanja Rosenkranz (decade competing/teaching, Flysurfer distributor).
     Team: Lilli, Ingo, Gonzalo, Cris, Wiebke, Andrea. Camps: Tarifa, Conil,
     Dakhla, Essaouira, Sri Lanka. Base: Los Lances Norte.
3. **Asked the one real fork** (how loud vs how calm). Annabel chose **the duality**.
4. **Built `index-brand.html`** — standalone, their real brand system, their exact
   copy, the duality structure (hero → yellow intro → services → dark soul → cyan
   pillars → founder+team → dark Tarifa/camps → review marquee → glow CTA → footer).
   Pulled real team/camp photos into `assets/web/photos/site/`. Kept the espresso
   `index.html` untouched for side-by-side comparison.
5. **Verified** (Playwright, fym-tarifa server :8849, /index-brand.html): desktop +
   mobile 390, console clean, 0 broken images, fixed mobile footer overflow,
   scrubbed dash punctuation, de-duplicated Tanja's photo. Ship Gate passed.
6. **Docs updated:** content.md (real team, founder story, destinations, brand
   tokens, current site/email) + design.md (full iteration entry + confirm-list).

## Confirm before launch

Review permission for quotes; heading "Every experience is built to bring
something back" is a paraphrase (their line: "every experience we offer is
designed to bring something positive") — confirm/swap; full roster + roles;
current contact email (freeyourmindexperience.com vs old kitesurf-tarifa-spain.com);
prices still routed to WhatsApp.

## Files

- New: `index-brand.html`, `assets/web/photos/site/*` (tanja, lilli, ingo,
  gonzalo, cris, wiebke, camp-hero, philosophy, tarifa-place), `assets/web/brand/favicon.webp`.
- Updated: `content.md`, `design.md`.
- Server: launch.json `fym-tarifa` (python http on :8849, serves the project).
