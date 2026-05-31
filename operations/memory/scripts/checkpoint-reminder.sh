#!/usr/bin/env bash
set -u

aios_root="$HOME/Documents/AI-OS"
checkpoint_dir="$aios_root/operations/memory/checkpoints"

[ -d "$aios_root" ] || exit 0
[ -d "$checkpoint_dir" ] || exit 0

recent_work_count=$(
  find "$aios_root" \
    -path "$aios_root/.git" -prune -o \
    -path "$aios_root/knowledge/.git" -prune -o \
    -path "*/node_modules" -prune -o \
    -path "*/.venv" -prune -o \
    -path "$aios_root/operations/memory/checkpoints" -prune -o \
    -type f -mmin -120 -print 2>/dev/null \
  | wc -l | tr -d ' '
)

recent_checkpoint_count=$(
  find "$checkpoint_dir" -name "*.md" -mmin -120 -print 2>/dev/null \
  | wc -l | tr -d ' '
)

if [ "$recent_work_count" -gt 0 ] && [ "$recent_checkpoint_count" -eq 0 ]; then
  cat <<EOF
AI-OS Checkpoint Reminder:
- Files under AI-OS changed in the last 2 hours, but no recent checkpoint was saved.
- If this session created reusable decisions, open loops, or next-session context, write:
  operations/memory/checkpoints/YYYY-MM-DD-HHMM-session-slug.md
- Keep it under 100 lines. Do not store secrets. Use checkpoints for continuity, not transcripts.
EOF
fi
