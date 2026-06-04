# /audit-package — Bundle & Deploy to Vercel

Assemble the three deliverables (audit, homepage redesign, dashboard) into a branded portal and deploy to Vercel. This is Step 7 of the pipeline — the last thing before outreach.

**Usage:** `/audit-package <prospect-name>`

## Automation mode

When `AUDIT_AUTOMATED=1` is set in the environment, skip any interactive checkpoints — no user confirmations, no browser `open` calls, no manual review pauses. The skill runs end-to-end and reports via files only. Default (unset) = interactive mode, same behavior as today.

## Good Example (Pepper Pong)

Copied `homepage-redesign.html`, `dashboard-preview.html`, and `assets/` into a `<prospect>-audit/` folder. Converted `audit-client.md` → `audit-client.html` using the Pepper Pong brand palette (coral/ink/Inter, 3-card links, topbar back-nav, table with yes/no styling). Built `index.html` landing page with 3 brand-matched cards linking the three deliverables. Ran `vercel --prod --yes` from the folder — took 9s, deployed to `pepper-pong-audit.vercel.app`. Shareable URL pattern auto-aliases to latest production push.

## Bad Example

Deployed from a folder named `deploy/` — Vercel auto-named the project `deploy`, leaving the prospect with a weird URL `deploy-xyz.vercel.app`. Had to rename after the fact. Or: linked the `mockups/` folder directly instead of copying to a clean `<prospect>-audit/` folder — the `v1-handbuilt/` archive shipped to production alongside the real deliverables. Or: forgot to convert `audit-client.md` to HTML, only linked the mockups — prospect opened the portal and saw "Coming Soon" for the audit section.

## Steps

### Step 0a — Leakage audit (loose prospect assets outside `prospects/`)

Run this from the pipeline root before anything else:
```bash
find . -type f \( -iname "*.png" -o -iname "*.jpg" -o -iname "*.jpeg" \
  -o -iname "*.webp" -o -iname "*.gif" -o -iname "*.mp4" -o -iname "*.mov" \) \
  -not -path "*/prospects/*" -not -path "*/.venv/*" -not -path "*/.git/*"
```
If anything returns: a prospect asset leaked out of its folder. Inspect each hit, identify the prospect (by filename or `md5`-match against `prospects/*/mockups/assets/`), and move it into that prospect's `scrape/screenshots/` or `mockups/assets/`. Do NOT delete — the leak means a script wrote to the wrong path; the file may still be referenced. If you cannot identify the prospect, ask Annabel.

### Step 0b — Prune intermediate artifacts (MANDATORY before packaging)

By the time Step 7 runs, the prospect folder holds 30-50+ screenshots that were useful for Steps 2-6 but are now dead weight: scrape screenshots (3 passes × every page), reference-site screenshots, Stitch iteration screenshots + v1/v2 intermediate HTML, `facts/` scrape responses. These take disk space and make every future session re-scan them.

**What to DELETE:**
- `prospects/$NAME/scrape/screenshots/` — the entire directory. Source-of-truth is `scrape-data.md`, which quotes the findings; screenshots were visual context for Claude during analyze + redesign. No longer needed.
- `prospects/$NAME/companion/*/scrape/screenshots/` — same logic for companion properties.
- `prospects/$NAME/reference/*/` — entire subfolders per reference brand. Reference sites were inspiration for `/audit-redesign`; once the mockup is built, the execution cues are baked into the HTML. **PRESERVE `prospects/$NAME/reference/reference-summary.md`** — the breadcrumb file `/audit-redesign` Phase 0 reads on re-runs. Delete sibling `<brand>/` subfolders; keep the top-level summary .md.
- `prospects/$NAME/stitch/homepage-stitch-v1.html`, `homepage-stitch-v1.png`, and any `v2/v3` iterations. Keep ONLY the canonical `homepage-stitch.html` that fed Phase B (or delete the whole `stitch/` dir — the spec/audit/mockup have the full record).
- `prospects/$NAME/mockups/v1-handbuilt/` (if present) — historical artifact, belongs in the POSTMORTEM, not in the deliverable lineage.
- `prospects/$NAME/facts/*-metadata.json` and oversized raw scrape responses that landed on bot walls (e.g., OpenTable Akamai pages) — keep only `verified-facts.md`.

