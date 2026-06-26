---
date: 2026-06-19
time: 09:24
project: apartment-hunt
status: CROSS-SOURCE ADDRESS DEDUP BUILT, VERIFIED, AND LIVE. Clean Denver digest on disk — 7 unique matches, 2 garage-confirmed in-ring, zero duplicate/contradictory cards. Next action Annabel just asked for = widen the search ring by ~1 mile (NOT yet started; she said "widen by 1 mile" then immediately asked for this checkpoint).
supersedes: 2026-06-19-0828-apartment-hunt-first-garage-digest-and-exa-cap-fixes.md
---

# Session: apartment-hunt — cross-source address dedup fixed

## Where this stands

The full-enrichment build from this morning is done and the duplicate/contradiction
bug from prior checkpoints is FIXED in code and verified in a real run. The
on-disk Denver digest is clean: 7 unique cards, no address appears twice, no
contradictory garage labels.

Immediate open action: **widen the search ring by ~1 mile** — Annabel asked for
this, then asked for a checkpoint before I started. So the ring-widen is the
first thing to do in the next turn. Nothing is mid-flight.

## What got fixed this session (the dedup work)

Root cause: `_dedupe_key` only deduped by normalized URL, so the same physical
house listed on two sites (Zillow + Highrises) or with/without a directional
("238 Harrison" vs "238 N Harrison") survived as two cards — sometimes with
CONTRADICTORY garage labels (one "confirmed", one "none found").

Fix (in `apartment_hunt.py`):
- `_address_key(ls)` — parses `(house number, street, ZIP)` from title/snippet.
  Deliberately DROPS the N/S/E/W directional (so "238 Harrison" == "238 N
  Harrison"); uses ZIP as the guard so two different streets don't collide.
  Returns None when no address is parseable (e.g. Craigslist "Wash Park house").
- `collapse_by_address(listings)` — groups by `_address_key`, collapses each
  group to one representative, MERGES garage signal with precedence
  **confirmed > none found > unverified** (positive evidence wins over a page's
  silence). Backfills missing price/beds/baths/sqft from the dups. No-address
  listings pass through untouched. `_GARAGE_RANK` constant holds the precedence.

Wired in `build_html_digest.py` `filter_and_sort()` AFTER enrichment (so
`garage_status` is populated), right after the `keep()` filter. Logs
`collapsed N → M` when it collapses anything.

Verified two ways:
1. Unit test on the exact 10 prior cards → 10→8, both contradictions resolved to
   "confirmed", different-number/different-street addresses stayed separate.
2. Real rebuild: `141 candidates → 9 matched → collapsed 9→7`. 238 Harrison and
   64 S Garfield each now appear ONCE, both ✓ confirmed garage.

## Current digest (clean, on disk + Desktop)

7 unique matches, all in/near the ring:
1. 238 Harrison St 80206 — $4,200 — 3BR/2BA 2,508sf — Cherry Creek — ✓ garage
2. 64 S Garfield St 80209 — $4,995 — 3BR/4BA 2,621sf — Wash Park — ✓ garage
3. Wash Park 3bd/2ba house — $3,200 — 3BR — Wash Park — unverified (craigslist)
4. Wash Park remodeled 3bd/2ba — $3,200 — 3BR — Wash Park — unverified (craigslist)
5. 225 S Monroe St 80209 — $4,000 — 3BR/4BA 4,626sf — Wash Park — no garage
6. 287 S Holly St 80246 — $4,635 — 3BR/3.5BA 2,695sf — Glendale — no garage
7. Verified 3BR Virginia Village — $3,530 — 3BR/2.5BA 2,589sf — no garage

Real shortlist = the 2 garage-confirmed in-ring houses (#1, #2).

## Exa is still dead (unchanged from prior checkpoint)

Exa 403s on every query despite the hardened 6-attempt/2.5–12.5s backoff →
confirmed IP/time-windowed ban, NOT fixable with more retries. The Reddit /
owner-direct / sublet channel contributes ZERO. Firecrawl (Zillow seed + JS
seeds + Zumper) + Craigslist carry the whole run. Don't keep trying to "fix" Exa
backoff — the ban is upstream. If the Reddit channel matters, needs a different
transport (e.g. reddit-cli) not an Exa tweak.

## Sources actually working today

- Firecrawl → Zillow (main workhorse, most candidates)
- Firecrawl seeds (JS/blocked sites incl. Zumper)
- Craigslist (denver.craigslist.org)
- Direct public (plain HTML / JSON-LD)
- Exa = DEAD (403)

## Next steps (start here)

1. **WIDEN THE RING BY ~1 MILE** (Annabel's explicit ask, not yet started).
   Edit the Denver profile in `profiles.py` — extend `target_zips` /
   `neighborhoods` and the Zillow search bounds by one more mile of ring, NOT
   back to metro-wide. Then rebuild and report the new match count.
   - Candidate adjacent areas to add: Hale, Congress Park, Country Club, Belcaro,
     Cory-Merrill, Crestmoor (confirm against profile's current list first).
2. Rebuild: `cd projects/apartment-hunt && python3 -u build_html_digest.py --city denver`
   (re-scrapes + enriches ~140 pages, ~couple min; run uninterrupted).
3. Backlog: daily auto-run wrapping the build (Annabel hasn't confirmed).
4. Backlog: if Reddit/owner-direct channel is wanted, replace Exa transport.

## Reference

- Run command: `cd projects/apartment-hunt && python3 -u build_html_digest.py --city denver`
- Current digest (clean): `projects/apartment-hunt/digest_denver_latest.html` (7 cards)
- Desktop copy: `~/Desktop/apartment-hunt-denver-2026-06-19.html`
- Key code: `apartment_hunt.py` — `_address_key` / `collapse_by_address` / `_GARAGE_RANK` (~L1668+), `_dedupe_key` (~L1663), profile in `profiles.py`
- Wiring: `build_html_digest.py` `filter_and_sort()` (~L74)
- Prior checkpoint: `operations/memory/checkpoints/2026-06-19-0828-apartment-hunt-first-garage-digest-and-exa-cap-fixes.md`
