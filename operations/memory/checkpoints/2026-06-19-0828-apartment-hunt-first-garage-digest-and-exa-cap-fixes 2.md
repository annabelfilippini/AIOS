---
date: 2026-06-19
time: 08:28
project: apartment-hunt
status: FIRST GARAGE-LABELED DIGEST IS LIVE ON DISK (11 cards, 20:33 build). Two follow-up fixes made + verified (ENRICH_CAP 70→160, Exa backoff hardened) but the re-run that would exercise them DIED mid-fetch and never wrote a new digest. Next action = re-run the build to get all 128 candidates enriched.
supersedes: 2026-06-18-2002-apartment-hunt-garage-enrichment.md
---

# Session: apartment-hunt — first real garage digest + Exa/cap fixes

## Where this stands

The stale 12:13 digest from prior sessions is GONE. A real garage-labeled
Denver digest now exists on disk and on the Desktop. Then I made two follow-up
fixes to widen coverage, but the re-run to test them was killed before it
produced output, so those fixes are **written + import-verified but not yet
exercised in a completed run**.

## First build DID complete (this is the current digest on disk)

`python3 -u build_html_digest.py --city denver` ran clean (exit 0, 20:33):
- **128 candidates** passed the basic filter.
- Enriched **70/70** (hit the old cap; **58 not enriched** that run).
- **11 matched** the full criteria (Cherry Creek ring + 3bd + ≥2ba, read from
  the actual detail page).
- Garage badges: **1 confirmed / 4 none found / 6 unverified.**
- All 11 are in-ring (80206 Cherry Creek, 80209 Wash Park, 80246 Hilltop).
- Wrote `projects/apartment-hunt/digest_denver_latest.html` and
  `~/Desktop/apartment-hunt-denver-2026-06-18.html`.
- Known cosmetic issue: a couple of cross-source duplicates survive in the 11
  (64 S Garfield, the Wash Park 3bed/2bath house each appear twice) — dedup
  isn't catching the same listing across different source URL/title formats.

## Exa diagnosis — KEY IS VALID, 403s are transient burst rate-limiting

Important correction to the prior checkpoint's worry: the `403 Forbidden` on
every Exa query is NOT a bad/expired key.
- `.env` `EXA_API_KEY` is a real 36-char UUID (prefix `7d8072…88e`);
  `FIRECRAWL_API_KEY` is valid (`fc-aa5…`).
- Direct test of the key → **200** with real Cherry Creek listings.
- Replayed the build's EXACT full body (`type:neural`, `useAutoprompt`,
  `contents` block, `startPublishedDate`) → all **200**. No single param causes
  the 403.
- Conclusion: Exa burst-bans the heavy sweep (9+ queries fired back-to-back
  plus the per-PM-domain sweep). The old 4-attempt/1.5–4.5s backoff was too
  short to outlast the ban window, so the whole Reddit/sublet channel
  contributed zero. Firecrawl seeds carried the run (that's where the 128 came
  from).

## Fixes made this session (written + import-verified, NOT yet run to completion)

**apartment_hunt.py**
- `ENRICH_CAP` 70 → **160** so all 128 candidates get their detail page read
  (directly converts "unverified" → real garage labels, lifts match count
  without touching the area filter).
- `_exa_search` backoff hardened: 4→**6 attempts**, sleeps now
  `2.5/5/7.5/10/12.5s` (was `1.5/3/4.5`) to outlast a burst ban.
- `import apartment_hunt` clean; `ENRICH_CAP=160` confirmed bound.

## The re-run FAILED to complete

Launched the re-run in background. It died after the FIRST Exa query (log has
only 3 lines, ends on one 403; process gone; task output empty; no digest
written). Most likely killed when the session context shifted during the new
longer backoff sleep. **The on-disk digest is still the GOOD 20:33 11-card
version — it was NOT overwritten** (the dead run never reached the "Wrote …"
stage).

## Next steps (start here in the new session)

1. **Re-run and let it finish** — this is the whole open action:
   `cd projects/apartment-hunt && python3 -u build_html_digest.py --city denver > /tmp/denver_build.log 2>&1`
   Run it so it isn't interrupted; with cap=160 it enriches all ~128 (more
   Firecrawl scrapes, so it takes longer than the 70-cap run).
2. **Expect:** more confirmed-garage labels (fewer "unverified"), match count
   likely rises above 11, Exa may now contribute (hardened backoff) — or may
   still 403 if Exa's ban is IP/time based, in which case Firecrawl still
   carries it.
3. Check garage footer ("X of Y confirmed garage") and the in-ring count.
4. If still thin after full enrichment: loosen ring → "ring + one more mile"
   (widen `target_zips`/`neighborhoods`/Zillow bounds), NOT back to metro-wide.
5. Backlog (cosmetic): fix cross-source dedup so the same address from two
   sources collapses to one card.
6. Still-open from prior checkpoint: daily auto-run wrapping the build
   (Annabel hasn't confirmed).

## Reference

- Run command: `cd projects/apartment-hunt && python3 -u build_html_digest.py --city denver`
- Current digest (good): `projects/apartment-hunt/digest_denver_latest.html` (20:33, 11 cards)
- Desktop copy: `~/Desktop/apartment-hunt-denver-2026-06-18.html`
- Prior checkpoint: `operations/memory/checkpoints/2026-06-18-2002-apartment-hunt-garage-enrichment.md`
- Key code: `apartment_hunt.py` — `_exa_search` (~L727), `ENRICH_CAP` (L1230)
