#!/usr/bin/env bash
set -euo pipefail

aios_root="${AIOS_ROOT:-$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)}"
status=0

check_runtime_dir() {
  local runtime_dir="$1"

  [ -d "$runtime_dir" ] || return 0

  while IFS= read -r skill_dir; do
    local name
    name="$(basename "$skill_dir")"

    case "$name" in
      .system|cache)
        continue
        ;;
    esac

    if [ -L "$skill_dir" ]; then
      local target
      target="$(readlink "$skill_dir")"
      case "$target" in
        "$aios_root"/*|"$aios_root"/agents/*)
          continue
          ;;
      esac
    fi

    if [ -f "$skill_dir/SKILL.md" ]; then
      printf 'runtime-only skill: %s\n' "$skill_dir"
      status=1
    fi
  done < <(find "$runtime_dir" -mindepth 1 -maxdepth 1 \( -type d -o -type l \))
}

check_runtime_dir "$HOME/.codex/skills"
check_runtime_dir "$HOME/.claude/skills"

if [ "$status" -ne 0 ]; then
  cat <<'MSG'

Move durable skills into AI-OS first, then symlink runtime folders back to the
canonical skill:

  agents/shared/skills/<skill-name>/             # Claude + Codex
  agents/garry/skills/<skill-name>/              # Claude/Garry only
  agents/business-partner/skills/<skill-name>/   # Codex only

MSG
fi

exit "$status"
