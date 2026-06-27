---
date: 2026-06-27 17:00
project: stoop
status: in-progress
type: checkpoint
slug: stoop-per-week-availability
---

# Stoop — When2Meet grid + per-week (dated) availability

Follows `2026-06-27-0858-stoop-teaser-photo-availability.md`. Two changes this
session, both in the single-file app `projects/stoop/index.html`.

## 1. Availability editor → When2Meet-style paint grid
Replaced the per-day chip picker with a drag-to-paint grid (Annabel liked the
When2Meet look). Days = columns (Sun–Sat), 30-min slots 9am–8pm = rows (161
cells). Dark header w/ day initials, warm paper cells, solid hour lines + dotted
half-hour lines, accent fill. Pointer events + `elementFromPoint` for
mouse/touch drag; tap toggles. Cells have `touch-action:none` (paint over
scroll). `bindPaint()` + `renderDayTimes()` + `setCell()`.

## 2. Per-week availability — data model changed recurring → dated
**Decision (asked Annabel): pure per-week + copy**, not recurring-default-with-
overrides. Each week is set on its own; "copy last week" mitigates busywork.

- `avail` is now keyed by **exact date `YYYY-MM-DD` → [time labels]**, NOT
  day-of-week. This was the core refactor.
- Helpers added: `dateKey(d)`, `weekStart(d)` (Sunday), `addDays(d,n)`.
- Grid gained a **week switcher** (`‹ label ›` + `copy last week`), state in
  `obWeek` (Sunday of shown week), init `weekStart(today)` in `fillOnboard`.
  `‹` disabled on current week (no setting the past); forward unbounded.
  `copyLastWeek()` mirrors the prior week's 7 dates into the shown week.
- Booking calendar consumers switched to date keys: `openCount(date)`,
  `renderMonth` (uses `n=openCount(date)`), `selectDay` reads
  `avail()[dateKey(date)]`.
- **Storage key bumped `stoop-profile` → `stoop-profile-v2`** so stale
  dow-keyed localStorage is discarded; "Start fresh" now uses the `KEY` const.
- Delaney seed: `DEFAULT.avail={}`; `seedAvail()` generates dated openings for
  the next 28 days (Tue/Thu 4–6pm, Sat 9–11am) at boot. ponytail: small dow
  pattern expanded to dates only for demo data, not a recurring abstraction.

## Verified (preview MCP `stoop`, port 8762) — no console errors
- Seed dated correctly: today Sat 6/27 → 3 slots; past weekdays this week
  skipped (`d<today`). Keys look like `2026-06-30`.
- Week nav: prev disabled on current week, re-enables after `›`; labels
  "Jun 21 – Jun 27" etc.
- Copy last week: blank future week → 9 cells after copy.
- Month view shows openings only on set dates (Jun 27 + 30, "3 open"); clicking
  Tue 30 lists 4/5/6 pm.

## Open / next
- **Weekly busywork**: pure per-week means each week must be set or it's empty.
  Offered Annabel a "copy to next 4 weeks" button for steady-rhythm case —
  not yet decided.
- Single profile slot still the next real limit (multi-kid needs profiles array
  + routing). Teaser neighbors still stubs.
- Deferred unchanged: hyperlocal feed, parent dashboard, builder polish.
