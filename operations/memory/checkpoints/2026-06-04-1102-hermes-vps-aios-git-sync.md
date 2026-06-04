---
date: 2026-06-04
time: 11:02
project: ai-os
status: in-progress
next-session: Begin Step 1 by reviewing and cleaning the Mac AI-OS working tree before enabling GitHub sync with the Hermes VPS.
---

# Session: Hermes VPS And AI-OS Git Sync Setup

## What we worked on

- Installed and configured Hermes on a Hetzner VPS so Hermes can run separately from Annabel's Mac.
- Clarified the architecture Annabel wants: Mac AI-OS remains the main working copy, GitHub acts as the bridge, and Hermes on the VPS gets its own editable AI-OS working copy synced through Git.
- Got Hermes Workspace visible through a Mac SSH tunnel at `localhost:3001`.
- Confirmed the VPS-hosted Hermes gateway core APIs reached healthy/portable mode; dashboard-backed APIs require the dashboard process/tunnel.

## Decisions made

- Use GitHub sync, not a direct network mount from the VPS into the Mac filesystem.
- Treat a Git clone on the VPS as a live editable AI-OS working copy, not a lesser copy.
- Start with pull-only automation when working trees are clean. Add Hermes push later, ideally to a branch such as `hermes/...`, not blindly to the shared branch.
- Do not delete local Hermes yet; leave it stopped while validating VPS Hermes.
- Hermes's 83 skills are likely bundled/default Hermes skills, not automatically AI-OS canonical skills.

## Current state

- Mac AI-OS remote: `https://github.com/annabelfilippini/AIOS.git`.
- Mac AI-OS branch: `chore/aios-cleanup-2026-05-31`.
- Current branch is already on GitHub at `origin/chore/aios-cleanup-2026-05-31`.
- Mac AI-OS has many uncommitted changes and untracked files. Do not enable automation until these are reviewed and committed or ignored.
- VPS exists and accepts SSH as root. Hermes Workspace is under `/root/hermes-workspace`.
- VPS Hermes Agent config/data live under `/root/.hermes`; agent install path surfaced as `/usr/local/lib/hermes-agent`.

## Open questions

- Which local uncommitted AI-OS changes should be committed, ignored, or parked before sync automation?
- Should Hermes be allowed to push directly after review, or only push to a dedicated Hermes branch?
- How should AI-OS canonical skills in `skills/` be exposed to Hermes after the VPS AI-OS clone exists?
- Should Hermes VPS processes be moved into `tmux` or system services so terminals do not need to stay open?

## Next steps

1. Review Mac AI-OS dirty tree with `git status --short`.
2. Decide what to commit/ignore/park from current uncommitted changes.
3. Commit the intended current state and push it to GitHub.
4. On the VPS, create a GitHub deploy key with write access for the private AIOS repo.
5. Clone AI-OS to `/root/AI-OS` on the VPS and check out `chore/aios-cleanup-2026-05-31`.
6. Configure Hermes to work inside `/root/AI-OS`.
7. Add conservative clean-tree auto-pull on the VPS only after the clone is stable.

## Context to preserve

- Keep the simple model: `Mac AI-OS <-> GitHub <-> VPS /root/AI-OS <-> Hermes`.
- Avoid direct SSHFS/Tailscale filesystem mounting as the primary sync method; it is more fragile than Git for this use case.
- Browser access to VPS Hermes uses SSH tunnels, e.g. local `3001` forwarding to VPS `3000`, plus gateway/dashboard ports as needed.
- The Telegram bot token seen during setup should be treated as exposed and regenerated before real use.

## System refinement candidates

- Add an AI-OS sync SOP for "Mac source of truth + VPS agent clone" with deploy key setup, clean-tree pull script, and branch policy.
- Add a Hermes VPS runbook covering the three processes/tunnels and how to move them into persistent services.
