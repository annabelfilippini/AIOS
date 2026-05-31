#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"

print_skill() {
  local dir="$1"
  local file="$dir/SKILL.md"
  local name description

  name="$(awk -F': ' '/^name:/ {print $2; exit}' "$file")"
  description="$(awk -F': ' '/^description:/ {print $2; exit}' "$file")"

  printf "skill\t%s\t%s\t%s\n" "${name:-$(basename "$dir")}" "$dir" "${description:-}"
}

print_connection() {
  local dir="$1"
  local file="$dir/CONNECTION.md"
  local name display_name binary

  name="$(awk -F': ' '/^name:/ {print $2; exit}' "$file")"
  display_name="$(awk -F': ' '/^display_name:/ {print $2; exit}' "$file")"
  binary="$(awk -F': ' '/^binary:/ {print $2; exit}' "$file")"

  printf "cli\t%s\t%s\t%s\t%s\n" "${name:-$(basename "$dir")}" "$dir" "${display_name:-}" "${binary:-}"
}

for dir in "$ROOT"/skills/*; do
  [[ -d "$dir" && -f "$dir/SKILL.md" ]] || continue
  print_skill "$dir"
done

for dir in "$ROOT"/cli-connections/*; do
  [[ -d "$dir" && -f "$dir/CONNECTION.md" ]] || continue
  print_connection "$dir"
done
