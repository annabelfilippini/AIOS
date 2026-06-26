---
date: 2026-06-17
time: 12:29
project: style-feed (personal shopping feed, "The Edit")
status: DONE + verified on-screen. Feed live with 958 items, vision-tagged on Haiku (1042/1043). Brand cut: Dairy Boy 24 (capped), Zara 16, Revolve 3 (205 dropped). Top of feed reads on-taste (wide-leg denim, neutral trousers, riding boots, beige knits); "why" lines + co-signs render correctly.
next-session: Open levers — (1) Revolve only surfaced 3 because the pulled catalog was party/going-out heavy; re-pull a cleaner Revolve collection (linen / quiet labels) if she wants more from them. (2) Round-2 brands still deferred (Aritzia/Lululemon/Abercrombie/Anthropologie — each needs an image or proxy step). (3) Tune BRAND_MIN_SCORE (56) / BRAND_KEEP (24) if brand cut feels thin/loose — caches warm, rebuild is fast. (4) Consider a per-creator cap (Carly alone is 504 raw). View live at localhost:8801/feed.html (hearts POST to data/feedback.json) or ~/Desktop/the-edit-feed.html. Preview server config "style-feed-shot" added to .claude/launch.json on port 8813.
---

# Session: The Edit — added 4 creators + a brand-catalog pull pipeline

## Shipped this session (in order)
1. **Hardened sources** — Brigette Pheloung + Paige Lorenze were read from
   ephemeral `~/.claude/.../tool-results/*.json`; copied into
   `data/sources/{brigettepheloung,paigelorenze}.json` and repointed `SOURCES`.
2. **Dropped Alix Earle** ("not old money").
3. **Added 4 verified old-money creators** (ShopMy storefronts pulled via
   Firecrawl into `data/sources/`): carlyriordan (504), graceatwood (169),
   merrittbeck (225), marylawlesslee (39).
4. **Built the brand-catalog pipeline** in `build_feed.py`:
   - `BRANDS` config + `BRANDS_DIR = data/brands`; `BRAND_KEEP=24`,
     `BRAND_MIN_SCORE=56`.
   - Refactored the merge into `_ingest(name, path, is_brand)` tracking two sets
     per item: `creators` (hand-picked, always kept) and `brands` (catalog,
     trimmed). Display + co-sign use `creators | brands`.
   - Curation step after the score-sort: brand-only items keep just the top
     `BRAND_KEEP` per brand that also clear `BRAND_MIN_SCORE`; everything else
     dropped. Summary prints `brand_kept={...}`.
5. **Pulled 3 brand catalogs** into `data/brands/` (same `{"json":{"products":
   [...]}}` shape): dairyboy (137, via free Shopify JSON
   `dairyboy.com/collections/clothing/products.json?limit=250`), revolve (110,
   43 designer brands, Firecrawl), zara (75, Firecrawl).
6. **Validated the API key** with a live Haiku call (108 chars, `sk-ant-`, OK)
   before the long run, then launched the rebuild with
   `STYLE_FEED_VISION_MODEL=claude-haiku-4-5` (Haiku to cut cost ~5x).

~1,377 raw products in; compiles clean; only intended `it["creators"]` refs
remain. feed.html auto-copies to `~/Desktop/the-edit-feed.html`.

## Tunable knobs (first thing to revisit after seeing the cut)
- `BRAND_MIN_SCORE` (56) — raise for a tighter, smaller brand cut; lower if a
  brand surfaces too few. `BRAND_KEEP` (24) — max per brand.
- Creator storefronts are NOT score-capped (Carly alone is 504 raw); if the feed
  feels flooded, consider a per-creator cap too.

## Deferred (round 2, all need an extra step)
- Brands: **Aritzia** (images 403, need rehost/proxy), **Lululemon**
  (image from product detail page), **Abercrombie** (Firecrawl `proxy:"stealth"`),
  **Anthropologie** (untested, needs one probe).
- Creators (borderline, lean color/trend): taramariagonzalez, emilyoberg,
  juliaberolzheimer, lizadams, blaireadie. Best fit but **no ShopMy**: Sarah
  Vickers (Classy Girls Wear Pearls).

## Pending non-feed
- **agency-audit-network delete HELD** — nests `dad-pilot/` (Tom's pilot, flagged
  active in memory). Awaiting Annabel: delete all, or preserve dad-pilot (move to
  `projects/dad-pilot/`) first. `rm` blocked this session → use `mv` to `~/.Trash`.
- **freeyourmind-tarifa** already removed (Trash).
