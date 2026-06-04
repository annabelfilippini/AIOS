# /audit-scrape — Site Scraping & Data Collection

Scrape a prospect's website with Firecrawl. Capture screenshots (desktop full, viewport, mobile), rendered markdown, metadata, and technical details. Produces raw data for `/audit-seo` and `/audit-analyze`.

**Usage:** `/audit-scrape <prospect-name> <url> [--ref <reference-url>]`

The optional `--ref` parameter captures an inspiration/reference website (e.g., glossier.com, spikeball.com) that the prospect's redesign should draw from. When provided, the reference site is also scraped (homepage + 1-2 key pages) and saved alongside the prospect data. This reference flows through the entire pipeline — SEO, analysis, and design all use it.

## Phase 0: Scope & Input Gate (required, output before scraping)

**Scope statement.** Output: (a) prospect name + URL, (b) vertical (restaurant / retail / service / DTC / other), (c) reference URLs collected, (d) verified-facts sources confirmed, (e) mode (interactive or automated). Do not proceed until user confirms in interactive mode.

**Required inputs (ASK before scraping):**

1. **Reference URLs (≥2 for restaurants + local businesses, ≥1 for everything else).** Redesign quality is bottlenecked by reference quality. Ask: "Which 2-3 sites should the redesign draw execution cues from? (Same vertical, comparable tier.)" Pass via `--ref`, repeatable. If the user refuses to pick, note in scrape-data.md — but the completion gate still requires the `reference/` directory have at least one subdir.
2. **Verified-facts sources confirmed.** For restaurants: Yelp + OpenTable + Google Business Profile. For DTC: Trustpilot + Google reviews + site. For service: GBP + LinkedIn. Confirm the prospect actually has presences on each before promising the scrape.
3. **Branding pass runs automatically in Pass 1** (see Step 3). Verify by checking `prospects/$NAME/branding.json` exists after Pass 1.

These three outputs (reference scrapes, `facts/verified-facts.md`, `branding.json`) are HARD DEPENDENCIES for `/audit-redesign`. The completion gate at the bottom of this skill enforces them — if absent, `/audit-redesign` fails fast and points back here.

## Automation mode

When `AUDIT_AUTOMATED=1` is set in the environment, skip any interactive checkpoints — no user confirmations, no browser `open` calls, no manual review pauses. The skill runs end-to-end and reports via files only. Default (unset) = interactive mode, same behavior as today.

## Redesign-only mode (`AUDIT_REDESIGN_ONLY=1`)

When the user wants a redesign without the full audit ("just the redesign, skip the audit"), set `AUDIT_REDESIGN_ONLY=1`. This changes the page set to the minimum `/audit-redesign` needs:

