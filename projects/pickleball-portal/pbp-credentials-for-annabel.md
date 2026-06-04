---
title: Pickleball Portal — Access & Credentials Guide
type: output
status: active
venture: pickleball-portal
tags: [credentials, handoff, annabel]
created: 2026-03-31
modified: 2026-03-31
audience: Annabel Filippini
⚠️ SENSITIVE: Do not share outside family/team
---

# Pickleball Portal — Access & Credentials Guide
*For Annabel Filippini — March 31, 2026*

---

## How the Site Works & How Money Flows

### The One-Paragraph Version
Pickleball Portal publishes articles about pickleball — paddle reviews, how-to guides, gear rankings. When readers click product links in those articles and buy something, the site earns a commission. That's it. No products, no subscriptions, no ads (yet). Pure affiliate revenue.

### The Full Picture

**1. Traffic comes in from Google**
Someone searches "best pickleball paddle for beginners" → Google shows our article → they click → they land on the site. ~100K+ monthly visitors, almost all from organic search. No paid ads.

**2. They read an article or browse paddle pages**
Two main content types:
- **Blog articles** (`/blog/...`) — written by real humans (12 contributors). Reviews, guides, "best of" lists.
- **Paddle database** (`/paddles/...`) — 428 paddles with specs, ratings, price comparisons. Pikolai keeps these current.

**3. They click a product link**
Every article and paddle page has affiliate links. Main partners:
- **Amazon** — most clicks. 3-8% commission. Tag: `pickleball07a-20`
- **JustPaddles** — auto-injected on every paddle page. ~10% commission via Refersion.
- **Pickleball Central** — major retailer, currently broken (Everflow migration). **Fix this = immediate revenue.**

**4. They buy something**
The click drops a cookie on their browser. If they buy *anything* on Amazon within 24 hours (not just the paddle they clicked), we earn commission. JustPaddles pays on the specific product.

**5. Commission lands in PayPal**
Amazon deposits to PayPal (`tom@pickleballportal.com`) monthly when balance exceeds $10. JustPaddles/Refersion pays monthly.

### Where the Money Actually Comes From (Ranked)
1. **Amazon Associates** — largest, most consistent. Every paddle review + gift guide + shoe review has Amazon links.
2. **JustPaddles** — second. Embedded on all 428 paddle pages automatically.
3. **Pickleball Central** — should be second, currently $0 because tracking is broken. Fix immediately.
4. **ShareASale / other** — small, passive.

### What Drives More Revenue
More traffic × better placement of affiliate links = more money. Pikolai's job is to keep paddle data current (prices, availability) so the links don't go stale. Your job (if you take it on) would be editorial — making the articles better, adding new content, improving SEO rankings.

---

## Master Login — Dan's Account

Most PBP services were set up under Dan Langston (former editor). Use this to access the majority of affiliate programs and tools:

```
Email:    dan@pickleballportal.com
Password: R$0gallegos!
```

---

## PHASE 1 — Set Up Yourself Right Now (Dan's Login Works)

These you can access immediately with `dan@pickleballportal.com / R$0gallegos!`:

