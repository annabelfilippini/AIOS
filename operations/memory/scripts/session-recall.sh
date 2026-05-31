#!/usr/bin/env bash
set -u

aios_root="$HOME/Documents/AI-OS"
recall_script="$aios_root/operations/memory/scripts/recall.mjs"
cwd="${PWD:-$(pwd)}"

if [ ! -f "$recall_script" ]; then
  exit 0
fi

case "$cwd" in
  "$aios_root"|"$aios_root"/*) ;;
  *)
    cat <<EOF
AI-OS Memory Reminder:
- Current session is not inside AI-OS, so this is a root memory brief.
- If this session touches AI-OS, first cd into the relevant leaf folder and run:
  node "$recall_script" --cwd "\$PWD" --query "<current request>"
- Do not load raw memory or identity files by default.

EOF

    node "$recall_script" --cwd "$aios_root" --query "ai-os-memory" --limit 2
    exit 0
    ;;
esac

query="$(basename "$cwd")"
if [ "$cwd" = "$aios_root" ]; then
  query="ai-os-memory"
fi

cat <<EOF
AI-OS Startup Memory Recall:
- Read this brief before broad searches.
- Then rerun recall with the user's exact task if the task is more specific:
  node operations/memory/scripts/recall.mjs --cwd "\$PWD" --query "<current request>"
- Do not read raw-sessions/, SOUL.md, USER.md, or broad memory unless the brief is insufficient.

EOF

node "$recall_script" --cwd "$cwd" --query "$query" --limit 3