- **Homepage only** from the prospect — not 8 pages. Menu / about / reservations / contact are usually CMS-walled (Toast, Squarespace), return reCAPTCHA stubs, and waste Firecrawl calls. The real facts come from third-party sources (Yelp, Google), not the prospect's sibling pages.
- **Smell test on sibling pages.** If you do scrape more than the homepage, check each page's markdown length. <500 chars → it's a CMS stub, don't scrape siblings on the same CMS. Miss Kim (Apr 19 2026) returned 5 stubs × Toast reCAPTCHA — wasted 5 calls. Next run: stop at page 1.
- **One pass per page,** not three. Desktop-full + markdown is enough. Mobile viewport screenshots of the prospect's site are low-value in redesign mode (you're building responsive CSS from scratch; mobile on *reference* sites matters, on the prospect's it doesn't).
- **Facts sources are load-bearing.** Still scrape Yelp + Google knowledge panel + any third-party profile (Zingerman's for ZCoB members, LinkedIn for solo operators). OpenTable often bot-walls — document and move on.
- **Branding scrape lives in the main `scrape.py`**, not a separate `branding.py`. One venv activation, one Firecrawl client, one file. See "Unified scrape script" below.

Cost for redesign-only: ~1 homepage call + ~3 facts calls + ~1 call per reference page × N refs ≈ 8–12 total. Compare to full audit's ~24+.

## Good Example (Pepper Pong)

Firecrawl scraped 8 pages × 3 screenshot types. Got JS-rendered content Shopify hides from raw HTML — urgency copy, product galleries, video embeds. Combined with curl for meta tags, structured data, alt text audit, third-party scripts. Crawled 4 child sitemaps. 400-line scrape-data.md with 20 findings before analysis started.

## Bad Example

Used `curl` + `WebFetch` instead of Firecrawl. Got raw HTML but missed all JS-rendered content. WebFetch only returned `<head>` on Shopify. Wasted 30 minutes. **Lesson: Firecrawl first, always.**

## File-location rule (HARD REQUIREMENT)

**All prospect-specific files live inside `prospects/$NAME/`. Never at project root, `~/Downloads/`, or elsewhere.** Covers:

- Scripts (`scrape.py`, `analyze-html.py`, `sitemap.py`) → `prospects/$NAME/`
- Data outputs (scrape data, audit docs, mockups, outreach drafts) → `prospects/$NAME/`
- All images/screenshots/videos/downloaded assets → `prospects/$NAME/scrape/screenshots/`, `prospects/$NAME/mockups/assets/`, or `prospects/$NAME/reference/<brand>/`
- Reference material → `prospects/$NAME/reference/`
- Companion property data → `prospects/$NAME/companion/<name>/`

**Bad** (v1 on Pepper Pong + Adelitas): `website-audit/scrape-adelitas.py` at project root, CDN assets landing in `~/Downloads/`.

**Good:** `website-audit/prospects/adelitas/scrape.py` — generic script name, prospect identity from folder. All writes use absolute paths anchored to `BASE`, never CWD.

**Project root may contain only:** `BUILD-PLAN.md`, `CLAUDE.md`, `.env`, `.venv/`, `.claude/`, `prospects/`, and cross-prospect postmortems. **Zero loose media at project root — ever.**

**Path resolution in per-prospect scripts:**
```python
# Script at prospects/<name>/scrape.py resolves the project root as:
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
load_dotenv(PROJECT_ROOT / ".env")

# And its own folder as:
BASE = Path(__file__).resolve().parent

# EVERY image/asset write uses an absolute path under BASE:
screenshots_dir = BASE / "scrape" / "screenshots"
screenshots_dir.mkdir(parents=True, exist_ok=True)
(screenshots_dir / f"{page_name}-desktop-full.png").write_bytes(resp.content)
# NEVER: open("screenshot.png", "wb")  — CWD at run time is unpredictable
```

**Leakage audit (run before any deploy / hand-off):**
```bash
# From the pipeline root. Should return zero results.
find . -type f \( -iname "*.png" -o -iname "*.jpg" -o -iname "*.jpeg" \
  -o -iname "*.webp" -o -iname "*.gif" -o -iname "*.mp4" -o -iname "*.mov" \) \
  -not -path "*/prospects/*" -not -path "*/.venv/*" -not -path "*/.git/*"
```
Any hit = a leaked prospect asset. Move to the right `prospects/<name>/` subfolder before proceeding. `/audit-package` Step 0 runs this check automatically.

## Steps

1. Create `prospects/$NAME/scrape/screenshots/`.
2. **Page set depends on mode:**
   - **Full audit (default):** 8+ pages — homepage, main product/service, about, how-to/features, reviews, press, FAQ, 1-2 vertical-specific.
   - **Redesign-only (`AUDIT_REDESIGN_ONLY=1`):** homepage only. Sibling pages are usually CMS-walled and add no value. Every fact the mockup needs comes from facts sources (Yelp / Google / third-party profiles).
   - **Smell test (all modes):** after page 1, check `len(markdown) < 500`. If true AND the site is on a known CMS (Toast, Squarespace, Shopify, WordPress), skip the remaining sibling pages — they'll be reCAPTCHA stubs. Document which ones you skipped in `scrape-data.md`.
3. **Unified scrape script.** `scrape.py` should handle prospect pages + references + facts sources + branding in ONE file. One `FirecrawlApp` instance, one venv activation. Do NOT write a separate `branding.py` — the branding format is one additional API call, fold it into the homepage scrape block of `scrape.py`.
4. **Firecrawl passes per page:**
   - **Homepage (always):** `formats=["markdown", ScreenshotFormat(full_page=True), "branding"]`, `wait_for=3000` → screenshot + markdown + metadata + brand tokens. Save the branding payload to `prospects/$NAME/branding.json` — **hard dependency for `/audit-redesign`.**
   - **Full-audit sibling pages:** `formats=["markdown", ScreenshotFormat(full_page=True)]`, `wait_for=3000` → 1 pass, desktop-full only. Drop the separate mobile + viewport passes unless the specific audit finding requires them — they triple the call count for marginal visual value. (Pepper Pong Apr 2026 lesson: mobile scrapes were rarely referenced downstream.)
   - **References:** 1 pass per page, desktop-full + markdown.
   - **Facts sources (Yelp, Google, OpenTable, Zingerman's profile, etc.):** 1 pass, `wait_for=4000`, desktop-full + markdown. Accept OpenTable bot-walls silently — fall back to Yelp + Google.
   - Download GCS screenshot URLs with `requests.get()` (not base64).
4. **Raw HTML (curl + Python) per page:** meta tags, JSON-LD, heading hierarchy (H1-H6), image alt audit (total/empty/generic/missing), third-party scripts.
5. **Sitemap crawl:** sitemap.xml → child sitemaps → all URLs grouped by type.
6. **If `--ref` provided — scrape the reference site:**
   - Firecrawl homepage + 1-2 standout pages (product page, about, or whatever makes the reference site great)
   - Full-page desktop screenshot + markdown for each
   - Save to `prospects/$NAME/reference/<brand>/` (screenshots + markdown)
   - Note in scrape-data.md: what the reference site does well — layout, typography, color usage, content structure, CTAs, whitespace, navigation patterns
   - This is NOT about copying — it's about understanding what "good" looks like for this type of business

6.5. **Write `prospects/$NAME/reference/reference-summary.md` (REQUIRED if any ref was scraped).** This file is the durable breadcrumb — it survives `/audit-cleanup` so re-runs of `/audit-redesign` on shipped prospects can pass Phase 0 without re-scraping. Template:

   ```markdown
   # Reference Sites — <Prospect>
   Chosen <YYYY-MM-DD>. Each ref was scraped to `reference/<brand>/` (may have been pruned by /audit-cleanup).

   ## <Brand 1> — <URL>
   Why chosen: <one-line reason, same-vertical / same-tier / execution-quality>
   Execution takeaways for <prospect>: <2-3 bullets — typography, hierarchy, CTA pattern, etc.>
   Do NOT copy: <1 line — identity cues that belong to this ref, not to <prospect>>

   ## <Brand 2> — <URL>
   ...
   ```

   One block per reference. This is the file `/audit-redesign` Phase 0 accepts as proof of reference consideration when the full `reference/<brand>/` scrapes have been pruned.
7. Compile `prospects/$NAME/scrape-data.md`. Review screenshots visually.

8. **Verified facts scrape + consolidation (HARD DEPENDENCY for `/audit-redesign`).** For local businesses, scrape the prospect's owned third-party presences AND write the consolidated canonical file. Two deliverables:

   **8a. Raw source dumps.** Scrape each source to its own file under `prospects/$NAME/facts/`:

   | Vertical | Sources to scrape (Firecrawl) | Raw files |
   |---|---|---|
   | Restaurant | Yelp biz page, OpenTable listing, Google Business Profile | `yelp-<location>.md`, `opentable-<location>.md`, `google-<location>.md` |
   | Retail / DTC | Trustpilot, Google reviews, press mentions, Shopify product pages | `trustpilot.md`, `google-reviews.md`, `press.md` |
   | Service | Google Business Profile, Yelp, LinkedIn | `gbp.md`, `yelp.md`, `linkedin.md` |

   Capture hours, phone, address, photo gallery, top 3-5 review quotes (verbatim + attributed + dated where possible), menu items, press URLs. One file per source, not merged.

   **Bot-wall fallback:** OpenTable + Google often Akamai/reCAPTCHA-block Firecrawl. When that happens, fall back to Yelp + the prospect's own site + any press already in scrape data. Note in `verified-facts.md` which sources succeeded and which failed.

   **8b. Consolidate into `prospects/$NAME/facts/verified-facts.md` (REQUIRED — not optional).** This is the single file `/audit-redesign` reads. Raw dumps alone do not satisfy the gate. Template:

   ```markdown
   # Verified Facts — <Prospect Name>
   Scraped <YYYY-MM-DD>. Every fact here cites a source file in this directory.

   ## Sources
   - ✓ Yelp — facts/yelp-<location>.md
   - ✗ OpenTable — Akamai-blocked
   - ✓ Google Business — facts/google-<location>.md

   ## Identity
   - Legal name: <exact, from source>
   - Address: <exact, from source>  [source: yelp-broadway.md]
   - Phone: <exact format as published>  [source: yelp-broadway.md]

   ## Hours
   - Mon–Fri: <exact>  [source: google-broadway.md]
   - Sat–Sun: <exact>  [source: google-broadway.md]

   ## Reservations / Booking
   - <URL + platform>  [source: ...]

   ## Menu Items
   - <Item name>: <verbatim description>  [source: ...]

   ## Verified Review Quotes
   - "<verbatim quote>" — <attribution>, <platform>, <date>  [source: ...]

   ## Press
   - <Publication> — <date> — <URL>  [source: ...]

   ## Team
   - <Name, role>  [source: <press URL where current role confirmed>]

   ## Programming / Events (optional)
   - <Event name, day, description>  [source: ...]
   ```

   **Every line has a `[source: ...]` citation.** Anything without a citation does not enter `verified-facts.md`, and anything not in `verified-facts.md` does not enter the mockup. When a field has no source, write `— (not verified)` and leave it for the copy spec to handle with soft language.

## Completion Gate (must pass before declaring done)

Verify each item below by reading/listing the file. Do not declare complete on intent — check the filesystem.

- [ ] `prospects/$NAME/branding.json` exists and has non-empty `colors` + `fonts`
- [ ] `prospects/$NAME/facts/verified-facts.md` exists (the CONSOLIDATED file, not just raw source dumps)
- [ ] `verified-facts.md` has Identity + Hours + at least 3 review quotes, each with a `[source: ...]` citation
- [ ] `prospects/$NAME/facts/` contains at least one raw source file (yelp-*.md / google-*.md / trustpilot.md / etc.)
- [ ] `prospects/$NAME/reference/` directory exists and contains at least ≥1 subdirectory with scraped content (≥2 for restaurants / local biz)
- [ ] `prospects/$NAME/reference/reference-summary.md` exists and has a block per scraped ref (name, URL, why, takeaways). This file is the durable breadcrumb — it survives cleanup.
- [ ] `prospects/$NAME/scrape/screenshots/` contains desktop-full + mobile PNGs for the homepage at minimum
- [ ] `prospects/$NAME/scrape-data.md` written
- [ ] Leakage audit passes — no `.png`/`.jpg`/`.mp4` outside `prospects/<name>/`

If any unchecked → output "SCRAPE INCOMPLETE" and list what's missing + how to re-run. Do not say "ready for /audit-redesign."

## Do Not

- Do not skip Step 8b — raw source dumps alone do NOT satisfy the facts gate. Write the consolidated `verified-facts.md`.
- Do not invent facts in `verified-facts.md` to fill empty fields. Missing source → `— (not verified)`.
- Do not scrape without reference URLs in interactive mode — ask first.
- Do not write prospect-specific files outside `prospects/$NAME/`.
- Do not use `WebFetch`/`curl` in place of Firecrawl for primary scraping.
- Do not use `app.scrape_url()` (v3 API, removed) — method is `app.scrape()`.
- Do not retry a timed-out Firecrawl call without checking if the first one succeeded.
- Do not declare the scrape done if the completion gate has any unchecked item.

## Assumes

- **Expects:** Prospect name + URL. `--ref <url>` (repeatable, required-unless-noted). `.env` with `FIRECRAWL_API_KEY` at project root. Venv at `.venv/` at project root.
- **Produces (all inside `prospects/$NAME/`):**
  - `scrape.py`, `analyze-html.py`, `sitemap.py`, `facts.py` — the scripts that did the work (kept for reproducibility + next-prospect template)
  - `scrape-data.md` — primary deliverable
  - `scrape/screenshots/*.png`, `scrape/*.md`, `scrape/*-metadata.json`, `scrape/raw-html-analysis.json`, `scrape/url-inventory.json`
  - **`branding.json`** — Firecrawl branding payload (HARD dep for `/audit-redesign`)
  - **`facts/verified-facts.md`** — consolidated canonical facts file (HARD dep for `/audit-redesign`)
  - `facts/<source>.md` — raw source dumps (yelp-*, google-*, opentable-*, trustpilot, etc.)
  - `reference/<ref-name>/*` — ≥2 expected for restaurant/local-biz, ≥1 otherwise
  - `companion/<name>/*` if the prospect has a sister property also being scraped
- **Cost:** 24 Firecrawl calls per prospect (3 passes × 8 pages) + 1 branding call + ~3 facts calls (Yelp/OpenTable/GBP). +3-6 calls per reference site. Drop viewport (Pass 2) to cut to 16.

## Firecrawl API Reference (v4.22+)

The Firecrawl Python SDK has changed APIs across versions. These patterns are verified working:

```python
from firecrawl import FirecrawlApp
from firecrawl.v2.types import ScreenshotFormat

app = FirecrawlApp(api_key=os.environ["FIRECRAWL_API_KEY"])

# Correct method name: app.scrape() — NOT app.scrape_url()
result = app.scrape(url,
    formats=["markdown", ScreenshotFormat(full_page=True)],
    wait_for=3000
)

# Result fields are ATTRIBUTES, not dict keys:
result.markdown        # str — rendered page content
result.screenshot      # str — URL to download screenshot
result.metadata        # DocumentMetadata object (NOT a dict)

# Metadata is an object — use getattr(), not .get():
title = getattr(result.metadata, 'title', 'fallback')
description = getattr(result.metadata, 'description', '')

# To serialize metadata to JSON:
meta_dict = {k: v for k, v in vars(result.metadata).items() if not k.startswith('_')}

# Mobile screenshot:
result = app.scrape(url, formats=["screenshot"], mobile=True, wait_for=3000)
```

**Load .env manually** — Firecrawl doesn't auto-read .env:
```python
with open(".env") as f:
    for line in f:
        if "=" in line and not line.startswith("#"):
            k, v = line.strip().split("=", 1)
            os.environ[k] = v
```

## Known Failure Modes

- **`scrape_url` doesn't exist:** Method is `app.scrape()`, not `app.scrape_url()`. Changed in v4.x.
- **`metadata.get()` fails:** Metadata is a `DocumentMetadata` object, not a dict. Use `getattr()` or `vars()`.
- **GCS URLs not base64:** Screenshots are URLs. Download with `requests.get()`.
- **WebFetch fails on Shopify:** Use Firecrawl for content, curl for meta extraction.
- **`screenshot@fullPage` invalid:** Use `ScreenshotFormat(full_page=True)` from `firecrawl.v2.types`.
- **No .env auto-loading:** Must manually parse .env file or use `python-dotenv` to load API key into os.environ before creating FirecrawlApp.
