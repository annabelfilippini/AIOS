#!/usr/bin/env bash
set -euo pipefail

command -v npx >/dev/null
DISABLE_TELEMETRY=1 npx skills --version
