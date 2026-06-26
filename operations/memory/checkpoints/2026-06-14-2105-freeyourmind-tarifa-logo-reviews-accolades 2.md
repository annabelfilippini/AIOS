---
date: 2026-06-14
time: 21:05
project: websites / freeyourmind-tarifa
status: in-progress (homepage with logo + reviews + accolades; vibe approved by Annabel)
next-session: If she likes it, build inner pages (Courses, Offers, Accommodation, Tarifa, Contact). Decide whether to keep the bright cyan/yellow logo as-is or do a simplified one-colour treatment for tighter harmony with the calm palette. Confirm IKO/VDWS + prices before live; get FyM's own photos (IG @fym_experience) to replace the Unsplash placeholders; get reviewer permission before featuring quotes live.
supersedes: 2026-06-14-2020-freeyourmind-tarifa-new-site-homepage-v1.md
---

# Session: Free your Mind homepage + logo, real reviews, TripAdvisor accolades

## Where it stands

Homepage for the second Tarifa kite school (kitesurf-tarifa-spain.com, "Free your
Mind") is built in the **soft editorial / wellness lane** (warm ivory + terracotta

+ sea-teal, Fraunces serif + Inter, sharp corners), deliberately different from
the Freeride site's cinematic/adrenaline lane. Annabel approved the vibe ("this
looks good") and asked for their logo + reviews + accolades, all now added.

## What was added this session (on top of homepage v1)

+ **Logo** in the header: their real cyan/yellow mark `assets/web/brand/logo.png`
  (pulled from their site). Reads over the golden hero (drop-shadow) and on the
  scrolled ivory header. Footer keeps the elegant text wordmark (the logo's black
  parts vanish on the dark footer). Flagged: the bright logo is a slightly more
  playful energy than the calm palette; offered a simplified one-colour option.
+ **Reviews section** "What people say" (after the teal promise band): real
  TripAdvisor data scraped this session, **5.0 / 350 reviews / #3 of 27 classes
  in Tarifa**, plus three real review quotes as sharp white cards with gold stars
  (Kai E, Veronica S, Dennis). All facts in content.md.
+ **Accolades** row "Awarded by TripAdvisor": their own badge images for
  Certificate of Excellence **2016, 2017, 2018, 2019** + **Travelers' Choice 2020**
  (`assets/web/awards/`). The promise band's TripAdvisor line was upgraded to the
  real 5.0/350/#3 numbers.

## Decisions

+ Using their own logo + TripAdvisor award badges on their own redesign is fine
  (their brand + trust marks they legitimately hold). Distinct from the photo rule
  (still no copyrighted FyM photos; site photos remain Unsplash placeholders).
+ Reviews must be REAL (no invented testimonials): scraped from TripAdvisor, quoted
  faithfully, flagged [recheck] + get permission before live.
+ Footer stays a text wordmark, not the logo (dark bg eats the logo's black ink).

## Context to preserve

+ Preview: local server **port 8848**, `http://localhost:8848/index.html`
  (cache-bust `?v=`). Also opened the file directly in her browser for review.
+ Verified with Playwright per the new global rule (absolute screenshot filename;
  force-reveal `.reveal` els before full-page capture or off-screen sections shoot
  blank). Desktop 1440 + mobile 390: logo reads in both header states, reviews
  stack, accolade badges wrap, console 0 errors.
+ Assets: `assets/web/` (11 Unsplash photos) + `assets/web/brand/logo.png` +
  `assets/web/awards/` (5 TripAdvisor badges + guarantee.png). content.md +
  design.md updated (new Accolades/Reviews facts; logo line; two iteration entries).
+ Also this session: added a Verification note to the GLOBAL
  `projects/websites/design.md` (open finished sites in a real browser every time;
  Playwright screenshot mechanics).
+ Tree note: AI-OS working tree remains large/dirty from prior sessions; only the
  freeyourmind-tarifa files, the global websites design.md note, and checkpoints
  changed across this session.
