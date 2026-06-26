---
date: 2026-06-21
time: 15:01
project: style-feed (personal shopping feed, "The Edit")
status: in-progress
next-session: Email purchase signal + styling layer SHIPPED and verified in browser. Annabel reviewed nothing live yet this session — show her the Everyday/Shoes/Accessories tabs (italic rose "Goes with / More like your new Zara shorts" reasons). REMAINING TUNING she may want: (1) goes-with still skews to knits/outerwear (cardigans "go with" everything) and to the embroidered shorts — could demote knit pairings or weight striped/other buys up; (2) variety caps are GOES_CAP=110/MORE_CAP=80 with per-buy cap 24 + per-buy-cat cap 8 — adjust if too many/few; (3) decide if "more like" (more shorts) is wanted at all or if she only cares about "goes with" (completing the outfit). REFRESH PATH is manual: re-run the Gmail pull (see below) each time she wants new purchases folded in — it is a Claude/Gmail-MCP step, NOT a cron-able CLI like nuuly-cli. Other deferred direction items unchanged: activewear store (Workout only ~8), undergarments source. The purchase + styling architecture is now the template for any future "owned/recent" signal.
---

# Session: The Edit — Nuuly turned up + email purchases + "goes with your new X" styling

## 1. Nuuly influence turned UP (Annabel asked last session, done first)
All in `build_feed.py`. Added an env-guarded probe and tuned 3 knobs:
- `NUULY_VIS_SCALE/CAP` 0.65/20 -> **0.8/24**
- `NUULY_RENTAL_WEIGHT` 1.75 -> **2.0**, new `NUULY_CLOSET_WEIGHT` 1.0 -> **1.25**
- `nuuly_adjust` brand/cat caps +11/+8 -> **+14/+10**
Verified via NEW probe `NUULY_PROBE=1 python3 build_feed.py` (synthetic relaxed-knit vs
bodycon-satin archetypes): on-taste lift +39->+48, off-taste stays +11->+13, vision GAP
+17->+21 (MORE discrimination), saturation held 9%->10% (no re-saturation). Profile shift:
relaxed silhouette 89->94, cotton up. The probe block lives after the `base` loop and
`sys.exit(0)`s — reuse it before/after any future NUULY_* edit.

## 2. Email purchase signal — STRONGEST owned input (built + verified)
Annabel's real goal (she clarified): "look at my emails, see what I recently bought, then
suggest things that go with it" (e.g. her two new Zara shorts -> cute tops/shoes to pair).
- **Pull:** a general-purpose SUBAGENT used the Gmail MCP (search_threads/get_thread) to pull
  recent (>= 2026-02-21) fashion order confirmations, filtered to HER orders + fashion only,
  deduped per order. Wrote **`data/purchases.json`** (12 items, shape mirrors nuuly.json:
  `{pulled_at, purchases:[{id,source,signal,retailer,brand,name,color,size,price,date,order,img}]}`).
  11/12 have real product images (Zara static.zara.net, Aritzia, Farfetch, GOAT). The pull is a
  Claude/Gmail-MCP step (no CLI) — re-run the subagent to refresh. Queries + rules are in the
  subagent prompt; key gotchas: dedupe shipping vs confirmation emails, drop "Hi Emily/Claire"
  (others' orders forwarded to her inbox), Farfetch greets Emily but ships to Annabel (kept).
  The 12 buys: 2 Zara shorts (striped, embroidered ecru), Abercrombie A-line short, Aritzia
  Butter short + cami + sweatfleece hoodie + Martini satin halter, 3 Zara sleeveless tops,
  2 Onitsuka Tiger Mexico 66 sneakers.
- **Integration (reuse, not a 3rd scorer):** purchases are appended into the SAME
  `nuuly_likes`/`nuuly_pool` as Nuuly (id prefix `buy:`), so ALL machinery (vision tagging,
  N_brand/N_cat centroid, nuuly_adjust, merged Lcounts, Ncounts base prior, nuuly_vision_adjust)
  picks them up free. Only diffs: `PURCHASE_WEIGHT = 2.5` (owned > rental 2.0) + real recent
  dates (so this month's buys dominate recency), and a source-aware why ("You recently bought X"
  vs "You wear X on Nuuly") via `purchase_brands`. Verified: pool 147->159, vision 154/159,
  profile shifted toward her buys (relaxed 94.3, cotton 104, fitted up). Probe gap still +20.

## 3. Styling layer — "Goes with / More like your new <purchase>" (the headline ask)
New pass in `build_feed.py` (after `occasions_of`, before `card`):
- `recent_buys` = purchases within 90d, joined with their vision tags (`_pool_vision`),
  each with cats (classify) + occ (occasions_of) + neutral palette + recency weight.
- `COMPLEMENT` map (bottom<->top/knit/outerwear/shoe/bag/accessory, etc.). `styling_match`:
  SAME category + close palette => **"more like"**; complementary category + SHARED occasion +
  close palette (>=.75) + on-taste (base>=58) => **"goes with"** (gated hard so it's a real
  suggestion, not wallpaper). First cut tagged 775/877 (everything) — fixed with: score per
  match, separate `GOES_CAP=110`/`MORE_CAP=80`, and per-buy (24) + per-buy-category (8, goes
  only) variety caps using SEPARATE counters (sharing one counter starved goes-with — bug).
  Result: 49 goes-with across shorts(18+12)+halter(6) across knit/bag/outerwear/shoe/accessory,
  80 more-like. Boost +6 (more) / +5 (goes) * recency, reason inserted at why[0] (never above
  "You loved this"). Tasteful: striped sweater->striped shorts, woven tote->eyelet shorts,
  CHANEL clutch->satin halter (occasion-aware), Tory Burch jelly heels->shorts.
- **UI:** quickchoose.html card template did NOT render `why` at all. Added a `.why` line
  (italic Cormorant, --love rose) shown ONLY for "Goes with/More like" reasons (not generic
  "You loved this" clutter). VERIFIED in browser (:8801 the-edit): reasons render between
  title and price, 23 styled cards on Everyday tab, 0 console errors, screenshot confirms.

## Files touched
`build_feed.py` (probe, purchase loader, PURCHASE_WEIGHT, source-aware why, styling pass,
profile section, prints), `quickchoose.html` (.why CSS + card line), NEW `data/purchases.json`.
feed.html already renders .why so it shows there too.
