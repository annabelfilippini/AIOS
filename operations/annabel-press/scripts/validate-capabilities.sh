#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
failed=0

fail() {
  printf "FAIL %s\n" "$1" >&2
  failed=1
}

require_file() {
  local file="$1"
  [[ -f "$file" ]] || fail "Missing file: $file"
}

require_frontmatter_key() {
  local file="$1"
  local key="$2"
  grep -Eq "^${key}:" "$file" || fail "Missing '${key}' in $file"
}

if [[ ! -d "$ROOT/skills" ]]; then
  fail "Missing canonical skills directory: $ROOT/skills"
fi

if [[ ! -d "$ROOT/cli-connections" ]]; then
  fail "Missing canonical CLI connections directory: $ROOT/cli-connections"
fi

for dir in "$ROOT"/skills/*; do
  [[ -d "$dir" ]] || continue
  file="$dir/SKILL.md"
  require_file "$file"
  require_frontmatter_key "$file" "name"
  require_frontmatter_key "$file" "description"
done

for dir in "$ROOT"/cli-connections/*; do
  [[ -d "$dir" ]] || continue
  file="$dir/CONNECTION.md"
  require_file "$file"
  require_frontmatter_key "$file" "name"
  require_frontmatter_key "$file" "display_name"
  require_frontmatter_key "$file" "binary"

  if [[ -d "$dir/scripts" ]]; then
    while IFS= read -r script; do
      [[ -x "$script" ]] || fail "Script is not executable: $script"
    done < <(find "$dir/scripts" -type f | sort)
  fi
done

for profile in "$ROOT"/agents/*/profile.yaml; do
  [[ -e "$profile" ]] || continue
  require_frontmatter_key "$profile" "agent"
done

if rg -L -n "BEGIN (RSA|OPENSSH|DSA|EC) PRIVATE KEY|api[_-]?key[=:]|access[_-]?token[=:]|secret[=:]" "$ROOT/skills" "$ROOT/cli-connections" >/tmp/annabel-press-secret-scan.txt; then
  cat /tmp/annabel-press-secret-scan.txt >&2
  fail "Potential secret-like text found in canonical capability folders"
fi

if [[ "$failed" -eq 0 ]]; then
  printf "Annabel Press capability validation passed.\n"
fi

exit "$failed"
