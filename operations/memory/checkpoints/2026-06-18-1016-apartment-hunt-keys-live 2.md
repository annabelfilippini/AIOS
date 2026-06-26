---
date: 2026-06-18
time: 10:16
project: apartment-hunt
status: READY TO RUN LIVE — Both API keys are in .env and verified loading. Multi-city tool fully ready. Next action is the first live Denver pull (not yet run).
supersedes: 2026-06-18-0934-apartment-hunt-multi-city-awaiting-keys.md
---

# Session: apartment-hunt — keys in, ready for first live run

## Where this stands

The blocker is cleared. Annabel created `projects/apartment-hunt/.env` (I
scaffolded it + opened in TextEdit; she pasted keys and saved). Verified via
python-dotenv without exposing values:

- `EXA_API_KEY` — set, len 36 (UUID-shaped), loads fine.
- `FIRECRAWL_API_KEY` — set, len 35, `fc-` prefix correct.
- File ends with a newline (the python-dotenv gotcha she's hit before).

Nothing has been run live yet. The build itself was finished and verified in the
prior sessions (multi-city `profiles.py`, `--city` flag, Editorial Cream HTML).

## Next (the immediate next action)

1. **First live Denver pull:**
   `cd projects/apartment-hunt && python3 build_html_digest.py --city denver`
   (writes `digest_denver_latest.html` + a dated copy on the Desktop). Or the
   markdown pipeline: `python3 apartment_hunt.py --city denver`.
2. Sanity-check the first digest's coverage report — some Denver aggregator URLs
   are by-analogy and may show error/blocked (expected; Exa/CL/Zillow are the
   backbone).
3. Tighten Denver budget/neighborhoods in `profiles.py` once friends decide.
4. Delete throwaway `sample_sf.html` / `sample_denver.html`.

## Reference

- Build details + caveats: `projects/apartment-hunt/notes/2026-06-17-multi-city-profiles-and-editorial-cream-ux.md`
- Prior checkpoints: 2026-06-17-1537, 2026-06-18-0934 (both superseded by this).
