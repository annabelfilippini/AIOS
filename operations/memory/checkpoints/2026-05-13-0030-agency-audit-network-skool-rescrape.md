---
date: 2026-05-13
time: 00:30
project: agency-audit-network
status: paused
next-session: Draft Skool DMs to Keith Mortier, Bill Candelaria, and Frank Gannon — the top 3 implementation-operator partner candidates from the re-scrape.
---

# Session: Agency Audit Network — re-scrape with implementation-only filter

## What we worked on

Started from `2026-05-12-1721-agency-audit-network.md` checkpoint. Annabel pushed back on the Nick Rakis recommendation — strategy/education agencies are not real referral partners because the audit hands off build/train/maintain work. Recalibrated the filter to **implementation operators only**, then re-scraped both Mansel (ainative, 64 members) and Mark Kashef (earlyaidopters, 1.4k members) Skool communities with the corrected criteria.

## Decisions made

- **Partner filter is implementation-only.** Saved as memory `feedback_agency_partner_filter.md` in `~/.claude/projects/-Users-annabelfilippini/memory/`. Reject strategy/education/coaching/advisory positioning even when bio says "agency."
- **Nick Rakis demoted from ⭐⭐⭐ to Skip.** "AI Education and Strategy agency" is exactly the rejected shape; his public identity (Accelio CEO + Strategyzer coach) confirms.
- **Manish Unadkat demoted to v2 partner.** Zoho CRM consulting is real implementation but wrong vertical (service businesses, not product brands).
- **Mark Kashef community is the bigger pool.** 199 high-activity members captured vs Mansel's 56. Implementation-density is much higher (paid AI-builder community).
- **Pagination breakthrough:** Skool ignores `?page=` and `?p=` but honors `?levels=N` (1-9). Level-sweep + `?t=admin` is the working pattern; saved in methodology section of the Mark file.

## Open questions

- Identity verification: is `nick-r-2299` on Skool the same Nick Rakis (Accelio/Pivadigm/Strategyzer)? Plausible but unverified. Moot for outreach since he's now Skip-tier.
- Capacity of top picks (Forrest Shaw is CIO day job; Michael Henry is doctor + tutorials) — surface on the intro call.
- Whether Mark Kashef + co-owner Taha El Harti partnership conversation should happen before or after first wave of member DMs.

## Next steps

1. **Security cleanup (still owed from prior session, now urgent — auth_token surfaced in a sub-agent transcript this session):**
   - `rm ~/Documents/skool/skool-curl.txt`
   - Log out of Skool in browser to invalidate the JWT.
2. Draft 3 Skool DMs:
   - **Keith Mortier** (`keith-mortier-9769`, ObsidianLogic.ai) — top Track 1 fit, anti-strategy positioning mirrors ours.
   - **Bill Candelaria** (`bill-candelaria-1322`) — "Scaling Small Businesses with AI + Automation."
   - **Frank Gannon** (`frank-gannon-8833`, Mansel community) — Airtable + Make, explicitly seeking opportunities.
3. After DMs: website copy for Annabel's Claude Design build (deferred from last session).
4. Park Manish Unadkat, Marc Olsen, Amando Garza, Jeremy Krystosik, Nato Guajardo, Carlos Becerra as v2 vertical-specific partners.

## Context to preserve

**Files produced this session:**

- `projects/agency-audit-network/research/mansel-members-agency-candidates-2026-05-12-v2.md` — 56/64 members captured, demotions documented vs v1
- `projects/agency-audit-network/research/mark-kashef-members-agency-candidates-2026-05-12.md` — 199/1400 captured (high-activity slice), 6 strong Track 1 picks
- `~/.claude/projects/-Users-annabelfilippini/memory/feedback_agency_partner_filter.md` — durable filter rule

**Top Track 1 picks (implementation operators):**

- Keith Mortier (ObsidianLogic.ai) — ⭐⭐⭐
- Bill Candelaria — ⭐⭐⭐
- Philip Couboura (wiselydrivenai.com) — ⭐⭐⭐
- Ben Williams (Voice Agents + SME) — ⭐⭐⭐
- Frank Gannon (Mansel) — ⭐⭐⭐
- Fred Vinson — ⭐⭐⭐ (local-biz half only; skip the coaches half)
- Christian Landsteiner (n8n+Make, lv5 active) — ⭐⭐ (Austria timezone caveat)
- Forrest Shaw (Mansel, CIO day job) — ⭐⭐

**Direct-partnership conversation candidates (parallel to Mansel):**

- Mark Kashef + Taha El Harti (Early AI-dopters co-owners).

## System refinement candidates

- **Skool pagination pattern documented** in `mark-kashef-members-agency-candidates-2026-05-12.md` methodology section. Worth promoting into `cli-connections/` or the `skool-press.mjs` script as a `--level-sweep` flag.
- **Implementation-only filter regex** is in `/tmp/skool-scrape/score.mjs` (now deleted). Should be re-implemented inside the skool-press tooling as a `--filter=implementation` mode so future scrapes auto-rank.
- **Sub-agent sandbox surprise:** the general-purpose Agent has no Write/Bash-write permission in this environment. Future scraping/research tasks that produce files must be run from the main session, not delegated.
