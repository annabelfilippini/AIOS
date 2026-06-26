
## 2026-06-26 — Per-event taste engine (Batch 1 of 2)
- NEW projects/style-feed/data/closet.json (real wardrobe: purchases + Nuuly box + 2 guess staples, tagged slot/occ/tones)
- NEW projects/style-feed/style_engine.py (event -> occasion -> formula -> ranked owned pieces; demo() self-check passes)
- Verified: 5 lanes all build owned-piece looks, no red, slots filled.
- NEXT (Batch 2): wire /api/looks endpoint in day-planner/serve.py + render from it instead of hardcoded/regex.
- Refinement: active lane should prefer matching Butter set (cami+short) over a generic white tee.

## 2026-06-26 — The Edit wired to engine (Batch 2 DONE)
- the-edit.html now dynamic via /api/looks (lane-grouped weekly, keeps data-occ).
- build_week groups by lane + attaches deduped events list. serve.py simplified.
- Both Morning Edit + The Edit live from the engine. Verified end to end.
- Not committed. Open: AA-meeting->work mismatch; per-event distinct looks; life-os SPA re-test.
