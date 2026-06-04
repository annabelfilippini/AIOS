# Pickleball Portal — Affiliate Program Tracker
Last updated: 2026-04-04

## Quick Reference

| Network | Login Email | Brands Covered | Status |
|---------|-----------|----------------|--------|
| Amazon Associates | tfilippini@gmail.com | Amazon listings (tag: pickleball07a-20) | ACTIVE — $25/210 clicks (March 2026) |
| AvantLink | daniellangston10@gmail.com | Selkirk | NEED TO APPLY |
| ShareASale / Awin | tomfilippini | JOOLA, HEAD | NEED TO CHECK |
| Refersion | dan@pickleballportal.com | CRBN, JustPaddles (dead) | NEED TO APPLY for CRBN |
| Impact | tfilippini@gmail.com | ONIX, Plunge | NEED TO APPLY for ONIX |
| Skimlinks | tfilippini@gmail.com | Catch-all for 48K+ non-Amazon merchants | ACTIVE — deployed April 2026, Publisher 188369 |
| Genius Links | daniellangston10@gmail.com | Amazon geo-routing | DEAD — not integrated in code, no references found |
| Affiliatly | tfilippini@gmail.com | Engage Pickleball | CHECK STATUS |
| UpPromote | — | Paddletek, Holbrook, Six Zero | NO ACCOUNT — SIGN UP |
| Admitad | — | Wilson | NO ACCOUNT — SIGN UP |

---

## Brand-by-Brand Tracker

### Tier 1 — Sign Up Immediately (highest revenue impact)

| Brand | Paddles on Site | Network | Commission | Cookie | Status | Link Format | Notes |
|-------|----------------|---------|-----------|--------|--------|-------------|-------|
| Selkirk | 35 | AvantLink | 15% | 30 days | APPLIED 2026-04-03 | TBD after approval | Applied via selkirk.com affiliate page → AvantLink. Awaiting approval. |
| JOOLA | 50 | Awin | ~10-12% (negotiable) | 30 days | APPLIED 2026-04-03 | TBD after approval | Registered via Awin. Awaiting approval. |
| CRBN | 14 | Refersion | 10% (15% after 100 sales) | 30 days | APPLIED 2026-04-03 | TBD after approval | Registered via Refersion. Awaiting approval. |
| Paddletek | 18 | UpPromote | 10% | TBD | NO AFFILIATE PROGRAM | N/A | Ambassador/player program only — not a publisher affiliate. Consider direct email pitch. |

### Tier 2 — Worth Signing Up

| Brand | Paddles on Site | Network | Commission | Cookie | Status | Link Format | Notes |
|-------|----------------|---------|-----------|--------|--------|-------------|-------|
| Holbrook | 24 | UpPromote | 10-15% | TBD | NOT APPLIED | TBD | Clarify: cash or store credit? af.uppromote.com/holbrookpickleball/register |
| RPM | 10 | Direct | 15% | TBD | NOT APPLIED | Discount code? | Ask about tracked affiliate links (not just discount codes). rpmpb.com/pages/ambassador |
| Engage | 17 | FlexOffers / Skimlinks | 8-10% | TBD | NOT APPLIED | TBD | Available via Skimlinks — may auto-activate when Skimlinks is turned on |
| ONIX | 35 | Impact | 5-12% | 30 days | NOT APPLIED | TBD | Apply at onixpickleball.com/pages/become-an-onix-affiliate |
| Six Zero | 10 | UpPromote | TBD | TBD | NOT APPLIED | TBD | af.uppromote.com/six-zero-7668/login |
| Wilson | 4 | Admitad | 8% | 30 days | NOT APPLIED | TBD | wilson.com/en-us/explore/affiliate-program |
| HEAD | 5 | Awin | 6% | 30 days | NOT APPLIED | TBD | Awin merchant #27978 |

### Tier 3 — Contact Directly (no affiliate program found)

| Brand | Paddles on Site | Status | Contact | Notes |
|-------|----------------|--------|---------|-------|
| Gearbox | 24 | NO PROGRAM | info@gearboxsports.com | Has sponsorship page but no affiliate setup |
| Diadem | 21 | AMBASSADOR ONLY | Website contact | Not ideal for multi-brand review site |
| Gamma | 18 | AMBASSADOR ONLY | marketing@gammasports.com | Requires exclusive paddle use — doesn't work for us |
| BnB | 15 | UNCLEAR | support@bnbpickleball.com | May have program in progress |
| Ronbus | 14 | LOYALTY ONLY | Direct contact | "Ronbus Connect" = customer loyalty, not affiliate |

