#!/usr/bin/env bash
set -euo pipefail

command -v shopify >/dev/null
shopify version
