# 2026-06-02 — Zillow source added via Firecrawl

## What changed

Zillow is now a real source instead of a perpetual 403 in the coverage report.

- New `fetch_zillow_firecrawl()` and `_parse_zillow_html()` in `apartment_hunt.py`.
- Wired into `main()` between Exa and the dedup step.
- Removed the dead `zillow.com` entry from `DIRECT_SOURCE_SEEDS` (it always returned HTTP 403, wasting a fetch and cluttering coverage).
- New env var: `FIRECRAWL_API_KEY` in `.env`. Pipeline skips Zillow gracefully if missing.

## Why Firecrawl and not Playwright

The cron runs at 9am every day from the same IP. Headless Playwright hitting Zillow on a fixed schedule gets captcha-walled within a week or two, then silently returns zero. Firecrawl handles JS rendering plus rotating residential proxies behind the scenes, so the cron stays reliable.

Cost: ~1 Firecrawl credit per run (one URL per day). Free tier covers this comfortably.

## How it works

1. Build a `searchQueryState` JSON blob with SF map bounds, beds 3-3, price 3200-8250, for-rent only.
2. URL-encode it onto `https://www.zillow.com/san-francisco-ca/rentals/`.
3. POST to `https://api.firecrawl.dev/v1/scrape` with `formats: ["rawHtml"]` and `waitFor: 3000` (lets the React app render `__NEXT_DATA__`).
4. Regex out the `__NEXT_DATA__` `<script>` tag, JSON-parse, walk to `props.pageProps.searchPageState.cat1.searchResults.listResults`.
5. Map each result to a `Listing` with `source="zillow"`. Address goes into both the `neighborhood` field (for digest display) and the snippet (so `matches_neighborhood()` can hit a SF ZIP or neighborhood string).

## Failure modes to watch for

- **Zillow renames a `__NEXT_DATA__` key.** Parser returns `[]`, coverage report shows `zillow ... ok ... 0 listings`. Visible but not loud. Glance at the coverage section the first week after enabling, and any time Zillow ships a redesign.
- **Firecrawl rate limits or 4xx.** Coverage report shows `error: firecrawl HTTP <code>: <body>`. Nothing else in the pipeline is affected.
- **Empty rawHtml.** Coverage report shows `error: firecrawl returned empty rawHtml`. Usually a transient Firecrawl side issue — runs the next day will recover.

## To verify it's actually working

```bash
cd ~/Documents/AI-OS/projects/apartment-hunt
.venv/bin/python apartment_hunt.py --dry
```

Look for these two lines in the output:

```text
Fetching Zillow via Firecrawl…
  N raw listings (ok: firecrawl rendered + __NEXT_DATA__ parsed)
```

If you see `0 raw listings (ok: ...)` that's the schema-shift case above — open Zillow's rentals page in a browser, view source, and check what the `__NEXT_DATA__` shape looks like now.

## Side fix included in the same session

`SEEN_PATH` in code was `seen_3br_sf_core.json` but the populated file on disk was `seen.json` (76 entries, last touched 2026-05-07). Cron has been running on an empty seen-set for weeks. Migrated by renaming `seen.json` → `seen_3br_sf_core.json` so the dedup history is preserved.
