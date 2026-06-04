# Miss Kim Ann Arbor — Redesign Only

Shipped 2026-04-19. First redesign run using `/audit-redesign` without `/audit-analyze` or `/audit-seo` (no audit report, no audit-tag pills — pure design work).

## Deliverable

- `mockups/homepage-redesign.html` — 1,542 lines, single-file inline CSS
- `mockups/assets/` — 12 images, all local, zero hotlinks

## What makes this redesign work

**Brand DNA preserved.** "Really Great Korean Food" is the hero H1 (not replaced with "Elevated Korean Cuisine" or any AI-luxury phrase). Zingerman's Community of Businesses lineage visible in the footer. Chef Ji Hye Kim's fermentation-scholar framing anchors the About block.

**Typography.** Fraunces (editorial serif, variable optical-size axis) for display + Inter book-weight sans for body. Retired the Toast-CMS default Lato.

**Palette.** Bone cream ground `#F3EEE4`, soft-black ink `#1A1715`, warm clay accent `#B4412B` (reads gochujang, not generic brand-red). Pine green `#2F5240` isolated to the Little Kim strip so the two identities don't compete. Retired the Toast-CMS default cyan `#1191B8`.

**Sections in order:**
1. Hero — full-bleed KFC + banchan photo, serif H1 overlay, OpenTable + Toast Order dual CTA
2. Hours strip — today's hours + "Reserve / Order / Directions" quick actions
3. Signature Dish — Cacio e Pepe Tteokbokki spotlight (Jan 2025 Zingerman's blog feature) with $18 price
4. Chef Ji Hye Kim — candid-with-cookbooks portrait + bio + press prose (NYT / Zingerman's blog lines, inline, no logo bar)
5. Menu — Bull & Last–style typographic list, 5 categories (01–05) with dish names + descriptions only, no pricing (coherence: only 5 of 13 items had verified prices, so all stripped)
6. Rotating Weekly Specials — Wednesday Chicken Dinner $20 + Ssam Plates $22–$29
7. Review Wall — 4 verified Yelp quotes in 2×2 grid with attribution + date, hairline borders (no cards, no stars)
8. Private Events + Chef Pop-Ups — two-up
9. Visit — address / hours table / phone / email + stylized map + verbatim parking block on dark charcoal band
10. Little Kim — sister-concept strip with pine-green accent
11. Footer — Zingerman's block + Instagram marquee + inline SVG socials

## Reference sites that informed the design

Picked by Annabel, scraped and visually absorbed:

- **Rare Bird Rooftop** — hero treatment, photography tone
- **Bull & Last** (homepage + menus) — typographic menu with category numerals, editorial restraint
- **King NYC** — press prose inline (not logo bar), minimal nav
- **La Semilla** — whitespace discipline, warm palette, farm-to-table voice

Full breakdown in `reference/reference-summary.md`.

## Verified facts + sources

All claims on the page trace to `facts/verified-facts.md`. Sources:

- Yelp biz page (52K chars — review quotes, menu grid, ratings)
- Google knowledge panel (34K chars — hours, GBP info, Products panel)
- Zingerman's profile page (blog posts referencing Cacio e Pepe, Eric Kim/Matt Rodbard visit)
- Miss Kim homepage (address, phone, email, OpenTable link, existing photography URLs)
- OpenTable: **bot-walled** — documented, fell back to Yelp + Google

## Deliberate exclusions

Three things that *could* have made the page louder but were dropped because the source wasn't clean enough:

1. **Tuesday Banh Mi Special.** Google's Products panel showed it, but Miss Kim is closed Tuesdays. Dropped entirely.
2. **James Beard nominee / semifinalist copy.** The homepage photo file is named `jamesbeard.jpg` but no scraped source confirms the nomination. Used a different Chef Ji Hye photo (with cookbooks) and wrote zero award claims.
3. **Prices on 8 menu items.** Only 5 of 13 main-menu dishes had verified Yelp-grid pricing; the rest would have required invention. Stripped all main-menu prices to keep coherence; kept pricing in Signature Dish and Weekly Specials where every item has a verified price.

## Reusable artifacts

- `scrape.py` — single-pass Firecrawl of home + references + facts sources (template for next restaurant redesign)
- `branding.py` — Firecrawl `branding` format scrape (should be folded into `scrape.py` in the skill going forward)
- `redesign-spec.md` — 10-section copy spec with every verbatim string fenced `DO NOT REWRITE:`
- `reference/reference-summary.md` — design-DNA breakdown of all 4 references

## Decisions flagged for future copy pass

- Hours use semantic `<li><span>Day</span><span>Time</span></li>` instead of the spec's single em-dash-joined string. Visually identical; accessibility stronger. Kept.
- Menu section is ~2.5× the Reviews section vertically — length driven by 5 real categories with verified dishes. Tightening would mean cutting menu. Kept.

## Postmortem → skill improvements

Documented separately in `/audit-scrape` and `/audit-redesign` skill edits (2026-04-19). TL;DR:
- Redesign-only mode should skip CMS-walled sibling pages when the homepage smell test fails
- Branding scrape folded into main scrape script (no separate `branding.py`)
- Phase B agent's internal QA is authoritative; don't spawn a second independent QA agent in main session
- No ScheduleWakeup for scrapes <5 min
- No sips cropOffset in main session — delegate to the producing agent
