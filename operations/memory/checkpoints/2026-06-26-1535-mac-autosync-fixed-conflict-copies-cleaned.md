---
date: 2026-06-26 15:35
project: aios-infra
status: done
type: checkpoint
slug: mac-autosync-fixed-conflict-copies-cleaned
---

# Mac→GitHub autosync fixed end to end; iCloud conflict copies purged

## Where we landed
Mac autosync to `github.com:annabelfilippini/AIOS` (branch `main`) now works
unattended. It had been silently failing on the Mac side for weeks (2400+
runs). Hermes/VPS side was always fine. Confirmed live: cron is now producing
`autosync(mac)` commits on its own 5-min schedule (saw 21:24/21:25/21:30 ticks).
Tree clean, local == origin.

## Two root causes (both fixed)
1. **macOS TCC** blocked cron from `~/Documents` (protected folder) — every run
   died with `Operation not permitted`. Fixed: Annabel granted Full Disk Access
   to `/usr/sbin/cron` (System Settings → Privacy & Security → Full Disk Access).
   A *running* cron daemon caches the denial, so it only took effect on the next
   tick after the grant.
2. **Headless git auth** — once cron could run, git couldn't reach the login
   keychain (needs a GUI session) → `could not read Username ... Device not
   configured`. Fixed by switching origin to **SSH**:
   - remote changed `https://...` → `git@github.com:annabelfilippini/AIOS.git`
   - registered existing `~/.ssh/id_ed25519.pub` (no passphrase) to her GitHub
     via `gh ssh-key add` after `gh auth refresh -h github.com -s admin:public_key`
   - verified with a real cron-context test: `env -i HOME=... PATH=... git
     ls-remote origin` returns `main` with no prompt.
   - **No token on disk.** Tried file-based `~/.git-credentials` first; the
     safety classifier blocked it (plaintext token = credential leakage). SSH is
     the better path anyway — nothing secret in a file.

## Conflict-copy cleanup
iCloud/file-sync had spawned `"name 2.ext"` duplicate copies; the first big
autosync committed ~470 of them. Cleaned:
- Deleted 543 ` 2` files where the original (without ` 2`) still existed; kept
  nothing orphaned. Also removed 2 tracked ` 2.part` incomplete-download
  fragments.
- Added ignore rules to root `.gitignore`:
  `*[ ][2-9].*`, `*[ ][2-9]`, `*.part`. So future conflict copies and partial
  downloads never get committed again. (Verified with `git check-ignore`.)

## How it runs / verifies
- Cron: `*/5 * * * *` → `operations/git-sync/aios-autosync.sh`, log at
  `operations/git-sync/mac-autosync.log`.
- Health check anytime: `tail -3 operations/git-sync/mac-autosync.log` — want
  `autosync(mac)` commit lines or "Already up to date", never "Operation not
  permitted" / "Device not configured".
- The script: fetch → `git add -A` + commit if dirty → `pull --rebase` → push.

## NEXT
- Nothing required; it's hands-off now. If the SSH key is ever rotated/removed,
  re-add via `gh ssh-key add ~/.ssh/id_ed25519.pub`.
- Watch first few cron cycles over the next hour to confirm no auth regressions
  (low risk — already saw clean ticks).

Related: [[project_life_os]], [[project_day_planner]].
