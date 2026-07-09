---
date: 2026-07-08
time: 17:35
project: apartment-hunt
status: DEPLOYED to Render (always-on, Mac-independent) and serving the updated form — VERIFIED healthy (HTTP 200, all form controls present). Firecrawl UPGRADED to Standard on 2026-07-08 (100,000 credits/mo, ~450 searches; cycle 2026-07-08 -> 2026-08-08). Balance confirmed 100,179 via credit-usage endpoint. Friends can run FULL searches today — credit constraint gone. END-TO-END VERIFIED on Render 2026-07-08 18:09: full run completed in ~15 min, 12 real houses, ZERO apartment-complex leaks, cost 296 credits (99,883 left). Both keys confirmed working on Render. Old Tailscale funnel link superseded by Render. Link ready to share: https://denver-apartment-search.onrender.com

RING WIDENED to ~20-min radius of Cherry Creek (2026-07-08 ~18:30, "widest" incl. west side + downtown). Edited profiles.py only: _DENVER_RING_HOODS, fallback_neighborhoods, target_zips (+17 ZIPs), cl_location_to_hood, exa_neighborhoods, zillow_map_bounds (now W -105.11/E -104.79/S 39.58/N 39.84), blocked_location_markers=("highlands ranch","highland ranch") to stop the far suburb substring-matching "highlands". Suburbs (Aurora/Englewood/GV) bounded by ZIP not name. Assert-tested (9 new-area kept, 3 far dropped). Pushed to deploy repo -> Render auto-redeployed. VERIFIED live 2026-07-08 18:52: 27 houses (was 12), 0 apartment leaks, new areas present (Central Park/Sloan's/Englewood/GV/Hampden). Cost so far this widen: ~660 credits (one run collided w/ redeploy + spent ~293 but result died with swapped-out instance; re-ran clean).

TIGHTENED 2026-07-08 ~19:00 (Annabel: "Greenwood Village is ~30 min"). profiles.py: removed far/arterial hood NAMES (greenwood village, denver tech center/dtc, englewood, hampden/hampden south, west aurora) so shared arterial/suburb names stop matching (Hampden Ave->Lakewood, Englewood-label->Centennial 80112); removed ZIPs 80111 (GV) + 80014 (deep Aurora); remapped 80231->washington virginia vale; tightened zillow_map_bounds to W -105.06/E -104.82/S 39.62/N 39.82. Far suburbs now covered ONLY by tight Denver ZIPs (Englewood-proper via 80110/80113, Southmoor via 80237, inner Aurora via 80010/80012). Assert-tested against the 6 real offenders from the prior run (all drop) + 9 genuine in-ring (all kept). Pushed -> Render redeployed, healthy. NOT re-run as a paid search (assert-covered); offered.

HILLTOP NOTE: Hilltop shows ~nothing not from a bug — only ~3 3BR houses exist there and they cluster at/above the $5,000 cap (verified via firecrawl_search: HotPads shows 3, one at $4,800). Levers: raise Price max on the form, or add a Hilltop-specific seed for guaranteed sweep.
ROBUSTNESS NOTE: Render instances have ephemeral disk + in-memory run state, so a redeploy/restart mid-search wipes that run's result (as happened once). Fine for normal use; persist results if bulletproofing later.
supersedes: 2026-07-08-1505-apartment-hunt-houses-only-fix.md
---

# Session: apartment-hunt — Render deploy + friend-facing controls

## What Annabel asked
Move the friend search off her Mac (so it runs when the laptop is asleep), and
let friends adjust garage / baths / rooms / price range so they can widen when
nothing comes back. Considered per-friend API keys — decided against (two
signups + paid Firecrawl = too much friction); keep her keys server-side.

## Live URL
https://denver-apartment-search.onrender.com  (Render Starter, ~$7/mo, always-on)

## What was built this session
1. New friend-facing form controls (search_server.py + build_html_digest.py):
   - Price MIN + MAX (was max only). --min-price flows into CL + Zillow queries.
   - Garage toggle -> --require-garage. Full run = page-verified garage_status
     == "confirmed"; quick sweep/unenriched = falls back to a "garage" text
     mention. Assert-tested.
   - Beds/baths already existed. Home type + depth unchanged.
2. Render deploy:
   - search_server.py now binds HOST/PORT from env (Render sets $PORT; local
     default unchanged at 127.0.0.1:8787). Added `import os`.
   - Standalone deploy copy at ~/Documents/apartment-search-deploy (5 app files
     + render.yaml + .gitignore + README), pushed to a NEW PRIVATE GitHub repo
     github.com/annabelfilippini/denver-apartment-search. Did NOT connect Render
     to the AIOS monorepo (would expose all personal files).
   - render.yaml: python web service, plan starter, HOST=0.0.0.0,
     EXA_API_KEY + FIRECRAWL_API_KEY as sync:false (set in dashboard).
   - reddit-cli source is skipped in cloud (needs local browser cookie) —
     non-fatal, that channel just returns nothing.

## Verified
- Standalone copy imports + binds env port + serves the new form (local smoke).
- Render URL: HTTP 200, form has price min/max, beds, baths, garage, houses-only,
  quick sweep. Repo confirmed PRIVATE.

## NOT verified / open
1. Keys-on-Render + full search path: untested to save the ~184 remaining
   credits. Told Annabel to (a) eyeball the two env vars in Render's Environment
   tab vs .env for paste errors now, (b) run the first real search after the
   2026-07-13 reset.
2. Deploy repo is a COPY, not the source of truth
   (~/Documents/AI-OS/projects/apartment-hunt). After code changes there,
   re-copy the 5 files + push to the deploy repo, or Render auto-redeploys on
   push to that repo's main.
3. Old Tailscale funnel link can be retired; local 8787 server left running for
   Annabel's own use.
