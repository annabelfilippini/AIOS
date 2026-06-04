---
date: 2026-06-01
time: 18:12
project: instagram-carousel-skill
status: shipped
next-session: First real use of the skill on a new brand. Touch `~/.claude/state/active-skills/instagram-carousel.lock` per SKILL.md §0, build a carousel, watch corrections accumulate in `references/preferences.md` automatically. When done, `rm` the lockfile. If a correction lands in `## Uncategorized`, manually recategorize it and either expand `CATEGORY_RULES` in `save_correction.py` or add a phrase to `TRIGGER_PATTERNS` if a clear correction missed the regex.
---

# Session: instagram-carousel skill batches 2 + 3 shipped

## What we worked on

### Batch 2 — relocation
- Moved `projects/vital-health-webflow-migration/projects/00-social-content/claude/2026-05-31/vh-intro-carousel/` (14 items, ~50 MB) → `projects/vital-health-webflow-migration/media/2026-05-31-vital-health-intro/`.
- Removed the now-empty `projects/00-social-content/claude/` subtree. Left sibling `projects/00-social-content/2026-05-31/` alone — out of scope (carries unrelated work from earlier sessions).
- Copied the 6 final slide PNGs to `~/Documents/AI-OS/skills/instagram-carousel/inspiration/vital-health-intro-2026-05-31/` with a structured `note.md` covering the 6-slide arc table, what to lift, what NOT to lift, and cross-refs to `pipeline-log.md` + `preferences.md` + `ad-analyses-health.md`.
- Verified 6/6 SHA-256 hashes match between source and inspiration copies (byte-identical).
- Verified `~/Desktop/vh-intro-carousel-review.html` still parses with all 6 inline base64 images intact post-move.

### Batch 3 — hooks layer
- Wrote `~/Documents/AI-OS/skills/instagram-carousel/scripts/save_correction.py`. Aggressive trigger regex (20+ patterns, case-insensitive). Category inference walks 6 ordered keyword groups → `## Typography`, `## Photography`, `## Copy`, `## Layout / Composition`, `## TEXT-ON-PHOTO LEGIBILITY`, `## Voice`, with `## Don't do this` and `## Uncategorized` as fallbacks. Inserts entries at the END of the matched category (preserves order with existing entries).
- Wrote `~/Documents/AI-OS/skills/instagram-carousel/scripts/enforce_media_folder.py`. Inspects tool payload; blocks Write/Edit of `.png/.html/.yaml/.jsonl` outside `*/media/YYYY-MM-DD-<slug>/`. For Bash: smart write-detection — only flags redirection targets, `cp`/`mv`/`rsync`/`install` *destinations* (last protected-ext arg, not source), `tee`, `dd of=`. Reads like `cat foo.png` are NOT flagged.
- Wrote `~/.claude/hooks/listen-for-corrections.sh` + `~/.claude/hooks/enforce-media-folder.sh`. Both are thin bash wrappers: check lockfile → exec the python script. Both chmod +x.
- Registered both in `~/.claude/settings.json`: UserPromptSubmit (listener) + PreToolUse on Write|Edit|NotebookEdit|Bash (enforcer). JSON validates.
- Added SKILL.md §0 with `touch`/`rm` instructions for the lockfile.

### Scoping model
- Hooks are session-globally registered (Claude Code matchers only filter by tool name, not by active skill) but **lockfile-gated**: first line is `[ -f ~/.claude/state/active-skills/instagram-carousel.lock ] || exit 0`. Outside an active run the overhead is one bash spawn + one filesystem stat (~1ms), then exit 0. Inside one, the listener captures corrections and the enforcer fences writes.
- Same architectural pattern as the existing `file-placement-guard.sh` (registered globally, fires narrowly).

## Decisions made