### Already Active

| Brand/Network | Commission | Tag/ID | Link Format | Status |
|--------------|-----------|--------|-------------|--------|
| Amazon Associates | Varies (~4-8%) | pickleball07a-20 | `amazon.com/dp/ASIN?tag=pickleball07a-20` | ACTIVE — $25/210 clicks (March 2026). 36 ASIN + 392 search fallbacks. 5 untagged links in Supabase need fixing. |
| Skimlinks | Varies (75% of merchant commission) | Publisher 188369 | Auto-monetized outbound links | ACTIVE — deployed April 2026. Amazon/amzn.to excluded. |
| JustPaddles | N/A | N/A | N/A | DEAD — all links removed from code. 17 text mentions remain in content. |

---

## Revenue Estimates (conservative)

Assumptions: 100K monthly visitors, 5% click-through on paddle pages, 2% conversion on affiliate clicks.

| Scenario | Monetized Links | Est. Monthly Clicks | Est. Conversions | Avg Commission | Est. Revenue |
|----------|----------------|--------------------|--------------------|----------------|-------------|
| Current (Amazon only) | ~50 paddles | ~500 | ~10 | $8 | ~$80/mo |
| + Tier 1 brands | ~167 paddles | ~1,670 | ~33 | $15 | ~$500/mo |
| + Tier 2 brands | ~272 paddles | ~2,720 | ~54 | $12 | ~$650/mo |
| + Skimlinks catch-all | ~428 paddles | ~4,280 | ~85 | $10 | ~$850/mo |
| **Total potential** | **428 paddles** | **4,280** | **85** | **~$12** | **~$1,000+/mo** |

Note: These are conservative. Actual numbers depend heavily on traffic to paddle pages, user intent, and paddle price points ($100-250 avg).

---

## Action Items

### This Week (no deploy needed)
- [x] Log in to AvantLink → apply for Selkirk program (applied 2026-04-03)
- [x] Apply for JOOLA via Awin (registered 2026-04-03, awaiting approval)
- [x] Apply for CRBN via Refersion (registered 2026-04-03, awaiting approval)
- [x] Paddletek — no publisher affiliate program (ambassador/player only)
- [x] Log in to Skimlinks → have access (2026-04-03), check activation status
- [x] Amazon Associates verified — $25/210 clicks March 2026
- [x] Genius Links assessed — NOT integrated in code, effectively dead

### Once Approved (requires Vercel deploy access)
- [ ] Update PriceComparison.tsx to append affiliate params per brand (Selkirk/JOOLA/CRBN)
- [ ] Fix 5 untagged Amazon links in Supabase (SQL UPDATE needed)
- [x] Add Skimlinks script tag to layout.tsx (deployed April 2026, Amazon excluded)
- [x] JustPaddles links removed from code (690352a). 17 text mentions remain in content.
- [x] GA4 affiliate click tracking deployed (AffiliateTracker.tsx in layout)

### Brands to Email (no program exists)
- [ ] Email Gearbox: info@gearboxsports.com — pitch affiliate partnership
- [ ] Email BnB: support@bnbpickleball.com — ask about affiliate program
- [ ] Email Diadem: website contact — pitch content partnership
- [ ] Email Ronbus: direct contact — ask about publisher affiliate setup

---

## Skimlinks Setup Notes

When activating Skimlinks as the catch-all:
1. **Exclude Amazon** — we have a direct Amazon Associates account with better rates
2. **Exclude any brand where we have a direct program** (Selkirk, JOOLA, CRBN, etc.)
3. Skimlinks takes 25% of commission — only use it for brands where we have no direct relationship
4. Add the Skimlinks script to layout.tsx: `<script src="https://s.skimresources.com/js/PUBLISHER_ID.skimlinks.js"></script>`
5. Skimlinks will auto-monetize outbound links to 48,000+ merchants

---

## Network Dashboard URLs

| Network | Dashboard | Login |
|---------|-----------|-------|
| Amazon Associates | affiliate-program.amazon.com | tfilippini@gmail.com |
| AvantLink | classic.avantlink.com | daniellangston10@gmail.com |
| ShareASale | account.shareasale.com | tomfilippini |
| Refersion | app.refersion.com | dan@pickleballportal.com |
| Impact | app.impact.com | tfilippini@gmail.com |
| Skimlinks | hub.skimlinks.com | tfilippini@gmail.com |
| Genius Links | app.geniuslink.com | daniellangston10@gmail.com |
| Beehiiv (newsletter) | app.beehiiv.com | dan@pickleballportal.com |
