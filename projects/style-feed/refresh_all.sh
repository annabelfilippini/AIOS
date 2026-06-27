#!/bin/bash
# Daily style-feed refresh: influencer ShopMy storefronts + Annabel's Pinterest board.
# Run by the launchd agent com.annabel.stylefeed-refresh (and fine to run by hand).
export PATH="/opt/homebrew/bin:/usr/bin:/bin:/usr/sbin:/sbin"
cd "$(dirname "$0")" || exit 1
PY=/opt/anaconda3/bin/python3
echo "===== refresh $(date '+%Y-%m-%d %H:%M:%S') ====="
"$PY" refresh_sources.py
"$PY" refresh_pinterest.py
echo ""
