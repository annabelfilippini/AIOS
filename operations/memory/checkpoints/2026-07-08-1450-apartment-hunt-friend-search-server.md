---
date: 2026-07-08
time: 14:50
project: apartment-hunt
status: LIVE & VERIFIED end to end. Friend-facing self-serve search page built, exposed at https://annabels-macbook-pro.tail09a74d.ts.net/ via Tailscale Funnel. Friends adjust budget/beds/baths/home-type/depth; Cherry Creek 10-min ring stays locked. One full run (9 houses) and one quick sweep (19 listings) completed live. CREDIT WARNING: 184 Firecrawl credits left until 2026-07-13 reset; each search costs ~200+.
supersedes: 2026-06-20-1452-apartment-hunt-new-sources-and-exa-fix.md
---

# Session: apartment-hunt — friend-facing search server + funnel

## What Annabel asked
Make the Denver search self-serve for friends: they query whenever they want
(no cron), can adjust criteria (budget especially), her API keys are fine to
use. Ring stays: 10-min drive from Cherry Creek, ~$5,000, 3bd/2ba. Houses-only
no longer required.

## What was built
1. `build_html_digest.py` — override flags: `--max-price`, `--min-beds`,
   `--max-beds`, `--min-baths`, `--any-type` (noun house->home, drops CL
   housing_type=6), `--no-enrich`, `--out PATH` (skips Desktop copy +
   digest_denver_latest.html so friend runs don't clobber hers). Applied via
   `dataclasses.replace` in `_profile_with_overrides`; ring/ZIPs/bounds/seeds
   NOT overridable. Assert-tested.
2. `search_server.py` (new, stdlib only) — Editorial Cream form on
   127.0.0.1:8787: budget, beds min/max, baths, houses-only vs any type,
   full vs quick depth. POST /search -> subprocess run (one at a time,
   global lock, values clamped server-side), /status self-refreshing with log
   tail + Cancel button, /result serves digest with injected "New search"
   link. State in `web/` (gitignored).
3. Exposure: `tailscale funnel --bg 8787` ->
   https://annabels-macbook-pro.tail09a74d.ts.net/ (off:
   `tailscale funnel --https=443 off`). Needs Mac awake + server running.

## Verified live
- Full run (3BR/2BA/$5k/houses): 131 candidates enriched -> 9 in-ring houses.
  Took ~70 min (June runs were 8-10; Firecrawl slow today).
- Quick sweep ($5.5k): 19 listings, ~8 min. Cancel button used mid-run by
  Annabel from her browser and cleaned up correctly.
- Public URL serves form + results over the internet (curl-verified).

## Hard numbers (measured, replaces earlier estimates)
- Quick sweep burned ~220 credits (406 -> 184): the 29 firecrawl seed
  extractions dominate, NOT enrichment. Full run adds ~130 enrichment scrapes.
- 184 credits left; plan is 5,000/mo resetting 2026-07-13 => ~20 searches/mo.
- Balance check: `curl https://api.firecrawl.dev/v1/team/credit-usage -H
  "Authorization: Bearer $FIRECRAWL_API_KEY"`.
- Exa: open-web pass fine, Reddit pass 403s and circuit-breaks (known).
- reddit-cli cookie still live (2 DenverList offers) — 18 days old, expect
  expiry soon.

## Environment notes
- Killed stale `python3 -m http.server 8787` (style-feed leftover from Jun 15,
  bound on ALL interfaces, shadowing the port on IPv6/localhost).
- Server runs via `nohup python3 search_server.py` from the project dir
  (log: web/server.log). Dies on reboot — restart by hand; no launchd yet.
- Tailscale was Stopped; `tailscale up` reconnected. Funnel config persists.

## Next steps / open
1. If friends need >20 searches/mo: trim firecrawl_seeds for friend runs, or
   Firecrawl top-up/upgrade — decision for Annabel.
2. Optional launchd plist so server + funnel survive reboots.
3. Send friends the URL: https://annabels-macbook-pro.tail09a74d.ts.net/
4. Uncommitted: search_server.py (new), build_html_digest.py, README,
   .gitignore, notes/2026-07-08-friend-search-server.md.
