---
date: 2026-06-02
time: 09:55
project: apartment-hunt
status: active-folder-only
next-session: check projects/apartment-hunt/digest_latest.md and digests/ after cron; no Telegram token needed
---

# Session: apartment-hunt folder-only reset

## What we worked on
- Annabel asked to remove the Telegram connection and have apartment hunt results written to a folder for now.
- Updated `projects/apartment-hunt/apartment_hunt.py` to be folder-only:
  - Normal run writes `digest_latest.md`.
  - Normal run writes a dated archive in `digests/YYYY-MM-DD.md`.
  - Normal run updates `seen_3br_sf_core.json`.
  - `--dry` still writes markdown but skips seen-set updates for testing.
- Updated `projects/apartment-hunt/README.md` so it no longer mentions Telegram.

## Decisions made
- No Telegram token refresh is needed for the current workflow.
- Keep cron as-is: daily 9am run still works because it calls `.venv/bin/python apartment_hunt.py`.
- Keep `--dry` as the safe testing path.
- Keep the current 3BR Russian Hill/North Beach search criteria from the previous reset.

## Open questions
- Should the daily cron be changed to a different time while Annabel is actively searching?
- Should we add a quick local index page for browsing archived digests more comfortably?

## Next steps
1. Let cron run or run manually:

```bash
cd /Users/annabelfilippini/Documents/AI-OS/projects/apartment-hunt
.venv/bin/python apartment_hunt.py
```

2. Read results from:
   - `projects/apartment-hunt/digest_latest.md`
   - `projects/apartment-hunt/digests/`

## Context to preserve
- Current search: exact 3BR, Russian Hill first, North Beach second, Hayes Valley/Marina/Pacific Heights fallback.
- Budget: ideal <= $7,500/month, stretch <= $8,250/month.
- Hard no: Tenderloin, TenderNob, Lower Nob, Polk Gulch, Civic Center.
- Access boundary remains: authenticated sources can be added with explicit permission and site-compatible use, but no login bypass, CAPTCHA evasion, or access-control circumvention.

## System refinement candidates
- Consider adding a small `open_latest` helper or static HTML digest index so folder-only apartment results are easier to scan.
