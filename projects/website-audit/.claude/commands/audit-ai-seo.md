# /audit-ai-seo — AI Discoverability Audit

Audit whether LLMs (ChatGPT, Claude, Perplexity, Gemini) will recommend the prospect's business when users ask category questions. Checks crawler access, schema markup, content structure, authority signals, and runs live test queries against Perplexity. This is the 2026 differentiator — most "website audit" providers only look at Google SEO.

**Usage:** `/audit-ai-seo <prospect-name>`

## Automation mode

When `AUDIT_AUTOMATED=1` is set in the environment, skip any interactive checkpoints — no user confirmations, no browser `open` calls, no manual review pauses. The skill runs end-to-end and reports via files only. Default (unset) = interactive mode, same behavior as today.

## Good Example (Adelitas)

Score 34/100. Crawler access: 10/25 (robots.txt present but blocks `/menu/*`, no llms.txt, sitemap missing). Schema: 0/25 (zero JSON-LD on homepage — no LocalBusiness, no Restaurant, no Menu). Content structure: 14/25 (has FAQ, but buried three clicks deep; no entity-clarity sentence in hero). Authority: 10/25 (Chef Silvia mentioned once, no structured bio). Live queries: Perplexity "best Mexican restaurant Ann Arbor" surfaces 3 competitors, Adelitas appears at position 7 with stale 2023 hours. Recommendations ranked: (1) add LocalBusiness + Restaurant schema — 1 hr of work, largest impact; (2) create `/llms.txt` listing menu PDF and about page; (3) add FAQ to homepage; (4) fix hours in Google Business Profile so Perplexity picks up accurate data.

## Bad Example

Ran one `curl` on robots.txt, said "robots.txt looks fine, nothing else to check." No schema audit, no llms.txt check, no Perplexity query, no authority signal analysis. Generic "add structured data" recommendation with no specifics. Useless to the client — they could have Googled this.

## Steps

1. Read `prospects/$NAME/scrape-data.md` for business context (category, location, name).
2. **Crawler access checks** (curl + parse):
   - `curl -s $SITE/robots.txt` → present? blocks critical paths? allows GPTBot, ClaudeBot, PerplexityBot?
   - `curl -s $SITE/llms.txt` → present? well-formed? (most sites = 404, that's normal — flag as opportunity)
   - `curl -s $SITE/sitemap.xml` → present? valid XML? includes key pages?
3. **Schema markup audit** — for each scraped page in `scrape-data.md`, grep the raw HTML for `application/ld+json`. Parse any JSON-LD found. Check for:
   - Homepage: Organization or LocalBusiness (required), WebSite (nice)
   - Category-specific: Restaurant + Menu (for restaurants), Product (for e-comm), Service (for services)
   - About: Person schema for founders/key staff
   - FAQ page: FAQPage schema
   - Score 0-25 based on coverage.
4. **Content structure checks** (read scrape markdown):
   - One-sentence entity clarity in hero? ("Adelitas is a family-run Mexican restaurant in Ann Arbor since 1994.")
   - FAQ section present and linkable from homepage?
   - H1/H2 hierarchy clean (one H1, H2s describe sections, no skipped levels)?
   - Author/authority page for founders with structured credentials?
   - Score 0-25.
5. **Authority signal checks:**
   - Founder/chef/owner bio present with name, credentials, tenure?
   - Press mentions linked or quoted?
   - Review count + aggregate rating visible on site (not just Yelp)?
   - Location + hours + phone in plain text (not just in image)?
   - Score 0-25.
6. **Live LLM test queries** via Perplexity API (or manual if API unavailable):
   - "best [category] in [city]" — does prospect appear in top 5? With what framing?
   - "[prospect name] [city]" — does Perplexity return accurate hours/phone/description?
   - "[category] [city] with [differentiator]" (e.g., "Mexican restaurant Ann Arbor with outdoor seating") — how well does prospect's content support this discovery?
   - Score 0-25. Document what Perplexity actually says verbatim — this is gold for the client report.
7. **Compile** `prospects/$NAME/ai-seo-research.md`:
   - Total score /100 with four subscores
   - What's working (minimum two items, even on low scores — something is always there)
   - What's missing, ranked by impact × effort (highest-impact/lowest-effort first)
   - Verbatim Perplexity query results
   - Three concrete recommendations with copy-pasteable code where possible (JSON-LD blocks, llms.txt template, FAQ schema stub)

## Assumes

- **Expects:** `prospects/$NAME/scrape-data.md` from `/audit-scrape`. `curl` available. `jq` available for JSON-LD parsing. Optional: `PERPLEXITY_API_KEY` in env for Step 6 (if missing, prompt Annabel to run the three queries manually in Perplexity and paste results).
- **Produces:** `prospects/$NAME/ai-seo-research.md`
- **Quality bar:** All four subscores populated. Schema audit references actual JSON-LD blocks found (or explicitly notes "zero JSON-LD on any scraped page"). At least one Perplexity query result included verbatim. Three recommendations are specific, not "add structured data."

## Known Failure Modes

- **"No schema" is the default answer for small biz sites.** Don't skip the audit because you're confident it'll be zero — the client needs to see the zero. Paste the `find` result showing no JSON-LD blocks.
- **robots.txt blocking LLM bots is common and harmful.** Squarespace and Wix default to blocking `GPTBot` and `ClaudeBot` — flag this explicitly. It's a one-line fix with massive discovery upside.
- **Perplexity API 429s on rapid queries.** Stagger test queries with 5s sleep between. If API unavailable, do the three queries manually in perplexity.ai and paste output into the research doc — don't skip the step.
- **Schema recommendations without code are useless.** Include copy-pasteable JSON-LD blocks in the recommendations section. The client's web person should be able to paste and adapt.
- **Scoring inflation.** If a site has robots.txt + sitemap but nothing else, that's 10/100, not 40/100. Don't pad to make the client feel better — the whole point is to show the gap.
