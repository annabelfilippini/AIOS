#!/usr/bin/env bash
set -euo pipefail

aios_root="${AIOS_ROOT:-$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)}"
cd "$aios_root"

echo "== Markdown lint =="
npx markdownlint-cli2

echo "== Whitespace check =="
git diff --check

echo "== Runtime skill drift =="
"$aios_root/operations/compound-engineering/check-runtime-skill-drift.sh"

echo "== Stale Claude path check =="
stale_hits="$(rg -l --no-messages 'Documents[/]Claude|~[/]Documents[/]Claude' \
  "$HOME/.claude/CLAUDE.md" \
  "$HOME/.claude/hooks" \
  "$HOME/.codex/AGENTS.md" \
  "$HOME/.codex/hooks" \
  "$aios_root/AGENTS.md" \
  "$aios_root/CLAUDE.md" \
  "$aios_root/agents" \
  "$aios_root/operations/annabel-press" \
  "$aios_root/operations/compound-engineering" || true)"
if [ -n "$stale_hits" ]; then
  echo "$stale_hits"
  echo "Stale Claude paths found."
  exit 1
fi

echo "== Runtime credential shape check =="
credential_hits="$(rg -l --no-messages -i \
  'FIRECRAWL_API_KEY =|X-Goog-Api-Key|api[_-]?key =|secret =|password =' \
  "$HOME/.codex/config.toml" \
  "$HOME/.claude/settings.json" \
  "$aios_root/AGENTS.md" \
  "$aios_root/CLAUDE.md" || true)"
if [ -n "$credential_hits" ]; then
  echo "$credential_hits"
  echo "Credential-looking literals found in startup/runtime config."
  exit 1
fi

echo "== Memory safety check =="
node operations/memory/scripts/check-memory-safety.mjs

echo "AI-OS system lint passed."
