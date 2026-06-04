# Website Audit — Walk-Through-First, Skills-After Approach

## Context

Summer income stream: personalized website audits for small businesses. Cooldown (warm lead) responded with genuine interest after receiving a hand-crafted audit on Apr 9 — first real demand signal. BB evaluated the automated cold pipeline as weak, but the manual audit clearly works.

**Annabel's directive:** Walk through the entire process manually, step by step, get every stage right. After EACH successful step, create a skill. Recursively improve on failures. This follows the Ras Mic methodology.

## The Deliverable Package

Three-part package per prospect:

### Part 1: Site Audit
What's broken, what's underperforming, what's missing. Technical health, SEO (including keyword ranking analysis), accessibility, content/UX, design critique, AI opportunities.
- **Quality bar:** Cooldown audit — 280 lines, findings like "announcement bar links to wrong page", not generic "improve your SEO"

### Part 2: Redesign Recommendations + Mockups
HTML mockups using their actual brand assets. Annotated: what changed and why.
- **Quality bar:** Cooldown redesign — uses actual fonts, colors, voice. Feels like their site, but better.

### Part 3: Dashboard / Capability Preview
Preview of ongoing value for THIS specific business. Site health dashboard, SEO tracking, content calendar — whatever fits.
- **Purpose:** Moves conversation from "one-time audit" to "ongoing partnership."

### Delivery Format
Clean landing page deployed to Vercel. Prospect gets one link to a branded portal with all three deliverables.

## The Workflow (10 Steps, 10 Skills)

Each step is walked through manually on a real prospect. After each successful step, a skill is created. Skills live at `.claude/commands/` in this project.

