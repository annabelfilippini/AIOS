---
date: 2026-06-04
time: 12:28
project: ai-os
status: in-progress
next-session: Finish VPS GitHub access for nested repos so Hermes can clone knowledge, Wayloft, Annie intake, and Pickleball into /root/AI-OS.
---

# Session: Hermes Codex Setup And AI-OS GitHub Sync

## What we worked on

- Connected Hermes Workspace to OpenAI Codex on the VPS.
- Enabled Codex device-code authorization in ChatGPT Security settings, then completed Hermes Codex OAuth.
- Set Hermes default provider/model to `openai-codex` + `gpt-5.5`.
- Verified Hermes default path with a live one-shot response: `default gpt55 ok`.
- Discussed switching Hermes between Codex and Anthropic direct; Anthropic API-key auth is still not completed.
- Changed AI-OS root Git tracking so useful project folders are no longer broadly ignored.
- Committed and pushed safe AI-OS project workspace content to GitHub.
- Committed and pushed nested repos: `knowledge`, `projects/annie-intake`, `projects/wayloft`, and `projects/pickleball-portal/repo`.
- Fast-forwarded Mac AI-OS after VPS autosync/runtime-neutral doc commits.

## Decisions made

- Do not push literal every byte of AI-OS; keep secrets and generated folders out.
- Keep `.env`, auth files, keys, `node_modules`, venvs, logs, Vercel state, and runtime caches ignored.
- Treat `knowledge`, `annie-intake`, `wayloft`, and `pickleball-portal/repo` as separate repos, not as files inside root `AIOS`.
- Use GitHub as the bridge so Hermes on the VPS can access the same working context.
- Keep Hermes default on Codex `gpt-5.5` for now.

## Open questions

- Should Anthropic direct be added to Hermes with an API key for Claude switching?
- Should nested repos be cloned into `/root/AI-OS` with separate deploy keys or a broader machine key?
- Should AI-OS have a runbook for root repo plus nested repo sync on the VPS?
- Should Hermes default working directory be `/root/AI-OS` if it is not already?

## Next steps

1. Add GitHub auth on the VPS for nested repos: `annabelfilippini/wiki`, `annabelfilippini/annie-intake`, `annabelfilippini/wayloft`, and `twflipper/pickleball-portal-next`.
2. Clone those repos into:
   - `/root/AI-OS/knowledge`
   - `/root/AI-OS/projects/annie-intake`
   - `/root/AI-OS/projects/wayloft`
   - `/root/AI-OS/projects/pickleball-portal/repo`
3. Add/update a pull script that updates root AI-OS and each nested repo safely.
4. If desired, run `hermes auth add anthropic --type api-key` on the VPS, then switch Claude with `hermes config set model.provider anthropic`.
5. Verify Hermes can see the newly cloned nested repos from the Files/Chat context.

## Context to preserve

- Root AI-OS latest pushed commit after this session: `0278e11 docs(agents): make modes runtime-neutral`.
- Root AI-OS is clean on Mac and VPS.
- The VPS root repo remote uses SSH alias `github-aios` with deploy key `~/.ssh/aios_github_deploy`.
- Nested repo clone attempts failed over HTTPS because the VPS could not prompt for GitHub credentials.
- Pickleball push required `git pull --rebase`; generated `public/sitemap-0.xml` conflicts were resolved by keeping the newer/current sitemap side.

## System refinement candidates

- Add `operations/git-sync/README.md` documenting root + nested repo sync.
- Add a script to clone/pull all AI-OS nested repos on the VPS.
- Add a Hermes provider switch helper for Codex/Claude defaults.
- Add a pre-push safety check for secret-like paths across root and nested repos.
