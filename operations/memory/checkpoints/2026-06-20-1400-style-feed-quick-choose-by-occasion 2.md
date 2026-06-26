---
date: 2026-06-20
time: 14:00
project: style-feed (personal shopping feed, "The Edit")
status: in-progress
next-session: NEXT = build the NUULY CLI (Annabel's pick — she expects her Nuuly history to sharpen taste a lot). Pull BOTH rental history AND current closet (she confirmed both). Mirror the authenticated-cookie pattern of reddit-cli / skool-curl: export her logged-in Nuuly session cookie, build a small CLI (likely tools/nuuly-cli) that hits Nuuly's internal/JSON endpoints (no public API). Then feed Nuuly items into the taste engine as a strong signal (a worn rental ≈ a like; current closet = "owns/has"). First step next session: ask Annabel to grab the Nuuly cookie (Copy-as-cURL from a logged-in tab) and inspect the real account/order endpoints before coding. Then later: (a) email purchase signal via Gmail MCP, (b) DECIDE "My List" all-time vs fresh shortlist, (c) add an activewear store (Workout only ~6), (d) undergarments source + classify() change.
---

# Session: The Edit — pivot from scroll-feed to quick-choose by occasion

## What changed and why
Annabel does NOT enjoy shopping/scrolling. The Edit's job is to hand her a small
set to decide on fast and buy, not browse. Built a NEW bucket-first quick-choose
mode alongside the existing scroll feed (feed.html untouched).

## Built (verified in browser, :8801)
- **`projects/style-feed/quickchoose.html`** (new, hand-authored, data-driven).
  LAYOUT (revised per Annabel — she wants to SEE ALL options on one page, not a
  one-at-a-time deck): sticky **top tab bar** (Workout · Work · Going Out ·
  Everyday | Jackets · Shoes · Accessories · Undergarments, each with a live
  count) + a responsive **grid** of every option in the selected bucket (4-col
  desktop / 3 / 2 mobile). Each card = image + corner saved-♥ pin + brand/title/
  price + a ✕/♥ action row (in the info block, NOT overlaying the image) + View
  item link. ✕ fades the card out (dislike); ♥ toggles like + filled heart + soft
  border. "Show passed (n)" toggle reveals disliked. "My List" button → buy view
  with direct retailer links. Editorial-cream (Cormorant/Jost).
  (First built as a deck; replaced with tabs+grid same session.)
- **`build_feed.py`** now also dumps **`data/items.json`** (compact scored items +
  occ/cats/vision meta) after `cards = ...`. Skips home/beauty/loungewear.
- **`.claude/launch.json`**: added `the-edit` config (serve.py on 8801) so the
  preview harness can drive it. serve.py auto-serves quickchoose.html + items.json.

## Buckets (final)
The OUTFIT (occasion, garments only — bags/shoes/accessories excluded via a
`wearable()` guard): **Workout** (occ active, 6) · **Work** (occ work, 69) ·
**Going Out** (occ going-out, 54) · **Everyday** (occ casual/vacation OR a main
garment the tagger left occ-less, 256).
FINISHING (category): **Jackets** (outerwear, 30) · **Shoes** (shoe, 14) ·
**Accessories** (accessory+bag, 102) · **Undergarments** (PLACEHOLDER — greyed
"No source yet"; classify() drops bras/thongs/briefs so there's no data).

## Key implementation facts (for next session)
- Occasion was ALREADY in the engine: `occasions_of()` in build_feed.py returns
  {active, work, going-out, vacation, casual} from vision `formality` + fabric +
  brand + title keywords. No re-vision needed; derived for free. (FORMALITIES has
  no "athletic" — Workout leans on ATHLEISURE brands + ACTIVE_RE keywords, hence
  only 6 items. Add an activewear store to grow it.)
- quickchoose shares the feed's taste loop EXACTLY: same localStorage key
  `theedit:v1`, same `{liked:{id:meta},disliked:{...}}` shape, same `meta()`
  record (brand/creators/c/cats/neut/om/sil/form/neck/slv/len/fab/drp/bk), same
  `POST /feedback`, same GET-merge-on-boot (disk = source of truth). So swipes in
  EITHER view feed the same ranking + the same buy list.
- Verified: buckets count live; deck renders image (naturalWidth 1331)/brand/
  title/price/why/buy link; ♥ advances + bumps list; bags/shoes no longer leak
  into Going Out (now leads with a gown); buy links resolve to real retailer URLs
  (aritzia.com etc.); 0 console errors; mobile 375px clean. Removed 1 accidental
  test-like (Gala Bag) from feedback.json → back to 268 liked.

## OPEN QUESTION flagged to Annabel
"My List" currently shows ALL 269 historical likes — that's a feed again, not a
shortlist. Decide: keep all-time, or make it a fresh per-session shortlist (e.g.
only likes made in quick-choose, or a "move to cart / clear" action).

## EVOLVING-TASTE PACKAGE — BUILT + verified this session
Annabel asked: does it keep evolving as I like/✕? It didn't really (learned flat:
no recency, no live rerank in quick-choose, binary brand signal). Now it does:
1. **Timestamps.** Every swipe record carries `ts` (YYYY-MM-DD). Backfilled the
   575 legacy records to baseline 2026-06-17 (`data/feedback.bak.json` is the
   pre-backfill backup). Both views stamp today on new swipes: quickchoose
   `meta()` + feed `info()` (the feed copy lives in build_feed.py SCRIPT, NOT
   feed.html — feed.html is generated).
2. **Recency weighting (build_feed.py).** `recency_w(rec)` = 0.5**(age/45d).
   `_signals` + `_vision_signals` now accumulate weights, not counts. So recent
   taste leads, old decays. (`_vision_signals` signature changed: takes the
   liked/disliked DICT now, not a set — call sites updated.)
3. **Live recency-weighted rerank in quick-choose.** Ported the feed's
   buildProfile()/liveScore() into quickchoose.html with recency (HALF=45). Grid
   re-sorts by liveScore on every renderGrid (tab switch / toggle / reload), so
   order reflects latest swipes with no rebuild. base term = items.json `base`.
4. **Brand signal made PROPORTIONAL (was binary — the real flaw).** Old:
   `if Lb +11; if Db -15` → saturated, a few new swipes couldn't move a brand she'd
   already swiped. New: net = Lb-Db, `+min(11,7*net)` / `-max(15,9*net)`. Fixed in
   all THREE scorers: quickchoose liveScore, build_feed feedback_adjust, build_feed
   SCRIPT liveScore. VERIFIED: injecting fresh dislikes for A&F flips Work order
   from all-A&F to J.Crew/Reformation mix (in-memory test, disk untouched).
5. **`style-profile.md`** (auto-generated each build, project root): readable
   mirror of learned taste — palette (neutral 0.84 / old-money 0.76), top brands
   (J.Crew, Dairy Boy, Tuckernuck...), silhouettes/formality/fabrics, a "Lately
   (21d)" shift view, and what she passes on.
6. **`data/style-overrides.json`** (`{boost:[],hide:[]}`): hand lever she can
   edit — boost/hide by brand or keyword substring; applied last in build_feed so
   it wins over learned taste. This is the "correct it directly" piece.
Verified: 0 console errors; feedback.json still 292 loved / 283 passed, all
records have ts, no stray test keys.

## Direction memory updated
`project_style_feed.md` now carries the 4-part direction: (1) quick-choose ✓
built (tabs+grid, evolving), (2) email purchase signal, (3) Nuuly CLI both,
(4) living style profile ✓ (style-profile.md + overrides shipped).
