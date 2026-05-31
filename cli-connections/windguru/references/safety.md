# Windguru Safety

## Scope

- Personal-use wind-decision tool. Single user, human-paced queries.
- Reads one public JSON surface: `windguru.cz/int/iapi.php` (search + GFS
  forecast). Does **not** authenticate, post, or touch any account-owned area —
  and must not be extended to.
- Forecast data is advisory. Always surface model init time and lead days; never
  present a far-out GFS value as a guarantee.

## Rate & politeness

- One forecast fetch per spot. `plan` caches by `windguru_id` so a spot reachable
  from several origins is fetched once.
- Do not loop high-volume polling against `iapi.php`. If checking many spots,
  space requests at a human pace.
- A fetch failure or a no-forecast response degrades gracefully — the spot falls
  back to its catalog wind season rather than being dropped or retried hard.

## Secrets & data

- There is **no key, no login, no cookie, no token** for this source. Nothing to
  store — and nothing credential-like should ever be added to this folder.
- Spot → id mappings are non-secret and live in
  `tools/flightscope/data/kite-spots.json`.

## Dependencies

- Python stdlib only (`urllib`, `json`, `datetime`). No pip install, no browser,
  no Playwright. This is the cheapest engine in flightscope — unlike the Google
  Flights price path, which needs `fast-flights` + a headless browser.
