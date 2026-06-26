---
date: 2026-06-16
time: 19:45
project: style-feed (personal shopping feed, "The Edit")
status: Source pipeline hardened + roster cleaned. Next phase (more creators + brand-catalog pulls) scoped, tested feasible, and ready to build pending Annabel's go on scope/cost.
next-session: Build the curation batch (Part A creators + Part B brand pulls below). Verify on :8801 (hard-refresh, recurring stale-cache trap).
---

# Session: The Edit — hardened sources, dropped Alix, scoped the brand-pull phase

## Shipped & verified this session
1. **Hardened the source pipeline.** Brigette Pheloung + Paige Lorenze were read
   from ephemeral `~/.claude/.../tool-results/*.json` paths (a transcript cleanup
   would have silently broken the build). Copied both into
   `data/sources/{brigettepheloung,paigelorenze}.json`, repointed `SOURCES`, and
   added a comment never to point back at `.claude` paths. All sources now
   repo-local.
2. **Dropped Alix Earle** from `SOURCES` per Annabel ("not old money").
3. **Rebuilt OK:** `creators=3 items=179 wearable=116` (was 147 w/ 4 creators).
   Build also reports `broken=51` (dead image URLs) — pre-existing, worth a look,
   not blocking.

## Verified taste profile (from her own 50 likes / 50 passes in feedback.json)
- LOVES: neutral palette, linen / denim / cotton / leather, relaxed / wide-leg /
  straight / a-line / tailored-easy, ballet flats, leather sandals, western boots,
  structured leather bags, quiet brands. High `om` (old-money) + high `neut`.
- REJECTS: fitted / bodycon / clingy, loud color or busy print, novelty/logo
  (trucker caps), satin going-out dresses, crocheted/fringe/novelty bags.
- The scorer already encodes this (`text_score` OLDMONEY+/LOUD−, `color_adjust`
  colorfulness penalty, vision weights, `feedback_adjust`). Brand pulls just run
  through the same pipeline and surface top scorers = "clothes that fit her."

## Part A — creators to add (verified ShopMy handles)
Top 4 to add first: **carlyriordan** (Carly Riordan / College Prepster),
**graceatwood** (Grace Atwood / The Stripe), **merrittbeck** (Merritt Beck /
Style Scribe), **marylawlesslee** (Mary Lawless Lee / Happily Grey — palette match).
Borderline / hold: taramariagonzalez, emilyoberg, juliaberolzheimer, lizadams,
blaireadie. Best taste fit but **NO ShopMy, can't add**: Sarah Vickers (Classy
Girls Wear Pearls). Pull each via Firecrawl `shopmy.us/shop/<handle>` matching the
existing source shape (`load_products` wants `raw[0]["text"]`→json→`obj["json"]["products"]`).

## Part B — brand catalog pulls (feasibility tested live)
Needs a NEW loader: brand catalogs have a different shape than ShopMy and no
"creator" (label source = brand). Run pulls through existing `vision_tag`
(Haiku via `STYLE_FEED_VISION_MODEL=claude-haiku-4-5` to cut cost) + scorer, then
surface only top ~20/brand above a taste threshold.
- **Dairy Boy — EASY.** It's Shopify: pull free JSON at
  `dairyboy.com/collections/clothing/products.json?limit=250` (no Firecrawl).
  Images hotlink. Catalog skews cutesy/novelty (farm-animal prints, gingham
  boxers, sleep sets); her data liked plain sleep sets but passed novelty/
  cashmere-collar/capri, so the ranker will filter — surface the quiet pieces.
- **Revolve — EASY** (is4.revolveassets.com hotlinks). **Zara — EASY**
  (static.zara.net hotlinks).
- **Aritzia — data easy, images 403** (grab og:image from detail page / rehost).
- **Lululemon — data easy**, image from detail-page JSON-LD.
- **Abercrombie — HARD** (force Firecrawl `proxy:"stealth"`).
- **Anthropologie — untested**, needs 1 probe (likely Hard, URBN platform).

## Pending non-feed
- **agency-audit-network deletion HELD.** It nests `dad-pilot/` (Tom's pilot,
  flagged active in memory). Awaiting Annabel: delete all, or preserve dad-pilot
  (move to `projects/dad-pilot/`) first. `rm` is blocked this session (permission
  mode) — use `mv` to `~/.Trash`.
- **freeyourmind-tarifa** already removed (moved to `~/.Trash`, was untracked).
