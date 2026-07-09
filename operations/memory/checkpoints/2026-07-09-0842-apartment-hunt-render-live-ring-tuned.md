---
date: 2026-07-09
time: 08:42
project: apartment-hunt
status: LIVE & STABLE. Friend-facing Denver houses search deployed on Render (always-on, Mac-independent), Firecrawl upgraded to Standard (100k/mo), search area tuned to a ~20-min radius of Cherry Creek and tightened to drop far suburbs. Link ready to share. One clean full run verified 27 houses / 0 apartment leaks before the final tighten; tighten itself is assert-verified, not yet re-run as a paid search.
supersedes: 2026-07-08-1735-apartment-hunt-render-deploy.md
---

# Session: apartment-hunt — Render deploy, credit upgrade, ring tuning

## Live surface
- **URL (share this):** https://denver-apartment-search.onrender.com
- Runs on Render (Starter, always-on) — works with Annabel's Mac off. ~15 min/full run.
- Old Tailscale funnel link is superseded; local 8787 server left running for her own use.

## Repos / source of truth
- **Source of truth:** `~/Documents/AI-OS/projects/apartment-hunt/` (in the AIOS monorepo).
- **Deploy repo (what Render builds):** PRIVATE `github.com/annabelfilippini/denver-apartment-search`,
  a standalone COPY of 5 files (search_server.py, build_html_digest.py, apartment_hunt.py,
  profiles.py, requirements.txt) at `~/Documents/apartment-search-deploy/`.
- **To ship a change:** edit source → copy the changed file(s) to the deploy folder →
  `git commit && git push` → Render auto-redeploys. Deliberately NOT connected to the
  AIOS monorepo (would expose all personal files).
- Keys live as Render env vars (EXA_API_KEY, FIRECRAWL_API_KEY), set in the dashboard; not in git.

## Firecrawl
- **Standard plan, 100,000 credits/mo**, cycle 2026-07-08 → 2026-08-08. ~99k remaining.
- Full run ≈ 300 credits (~330 runs/mo). Balance check: `curl https://api.firecrawl.dev/v1/team/credit-usage -H "Authorization: Bearer $FIRECRAWL_API_KEY"`.
- Pricing (live 2026-07-08): Hobby $12/mo=5k, Standard $24/mo=100k, Growth $49/mo=500k (billed yearly).

## Code changes this session (all in source + deployed)
1. **Houses-only leak fixed** (apartment_hunt.py): drop Zillow apartment-complex pages by URL
   (`zillow.com/apartments/` or `/b/`) in keep_basic; Zillow map query excludes apa/condo/mf
   home types server-side when LISTING_NOUN=="house".
2. **Form controls** (search_server.py + build_html_digest.py): price MIN+MAX, garage toggle
   (--require-garage; full run = page-verified, quick = text-mention), plus existing beds/baths/type/depth.
3. **Per-seed yield logging** printed to run.log so dead seeds can be trimmed on evidence.
4. **Render port binding**: search_server.py reads HOST/PORT from env (local default unchanged).
5. **Search area (profiles.py)**: widened to ~20-min radius of Cherry Creek, then TIGHTENED —
   dropped far suburbs (Greenwood Village ~30 min, DTC, Centennial) and stopped arterial/suburb
   name spillover (Hampden Ave→Lakewood, "Englewood" label→Centennial 80112). Far areas covered
   ONLY by tight Denver ZIPs. Final bounds W -105.06/E -104.82/S 39.62/N 39.82. blocked_location_markers
   blocks Highlands Ranch. Assert-tested against the 6 real offenders (all drop) + genuine in-ring (all kept).

## Verified
- Full run on Render (pre-tighten, widest ring): 27 houses, 0 apartment leaks, new areas present
  (Central Park, Sloan's Lake, Englewood, etc.). Both API keys confirmed working on Render.
- Tighten: assert-verified locally; NOT yet re-run as a paid search (offered).

## Gotchas learned
- **Render ephemeral disk + in-memory run state**: a redeploy/restart mid-search wipes that run's
  result (happened once — search spent ~293 credits but its output died with the swapped-out
  instance). Always wait for a redeploy to settle before starting a search. Bulletproofing later =
  persist results off-instance.
- **Reddit source** (reddit-cli) needs a local browser cookie → skipped in cloud, non-fatal.

## Open / next
1. Optional: run one clean full search post-tighten for visual confirmation (~300 credits, ~15 min).
2. **Hilltop looks empty = market reality**, not a bug: only ~3 qualifying 3BR houses and they sit
   at/above the $5,000 cap (verified: HotPads shows 3, one at $4,800). Levers: friend raises Price
   max on the form, or add a Hilltop-specific seed URL for guaranteed sweep.
3. Optional robustness: persist results off-instance; add a per-day search cap; retire Tailscale link.
