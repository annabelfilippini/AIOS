# CFS AIOS Pilot — Dad Walkthrough Site

Single-page tabbed walkthrough for the meeting with Tom. Same theme as Annabel's main site.

## Run locally

From the repo root or this folder:

```sh
cd projects/agency-audit-network/dad-pilot/site
python3 -m http.server 8001
```

Then open <http://localhost:8001> in a browser.

(Use port `8001` because the main site usually runs on `8000`. Pick any free port if 8001 is in use.)

## What's inside

- **System Overview tab** — full architecture diagram (Erica's laptop ↔ Dropbox ↔ Cloudflare ↔ Supabase ↔ external APIs), with the five components explained and Erica's day after week 4.
- **Closed Skill Loops tab** — the three nested loops (brand / workflow / skill) plus the per-skill closed-loop diagram applied to LinkedIn, email, and newsletter.
- **Example tab** — the worked LinkedIn skill: rubric, three sample drafts with self-check reports, what gets logged after posting, and the week-4 vs week-6+ comparison.

## Files

- `index.html` — single page, three tabs
- `styles.css` — theme tokens lifted from `projects/site/styles.css`
- `script.js` — tab switching + URL hash sync

## Source docs

- `../plan-v1-2026-05-14.md`
- `../loops-explained-2026-05-14.md`
- `../linkedin-skill-demo-2026-05-14.md`
- `../../../consulting/prospects/charter-flight-support/voice.md`
