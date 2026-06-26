---
date: 2026-06-17
time: 13:00
project: wayloft
status: in-progress
next-session: Re-center the real app (apps/web) into Direction A, Editorial Cream squared. Strip the amber Signal theme, rebuild the app shell and the three screens (Setup / Earn / Burn), and rewrite .claude/rules/typography.md (it currently hard-mandates Geist) to Cormorant + Jost + JetBrains Mono. Then update the airline-scrape guardrail docs to the personal-use rule, then wire data (earn engine + scraped feed first, then Seats.aero + Duffel trip check). Open the design comparison page for the exact tokens.
---

# Session: Wayloft design direction chosen (Editorial Cream, squared)

## What we worked on

Picked up from the 12:08 restart checkpoint. Locked the three pending decisions,
recovered the lost reference images, and built + verified the design comparison
page. Annabel reviewed and chose a lane.

## Decisions made

**1. Direction chosen: A, Editorial Cream (the JETRADE lane).** Direction B
(Premium Dark) is retired. Annabel's one refinement: no rounded corners. Applied,
the cream lane is now squared (sharper, more editorial, closer to the real
JETRADE layout).

**2. Locked design tokens for the cream lane** (JETRADE's own source palette,
pulled live from the Dribbble shot, plus the chosen type):
- Ink `#0F0D0C`, warm ivory paper (`#F3EFE6` ground, `#FBF9F3` panels), sand
  `#CCC4AD`, **bronze accent `#846340`** (deliberately not amber), espresso card
  `#241F19`/`#3a3026`, warm grays `#4A4740` / `#9a917e` / `#A39F96`, hairline
  `#E6DECC`.
- Type: **Cormorant Garamond** (display/headings/wordmark), **Jost** (body +
  uppercase tracked labels), **JetBrains Mono** (all figures: points, dollars,
  rates, dates).
- Corners: **squared (radius 0)** on all panels, window, nav, tags/pills, list
  badges. Exceptions: avatar and card-network dots stay circular; the credit
  card keeps a 6px radius (physical object). Tags are sharp rectangles, not
  pills.

**3. Session decisions (carried in):** desktop-first; Duffel = use the API key
(must verify the key is actually set in env, not a stub, before the trip-check
build); earn+burn personal scope locked.

**4. Global rule added.** New bullet in `~/.claude/CLAUDE.md` (Working Style):
save pasted reference images to the project's references folder immediately,
do not rely on the chat transcript. Prompted by the lost images this session.

## Artifacts

- Comparison page: `projects/wayloft/design/comparison.html` (self-contained,
  3 references embedded base64). Desktop copy: `~/Desktop/wayloft-design-comparison.html`.
- Reference images saved: `projects/wayloft/design/references/` (ref-1 JETRADE,
  ref-2 gold card, ref-3 lavender layout-only).
- Verification screenshots: `projects/wayloft/design/screenshots/`.
- JETRADE source: Dribbble shot 26274029 by Rifqi Fachrizal R (a concept, not a
  live site). The pasted image is the highest-fidelity reference.

## Open questions

- Next move: re-center the real app now, or flesh out more Direction A screens
  (Setup, mobile) as static design first before touching `apps/web`? (Leaning:
  re-center.)
- Seats.aero: does Annabel have a Pro account (API token) or session-scrape?
- Keep Supabase (single user) or simplify to local-first? Leaning keep.
- The deal / trip-check numbers in the mock are illustrative, not live data yet.

## Next steps

1. Re-center `apps/web` into Editorial Cream squared: strip the amber Signal
   theme, rebuild the app shell and Setup / Earn / Burn screens using the locked
   tokens above. Use `comparison.html` as the visual spec.
2. Rewrite `.claude/rules/typography.md` (currently mandates Geist/Geist Mono)
   to Cormorant + Jost + JetBrains Mono.
3. Update `.claude/rules/data-pipeline.md` and project `CLAUDE.md` airline-scrape
   guardrail to the reopened personal-use rule: scrape aggregators (Seats.aero)
   and blogs/Reddit via her own sessions, low volume, cache hard, never hit
   airline.com directly.
4. Wire data in build order: earn engine + scraped deals feed first (reliable),
   then authenticated Seats.aero + Duffel trip check (fragile).

## Context to preserve

- Repo anchors: app at `apps/web`; routes `/optimizer`, `/recommend`, `/travel`,
  `/cards`, `/bonuses`, `/dashboard`; engine `lib/recommend/engine.ts`; flight
  wrappers `lib/flights/`; catalog `data/`.
- Annabel's real situation drives the screens: holds Chase Freedom Flex, new job
  with higher spend, interested in United + partners and hotel chains. Domain
  fact baked into the card-pick: Freedom points only become transferable once she
  also holds a Chase Sapphire, so "what card to get next" starts with a Sapphire.
