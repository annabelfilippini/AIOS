---
date: 2026-06-20
time: 15:21
project: websites / freeyourmind-tarifa
status: in-progress (homepage done with real IG photos + their real copy; inner pages still unbuilt)
next-session: Build the inner pages (Courses, Offers, Accommodation, Tarifa, Contact) — only the homepage exists. Use the same warm-cinematic lane + their REAL site copy (content.md), no invented taglines. Optional polish: a muted reel as a hero background loop (25 reels in assets/web/photos/instagram/). Pre-launch still pending: confirm IKO/VDWS + prices, get reviewer permission before quoting live.
supersedes: 2026-06-14-2105-freeyourmind-tarifa-logo-reviews-accolades.md
---

# Session: Free your Mind — Instagram unblocked, real photos + real copy

## What this session resolved

Picked back up on the FyM (second Tarifa kite school) redesign. Three things
landed: Instagram pull, copy regrounded in their real words, real photos swapped
into the homepage. Homepage built + verified; inner pages still don't exist.

## 1. Instagram UNBLOCKED (the long-standing blocker)

- Old @fym_experience handle (linked from their stale 2018 Jimdo site) is DEAD.
  Annabel found the live one: **@free_your_mind_experience**.
- Firecrawl can't touch instagram.com. Working method = `gallery-dl
  --cookies-from-browser chrome` (her logged-in session). Anonymous gallery-dl
  returns "user could not be found" = login gate, NOT a dead account.
- Pulled most recent 40 posts -> `assets/web/photos/instagram/`: 8 photo posts
  (one is a 7-image carousel) + 25 reels. Best image: sunset surf (♥358,
  3742393460). Reels are 1080x1920 vertical action.
- Saved reusable reference memory `reference-instagram-scraping` + MEMORY.md line.
- Built `instagram-picksheet.html` (+ Desktop copy) — branded contact sheet,
  base64-embedded, photos + reel poster frames, for review.

## 2. Copy regrounded in their REAL words (Annabel flagged invented taglines)

- She caught "Learning to kite should feel warm, not scary" as exactly the kind
  of invented marketing tagline she hates. ALL invented headings/prose replaced
  with their live-site language (scraped via Firecrawl) or plain labels:
  "What to expect on your kitesurfing holidays in Tarifa", "Our specials",
  "Kitesurf Tarifa", "Morocco camps", "Rated 5.0 on TripAdvisor", "Where to
  stay", "Tailor made trips, all year". Body uses their real prose (pristine
  waters / Costa de la Luz / chiringuitos / no-wind activities / "no one does it
  the way we do").
- Promoted the rule to GLOBAL `projects/websites/design.md` (Content section):
  client sites use the client's own words or plain labels, never fabricated
  taglines — with her flagged examples named. Also feedback memory
  `no-invented-headings` (+ MEMORY.md line). Fixed dead footer IG handle.

## 3. Real photos swapped in (Annabel: "you call the shots")

Curated via ImageMagick montages of all photos + reel frames. Final:
- hero <- sunset surf silhouette (the one she loves)
- Kitesurf Tarifa band <- bright daytime foil shot over water (contrast vs hero)
- Learn-to-kitesurf card <- instructor w/ gear
- Kite-camps card <- group shot (carousel img)
- Rent-&-supervise card <- rider w/ Flysurfer gear on sand
- KEPT own-gallery yoga / Morocco / CTA (no yoga or confirmed-Morocco in the pull)
- Skipped ALL text-overlay graphic posts (would read as reposts, not a site)
- Replaced gallery originals backed up in assets/web/photos/_gallery-backup/

## Verification

Playwright full-page screenshots each iteration (server :8851; cache-bust images
with ?cb= since img src has no version). All 12 imgs load, 0 broken. Latest:
`fym-homepage-v3.jpeg` (+ Desktop). Note: had to kill an orphaned playwright-mcp
Chrome (PID lock on mcp-chrome-ece883a profile) to free the browser this session.

## Context to preserve

- Files: index.html, content.md, design.md all current (docs updated this
  session). Kept helpers: instagram-picksheet.html, build_picksheet.py. Removed
  scratch make_montage.sh.
- Photos are now a mix of IG pull + their own website gallery — all their real
  content (logo + TripAdvisor badges also legitimately theirs). Still no Unsplash.
- Open (unchanged): inner pages unbuilt; pre-launch fact/permission confirms.
