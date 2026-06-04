#!/usr/bin/env bash
set -euo pipefail

repo="${AIOS_SYNC_REPO:-$HOME/Documents/AI-OS}"
branch="${AIOS_SYNC_BRANCH:-main}"
actor="${AIOS_SYNC_ACTOR:-$(hostname -s)}"

cd "$repo"

if [ ! -d .git ]; then
  echo "AI-OS sync skipped: $repo is not a git repo."
  exit 0
fi

current_branch="$(git branch --show-current)"
if [ "$current_branch" != "$branch" ]; then
  echo "AI-OS sync skipped: on $current_branch, expected $branch."
  exit 0
fi

if [ -d .git/rebase-merge ] || [ -d .git/rebase-apply ] || [ -f .git/MERGE_HEAD ]; then
  echo "AI-OS sync skipped: merge or rebase in progress."
  exit 0
fi

git fetch origin "$branch"

if [ -n "$(git status --porcelain --untracked-files=normal)" ]; then
  git add -A
  if ! git diff --cached --quiet; then
    git commit -m "autosync(${actor}): $(date -u '+%Y-%m-%d %H:%M UTC')"
  fi
fi

git pull --rebase origin "$branch"
git push origin "$branch"