- **Aggressive trigger phrasing.** 20+ patterns including soft signals ("rather", "prefer", "instead of") because deletion is cheap and missing a correction permanently is the worse failure mode. Refine via deletions, not negative lookaheads.
- **Lockfile-driven activation, not env vars.** Env doesn't reliably cross hook boundaries; a file does. Path: `~/.claude/state/active-skills/instagram-carousel.lock`. Same pattern will fit any other execution skill that wants hook scoping (linkedin-carousel, video-thumbnails, podcast-clips).
- **Bash hook does smart write-detection.** `cp src dst` flags ONLY dst; `cat foo.png` is never flagged; redirection / `cp` / `mv` / `tee` / `dd of=` covered. Avoided the false-positive that v1 of the regex had (source path of cp incorrectly flagged).
- **Exempt locations:** `/skills/instagram-carousel/inspiration/` (the case library legitimately holds .png files) and `/_archive/` (old runs preserved).
- **Refactored embedded-python into separate script files.** Original `enforce-media-folder.sh` used `exec python3 <<EOF` which silently broke (heredoc consumed stdin, so JSON payload was lost). Lesson: keep hook logic in proper `.py` files, bash wrappers stay tiny.

## Open questions

- Will the trigger regex catch all of Annabel's natural correction phrasings on the first real run, or will misses surface phrases worth adding? Need to use it to find out.
- Same for category inference: will the keyword router send things to the right section, or will too many land in `## Uncategorized`? If many do, expand `CATEGORY_RULES` in `save_correction.py`.
- Second-brand test (carried open since v5 checkpoint) — still pending. Skill is now ready for it.

## Next steps

1. **First real run on a new brand.**
   - `touch ~/.claude/state/active-skills/instagram-carousel.lock` per SKILL.md §0.
   - Build a carousel through the skill.
   - Watch corrections auto-append to `references/preferences.md`.
   - When done: `rm` the lockfile.
2. Audit any `## Uncategorized` entries that accumulate; either recategorize manually or expand `CATEGORY_RULES`.
3. If a clear correction missed the regex, add a verbatim phrase to `TRIGGER_PATTERNS` in `save_correction.py`.
4. Second-brand validation — pick a non-health brand (peptide / consumer product / etc) and run the skill end-to-end to test generalization.

## Smoke tests run

- **Listener (4/4 pass):** dormant w/o lockfile, appends "font is too generic" → § Typography, ignores "can you proceed", emits stdout system-reminder for "colour palette feels corporate" → § Photography. preferences.md SHA restored byte-identical after cleanup.
- **Enforcer (19/20 → 11/11 after fix):** dormant, allowed paths (media dated-slug, .md anywhere, inspiration exempt, _archive exempt, cat reads), blocked paths (png/html/yaml/jsonl outside media/, redirection, cp/mv/tee to wrong dest, jsonl outside, media/<no-date>/). One initial fail: `cp src.png dst.png` was flagging `src` (read) — fixed regex to take last protected-ext arg as destination only. Re-verified.

## Context to preserve

- **All hook artifacts:**
  - `~/.claude/hooks/listen-for-corrections.sh` (executable)
  - `~/.claude/hooks/enforce-media-folder.sh` (executable)
  - `~/Documents/AI-OS/skills/instagram-carousel/scripts/save_correction.py`
  - `~/Documents/AI-OS/skills/instagram-carousel/scripts/enforce_media_folder.py`
  - `~/.claude/settings.json` (UserPromptSubmit stanza added, second PreToolUse stanza added)
- **Lockfile location:** `~/.claude/state/active-skills/instagram-carousel.lock` (the parent dir is created; the file itself is touched only during an active run).
- **SKILL.md §0** documents the touch/rm lifecycle.
- **Bypass mechanism** (in case the enforcer is wrong about a path): `rm ~/.claude/state/active-skills/instagram-carousel.lock`. The blocked stderr message reminds Claude of this.

## System refinement candidates

- **Generic correction-listener-hook skill.** The pattern (lockfile → trigger regex → category inference → structured append) generalizes to any execution skill that learns from feedback. Worth codifying as a meta-skill that other skills opt into by declaring their preferences.md path + category set.
- **Generic enforce-output-folder hook.** Same idea for the fence: any execution skill that has a canonical output location can register a lockfile-gated PreToolUse hook. Could ship as a parameterized hook + a one-line `hook-config.yaml` per skill.
- **The "hook is registered globally but lockfile-gated" pattern** is the clean answer to "how do I make a session-global hook skill-scoped." Document it once, reuse forever.
- **Resolve in-progress.md.** It was used as a long-run progress tracker per global CLAUDE.md but never had a cleanup step defined. Either truncate after each session or treat as the rolling tail of the most recent batch — currently the latter by accident.
