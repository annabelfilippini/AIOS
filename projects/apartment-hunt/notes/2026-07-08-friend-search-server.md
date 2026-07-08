# 2026-07-08 — friend-facing search server + criteria override flags

Annabel's Denver friends should be able to run the search themselves and
adjust criteria (budget especially), on demand, no cron. Ring stays locked.

## build_html_digest.py

New flags, applied via `dataclasses.replace` on the profile before
`apply_profile` (see `_profile_with_overrides`):

- `--max-price N` — sets both ideal and stretch ceiling
- `--min-beds N` / `--max-beds N` — max is clamped to >= min
- `--min-baths N` — also rewrites the Craigslist `min_bathrooms` param
- `--any-type` — listing_noun "house" -> "home" (disables the house-mode hard
  filter and un-houses the Exa queries), drops CL `housing_type=6`
- `--out PATH` — write the digest only there (no `digest_<city>_latest.html`
  overwrite, no Desktop copy) so friend runs don't clobber Annabel's digest
- `--no-enrich` — skip detail-page enrichment. Surfaced on the form as
  "Quick sweep". MEASURED cost, not the estimate: a quick sweep burned ~220
  credits (406 -> 184) — the 29 firecrawl seed extractions dominate, not
  enrichment. ~20 searches/month on the 5,000 plan. Quick ≈ 8 min; the full
  run's enrichment stretched to ~70 min this session (Firecrawl slow/retries),
  vs 8-10 min in June. Credits reset 2026-07-13.

NOT overridable: neighborhoods/ring, target ZIPs, Zillow map bounds, seed
URLs. Known ceiling: portal seed URLs are hardcoded 3BR/house-typed, so
`--any-type` / beds overrides widen the filter side while those seeds keep
feeding houses; Craigslist, Zillow map search, and Exa adapt fully.

## search_server.py (new)

Stdlib-only ThreadingHTTPServer on 127.0.0.1:8787, Editorial Cream styling:

- `/` form: budget, beds min/max, baths min, houses-only vs any type.
  Values clamped server-side (public endpoint, don't trust the form).
- POST `/search` -> subprocess `build_html_digest.py --city denver <flags>
  --out web/result.html`, stdout to `web/run.log`. One run at a time
  (global lock); a second submit while running just lands on /status.
- `/status` self-refreshing page with log tail + elapsed + Cancel button.
- `/result` serves the finished digest with a "New search" link injected.
- `web/` is throwaway state (gitignored candidates: run.log, result.html,
  last.json).

## Exposure

`tailscale funnel --bg 8787` -> https://annabels-macbook-pro.tail09a74d.ts.net/
(persists in tailscale's config until `tailscale funnel --https=443 off`).
Requires the Mac awake + `python3 search_server.py` running. Also killed a
stale `python3 -m http.server 8787` (style-feed dev leftover from Jun 15) that
was shadowing the port on IPv6.
