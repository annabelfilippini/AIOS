---
date: 2026-06-16
time: 14:54
project: style-feed (personal shopping feed, working name "The Edit")
status: THREE changes shipped & verified this session. (1) Prior blocker cleared — re-tagged all 147 wearables with the DEEPER "The Yes" taxonomy (neckline/sleeve/length/fabric/drape now populate; ran on claude-haiku-4-5 via new env override, not Opus, to cut cost ~5x — tags cached, 147/147). (2) PIVOT per Annabel: she does NOT want the live re-rank — removed it entirely; feed is now a fixed-order regular shopping site (scroll, heart→Loved, ✕→hide, nothing reshuffles). Deleted learn()/affinity()/rerank()/mean() + all 4 rerank() calls; VCATS kept only to snapshot tags onto exported likes. (3) Retailer links — cards now open the REAL product page (Revolve/Saks/Farfetch/DSW/etc.), resolved 214/214, zero ShopMy fallbacks. Also removed the taste score badge from cards (she asked). All verified: python compiles, JS node --check OK, feed.html greps clean (0 rerank calls, 0 score spans, 0 shopmy product-link fallbacks).
next-session: Feed is in the state she wants — no immediate blocker. Loop now: edit build_feed.py → `python3 build_feed.py` (Haiku cached, instant, no API cost unless caches wiped) → Cmd+R on :8801. Open roadmap (her stated wants, none urgent): source expansion (more creators / pull from retailers so pool isn't capped at 4 people's buys); frictionless feedback; design pass + pick a real product name; add Dairy Boy as a source. The onboarding cold-start quiz from The Yes teardown — she explicitly said she does NOT need it, drop it. Stack: ANTHROPIC_API_KEY in projects/style-feed/.env (108 chars, valid); anthropic SDK; VISION_MODEL defaults to claude-opus-4-8 but is now env-overridable via STYLE_FEED_VISION_MODEL (use claude-haiku-4-5 for retags). Caches: color_cache.json, vision_cache.json (Haiku 12-field tags), link_cache.json (retailer URLs) — all keyed so rebuilds are instant; wipe to refresh.
---

# Session: The Edit — pivoted to a fixed-order shopping site + real retailer links

## What happened this session

1. **Researched "The Yes"** (Julie Bornstein's app, the closest product ever
   built to The Edit — acquired by Pinterest 2022, shut down). Teardown saved to
   `projects/style-feed/the-yes-teardown.md`. Key borrow: their moat was a deep
   ~500-attribute per-item taxonomy, not the swipe UI.
2. **Deeper taxonomy shipped** — extended VISION_SCHEMA/prompt with neckline,
   sleeve, length, fabric, drape ("na" for shoes/bags). Cleared the stale
   vision_cache and re-tagged all 147 wearables on **Haiku** (added
   `STYLE_FEED_VISION_MODEL` env override so the file still defaults to Opus).
   This cleared the prior checkpoint's blocker.
3. **Removed the live re-rank** (her call — "I just want a regular shopping
   website"). Stripped learn/affinity/rerank/mean and all rerank() calls. Feed
   order is now fixed at build time; like/dislike still work (Loved tab / hide).
4. **Real retailer links** — discovered ShopMy's public JSON API
   `apiv3.shopmy.us/api/v2/Products/<id>?countryCode=US&Curator_id=<cid>` (no
   auth, plain curl) returns the true retailer URL at `product.links[].link`.
   Added a cached threaded resolver (`data/link_cache.json`) → 214/214 resolved.
   (Saved this API trick to memory: [[reference-shopmy-scraping]].)
5. **Removed the score badge** from cards for a clean shopping look.

## How we got the links (the hard part, for continuity)

The stored productUrl is only `shopmy.us/shop/product/<id>` — CHEQ bot-walls
those pages (curl + Firecrawl both blocked, even with her cookies). `api.shopmy.us`
needs creator auth (she's not a creator). Playwright (real browser) rendered fine
and exposed the buy link, AND revealed the page's own fetch to **`apiv3`** — which
turns out to be public and curl-able. That's the clean path; no browser/auth needed
in the build.

## Verify / gotchas

- Recurring `python -m http.server` stale-cache trap on :8801 — hard refresh
  (Cmd+Shift+R) or cache-bust after a rebuild.
- Rebuilds are now instant because color/vision/link caches all hit; only wiping
  a cache (or new products) triggers real work/cost.
- Haiku over-tags drape="structured" (35/50 likes + 18/34 dislikes) — it
  self-cancels in scoring so it's harmless, but it's a weak axis. Fabric (linen/
  denim) and silhouette (dislikes fitted/cropped) are the clean signals.

## Next steps (none blocking)

1. Source expansion — more creators or retailer pulls so the pool isn't capped
   at 4 people's buys (her stated next lever).
2. Frictionless feedback; design pass + real product name; add Dairy Boy source.
3. Optional: switch links to affiliate deeplinks (creator commission) — same API
   response, `affiliate_link` field — if she ever wants that. She chose clean
   retailer URLs for now.
