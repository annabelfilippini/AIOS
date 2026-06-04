---
title: Pickleball Portal — Architecture Overview
type: output
status: active
venture: pickleball-portal
tags: [architecture, handoff, annabel, wayloft]
created: 2026-03-31
modified: 2026-03-31
audience: Annabel Filippini (engineering handoff / Wayloft context)
---

# Pickleball Portal — Architecture Overview
*Written for Annabel Filippini — March 31, 2026*

This document explains how pickleballportal.com is built, where everything lives, and how it all fits together. Use this as a reference for understanding the codebase or when thinking about how to structure Wayloft.

---

## The Short Version

Pickleball Portal is a **Next.js 15 website** deployed on **Vercel**, behind **Cloudflare** (CDN + DNS). Articles are Markdown files in the git repo. Paddle data (reviews, comparisons, specs) lives in **Supabase** (Postgres). Images are served from **Cloudinary**. Users can sign in with Google. Email is handled by **Resend** and **Beehiiv**.

---

## Hosting Stack

```
User's Browser
     │
     ▼
Cloudflare (CDN + DDoS protection + DNS)
     │  cloudflare servers proxy all traffic
     ▼
Vercel (hosting + deployment)
     │  Next.js App Router, Node.js runtime
     ▼
pickleball-portal-next (GitHub repo)
     │  code lives here, auto-deploys on push to main
     ▼
Supabase (database + auth)     Cloudinary (images)
```

**Domain:** pickleballportal.com — registered and DNS managed in Cloudflare
**Deployment:** Every push to `main` branch triggers a Vercel build automatically
**URL:** `https://www.pickleballportal.com`
**Repository:** `github.com/twflipper/pickleball-portal-next` (private)
**Framework:** Next.js 16 (App Router), React 19, TypeScript

---

## Where Content Lives

### Articles / Blog Posts (409 Markdown files)
**Location:** `content/posts/` in the git repo
**Format:** Markdown (`.md`) with YAML frontmatter
**How it works:** When the site builds, Next.js reads all `.md` files, parses the frontmatter (title, date, SEO meta, author, etc.), and generates static pages. No database involved for articles.

```
content/
├── posts/        ← 409 articles about pickleball
├── blog/         ← blog posts
└── pages/        ← static pages (about, etc.)
```

**Example frontmatter:**
```yaml
---
title: "Best Pickleball Paddles 2026"
slug: best-pickleball-paddles
date: 2026-01-15
author: pikolai
seo_title: "Best Pickleball Paddles 2026 — Expert Reviews"
seo_description: "We tested 47 paddles..."
featured_image: https://res.cloudinary.com/dfizq1up6/image/upload/...
---
```

### Paddle Data (reviews, specs, comparisons)
**Location:** Supabase database (Postgres)
**URL:** `https://cztfwumwvtiwsabdilxd.supabase.co`
**How it works:** The paddles page queries Supabase at runtime. Paddle specs (weight, grip, material, price, ratings) are stored as rows. This is the dynamic data — new paddles get added to Supabase, not to the git repo.

### Static Pages
**Location:** `content/pages/` — also Markdown files, same as articles

---

## Images

All images are served from **Cloudinary** (cloud CDN for images/video).
**Account:** `dfizq1up6` (shared across all Tom's ventures)
**Folder:** `pickleball-portal/` within Cloudinary

**How images are used:**
```
Cloudinary URL pattern:
https://res.cloudinary.com/dfizq1up6/image/upload/[transformations]/[path]

Example (paddle image, auto-resized for mobile):
https://res.cloudinary.com/dfizq1up6/image/upload/f_auto,q_auto,w_400/pickleball-portal/paddles/joola-vision.jpg
```

**Why Cloudinary:**
- Automatic format conversion (WebP for modern browsers, JPEG fallback)
- On-the-fly resizing with URL parameters — one image, infinite sizes
- CDN delivery (fast worldwide)
- No need to store image files in the git repo

**Uploaded via:** Cloudinary dashboard at cloudinary.com (or API)

---

## Database (Supabase)

**What's in Supabase:**
- Paddle catalog (specs, reviews, affiliate links)
- User accounts (who's signed up for the newsletter/my-feed)
- Price alerts (users watching for specific paddle prices)
- Meme data (user-generated meme metadata)

**Auth:** Google OAuth via Supabase Auth. Users sign in with Google — no passwords.

**Connection:** `NEXT_PUBLIC_SUPABASE_URL` env var points to the project URL

---

## Scheduled Tasks (Cron Jobs)

Two cron jobs run automatically on Vercel:

| Job | Schedule | What it does |
|-----|----------|-------------|
| `/api/cron/fetch-news` | 6:00 AM daily | Pulls latest pickleball news/headlines |
| `/api/cron/check-price-alerts` | 2:00 PM daily | Checks paddle prices, emails users who set alerts |

These are defined in `vercel.json` and run as serverless functions.

---

## Email

Two email systems:

**Resend** — transactional email (price alerts, auth emails, one-off notifications)
- Used for: "Your paddle price dropped!" alerts, welcome emails
- Library: `@resend/resend` npm package

**Beehiiv** — newsletter
- Publication ID: `pub_15b56ff7-0d22-4ea5-bcf7-31beb0db5623`
- Used for: the PBP weekly newsletter, subscriber management
- 2,219 active subscribers as of March 2026
- Pikolai (the AI CEO persona) "writes" the newsletter

---

## Analytics

**Google Analytics 4:** `G-J7Y27KM430` (correct ID — `G-0SFR446CDC` in `.env.local` is wrong, needs fixing)
**Microsoft Clarity:** session recordings and heatmaps

---

## The "Pikolai" Persona

Pickleball Portal is publicly operated by **Pikolai Starostin** — a fictional AI CEO persona. Tom runs it behind the scenes. Pikolai's voice/personality lives in `~/Vault/_shared/skills/` and is used when writing articles, newsletters, and social content.

---

## Deployment Flow

```
1. Edit code locally on laptop
2. git push origin main
3. Vercel auto-detects push, starts build
4. Next.js builds all static pages from Markdown files
5. Deploys to Vercel CDN
6. Cloudflare serves traffic from cache
7. Live in ~2 minutes
```

**Environment variables** (secrets, API keys) are set in Vercel's dashboard — never committed to git.

---

## Local Development

```bash
cd pickleball-portal-next
npm install
cp .env.local.example .env.local   # fill in API keys
npm run dev                         # starts at localhost:3000
```

---

## Key Files to Know

| File/Folder | What it is |
|------------|------------|
| `src/app/` | All pages and routes (Next.js App Router) |
| `src/lib/content.ts` | Reads Markdown files, parses frontmatter |
| `src/lib/paddles.ts` | Queries Supabase for paddle data |
| `content/posts/` | All 409 articles |
| `vercel.json` | Cron job schedule |
| `next.config.ts` | Cloudinary image domains, Next.js settings |

---

## What's NOT in This Repo

- **The newsletter content** — lives in Beehiiv
- **Paddle database** — lives in Supabase (not git)
- **Images** — live in Cloudinary (not git)
- **Secrets/API keys** — live in Vercel environment variables (not git)

---

## Things That Need Fixing

1. **GA4 ID is wrong in `.env.local`** — should be `G-J7Y27KM430`, currently set to `G-0SFR446CDC`
2. **IndexNow `.txt` serving is broken** — Next.js catch-all route intercepts `.txt` extension requests
3. **~111 articles need SEO rewrites** — have a plan but haven't executed

---

*Questions? Ask TJ in Discord #pickleball-portal or reach Tom directly.*
