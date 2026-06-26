---
date: 2026-06-18
time: 09:34
project: apartment-hunt
status: DONE pending keys — Multi-city refactor + Editorial Cream HTML shipped and verified against sample data. Blocked on Annabel adding EXA + Firecrawl API keys to .env before a live Denver pull. Gave her the signup instructions; awaiting keys.
supersedes: 2026-06-17-1537-apartment-hunt-multi-city-and-cream-ux.md
---

# Session: apartment-hunt — multi-city + Editorial Cream (awaiting API keys)

## Where this stands

The build is complete and verified. The only thing left to go live is API keys,
which Annabel does not have configured yet (no `.env` exists).

## What shipped (last session, unchanged)

- **`profiles.py`** (new) — `SearchProfile` dataclass + `PROFILES` registry holds
  all city-specific data. Ships `sf` (unchanged behavior) and `denver`
  (whole-metro 3BR, wide budget, `require_neighborhood_match=False`).
- **`apartment_hunt.py`** — `apply_profile()` rebinds module globals; `--city
  {sf,denver}` flag (default sf). Generalized SF-only ZIP/neighborhood/per-person
  logic; per-city seen/digest/archive files.
- **`build_html_digest.py`** — restyled to Editorial Cream (Cormorant + Jost +
  mono figures, cream bg, brass accent, squared corners, no helper subtitles),
  `--city` aware. Fixed latent drop-listings bug (buckets preferred/fallback/other).
- Folder had been deleted by the AI-OS restructure; restored from git at the
  start of last session.

## This session

- Opened styled **sample** pages (`sample_sf.html`, `sample_denver.html`, mock
  data) in her browser so she could see the new design. These are NOT real
  inventory — they're throwaway samples and can be deleted.
- Gave her step-by-step signup instructions for both keys:
  - **Exa** (required): dashboard.exa.ai → API Keys → Create. Free $10 credit.
  - **Firecrawl** (recommended): firecrawl.dev/app/api-keys, key starts `fc-`.
    Noted she likely already has one from her connected Firecrawl MCP server.

## Next

1. Annabel adds to `projects/apartment-hunt/.env`:
   `EXA_API_KEY=...` and `FIRECRAWL_API_KEY=fc-...` (no quotes, no spaces around
   `=`, trailing newline — python-dotenv gotchas from her own notes).
2. First live run: `python build_html_digest.py --city denver` (writes
   `digest_denver_latest.html` + a Desktop copy).
3. Tighten Denver budget/neighborhoods in `profiles.py` once friends decide.
4. Delete `sample_sf.html` / `sample_denver.html` so they aren't mistaken for real.
5. Offered to scaffold `.env` with placeholder lines; she has not answered yet.

## Notes / caveats

- Denver property-manager list is empty (relies on Exa + r/Denver); some Denver
  aggregator URLs are by-analogy and may show as error/blocked in coverage.
- Change note: `projects/apartment-hunt/notes/2026-06-17-multi-city-profiles-and-editorial-cream-ux.md`.
