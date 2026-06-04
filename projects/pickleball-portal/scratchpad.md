# Pickleball Portal — Session Scratchpad
Last updated: April 10, 2026

## Context
Annabel is collaborating with her dad (Tom Filippini, owner/chairman) to revamp pickleballportal.com. Pikolai Starostin is the AI CEO persona on the site. Goal: make everything work properly, confirm affiliate revenue is firing, structure the site for Pikolai to genuinely operate it, and rebrand.

---

## Current Site Overview
- **URL:** pickleballportal.com
- **Founded:** 2017, acquired by Tom in 2021
- **Traffic:** 100K+ monthly visitors, DR 43
- **Content:** 800+ articles, 428+ paddles reviewed, 675+ URLs
- **Newsletter:** 2,200+ subscribers, 45% open rate (Beehiiv — account discontinued, recovery in progress)

## Tech Stack (modern — source of truth)
- **Frontend:** Vercel (auto-deploy broken — manual `npx vercel --prod --yes` only)
- **Database:** Supabase (project ref: cztfwumwvtiwsabdilxd)
- **Images:** Cloudinary (419/419 paddles synced)
- **Newsletter:** Beehiiv (discontinued — see Beehiiv Recovery project)
- **Email:** Resend (lazy-initialized to avoid build failures)
- **Auth:** Google OAuth
- **Affiliate:** Amazon Associates (pickleball07a-20), Skimlinks (publisher 188369, catch-all)
- **Repo:** github.com/twflipper/pickleball-portal-next (private)
- **Legacy (do not use):** WordPress — site migrated off WP. WP is abandoned.

## Key Features on Site
- Paddle Finder (quiz-based, 500+ paddles)
- Tournament Finder (154+ events, map/calendar/list, daily updates)
- Portal Score (proprietary 0-100 ranking)
- Price Tracker → /deals/ (19 retailers, Shopify JSON crawler every 6h)
- News aggregation (RSS, every 6h)
- Court Finder → /courts/
- Tools hub → /tools/ (links to all tools)
- Newsletter signup → /newsletter/

---

## What's Been Done (since Mar 31)

### Foundation Fixes (completed)
- **5 broken routes fixed** (86acb26): /tools hub page created, /newsletter page created, /court-finder→/courts redirect, /price-tracker→/deals redirect, /paddle-reviews→/news/topic/paddle-reviews redirect. All verified live on production Apr 10.
- **JustPaddles fully removed** (690352a): 274 dead affiliate links replaced with Amazon, 99 dead banner ads stripped.
- **Affiliate links fixed** (a7e9342): Removed nofollow/noreferrer that was blocking Amazon tracking.
- **Affiliate CTAs upgraded** (bee4d14): Added Skimlinks catch-all, fixed price checker.
- **Navbar scroll flicker fixed** (f4ef9b2)
- **Resend lazy-init** (1a38de7): Fixed build failures from missing API key at build time.
- **Amazon PA-API v5 migration** (986993f): Updated from deprecated API.

### System Triage (completed)
- **Dead scripts archived** (082e09c): Moved 25+ one-time migration scripts to scripts/_archive/.
- **Pipelines fixed** (082e09c): Cron routes added for price crawler, tournament scraper, news fetcher.
- **Docs overhauled** (e2b0189): OPERATIONS.md written, stale docs fixed, JustPaddles references removed from all docs.
- **CLAUDE.md + AGENTS.md updated** (986993f): Project rules, affiliate programs, known issues documented.

### Pending Affiliate Approvals
- Selkirk (AvantLink) — applied Apr 3
- JOOLA (Awin) — applied Apr 3
- CRBN (Refersion) — applied Apr 3

---

## What's Decided

### Pikolai's Role
- Currently branding only (no real automation)
- Goal: make him a real AI CEO
- Paperclip was evaluated but dropped — too glitchy as of Mar 2026
- Alternative: power Pikolai via scripts, cron jobs, or GitHub Actions

### Strategy Mode
- **SELECTIVE EXPANSION** (decided Apr 4) — 100K visitors already, fix foundation before building new features. SEO + existing traffic as the base.

### Only active humans touching site right now
Annabel + Tom Filippini

---

## Known Broken / Needs Attention
1. **Rankings scraper** — PPA API dead, DUPR returns 403. No fix path without new data source.
2. **Beehiiv API key** — needs rotation (exposed in Discord 2/16). Beehiiv account now discontinued anyway.
3. **IndexNow .txt serving** — Next.js catch-all intercepts it.
4. **Amazon Creators API** — blocked on Tom's credentials.
5. **Logo** — Tom says it looks "weird" / washed out in navbar.
6. **Domain transfer from Namecheap** — EPP code not arriving.
7. **30 untracked scripts** in scripts/ — mix of crawlers, fixers, one-offs. Need triage: commit, archive, or delete.

---

## Next Steps (in priority order)
1. **Untracked scripts triage** — 30 scripts sitting untracked. Decide what to commit vs archive vs delete.
2. **Newsletter strategy** — Beehiiv discontinued. What's the path forward for the 2,200 subscribers? (see Beehiiv Recovery project)
3. **Pikolai automation** — Start wiring up the first real automated capability (content calendar? affiliate monitoring?).
4. **Logo refresh** — Tom flagged navbar logo as "weird."
5. **Pending affiliate follow-ups** — Check Selkirk/JOOLA/CRBN approval status.

---

## Credentials Location
/Users/annabelfilippini/Documents/AI-OS/projects/Pickleball Portal/credentials.md

---

## Rules for This Project
Stored in: /Users/annabelfilippini/Documents/AI-OS/projects/Pickleball Portal/rules/
- **001_pace_and_detail.md** — No rushing. Think through details fully before acting.
