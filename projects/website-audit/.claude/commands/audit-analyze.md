# /audit-analyze — AI Analysis + Audit Documents

Synthesize scrape data and SEO research into two documents: an internal reference audit (exhaustive, tabular, for downstream steps) and a client-facing narrative audit (engaging, story-driven, for the prospect).

**Usage:** `/audit-analyze <prospect-name>`

## Automation mode

When `AUDIT_AUTOMATED=1` is set in the environment, skip any interactive checkpoints — no user confirmations, no browser `open` calls, no manual review pauses. The skill runs end-to-end and reports via files only. Default (unset) = interactive mode, same behavior as today.

## Good Example (Pepper Pong)

**Internal (`audit.md`):** Findings in severity/effort tables, deduplicated. Each issue appears once. Ends with prioritized action list (this-week / this-month / this-quarter). Integrates SEO keyword data inline — "invisible for 6/10 target keywords, root cause: vocabulary mismatch." AI Discoverability section pulls from `ai-seo-research.md` with the /100 score, subscores, and verbatim Perplexity results. No storytelling, pure reference.

**Client-facing (`audit-client.md`):** Narrative arc — opens with specific praise ("your brand voice is dialed in," "211 reviews at 4.95 is elite"), frames the core problem as opportunity not criticism ("the problem is discovery, not conversion"), includes a keyword visibility table prospects actually understand (checkmarks vs. X marks), writes out example meta descriptions they can copy-paste, includes an "AI is recommending your competitors" section with the verbatim Perplexity quote, ends with soft CTA bridging to design mockups. ~180 lines, readable in 10 minutes.

## Bad Example

One document that's half-polished, half-reference. Same findings repeated in executive summary, quick wins, AND detailed sections. Generic praise ("your site looks great!") instead of specific ("your Schools page is the best-structured content page on the site"). Findings like "improve your SEO" instead of "18/20 content pages have no meta description." Accessibility section full of "verify this" instead of actual findings.

## Steps

1. Read `prospects/$NAME/scrape-data.md`, `prospects/$NAME/seo-research.md`, and `prospects/$NAME/ai-seo-research.md`.
2. Identify the core narrative — what's the single biggest insight? (For Pepper Pong: discovery vs. conversion gap.)
3. **Write internal audit** (`prospects/$NAME/audit.md`):
   - Summary (3-5 sentences, core insight)
   - Sections: Technical Health, SEO, AI Discoverability, Accessibility, Content & UX, AI Opportunities
   - Each section: "Working" list + "Issues" table (finding / severity / effort)
   - SEO section integrates keyword research: visibility table, Trends data, autocomplete insights, root causes
   - AI Discoverability section integrates ai-seo-research: /100 score + four subscores, missing schema types, llms.txt/robots.txt issues, verbatim Perplexity query results, copy-pasteable JSON-LD blocks
   - AI Opportunities table: opportunity / impact / effort / connection to findings
   - Deduplicated priority action list at bottom (this-week / this-month / this-quarter)
4. **Write client-facing audit** (`prospects/$NAME/audit-client.md`):
   - What You're Doing Right (specific praise, show you understand their business)
   - The Big Opportunity (core insight framed as growth, not criticism)
   - Urgency section if applicable (Shark Tank decay, seasonal, competitive pressure)
   - Five Things to Fix This Week (concrete, copy-pasteable where possible)
   - Revenue Channels You're Missing (untapped markets from SEO research)
   - **How AI Is Recommending Your Competitors** — verbatim Perplexity results showing what LLMs return when asked about the category. Frame the gap as fixable with specific structured-data and content changes.
   - Where AI Fits In (practical, tied to their specific business)
   - The Housekeeping (smaller items, bulleted)
   - What's Next (soft CTA)
5. Cross-check: every finding in client doc has a backing entry in internal doc. No finding in client doc that isn't substantiated by scrape/SEO/AI-SEO data.

## Assumes

- **Expects:** `prospects/$NAME/scrape-data.md` from `/audit-scrape`, `prospects/$NAME/seo-research.md` from `/audit-seo`, `prospects/$NAME/ai-seo-research.md` from `/audit-ai-seo`
- **Produces:** `prospects/$NAME/audit.md` (internal), `prospects/$NAME/audit-client.md` (client-facing)
- **Quality bar:** Internal doc has severity/effort on every finding. Client doc tells a story a founder reads in 10 min. No generic advice — every finding references specific pages, URLs, or data. AI Discoverability section quotes verbatim Perplexity output.

## Known Failure Modes

- **Repeating findings across sections:** Each finding appears ONCE in internal doc. Client doc can reference themes but shouldn't list the same issue in three places.
- **Generic praise:** "Your site looks professional" is useless. "Your FAQ uses brand voice consistently ('QUESTIONS YOUR MOM WOULD ASK')" shows you actually read the site.
- **Accessibility padding:** Don't include "verify this" items to fill the section. If you can't confirm a finding from the scrape data, note it as unverified, don't list it as an issue.
- **Client doc too long:** Target ~150-200 lines. A busy founder should finish it in one sitting.
- **Missing the narrative:** The client doc needs a core insight that everything hangs on. "Here are 30 things wrong with your site" is a list. "Your site converts great — the problem is nobody finds it" is a story.