### Step 1: Prospect Selection (sheet-driven — no skill)
- **Prospect sheet** (Google Sheet managed by Claude — see `prospects-sheet.md` for schema) holds all targets. Columns: company, url, contact_name, contact_email, channel, status, notes, sent_date.
- Annabel curates the sheet (adds rows manually — warm/semi-warm leads she wants to audit). Claude reads/updates it across the pipeline.
- At the start of a run, pick the next row with `status: queued`. Update to `status: scraped` after Step 2, etc. Status progression: queued → scraped → audited → video-ready → sent → replied / dead.
- Judgment stays with Annabel (she decides who's on the list). The sheet is durable state for the pipeline, not a mass-outreach queue.

### Step 2: Site Scraping & Data Collection → `/audit-scrape`
- **Tool:** Firecrawl (not curl, not manual browsing)
- Scrape 8+ key pages: homepage, main product/service, about, how-to/features, reviews, press/social proof, FAQ, and 1-2 vertical-specific pages
- For each page: full-page desktop screenshot, viewport desktop screenshot, mobile screenshot, rendered markdown, metadata
- Also capture via raw HTML: meta tags, structured data (JSON-LD), heading hierarchy, image alt audit, third-party scripts
- Crawl all sitemaps for full URL inventory
- **Reference site (optional):** If Annabel provides an inspiration URL (e.g., glossier.com), scrape its homepage + 1-2 key pages. Save to `prospects/<name>/reference/`. Note what the reference site does well — layout, typography, color, CTAs, whitespace, navigation. This reference flows through the entire pipeline (SEO comparison, audit context, design inspiration).
- Compile into `prospects/<name>/scrape-data.md` + screenshots folder
- **Cost note:** 3 Firecrawl passes × 8 pages = 24 API calls per prospect (+3-6 for reference site). Consider dropping viewport (Pass 2) to cut to 16 if full-page desktop is sufficient.

### Step 3: SEO Keyword Research → `/audit-seo`
- Separate discipline from site scraping — strategic positioning analysis, not data collection
- Identify 8-10 keywords the prospect should rank for based on their business, products, and location
- Search each keyword, capture: who ranks on page 1, where (if anywhere) the prospect appears, search intent type
- Identify gaps: high-value keywords where the prospect is invisible
- Check prospect's existing pages against keyword targets — do they have content for what they should rank for?
- Compile into `prospects/<name>/seo-research.md`

### Step 3.5: AI Discoverability Audit → `/audit-ai-seo`
- **Why this exists (2026 wedge):** Small-biz web designers only look at Google SEO. LLMs (ChatGPT, Claude, Perplexity, Gemini) are increasingly where discovery happens — and they recommend businesses with structured data + clear entity signals. This skill is what most competitors don't do.
- Check crawler access: `robots.txt` (does it block GPTBot/ClaudeBot/PerplexityBot?), `llms.txt` (present?), `sitemap.xml` (valid?).
- Audit schema markup on every scraped page — look for JSON-LD (`application/ld+json`) blocks. Score coverage of LocalBusiness/Restaurant/Product/FAQPage/Person.
- Content structure: one-sentence entity clarity in hero, FAQ presence, H1/H2 hierarchy, authority bios.
- Live LLM test queries via Perplexity: "best [category] in [city]", "[prospect name] [city]", "[category] with [differentiator]". Capture verbatim output — this is the most persuasive thing in the final audit.
- Compile into `prospects/<name>/ai-seo-research.md` with /100 score, four subscores, three recommendations (with copy-pasteable JSON-LD blocks).
- **Inspired by Mansel Scheffel's AI SEO skill** — see `raw/Claude Code + Firecrawl + Playwright Builds Flawless Websites.md`. Ported from his build-from-scratch pipeline into our audit-existing-sites pipeline.

### Step 4: AI Analysis + Audit Documents → `/audit-analyze`
- Feed scrape data + SEO research + AI SEO research to Claude for structured analysis
- Produce TWO documents:
  - **Internal audit** (`audit.md`) — exhaustive reference with severity/effort tables, deduplicated findings, prioritized action list. For downstream steps and call prep.
  - **Client-facing audit** (`audit-client.md`) — narrative arc, engaging, ~180 lines. For the $500 tier deliverable alongside design mockups.
- Client doc structure: What's Working → Big Opportunity → Urgency → Quick Wins → Missing Revenue Channels → AI Opportunities → Housekeeping → What's Next

### Step 5: Design Critique + Redesign Recommendations → `/audit-redesign`
- **Design critique** — visual feedback on prospect screenshots (typography, whitespace, CTA visibility, color contrast, visual flow, mobile responsiveness)
- **Reference comparison (secondary, not primary)** — if a reference site was scraped in Step 2, it's useful for execution inspiration ("how does a good press bar look?"), NOT for dictating identity or layout. The audit drives what to fix. The reference optionally informs how to execute the fix.
- **Audit-informed design** — the audit findings from Step 4 drive design priorities. If the audit says "CTAs are buried" or "trust signals are missing," the redesign addresses those specific issues.
- **Stitch (optional)** — feed brand assets + audit findings + reference site patterns into Google Stitch to generate design variations as a visual canvas. Iterate with Annabel. Export a `design.md` (color tokens, typography, component rules) to guide the HTML build. (Ref: Mansel Scheffel's pipeline — see `/lookup-reference Mansel Scheffel` or `raw/Claude Code + Firecrawl + Playwright Builds Flawless Websites.md`)
- Identify 1-2 highest-impact pages to redesign
- Build HTML mockups using actual brand assets (fonts, colors, imagery)
- Annotate: what changed and why
- **QA the mockup before presenting:** Open in browser, verify every image loads, every link works, scroll interactions function, mobile responsive. Broken images = amateur hour. Use `/qa` or Playwright-style checklist.

#### Design Rules (Learned from Pepper Pong Walk-Through)
1. **The audit drives the redesign, not the reference site.** The audit tells you what's broken. Fix those things. Reference sites are optional inspiration for *how* to execute a fix, not a template to follow. If the original has a signature element (animated marquee, auto-playing videos, bold color), keep it and make it better — don't replace it with generic minimalism.
2. **Download images, don't hotlink.** CDN images (Cloudinary, Shopify) may block hotlinking or require auth. Download assets to `prospects/$NAME/mockups/assets/` and reference locally. This also means the mockup works offline and in any deployment.
3. **Auto-playing video thumbnails > static thumbnails.** If the original site has auto-playing UGC videos, the redesign should too. Use `<video autoplay muted loop playsinline>` with poster frames.
4. **Test the mockup in-browser before showing Annabel.** Every image, every scroll interaction, every responsive breakpoint. A broken mockup wastes the conversation on debugging instead of design feedback.
5. **Check image dimensions vs. container before placing.** Run `sips -g pixelWidth -g pixelHeight` on every image. Match aspect ratio to the CSS container shape — wide/landscape (16:9+) for full-width strips, square for cards. For `object-fit: cover`, check what gets cropped: will people be cut off awkwardly? Will the subject survive? If not, pick a different image or resize the container. A 71x60 thumbnail blown up goes blurry. A portrait photo in a landscape strip loses most of its content. This is the most common recurring issue.

### Step 6: Dashboard / Capability Preview → `/audit-dashboard`
- Design preview of ongoing value for THIS business
- Build as HTML mockup — vision, not working product
- **Purpose:** This is the pitch for ongoing engagement ($1K-3K implementation). The $500 package includes the dashboard as a preview/vision, not a live product.
- **Sections (validated on Pepper Pong):** AI scan hero (product + findings panel), Site Health grades, Keyword Rankings (branded pills + discovery list with accent bars), Google Trends chart, Content Pipeline (blog calendar mapped to invisible keywords), Quick Wins checklist, Growth Channels (collapsible details)
- **Skill created:** `/audit-dashboard` — see `.claude/commands/audit-dashboard.md`
- **Key insight:** Each company's dashboard should have a unique visual personality matching their brand. Check Obsidian `raw/` for fresh DTC/design inspiration before starting each dashboard. Don't default to a template.

#### Dashboard Design Rules (Learned from Pepper Pong Walk-Through)
1. **No white card boxes.** The #1 thing that makes a dashboard look AI-generated. Use transparent sections separated by thin horizontal lines on a clean white background. Learn from Aesop, Everlane, CDLP — editorial layouts, not SaaS dashboards.
2. **Use product photos, not action photos.** Large product shot in hero (at least 50% width), not a tiny thumbnail. Contained, not full-bleed.
3. **All-Inter font stack.** Montserrat/geometric sans at heavy weights reads as AI-generated. Inter at 400-700 feels editorial. Section headers 20px+ at weight 600, not 700.
4. **Keyword presentation: pills + accent list, not opportunity bars.** Owned keywords as compact pills (keyword + rank). Invisible keywords as a vertical list with colored left borders (red/orange/yellow by priority) and plain-English evidence lines. Opportunity progress bars are confusing — kill them.
5. **AI scan hero (optional).** Product image with scan-line animation, grid overlay, corner targeting brackets. Right panel with overall grade (B- at 56px weight 800), category breakdown, key findings with accent bars. Reinforces "we analyzed your site."
6. **Explain the data in plain English.** Every metric needs a "why" — evidence lines, not just numbers. But use collapsible `<details>` to avoid word-vomit.
7. **Don't fake progress.** Show honest current state. All items pending if nothing's done. Content pipeline items are "suggested," not "in progress."
8. **Chart annotations in white boxes, positioned off the line.** Text overlapping trend lines is unreadable.
9. **Growth channels use collapsible dropdowns.** Card surface = icon, name, one-line status, big metric. Details hidden behind "Why this matters" toggle.
10. **Use-case images: concept yes, hero strip no.** Showing the product in different contexts (office, tailgate, dinner party) is a good concept but executed as a strip under the hero it feels cluttered. Better integration: use within relevant Growth Channel cards or skip.

### Step 7: Package & Deploy → `/audit-package`
- Assemble `audit-client.html`, `homepage-redesign.html`, `dashboard-preview.html`, and `assets/` into a clean `<prospect>-audit/` folder (folder name = Vercel project name = URL).
- Convert `audit-client.md` → `audit-client.html` with brand palette (coral accents, Inter, editorial line-height, topbar back-nav, styled tables/lists).
- Build `index.html` landing page: 3 brand-matched cards (audit / homepage / dashboard) with hover glow, coral eyebrow, mailto footer.
- Deploy with `vercel --prod --yes`. Share the aliased URL (`<prospect>-audit.vercel.app`), never the deployment hash.
- This is the **follow-up deliverable** — sent when a prospect wants more after watching the video hook.

### Step 7.5: Final Asset Verify → `/audit-cleanup`
- Runs AFTER `/audit-package`. Catches anything Step 0b missed and anything regenerated during deploy.
- Re-runs leakage `find` from pipeline root (must return zero). Asserts `du -sh prospects/<name>` ≤20MB. Verifies Step 0b delete paths are gone. Scans deploy folder for stray images outside `assets/`.
- Fails loud on RED. GREEN = outreach is safe to send.

### Step 8: Video Walkthrough + Drive Upload → `/audit-video`
- **Annabel records** a 60-90sec screen recording: quick walk-through of the prospect's current site, 2-3 key audit findings, and the redesign mockup. Loom or QuickTime. Warm, direct, "I made this for you" energy.
- **Claude uploads** the finished video to a dedicated Google Drive folder (e.g. `website-audit/outbound/`) via the Google Drive MCP. Records the Drive file ID + shareable link in the prospect sheet under `video_link`.
- **Annabel clicks share** in Drive, adds the prospect's email (pulled from the sheet), and sends. Drive's native share email is warm by default — feels like a personal video, not a pitch.
- The video is the **hook**. It does 80% of the selling. Keep it short and specific.

### Step 9: Outreach Email Draft → `/audit-outreach`
- Short follow-up or accompanying email (sent same day as the Drive share).
- 2-3 sentences max. "Hey [name], made a quick video walking through [site] — happy to share the designs too if it sparks anything." Include portal link (`<prospect>-audit.vercel.app`) as the "more if you want it" option.
- Tone: the video did the work. The email is just context + next step. Never salesy.
- Annabel sends.

### Step 10: Delivery & Tracking (automated via sheet — no skill)
- Status column in the prospect sheet progresses: queued → scraped → audited → video-ready → sent → replied / dead.
- Claude updates status after each pipeline stage. Annabel updates to `replied` or `dead` as responses come in.
- `sent_date` auto-filled when status flips to `sent`.

## Skill Architecture

**10 skills total** (`/audit-scrape`, `/audit-seo`, `/audit-ai-seo`, `/audit-analyze`, `/audit-redesign`, `/audit-dashboard`, `/audit-package`, `/audit-cleanup`, `/audit-video`, `/audit-outreach`). Each created immediately after walking through that step on a real prospect.

Every skill follows this format:
- **Title + description** (one line each)
- **Good example** from the walk-through (what "right" looks like)
- **Bad example** from the walk-through (what would have gone wrong)
- **Steps** — minimal, concrete
- **Assumptions** — what it expects from upstream, what it produces downstream
- **Quality checks** — how to verify the output is good

Skills live at: `website-audit/.claude/commands/`

### Skill Contract Chain
```
[Prospect sheet: status=queued] — Annabel adds row
     ↓
/audit-scrape → produces prospects/<name>/scrape-data.md + scrape/screenshots/ + branding.json
               + optional: prospects/<name>/reference/ (inspiration site data)
               [sheet: status=scraped]
     ↓
/audit-seo → produces prospects/<name>/seo-research.md
     ↓
/audit-ai-seo → produces prospects/<name>/ai-seo-research.md
     ↓
/audit-analyze → produces prospects/<name>/audit.md + audit-client.md
               [sheet: status=audited]
     ↓
/audit-redesign → reads audit.md + reference/ + scrape/screenshots/ + branding.json
               → produces prospects/<name>/mockups/homepage-redesign.html + mockups/assets/
     ↓
/audit-dashboard → produces prospects/<name>/mockups/dashboard-preview.html
     ↓
/audit-package → produces prospects/<name>/<name>-audit/ (deploy folder) + live Vercel URL
               → <prospect>-audit.vercel.app
     ↓
/audit-cleanup → verifies no asset leakage, prospect folder ≤20MB, deploy folder is clean
               → GREEN report required before outreach
     ↓
/audit-video → Annabel records locally → Claude uploads to Google Drive folder
             → produces prospects/<name>/video-meta.json (drive_file_id, share_url)
               [sheet: status=video-ready]
     ↓
/audit-outreach → produces prospects/<name>/outreach-draft.md (short email, video + portal links)
               [sheet: status=sent after Annabel sends]
```

## Progress

### Walk-Through #1: Pepper Pong (pepperpong.com)
- [x] Step 1: Prospect selected — Dad's business, warm lead, Shopify store
- [x] Step 2: Site scraped with Firecrawl — 8 pages, 24 screenshots, full scrape-data.md
- [x] `/audit-scrape` skill created from Step 2
- [x] Step 3: SEO keyword research — 10 keywords, 4 visible, 6 invisible, seo-research.md complete
- [x] `/audit-seo` skill created from Step 3
- [x] Step 4: AI analysis + audit documents — internal (audit.md) + client-facing narrative (audit-client.md)
- [x] `/audit-analyze` skill created from Step 4
- [x] Step 5: Design critique + redesign mockups (v1 hand-built Apr 13, v2 Stitch pipeline Apr 14)
- [x] `/audit-redesign` skill created + rewritten Apr 14 to mandate Stitch + agent delegation
- [x] Step 6: Dashboard preview — AI scan hero, editorial section layout, keyword pills/accent list
- [x] `/audit-dashboard` skill created + rewritten Apr 14 to mandate Stitch + agent delegation
- [x] Step 7: Package & deploy — live at https://pepper-pong-audit.vercel.app (Apr 14)
- [x] `/audit-package` skill created from Step 7
- [x] Hook enforcement: `.claude/settings.json` reminds Claude to delegate HTML rebuilds to agents (Apr 14)
- [x] Postmortem written: `POSTMORTEM-pepper-pong.md` — ~5x token reduction vs. hand-build
- [ ] Step 8: Video walkthrough + Drive upload (Annabel records, Claude uploads)
- [~] `/audit-video` skill drafted Apr 14 — provisional until first real upload run
- [~] Step 9: Outreach draft written for Pepper Pong (hypothetical — Tom is Dad, not sent). Template validated.
- [~] `/audit-outreach` skill drafted Apr 14 — provisional until first real send on prospect #2
- [ ] Step 10: Delivery & sheet status tracking (no skill — sheet updates after Annabel sends)

### Infrastructure (resolved Apr 14)
- [x] Google Drive MCP authenticated — upload works via `create_file` + `parentId`; share tool missing (Annabel clicks share, matches human-gate rule)
- [x] Sheet updates = MANUAL. Drive MCP is read-only for sheets. Revisit gspread at 5+ prospects.
- [x] Master sheet `Company Resources` live at id `1YO_7B7F7qhJdXzXCJnvDGS2W3rslyLhHM8zXqsdAhxY`
- [x] Parent Drive folder `Website-Audits` (id `1RyLRyZyp94P7BVhnWUs9NsWcwB5c9otC`) holds the sheet + all per-prospect folders
- [x] **Step addition:** one Drive folder per prospect under `Website-Audits/`, holds the video + any links Annabel wants to reference. Pepper Pong folder id: `1TlE66LCe2geERbAlbOrmM-oc4yrPJSLu`. Annabel creates the folder before Step 8; Claude reads its id from the sheet (or asks) and uploads there as `parentId`.

## What We're NOT Building (Yet)

- ElevenLabs voice clone / video generation — now planned as Step 9, but implementation deferred until walk-through reaches that step
- Automated email sending — delivery stays human
- Google Sheets API integration — simple spreadsheet works at this scale
- launchd scheduling — no automation until skills are validated

## Kill Gate

10 personalized audits through warm channels in 2 weeks. Fewer than 3 conversations = kill.

## Key Reference Files

- `prospects/pepper-pong/scrape-data.md` — first complete scrape (template for future prospects)
- `projects/ai-site-audit/cooldown-audit.md` — gold standard audit output
- `projects/ai-site-audit/cooldown-outreach-draft.md` — proven outreach tone
- `projects/ai-site-audit/cooldown-redesign.html` — homepage redesign reference
- `projects/ai-site-audit/index.html` — landing page format reference