**What to KEEP (never delete):**
- `prospects/$NAME/mockups/homepage-redesign.html` + `dashboard-preview.html` — the deliverables
- `prospects/$NAME/mockups/assets/` — actively referenced by the mockups; deletion breaks them
- `prospects/$NAME/audit.md`, `audit-client.md`, `seo-research.md`, `scrape-data.md`, `redesign-spec.md` — project documents
- `prospects/$NAME/facts/verified-facts.md` — canonical fact source
- `prospects/$NAME/reference/reference-summary.md` — reference-site breadcrumb for `/audit-redesign` re-runs
- `prospects/$NAME/branding.json` (+ any companion branding files) — brand tokens may be reused
- `prospects/$NAME/scrape/raw-html-analysis.json`, `url-inventory.json`, `url-categorized.json` — small, audit-useful, safe to keep
- Top-level scripts (`scrape.py`, `analyze-html.py`, `sitemap.py`, `branding.py`, `verify-facts.py`) — reusable as template for the next prospect
- All `*-metadata.json` files under `scrape/` if small (<50KB each); bulk-delete only if they total >5MB

**How to run the cleanup:**

Claude's Bash tool cannot `rm -rf` in this workspace (auto-denied by permission rules), and pasting a long `&&`-chained `rm -rf` into the terminal breaks (zsh interprets some quoted paths as commands to execute, esp. with bracketed-paste). **Always write a script and hand the one-liner to Annabel.**

1. Print a "before" size report: `du -sh prospects/$NAME` + `du -sh prospects/$NAME/*`.
2. Enumerate the delete targets (paths + sizes) and show them to the user. If `AUDIT_AUTOMATED=1`, skip confirmation; otherwise wait for a yes on the first prospect run.
3. **Write a cleanup script** to `/tmp/$NAME-cleanup.sh` using the `Write` tool. Template:
   ```bash
   #!/bin/bash
   set -e
   P=<absolute path to prospects/$NAME>
   echo "BEFORE: $(du -sh "$P" | cut -f1)"
   rm -rf "$P/scrape/screenshots"
   rm -rf "$P/screenshots"
   rm -rf "$P/reference/<brand>"   # one per reference brand, preserve reference-summary.md
   rm -f  "$P/mockups/qa-*.png"
   rm -rf "$P/facts/scrape"
   rm -f  "$P/facts/scrape-summary.json"
   rm -rf "$P/companion/*/scrape/screenshots"
   rm -f  "$P/stitch/*-screenshot.png"
   echo "AFTER:  $(du -sh "$P" | cut -f1)"
   ```
4. Tell the user: `bash /tmp/$NAME-cleanup.sh` — one line, paste-safe.
5. User runs it, reports BEFORE/AFTER sizes. Typical reduction: 80–120MB → 2–15MB.

This keeps `prospects/` lean so future sessions load fast and disk doesn't bloat across 20+ prospects.

1. **Verify upstream artifacts exist:**
   - `prospects/$NAME/mockups/homepage-redesign.html` (from `/audit-redesign`)
   - `prospects/$NAME/mockups/dashboard-preview.html` (from `/audit-dashboard`)
   - `prospects/$NAME/audit-client.md` (from `/audit-analyze`)
   - `prospects/$NAME/mockups/assets/` (full asset directory)
   - `prospects/$NAME/branding.json` (for landing page brand colors)

2. **Create the deploy folder with the project name.** Naming matters — Vercel uses the folder name as the project slug, which becomes the URL. Use `<prospect-name>-audit/` pattern:
   ```
   cd prospects/$NAME/
   mkdir <name>-audit
   cd <name>-audit
   cp ../mockups/homepage-redesign.html .
   cp ../mockups/dashboard-preview.html .
   cp -r ../mockups/assets .
   ```

