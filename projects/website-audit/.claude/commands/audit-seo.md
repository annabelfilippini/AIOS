# /audit-seo — SEO Keyword Research

Research where a prospect ranks (and doesn't) in search. Check SERP positions, autocomplete behavior, Google Trends, and question-based queries. Diagnose vocabulary mismatches and untapped markets.

**Usage:** `/audit-seo <prospect-name>`

## Automation mode

When `AUDIT_AUTOMATED=1` is set in the environment, skip any interactive checkpoints — no user confirmations, no browser `open` calls, no manual review pauses. The skill runs end-to-end and reports via files only. Default (unset) = interactive mode, same behavior as today.

## Good Example (Pepper Pong)

10 keywords, invisible on 6. Root cause: site says "portable paddle sport," searchers type "mini pickleball set." Pytrends showed Feb 2026 peak (Shark Tank bump) now decaying to 8-20 — interest is event-driven, not sustained. Top states: Colorado (home), Oklahoma, Connecticut. DIY AnswerThePublic revealed trust queries dominate ("is it worth it", "is it legit", "why so expensive") while zero "for [segment]" queries exist — corporate/education markets aren't being reached yet.

## Bad Example

Ran 10 WebSearches, listed positions, said "done." No autocomplete data, no Trends analysis, no question queries, no vocabulary mismatch diagnosis. A checklist, not a strategic analysis.

## Steps

1. Read `prospects/$NAME/scrape-data.md` to understand the business.
2. Pick 8-10 keywords: branded (2-3), category (3-4), intent-based (3-4).
3. **WebSearch each keyword** — note prospect position, top 3 competitors, content types ranking.
4. **Google Autocomplete** via `suggestqueries.google.com/complete/search?client=firefox&q=KEYWORD` — count suggestions (4=low, 10=active), note real search language.
5. **pytrends** (Google Trends via Python):
   ```python
   from pytrends.request import TrendReq
   pytrends = TrendReq(hl='en-US', tz=360)
   pytrends.build_payload(['keyword'], timeframe='today 12-m', geo='US')
   ```
   - `interest_over_time()` → trend direction, seasonality, peak months
   - `interest_by_region(resolution='REGION')` → top states
   - Skip `related_queries()` — always 429s after the first two calls
6. **DIY AnswerThePublic** — autocomplete with prefixes:
   - Questions: "how to play [kw]", "what is [kw]", "is [kw]", "why is [kw]"
   - Segments: "[kw] for kids/office/schools/adults/families"
   - Comparisons: "[kw] vs [competitor]", "[kw] or [alternative]"
7. **Optional manual enrichment:** Google Keyword Planner (volume), Ubersuggest (difficulty), Google Trends browser (deeper geo).
8. Build scorecard, diagnose root causes, identify untapped markets, write top 3 recs.
9. Compile `prospects/$NAME/seo-research.md`.

## Assumes

- **Expects:** `prospects/$NAME/scrape-data.md` from `/audit-scrape`. `pytrends` installed in venv.
- **Produces:** `prospects/$NAME/seo-research.md`
- **Quality bar:** 8+ keywords, autocomplete + Trends for each, root cause diagnosis, at least one untapped market.

## Known Failure Modes

- **pytrends 429 after ~2 calls:** Prioritize interest_over_time + interest_by_region. One build_payload per session is safest.
- **Ubersuggest/SEMrush/AnswerThePublic JS-rendered:** Can't automate. Use DIY autocomplete prefixes instead.
- **Only branded keywords:** Branded tells you nothing about discovery. Category + intent are where the value is.
- **Gaps without causes:** "You don't rank" is useless. "You don't rank because your site says X and searchers say Y" is actionable.
