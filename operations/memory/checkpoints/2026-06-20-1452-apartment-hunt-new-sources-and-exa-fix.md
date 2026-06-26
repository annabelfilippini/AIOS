---
date: 2026-06-20
time: 14:52
project: apartment-hunt
status: DONE & VERIFIED. Added 4 new source channels (institutional SFH landlords, FRBO/by-owner, self-tour platforms, Reddit owner-direct) and discovered Exa is NOT dead — just rate-limited. Replaced the 30-min Exa stall with a smart circuit breaker. Rebuilt Denver: 116 candidates → 9 matched → 8 unique in-ring houses (was 7). +1-mile ring widen was already applied yesterday; kept current ring per Annabel.
supersedes: 2026-06-19-0924-apartment-hunt-cross-source-dedup-fixed.md
---

# Session: apartment-hunt — new sources + Exa rate-limit fix

## What Annabel asked
"Widen the mile and what are you able to pull from? I don't just want Zillow and
Craigslist. I also want sites most people don't even look at."

Decision via AskUserQuestion: wire in ALL FOUR new channels; KEEP current ring
(don't add a second mile — the +1 mile from yesterday is already live).

## The big correction: Exa is NOT dead
Prior checkpoints said Exa was IP-banned (403 on every call, channel contributes
ZERO). **Wrong as of today.** Exa is RATE-LIMITED, not banned: its open-web
Pass 1 returns ~107 listings fine, then later passes start 403ing. The old
6-retry × 12.5s backoff across ~60 queries = 30+ min of dead waiting and is what
made it *look* dead.

Fix (apartment_hunt.py `_exa_search` + module globals `_EXA_DISABLED` /
`_EXA_CONSEC_FAILS` / `_EXA_FAIL_LIMIT=5`):
- 403/429 → 3 short retries (1.5s, 3.0s) then move on.
- Successful query resets the consecutive-fail streak.
- Disable Exa for the rest of the run only after 5 CONSECUTIVE exhausted
  failures (a real sustained block, not the normal mid-sweep limit).
- Result: **107 Exa listings in 29s** vs a 30+ min stall. Pass 1 (open-web,
  source="exa") fully captured; Pass 2 (reddit) gets skipped — fine, the new
  reddit-cli channel covers that now.

## New source channels added
1. **Reddit owner-direct** (`fetch_reddit` in apartment_hunt.py) — uses the
   shared `tools/reddit-cli` (authenticated, read-only, session 4 days old, live
   read OK). Profile field `reddit_subreddits` (empty = skip; SF skips, Denver =
   DenverList, Denver, Colorado). Filters: offer-vs-request regex, housing-noun
   gate, drop title-ending-"?", drop off-site link-posts (news), 45-day recency.
   Reddit listings skip Firecrawl enrichment (Firecrawl can't read threads) →
   they stay "garage unverified" (DM-the-owner leads). Today: 0 fresh offers
   (recency cutoff drops stale 2024 DenverList posts) — channel works, just no
   fresh in-ring offers right now.
2. **+6 institutional SFH landlords** (firecrawl_seeds): Progress Residential,
   FirstKey, HomeRiver, Mynd, Poplar, Pathlight (on top of Invitation/AMH/MS
   Renewal/Tricon).
3. **+2 FRBO/by-owner**: forrentbyowner.com, Zillow for-rent-by-owner slice.
4. **+3 self-tour platforms (BEST-EFFORT)**: Rently, ShowMojo, Tenant Turner.
   These are per-PM booking widgets with no clean city-browse URL, so they
   usually return 0. Real win there = seeding specific Denver PM pages that use
   them (fast-follow, not done).

Denver firecrawl_seeds: 18 → 29.

## Current digest (clean, on disk + Desktop, 2026-06-20 14:44)
8 unique in-ring houses (was 7). Sources represented: zillow ×2, exa ×2
(highrises, realtor), craigslist ×2, direct:homefinder ×1, firecrawl:zumper ×1.
5 of 8 garage-confirmed. Cross-source address dedup collapsed 9→8.

## Files touched
- `profiles.py` — new `reddit_subreddits` field; Denver: +11 firecrawl_seeds,
  reddit_subreddits set. (still git-untracked: `?? profiles.py`)
- `apartment_hunt.py` — `import subprocess`; `fetch_reddit()` + reddit regexes +
  `_reddit_cli_path()`; `REDDIT_SUBREDDITS` global bound in `apply_profile`;
  reddit gate in `keep_basic`; reddit skip in `enrich_listing`; Exa circuit
  breaker in `fetch_exa`/`_exa_search`; reddit wired into `main()`.
- `build_html_digest.py` — reddit wired into `main()`; footer source line
  updated.
- `notes/in-progress.md` — batch progress (now all done).

## Next steps / backlog
1. (Optional) Commit — all changes are uncommitted; `profiles.py` is untracked.
2. Self-tour fast-follow: find Denver PMs using Rently/ShowMojo/TenantTurner and
   seed their specific listing pages (the city-browse URLs return ~0).
3. Daily auto-run wrapping `python3 -u build_html_digest.py --city denver`
   (Annabel hasn't confirmed). Build takes ~8-10 min, dominated by Firecrawl
   detail-page enrichment (116 pages this run).
4. If a second mile is ever wanted: extend zillow_map_bounds + ring hoods/ZIPs
   in profiles.py (Highlands, RiNo, Five Points, Lowry edges).

## Reference
- Run: `cd projects/apartment-hunt && python3 -u build_html_digest.py --city denver`
  (use `-u` + redirect to a file, NOT piped to tail — buffering hid past runs).
- Digest: `projects/apartment-hunt/digest_denver_latest.html`
- Desktop: `~/Desktop/apartment-hunt-denver-2026-06-20.html`
- reddit-cli: `tools/reddit-cli/reddit-cli` (cookie expires every few weeks;
  `doctor` flags staleness; re-import via Copy-as-cURL).
- Prior checkpoint: `2026-06-19-0924-apartment-hunt-cross-source-dedup-fixed.md`
