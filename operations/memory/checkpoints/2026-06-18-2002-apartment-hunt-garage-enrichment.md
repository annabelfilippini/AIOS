---
date: 2026-06-18
time: 20:02
project: apartment-hunt
status: CODE DONE & LOGIC-TESTED, LIVE RUN NOT YET COMPLETED — added detail-page enrichment (real garage/bath/bed/office/sqft), locked Denver to Cherry Creek + 10-min ring, garage labeling + garage-first sort, 2-bath/3-bed enforced everywhere, 8 more Firecrawl seeds + 9 Denver SFH property managers, Exa retry/backoff. The digest on disk is STILL the stale 12:13 pre-change version — the background build run was killed when the prior session closed and never wrote a new digest.
supersedes: 2026-06-18-1215-apartment-hunt-denver-houses-cherry-creek.md
---

# Session: apartment-hunt — garage enrichment + Cherry Creek ring lock

## Where this stands

Annabel's two complaints drove this session: (1) the hunt wasn't finding enough,
and (2) most results had no garage — and "if a garage isn't mentioned, they
don't have it," so she wanted requirements enforced much harder.

All code is written, saved, logic-tested, and imports clean. **The live run did
NOT complete** — I launched `python3 build_html_digest.py --city denver` in the
background (piped through `tail`, which buffered all output), the prior session
ended ~8h ago and killed the process, so `digest_denver_latest.html` and the
Desktop copy are STILL the old 12:13 version: 84 cards, zero garage badges, the
old metro-wide "elsewhere" listings. **Next action is simply to re-run the build
to produce the first garage-labeled digest.**

## Annabel's locked decisions (via AskUserQuestion)

- **Garage:** keep every house, but read the full page and label `✓ garage` /
  `no garage found` / `garage unverified`; sort garage-confirmed to the top.
  Nothing dropped for lacking a garage.
- **Area:** hard-restrict to Cherry Creek + the ~10-min drive ring (drop the ~69
  "elsewhere" houses). "More sites" = more sources feeding that tight zone.
- **Enforce after reading the page:** exactly 3 bedrooms AND ≥2 bathrooms.
  Keep showing no-price listings (she did NOT ask to drop those).

## What changed this session

**profiles.py**
- New `SearchProfile` fields: `min_bathrooms: int = 0`, `enrich_details: bool = False`.
- New `_DENVER_RING_HOODS` allow-list (preferred + ring + spelling variants).
- Denver retargeted: `require_neighborhood_match=True`; `neighborhoods=_DENVER_RING_HOODS`;
  `target_zips` trimmed to ring-only (removed 80211/80212/80205/80203/80204,
  added 80224); `min_bathrooms=2`; `enrich_details=True`.
- Sources widened: `firecrawl_seeds` 10→18 (added homes.com, dwellsy, rentals.com,
  renterswarehouse + institutional SFH landlords invitationhomes / amh / msrenewal /
  triconresidential — heavy garage inventory). `property_manager_domains` 0→9
  (realatlas, evernest, rpmcolorado, rentgrace, coloradorpm, allcountydenver,
  pmidenver, foxpropertymgmt, milehighpm) feeding the Exa per-manager sweep.

**apartment_hunt.py**
- `Listing` gained: `bathrooms`, `sqft`, `has_office`, `garage_status`
  ("confirmed"/"none found"/None), `enriched`.
- New globals `MIN_BATHROOMS`, `ENRICH_DETAILS` (declared + bound in `apply_profile`).
- `keep()` split into `keep_basic()` (price/beds/baths/staleness/house-mode/rental-hint,
  NO neighborhood gate) + `keep()` (= keep_basic + neighborhood gate). Bath floor
  added in keep_basic — only bites when bath count is known.
- **New enrichment engine:** `_ENRICH_SCHEMA`, `enrich_listing()` (Firecrawl
  /v1/scrape json on each detail URL; garage="yes" ONLY if explicitly shown, else
  "no"; folds the real address into snippet so the ring filter can place it;
  failures leave the listing unverified, never dropped), `enrich_candidates()`
  (ring-likely first, `ENRICH_CAP=70`, prints what it skips — no silent cap).
- `main()` flow when enrich on: dedupe → `keep_basic` → enrich survivors →
  `keep` → render. Markdown `_render_listings` shows garage/bath/sqft/office.
- Exa `_exa_search` now retries 403/429 with backoff (1.5/3/4.5s) instead of
  silently dropping (the prior cause of thin runs).
- Removed the dead SF-hardcoded module-level `FIRECRAWL_SEEDS` block (apply_profile
  binds it per-city anyway; the literal was a latent importer bug).

**build_html_digest.py**
- `filter_and_sort(listings, firecrawl_key)` now runs the same enrich pass before
  `keep()`; sort key adds garage-confirmed-first as the 2nd key.
- `_card()` renders garage badge (filled green `garage-yes` / red `garage-no` /
  muted `garage-unverified`), plus BA / sqft / office; keyword features now exclude
  the authoritative ones (house/garage/office/2 bath). Footer shows
  "X of Y have a confirmed garage." New CSS: `.tag.garage-yes/.garage-no/.garage-unverified`.

## Verified (logic, no network)

- Denver locks to ring: fake 80206 listing kept, 80212 (Berkeley) dropped.
- Bath floor: 1-bath listing dropped.
- SF profile untouched (enrich=False, min_bath=0).
- `_card()` renders all three garage states correctly.
- Both modules import clean; 18 firecrawl seeds, 9 PM domains, 10 ring ZIPs bound.

## Next steps

1. **RE-RUN to produce the first real garage-labeled digest** (the whole point —
   current digest is stale):
   `cd projects/apartment-hunt && python3 -u build_html_digest.py --city denver`
   Use `python3 -u` + redirect to a file (NOT piped through tail) so progress is
   visible — that buffering hid the last run entirely.
2. Read the result: expect the count to DROP from 84 (ring-only + real bath
   enforcement). That's intended — every survivor is in-zone with a known garage
   status. Check the "X of Y confirmed garage" footer.
3. If too thin: easiest loosener is ring → "ring + one more mile" (widen
   `target_zips`/`neighborhoods`/Zillow bounds), NOT back to metro-wide.
4. Verify a few institutional-landlord + PM-domain URLs actually returned data
   in the coverage report (some seed URLs are best-effort; failures show as
   error/0 and are harmless).
5. Open question still open from prior checkpoint: daily auto-run wrapping the
   build (Annabel hasn't confirmed).

## Open / declined

- Declined a `~/.claude/CLAUDE.md` edit (proposed a "don't pipe long background
  runs through tail/head; use `python3 -u` + file redirect" rule under Tool &
  Stack Assumptions) — Annabel said no.

## Reference

- Run command: `cd projects/apartment-hunt && python3 -u build_html_digest.py --city denver`
- Prior checkpoint (Denver house retarget): `operations/memory/checkpoints/2026-06-18-1215-apartment-hunt-denver-houses-cherry-creek.md`
- Build details: `projects/apartment-hunt/notes/2026-06-17-multi-city-profiles-and-editorial-cream-ux.md`
