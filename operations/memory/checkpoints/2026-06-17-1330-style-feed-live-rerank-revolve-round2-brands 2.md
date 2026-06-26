---
date: 2026-06-17
time: 13:30
project: style-feed (personal shopping feed, "The Edit")
status: SHIPPED + verified on screen. Live in-browser rerank now real (no rebuild per swipe). Revolve re-pulled to quiet/neutral (3 -> 24 kept). Anthropologie + Abercrombie added. Rebuilt to 1002 items on Haiku, 124/71 feedback baked.
next-session: (0) BUILD A DAILY-SCRAPE SCRAPER, then REMIND ANNABEL to add a /schedule routine that runs it daily across all her stores, surfacing new clothing items it predicts she'd like (she explicitly asked to be reminded once the scraper is built). (1) Aritzia still wanted but BLOCKED (Cloudinary 403 from any non-aritzia origin; image won't load in her browser either) -> only solvable by self-hosting images (download at build to data/img + base64/local path), which bloats the 1.2MB feed. Decide if worth it. (2) Lululemon parked (athleisure niche; image must come from PDP, not grid). (3) Abercrombie only 5 items (stealth scrape was partial); could pull more tailored-trouser pages. (4) Revolve listing pages first-paint ~16; /v/ SEO pages yield better quiet catalogs than /br/ collection pages.
---

# Session: The Edit — live rerank + better Revolve + round-2 brands

## The big win: taste now evolves live, no rebuild per swipe
Before today every heart/x only REMOVED the card + saved the signal; the order was
fixed at build time (build_feed.py:663 even said so). Rebuild was the ONLY way taste
reshaped ranking. Now:
- build_feed.py emits a cold, feedback-free `data-base` score per card.
- SCRIPT has buildProfile()/liveScore()/rerank() (mirrors vision_adjust +
  feedback_adjust); applyView() calls rerank() first.
- Every heart/x rebuilds the liked/disliked centroid in-browser and re-sorts all
  1002 cards. VERIFIED: hearting 12 items moved 986/1002 cards, max shift 325, top
  changed. Zero server round-trip.
- Two-tier model now: LIVE rerank every swipe (taste compounds); REBUILD only to add
  NEW inventory (can't surface items not in the HTML).

## Inventory changes (one rebuild baked all of it)
- revolve.json rebuilt from party-catalog to 33 quiet/neutral items (linen collection
  /occasions/linen/br/a3ffe2 + linen-trouser /v/white-linen-pants). Kept 3 -> 24.
  CDN is4.revolveassets.com hotlinks fine.
- anthropologie.json (11 items, images.urbndata.com OK) -> 10 kept.
- abercrombie.json (5 items, img.abercrombie.com Scene7 OK, scraped with proxy:stealth).
- Registered both in BRANDS. Rebuild: 1002 items, vision tagged 984/985 on
  claude-haiku-4-5, feedback liked=124 disliked=71.
- Aritzia DROPPED: assets.aritzia.com Cloudinary 403s the build UA AND a correct
  Referer AND weserv proxy. Won't render in her browser -> unusable without self-host.

## State / how she uses it
- serve.py on :8801 (feed.html), POSTs hearts to data/feedback.json. Desktop copy at
  ~/Desktop/the-edit-feed.html. Preview launch config name: `style-feed`.
- feedback.json verified intact at 124/71 after testing.

## Open thread: daily auto-scrape routine (Annabel's ask)
- She wants a scheduled routine that scrapes ALL her stores daily for NEW arrivals and
  surfaces the ones it predicts she'd like, feeding The Edit automatically.
- She asked to be REMINDED to add the /schedule routine ONCE the scraper is built —
  the scraper comes first, the routine wraps it. Don't offer the routine until the
  daily-scrape script exists.
- Today's pulls were ad-hoc Firecrawl scrapes saved to data/brands/*.json by hand; the
  scraper would generalize that into a repeatable per-store new-arrivals pull + merge +
  rebuild. No such script exists yet (build_feed.py only reads existing JSON).