3. **Convert `audit-client.md` → `audit-client.html`.** Use the prospect's brand colors (from `branding.json`). Required structure (from Pepper Pong reference):
   - Topbar with "← Back to all deliverables" link (ink-dark bg, white text, links back to index.html)
   - Container max-width 720px, Inter font, editorial line-height 1.65
   - `eyebrow` coral uppercase (category + date)
   - h1 800 weight, -0.025em letter-spacing, 38px
   - h2 700 weight, margin-top 56px
   - h3 700 weight, margin-top 36px
   - `p strong` for bold (ink color), `p em` for italics (coral, non-italic, 600 weight)
   - `ul` with coral dot bullets (absolute-positioned 6px circles)
   - `table` with border, thin dividers, coral "No" / green "Yes" cells
   - `code` inline-code monospace with light gray bg
   - `hr` thin line, 48px margin top/bottom
   - Footer: centered italic attribution
   - Mobile breakpoint at 600px

4. **Build `index.html` landing page.** 3-card pattern, matched to the prospect's brand. Structure:
   - Max-width 560px centered, all-Inter
   - Coral eyebrow with date (uppercase, letter-spacing 0.14em)
   - h1 with brand accent color on the prospect name
   - Subtitle in gray explaining the three deliverables
   - 3 cards linking audit / homepage / dashboard — each card has a number (01/02/03), title, badge (Read / Mockup / Preview), arrow, and 1-line description
   - Cards have hover border + coral glow, translateY(-1px)
   - Footer: "Prepared by Annabel Filippini" + "Get in touch" mailto link. **Email is `annabelflip1@gmail.com`** — not annabel.filippini@ or annabelfilippini@ (those are stale addresses in earlier prospects). Adelitas + Pepper Pong portals were shipped with wrong addresses; Hop Alley caught it.

5. **QA in browser before deploying.** Open `index.html` and click every link. Check audit-client renders cleanly (table styled, headings work, hr lines), homepage + dashboard load correctly from the new paths (assets resolve because we copied them too).

6. **Deploy to Vercel.** Requires `vercel` CLI installed + authenticated (see below).
   ```
   cd <name>-audit/
   vercel --prod --yes
   ```
   This is non-interactive when you pass `--yes`. First-time project setup will auto-create the Vercel project using the folder name. Subsequent deploys push to the same project — production alias `<project>.vercel.app` always points to the latest.

7. **Share the URL with the prospect.** Use the aliased URL `<project>.vercel.app`, not the deployment-specific hash. The alias updates automatically on every `vercel --prod` push, so you can iterate without sending new URLs.

## Assumes

- **Expects:** All three deliverables + branding.json + assets from upstream steps.
- **Produces:** `prospects/$NAME/<name>-audit/` folder + live Vercel URL at `https://<name>-audit.vercel.app`.
- **Quality bar:** Landing page, audit page, and both mockups share consistent brand DNA. Every link works. Mobile responsive. Production URL in under 2 minutes of script-work + 10s of deploy.

## Vercel Setup (one-time, per machine)

Skip if `vercel whoami` returns your username.

```
sudo npm i -g vercel
vercel login   # browser auth flow
```

Alternative without global install: `npx vercel --prod --yes` from the folder. Slower first run, no permissions needed.

## Known Failure Modes

- **Deploying from a badly named folder.** `deploy/` → project `deploy` → weird URL. Always rename to `<prospect>-audit/` before `vercel` runs.
- **Deploying `mockups/` directly.** The `v1-handbuilt/` archive subfolder ships to production. Always copy to a fresh deploy folder.
- **Forgetting the audit HTML conversion.** Prospect sees placeholder text. Always convert audit-client.md to audit-client.html before the `index.html` is built.
- **Hotlinked fonts in audit-client.html.** Use Google Fonts CSS `@import` — don't embed font files locally, that bloats the deploy.
- **Not running `vercel whoami` first.** If auth is stale, the deploy asks for login via browser/inbox code. Check auth state before attempting.
- **Sending the deployment-specific URL** (`project-abc123-scope.vercel.app`). That URL doesn't update on re-deploy. Always send the clean alias (`project.vercel.app`).
