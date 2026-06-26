---
date: 2026-06-16
time: 11:50
project: style-feed (personal shopping-advice feed, working name "The Edit")
status: BIG session, all shipped & verified. 4 creators, 214 items (148 wearable + 9 home + 57 beauty). Built this session: (1) Hinge ♥/✕ feedback loop; (2) CLOSED loop — serve.py writes data/feedback.json on every swipe, Claude + rebuild read it (she opens via ~/Desktop/Open The Edit.command → localhost:8801, NOT file://); (3) left CATEGORY SIDEBAR (All/Tops/Bottoms/Dresses/Outerwear/Shoes/Bags/Accessories/Swim/Home/Beauty/Loved w/ live counts; All = wearables only, Home+Beauty re-included but siloed); (4) heart+✕ both clear from feed, liked → Loved; (5) tuned engine to her swipes + fixed category bugs (title-only classify, denim/jeans/pump false-positives, dupe-image drop, top-handle). She is actively swiping; data/feedback.json currently 12 liked / 7 disliked.
next-session: She's using it live; her swipes land in data/feedback.json. To "update my feed": read data/feedback.json, `python3 build_feed.py`, she refreshes (Cmd+R). Taste so far: soft elevated tops/knits/bottoms (LESET, Sunday Best, Intimissimi, Guizio) + one gown; into beauty/skincare (Reale Actives, Embryolisse); shoes specific (Salomon sneaker YES, runners/heels/ballet-flats NO); passing all bags. Biggest remaining lever = (B) AI-vision silhouette/colour scoring (replaces the colour heuristic — the real magic). Smaller: Beauty bucket is large (57) + loosely classified; recover ~5-7 dropped dupe-image items via cleaner Brigette/Paige re-scroll-scrape; add Dairy Boy (Shopify); (D) design pass + real name. Build: projects/style-feed/build_feed.py → feed.html. Preview WITHOUT disturbing her 8801: temp launch.json entry on another port. Alex Cooper ShopMy empty (dropped).
---

# Session: Style Feed v1 — Hinge-style like/dislike + 2 new creators

## Ask

Annabel: "start with A [add creators], and treat this like Hinge — a heart and
an X on each product, a system to track what I like and don't, and use that as
feedback to cater the algorithm to my style. Price I don't care about for now."

## Done this session (the proof)

1. **Added 2 creators** (roadmap step A). Scraped via Firecrawl
   (`shopmy.us/shop/<handle>`, json + waitFor 8000):
   - **Alix Earle** (`alixearle`, 64 items) and **Abby Catlin** (`abbycatlin`,
     18 items — very on-taste: Free People, J.Crew, Aritzia, AGOLDE, Reformation).
   - **Alex Cooper** (`alexcooper`) — page loads but products array empty /
     hallucinated placeholders on retry; her ShopMy has nothing extractable.
     Dropped (also not an old-money curator). Noted, not a blocker.
   - Saved raw pulls durably in-project at `data/sources/<handle>.json` (shape
     `{"json":{"products":[...]}}`, which the existing `load_products` reads as-is).
     The 2 original creators still point at their `.claude` tool-result files.
   - Feed went 84 → **150 pieces, 4 creators**.
2. **Hinge-style feedback loop** (all in build_feed.py's generated feed.html):
   - ♥ + ✕ button on every card (hover-reveal on desktop, always-on for touch).
   - State persists in **localStorage** (`theedit:v1`), survives reload/rebuild.
   - **Live re-rank**: liking boosts similar pieces (same brand +10, category,
     colour-proximity +6) so they rise instantly; ✕ slides the card out and
     hides it. "Loved" view, "show dismissed" undo toggle, "Reset my likes".
   - **Export taste** button → downloads `feedback.json`; build_feed.py reads
     `data/feedback.json` on rebuild and bakes it in server-side (boost liked
     brands/cats/colour, penalise disliked, pin exact likes, drop exact dislikes).
     Inert until the file exists.
3. **Dropped the price gate** (Annabel: price doesn't matter now). No more
   PRICE_MIN/MAX filter and no price scoring; price still displayed. $2,600 bags
   etc. now appear and are judged on cut + colour only.
4. Fixed a category-tagging bug: plurals ("Pants", "Boots", "Ballet Flats") now
   tag correctly; "Short Sleeve Top" correctly stays `top` (not `bottom`).

## Verify / gotchas

- Verified in the :8801 preview: like → is-liked + Loved=1 + localStorage write +
  sibling LESET 100→116 (brand+colour affinity); ✕ → slide-out + hidden +
  dismissed=1 + write. No console errors. 150 cards, images load (0 failures).
- 65 retailer-hosted images still fail hotlinking and get dropped (same v0
  limitation; static.shopmy.us hotlinks fine). 212 non-apparel filtered out.
- Preview viewport oscillates to a 1px sliver on the "desktop" preset — fix is an
  explicit `resize width:1280 height:900` then screenshot.
- localStorage is per-origin: the Desktop `file://` copy and `localhost:8801`
  keep SEPARATE swipe stores. For continuity Annabel should open it the same way
  each time. (A future local backend would unify this.)
- Buttons are `pointer-events:none` until card hover, so coordinate-based test
  clicks miss them; `button.click()` (delegated handler on #grid) tests the path.

## Update (same session, after Annabel's first use)

- **Behaviour change she asked for:** hearting now ALSO clears the piece from the
  All feed (not just ✕). Both actions slide the card out; liked items live under
  the **Loved** view, dismissed under the toggle. All = the "to decide" pile.
  Implemented via a shared `shouldShow()` (All shows neither-liked-nor-disliked).
- **Image bug she caught:** two Show Me Your Mumu "Mini Dress" cards displayed
  black leggings. Root cause = SOURCE data, not code: the ShopMy scrape pinned
  one photo to several titles (lazy-load mismatch; `img-product-1753607162492`
  was on both dresses AND the real Airluxe leggings). Fix: build now drops any
  product whose imageUrl is shared by another (can't trust the pairing). Dropped
  5 apparel items → 145 pieces. To RECOVER them, re-scrape Brigette/Paige with
  scroll + longer waitFor so all images load before extraction (also moves them
  off the fragile `.claude` tool-result paths into data/sources/).
- **Closed the feedback loop (roadmap C) — her explicit ask: "the hearts and ✕s
  should go to you."** Added `serve.py` (stdlib http.server): serves the feed +
  `POST /feedback` writes `data/feedback.json` (atomic) + `GET /feedback` returns
  it + no-cache headers. feed.html now `push()`es full swipe state on every
  change and `hydrate()`s from disk on open (disk = source of truth across
  browsers). So every heart/✕ lands on disk where build_feed.py AND Claude read
  it. Launcher `~/Desktop/Open The Edit.command` (double-click → serve.py →
  browser at :8801). launch.json "style-feed" now runs `serve.py 8801 --no-open`.
  Verified end-to-end: browser swipe → data/feedback.json → Claude read it →
  rebuild logged "feedback applied". Build no longer drops exact-disliked
  server-side (client hides them; keeps undo working). She must now open via the
  launcher (localhost), NOT the old file:// Desktop copy — earlier file:// swipes
  don't carry over (different origin, and I can't read file:// localStorage).

- **Category sidebar (her ask: "everything is too compiled").** Rebuilt the page
  as a left sidebar + main. Tabs: All, Tops, Bottoms, Dresses, Outerwear, Shoes,
  Bags, Accessories, Swim, Home, Beauty, Loved, each with a live count; clicking
  filters the grid and retitles the main heading. "All" = wearables only (Home +
  Beauty excluded so the clothing browse stays clean). Export/Reset/show-passed
  moved into the sidebar foot. Responsive: sidebar collapses to a top strip under
  820px.
- **Re-included Home + Beauty.** Replaced the old DROP gate with `classify()`:
  apparel nouns (`cats_of`) win FIRST (protects cream/tea-length clothing), then
  BEAUTY, then HOME, then KEEP-leftover ("other"), else drop. No re-scrape (data
  was already pulled, just no longer discarded). Result: 214 items = 148 wearable
  + 9 home + 57 beauty. Verified in preview: tab filters exact (Bottoms = 14, all
  bottoms; Home = 9 real home goods), counts correct, images load (0 failed).
  NOTE: Beauty bucket is large (57) and loosely classified, but it's siloed in its
  own tab so it never touches the clothing feed.

- **Category false-positives (she spotted: a sweater in Bottoms, soap pump in
  Shoes).** Root causes: (1) `classify()` ran `cats_of` on brand+title, so brand
  "Joe's Jeans" tagged a sweater "bottom"; fix = categorise on TITLE only.
  (2) "denim" was a bottom keyword, so denim shirts/jackets read as bottoms; fix
  = removed "denim", and "jeans?" → "jeans" (plural only, so "jean jacket" stays
  outerwear). (3) "pump" matched "Soap Pump"; fix = removed "pumps?" from shoe,
  added "flats". Verified all three reclassify correctly + swept feed (no
  top/shirt/jacket left in bottom). Lesson: categorise on title, not brand.

## Next steps

- Annabel's read on the learning feel (heart a handful, see similar rise).
- B (AI-vision silhouette) is the real magic; C (frictionless feedback — drop the
  Export→copy→rebuild dance); D (design pass + real name); add Dairy Boy (Shopify).
