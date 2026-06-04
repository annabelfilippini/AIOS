# /audit-cleanup — Final Asset Verify

Post-deploy safety net. Confirms Step 0b prune actually happened, no images leaked out of `prospects/`, and the deployed folder is slim. Runs as Step 7.5 — after `/audit-package`, before outreach.

**Usage:** `/audit-cleanup <prospect-name>`

## Automation mode

When `AUDIT_AUTOMATED=1` is set, auto-prune any stragglers found and report via files only. Default (unset) = interactive — print the report, wait for user confirmation before destructive action.

## Good Example

After Pepper Pong deploy: `du -sh prospects/pepper-pong` → 14M. Leakage find → zero hits. All Step 0b delete paths absent. Deploy folder `pepper-pong-audit/` contains `index.html`, `audit-client.html`, `homepage-redesign.html`, `dashboard-preview.html`, `assets/` only — no `v1-handbuilt/`, no stray screenshots. Report: ALL GREEN. Safe to send outreach.

## Bad Example

Skipped cleanup. Prospect folder sat at 87M because Phase B regenerated screenshots into `scrape/` after Step 0b ran. Next prospect session pulled 87M into context on `ls -R`. Two weeks later, 20 prospects × 80M = 1.6G of dead screenshots. Or: deploy folder shipped with `mockups/v1-handbuilt/` intact because Step 0b was skipped — prospect's share URL surfaced the draft.

## Steps

### Step 1 — Leakage audit (re-run)

From the pipeline root. MUST return zero hits:

```bash
find . -type f \( -iname "*.png" -o -iname "*.jpg" -o -iname "*.jpeg" \
  -o -iname "*.webp" -o -iname "*.gif" -o -iname "*.mp4" -o -iname "*.mov" \) \
  -not -path "*/prospects/*" -not -path "*/.venv/*" -not -path "*/.git/*"
```

Any hit = a leaked asset (likely written post-Step-0a). Move it into the correct `prospects/<name>/` subfolder. Do NOT delete — may still be referenced.

### Step 2 — Size ceiling check

```bash
du -sh prospects/$NAME
du -sh prospects/$NAME/*
```

- ≤20MB: PASS. Step 0b worked.
- 20-40MB: WARN. Likely a `scrape/screenshots/` directory or `reference/` subfolder survived. Inspect the breakdown and re-prune per `/audit-package` Step 0b rules.
- >40MB: FAIL. Step 0b did not run or was incomplete. Run it now before proceeding.

### Step 3 — Verify Step 0b paths are gone

For each path, confirm it does NOT exist:
- `prospects/$NAME/scrape/screenshots/`
- `prospects/$NAME/reference/<brand>/` subfolders (individual brand scrape dirs)
- `prospects/$NAME/stitch/` (or at minimum no `v1/v2/v3` variants)
- `prospects/$NAME/mockups/v1-handbuilt/`
- `prospects/$NAME/companion/*/scrape/screenshots/` (if companion exists)

**Must still exist** (preserved by `/audit-package` Step 0b):
- `prospects/$NAME/reference/reference-summary.md` — if refs were ever scraped for this prospect. Absence here = `/audit-scrape` Step 6.5 was skipped OR cleanup over-deleted. Either way, `/audit-redesign` Phase 0 will fail on re-run.

Any path that still exists = Step 0b didn't complete. In interactive mode, print the list and ask before deleting. In `AUDIT_AUTOMATED=1`, delete and log.

### Step 4 — Deploy folder hygiene

Target: `prospects/$NAME/<name>-audit/` should contain ONLY:
- `index.html`
- `audit-client.html`
- `homepage-redesign.html`
- `dashboard-preview.html`
- `assets/` (mockup assets only — no loose files at the deploy-folder root)

Any other file or directory = stray. Common offenders: `v1-handbuilt/` (copied by accident), `.DS_Store`, duplicate `mockups/` subdirectory, stray `.md` files.

```bash
ls -la prospects/$NAME/<name>-audit/
find prospects/$NAME/<name>-audit/ -type f -not -path "*/assets/*" \
  \( -iname "*.png" -o -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.webp" \)
```

Second command MUST return zero — no loose images outside `assets/`.

### Step 5 — Report

Print a green/red status table:

```
CLEANUP REPORT — <prospect>
──────────────────────────
Leakage audit (root)        [PASS / FAIL: N hits]
Size ceiling (≤20MB)        [PASS: 14M / WARN: 32M / FAIL: 87M]
Step 0b paths gone          [PASS / FAIL: <list>]
Deploy folder hygiene       [PASS / FAIL: <list>]
Share URL reachable         [PASS / FAIL: <status>]
──────────────────────────
Overall: GREEN | YELLOW | RED
```

If anything is RED, the skill fails loud and refuses to return GREEN — Annabel sees it before the outreach draft.

## Assumes

- **Expects:** `/audit-package` has already run. Deploy folder exists at `prospects/$NAME/<name>-audit/`.
- **Produces:** Printed report. No files written unless pruning runs. Under `AUDIT_AUTOMATED=1`, writes `prospects/$NAME/cleanup-report.txt` with the same content.
- **Quality bar:** GREEN means the prospect folder is ≤20MB, no images have leaked, deploy is clean. Outreach is safe to send.

## Known Failure Modes

- **Running before `/audit-package`.** Deploy folder doesn't exist yet — Step 4 fails. Run `/audit-package` first.
- **Running while Phase B agents are still active.** A background agent may still be writing screenshots. Wait for all agents to return before running cleanup.
- **`du -sh` on an NFS / iCloud-synced path.** Size numbers lag. Force local with `du -sh --apparent-size` if needed.
- **`.DS_Store` counted as a fail.** macOS writes these silently. Allow-list `.DS_Store` in Step 4 — delete, don't fail.
