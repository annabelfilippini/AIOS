---
date: 2026-06-15
time: 16:35
project: style-feed (personal shopping-advice feed, working name "The Edit")
status: scrappy v0 shipped & verified — 2 creators, 84 taste-ranked pieces, live feed.html on Desktop. Annabel reviewed, greenlit the roadmap, and closed the session to resume next time.
next-session: Annabel chose to continue the roadmap (she has NOT yet given granular taste/price-band feedback — still worth asking for her gut read when she opens the feed). Recommended order: (A) add more creators [Abby Catlin, Alex Cooper, Alix Earle's simple stuff, Dairy Boy store] so it feels like HER blended feed — fastest, do first; (B) upgrade taste engine from color+keywords to AI-vision silhouette scoring (the real magic); (C) auto-refresh + save/dismiss self-learning; (D) proper Aesop/Aman/Byredo-grade design pass + real name. Build files: projects/style-feed/build_feed.py + feed.html. Re-run `python3 build_feed.py` (color cache makes it instant). To add a creator: scrape `shopmy.us/shop/<handle>` (firecrawl json + waitFor 8000), drop the result path into SOURCES in build_feed.py.
---

# Session: Style Feed scrappy v0 — influencer ShopMy purchases, filtered to Annabel's taste

## Ask

Annabel ("horrible shopper," relies on her sisters' California-trend eye and a
set of influencers) wants a personal-only tool that scrapes what her favorite
influencers buy, filters to HER taste (old money; white/grey/black neutral;
mid-to-premium), and tells her what to buy. Long term: outfit building, knows
her closet, self-improving. She wants it to feel futuristic but "give" old money.

## Decisions locked (from the brainstorm)

- **Scope:** build for herself only (design so it *could* open to sisters later,
  but don't pay that tax now).
- **Data source:** start with influencer ShopMy/LTK links, expand later. Do NOT
  scrape Instagram/TikTok — purchase links live on the shopping platforms.
- **Approach:** scrappy prototype first to feel whether the feed lands.
- **Product thesis:** *filter, don't copy* — e.g. only Alix Earle's simple stuff,
  not her whole loud feed. The taste filter is the magic.
- Influencers named: Paige Lorenze (+ Dairy Boy brand), Brigette Pheloung
  (Acquired Style), Abby Catlin, Alex Cooper, Alix Earle.
- Stores she likes (not exclusive): Zara, Aritzia, Lululemon, Nordstrom,
  Anthropologie, Free People, Revolve; open to boutiques incl. Australian.
- Design refs to inspect BEFORE the real design pass: aman.com, aesop.com,
  byredo.com + her 3 inspo screenshots (NET-A-PORTER app, The Row, an "Archive
  No.03" vintage/CBK-mood concept). Resolution: old money = soul, futuristic =
  execution (explains its picks, learns her), not sci-fi visuals.

## Done this session (the proof)

1. **De-risked the scary assumption.** ShopMy storefronts scrape cleanly with
   Firecrawl. One pull of Brigette's `/shop/acquiredstyle` = 168 products, 103
   brands, each with brand/title/price/image/outbound-retailer-link. See memory
   `reference-shopmy-scraping` for the exact pattern (`/shop/<handle>`, json +
   waitFor 8000).
2. Pulled 2 creators (Brigette + Paige) = 343 raw products → filtered out 195
   non-apparel (beauty/food/tools) + 17 out-of-band → 84 ranked pieces.
3. Built `projects/style-feed/build_feed.py`: text heuristics (liked brands,
   fabrics, price band) PLUS a colour read of each product photo (mean +
   p90 saturation of the garment, white bg removed). Neutral pieces rise, loud
   sink. This is the cheap stand-in for the v1 AI-vision upgrade.
4. Generated `feed.html` (quiet-luxury design, Cormorant + Jost, cream palette),
   copied to `~/Desktop/the-edit-feed.html`. Verified in Playwright: top = clear
   Tory Burch bag (100), cream knit set, black ballet flats; bottom = sequin
   dress (12), vivid Rat & Boa dress (16). Screenshots in scratch/.

## Verify / gotchas

- `/shop/<handle>` works; bare `shopmy.us/<handle>` fails all Firecrawl engines.
- ~1/3 of items have retailer-hosted images that block hotlinking (won't load);
  v0 drops them (filter on colorfulness != None). Production fix = cache/proxy.
- Colour heuristic can't read pattern from a text title (a "Cashmere Collared
  Sweater" that's actually rainbow-striped first scored 90 on text alone) — the
  photo-colour pass fixed that specific case. True silhouette/style needs the
  v1 AI-vision pass.
- A localhost `python -m http.server 8787` was left running (Playwright blocks
  file://). Harmless, serves only the project folder, dies on reboot.

## Next steps

- Get Annabel's read on the feed (taste accuracy, price band, design, creators).
- Then A → B → C → D per `next-session` above. A (more creators) is fastest and
  makes it feel personal; B (AI vision) is the real differentiator.