### Amazon Associates ⭐ (most important)
**What:** Primary revenue. Earn 3-8% commission on paddle purchases through your links.
**URL:** https://affiliate-program.amazon.com
**Login:** tfilippini@gmail.com / R$$$0gallegos$ *(Tom's Gmail account)*
**Note:** There are also UK (`pickleball07a-21`) and Canada (`pickleball00b-20`) associate IDs for international traffic.

### JustPaddles ⭐ (affiliate — embedded on every paddle page)
**What:** Affiliate program via Refersion. Every paddle page auto-injects a JustPaddles link with the affiliate code.
**Affiliate code:** `rfsn=6471927.deebc4`
**Dashboard:** https://www.refersion.com/affiliate
**Login:** dan@pickleballportal.com / Flight3618!
**Monthly reports:** Emailed to dan@pickleballportal.com from Refersion on the 1st

### Pickleball Central ⭐ (affiliate — NEEDS SETUP)
**What:** Major affiliate partner. Migrated from Refersion to Everflow in April 2025. Old tracking links (rfsn=7922876) are dead — no commissions being earned right now.
**Action required:** Log into Everflow, get your unique tracking link, give it to TJ to wire into the site.
**Dashboard:** https://pickleballcentral.everflowclient.io
**Login:** dan@pickleballportal.com / pickleball2025!
**What to do:** Log in → go to "My Links" or "Tracking Links" → copy your affiliate URL → give to TJ

### ShareASale
**What:** Affiliate network — some paddle brands pay commissions here.
**URL:** https://shareasale.com
**Login:** dan@pickleballportal.com / R$0gallegos! *(or tomfilippini account — try Dan's first)*

### Skimlinks
**What:** Auto-converts product links to affiliate links sitewide. Passive revenue.
**URL:** https://skimlinks.com
**Login:** tfilippini@gmail.com / R$0gallegos! *(try Dan's if that fails)*

### Google Search Console
**What:** Shows which keywords bring people to the site, if Google has crawl errors. Essential for SEO.
**URL:** https://search.google.com/search-console
**Login:** Google sign-in with dan@pickleballportal.com / R$0gallegos! *(or matt@pickleballportal.com / Niche-2017!)*

### Google Analytics
**What:** Traffic dashboard — page views, sessions, top articles, where users come from.
**URL:** https://analytics.google.com
**Property ID:** G-J7Y27KM430
**Login:** Google sign-in with dan@pickleballportal.com / R$0gallegos!

### Beehiiv (Newsletter)
**What:** Email newsletter platform, ~2,219 subscribers.
**URL:** https://app.beehiiv.com
**Login:** dan@pickleballportal.com / Pickleball2023 *(try this first, fall back to R$0gallegos!)*

### Ahrefs (SEO Research)
**What:** Shows keyword rankings, competitor analysis, backlinks. Core SEO tool.
**URL:** https://ahrefs.com
**Login:** Tom@flystraightline.com / P1ckleball! *(Tom's account — ask him to add you as a user)*

### Serprobot (Keyword Tracking)
**What:** Tracks where specific keywords rank on Google over time.
**URL:** https://preview.serprobot.com/app/login
**Login:** matt@pickleballportal.com / Pickle-2021!


### Microsoft Clarity ⭐ (set this up first day — currently OFF, needs activation)
**What:** Records real user sessions on the site. You can watch a video replay of anyone visiting pickleballportal.com — see exactly where they move their mouse, what they click, where they stop scrolling and leave. Also generates heatmaps (hot/cold zones on every page).

**Why it matters:** It tells you *why* traffic isn't converting. If people land on a paddle review and leave without clicking "Buy on Amazon," Clarity shows you where they dropped off. Essential for improving the site.

**Status:** Component is built into the site but not activated — the Project ID environment variable is empty.

**To activate:**
1. Go to https://clarity.microsoft.com
2. Sign in with dan@pickleballportal.com / R$0gallegos!
3. "Add new project" → name: Pickleball Portal → URL: pickleballportal.com
4. Copy the Project ID
5. In Vercel: Settings → Environment Variables → add `NEXT_PUBLIC_CLARITY_ID` = [your project ID]
6. Redeploy → recordings start within minutes

**After Tom activates in Vercel:** https://clarity.microsoft.com → you'll see live session data within 24 hours

### Cloudinary (Images)
**What:** All site images are stored and served here. This is a shared account across all Tom's ventures.
**URL:** https://cloudinary.com → console.cloudinary.com/console/media_library/folders/pickleball-portal
**Account:** `dfizq1up6` (shared — ask Tom to invite your email)
**Login:** api_key: 884411324738881 (ask Tom for dashboard login)
**⚠️ BOOKMARK THIS URL** (not the home view — it's confusing): https://console.cloudinary.com/console/media_library/folders/pickleball-portal

**Folder structure:**
```
pickleball-portal/
  content/       ~888 assets — article/blog images
  paddles/       ~527 assets — organized by brand (selkirk/, joola/, wilson/, etc.)
  memes/         20 assets — meme page images
  about/         about page images
  brand/         logos
  writers/       contributor headshots
  tournaments/   tournament photos
```

**⚠️ CRITICAL — always set BOTH when uploading:**
- `public_id` = controls the URL (e.g. `pickleball-portal/paddles/selkirk/slug`)
- `asset_folder` = controls where it appears in the dashboard sidebar
If you only set one, images end up in "Home" looking lost.

### Namecheap (Domain)
**What:** Where `pickleballportal.com` is registered. Don't change DNS here — Cloudflare manages it.
**URL:** https://namecheap.com
**Login:** tomfilippini / R$0gallegos *(Tom's account)*

### Social Media
| Platform | Username | Login |
|----------|----------|-------|
| Instagram | @pickleballportal | pickleballportal / ask Tom |
| Twitter/X | @pickleballport | matt@pickleballportal.com / Niche-2017! |
| Pinterest | — | matt@pickleballportal.com / Niche-2017! |
| YouTube | — | matt@pickleballportal.com / Niche-2017! |

---

## PHASE 2 — Needs Tom's Help (Requires His Access)

These need Tom to invite you — you can't just log in with Dan's account:

| Service | What it is | What Tom needs to do |
|---------|-----------|---------------------|
| **GitHub** | Code repository | Add your GitHub account as collaborator to `twflipper/pickleball-portal-next` |
| **Vercel** | Hosting / deployment | Invite your email to the project with Developer role |
| **Supabase** | Database (paddle data, users) | Invite your email as Developer |
| **Cloudflare** | DNS / CDN | Add your email as DNS Read access |
| **PayPal** | Where affiliate payouts land — tom@pickleballportal.com | Ask Tom to add you as authorized user |
| **Google Analytics** | Site traffic | Add your Google account as Analyst to the PBP property |

---

## PHASE 3 — Decide Whether You Need These

Lower priority — only set up if you're actively doing that type of work:

| Service | What it is | Login |
|---------|-----------|-------|
| **Monumetric** | Display ad network (potential future revenue) | tfilippini@gmail.com / Pickleballads2023 |
| **HARO** | Help A Reporter Out — PR mentions | dan@pickleballportal.com / Flight36183618 |
| **Impact/Plunge** | Affiliate program (Plunge cold plunge) | tfilippini@gmail.com / R10gallegos! |
| **ShareASale** | Affiliate network | tomfilippini / wiE@M9JB'Pt))BN |
| **GeniusLinks** | Smart affiliate link routing (geo) | dan@pickleballportal.com / Flight_12 |
| **Canva** | Design tool (old graphics) | daniellangston10@gmail.com / Flightline12 |
| **Authority Hacker** | SEO training course | tom@flystraightline.com / uquvedag |

---

## Bitwarden (Password Manager)

TJ uses Bitwarden to manage all credentials. If you need a password for something not listed here:
1. Ask TJ — "What's the login for [service]?"
2. TJ can look it up from the Bitwarden vault

If Tom adds you to the Bitwarden org, you'll have direct access.
**Account email:** tom@venturesabove.com

---

## About the Old WordPress Site

The old site ran on WordPress, hosted by WPX. **That's completely gone** — replaced by the current Next.js site. All WordPress admin logins, WPX hosting, plugin licenses (Elementor, GeneratePress, etc.) are obsolete.

To see what the old site looked like: https://web.archive.org/web/*/pickleballportal.com

---

## What Is Pickleball Portal?

A content site and affiliate platform. Revenue model:
1. Write articles about paddles and pickleball
2. Readers click product links in the articles
3. When they buy, you earn a commission (Amazon 3-8%, other programs vary)
4. Newsletter keeps readers coming back

Operated publicly under the AI persona **Pikolai Starostin** as editor. Tom owns it, you'll run it.

**Live site:** https://www.pickleballportal.com
**Repo:** `pickleball-portal-next` on GitHub

---

## Email Accounts on the Domain

| Address | Used for | Password |
|---------|---------|---------|
| dan@pickleballportal.com | Old editor's account, most service logins | R$0gallegos! |
| matt@pickleballportal.com | Some social/affiliate accounts | Niche-2017! |
| tom@pickleballportal.com | Tom's direct email | R$$$0gallegos! |
| pik@pickleballportal.com | Pikolai AI persona (X/Twitter) | PikolAI1! |

**Webmail access (legacy):** https://s25.wpx.net:20000
- IMAP: s25.wpx.net, port 143
- SMTP: s25.wpx.net, port 25

---

*Last updated: March 31, 2026 | Questions → TJ in Discord #pickleball-portal or ask Tom*
