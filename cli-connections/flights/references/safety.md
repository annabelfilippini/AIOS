# Flightscope Safety

## Scope

- Personal-use travel-decision tool. Single user, human-paced queries.
- Reads search/aggregator surfaces (Google Flights via `fast-flights`,
  flightconnections.com route maps). Does **not** touch airline-owned login,
  booking, checkout, seat maps, or CAPTCHA flows — and must not be extended to.
- Distinct from the Wayloft project. Wayloft's "never scrape airline sites" rule
  is scoped to that repo's litigation-risk posture; it does not govern this CLI.

## Rate & politeness

- Do not loop high-volume scrapes. Query the routes/price endpoints at the pace
  a human would. If batching multiple spots, space requests out.
- `fetch_mode="fallback"` is used so Google Flights degrades gracefully rather
  than retrying aggressively.

## Secrets & data

- Never commit cookies, cURL exports, JWTs, or session tokens into AI-OS.
- A flightconnections browser cookie (if needed) is referenced by path via
  `FLIGHTCONNECTIONS_CURL_FILE` and kept outside the repo.
- Optional config at `~/.config/flightscope/config.toml` (outside the repo).

## Dependencies

- `fast-flights` (pip) is the only third-party runtime dependency, and it is in
  the connector's `approval_required` list — install only with Annabel's OK.
- Everything else is Python stdlib.
