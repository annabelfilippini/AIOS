# 2026-05-21 Wiki / Obsidian Status

## Current State

- Canonical vault: `~/Documents/AI-OS/knowledge`.
- AI-OS compatibility symlink restored: `~/Documents/AI-OS/wiki -> knowledge`.
- Obsidian config tracks only core app settings:
  - `.obsidian/app.json`
  - `.obsidian/appearance.json`
  - `.obsidian/community-plugins.json`
  - `.obsidian/core-plugins.json`
- Obsidian workspace, graph, plugin folders, scripts, trash, imported media,
  large movies, and `wiki-explorer.html` are ignored.

## Git Situation

`knowledge/` is its own Git repo and is currently behind `origin/main` by 28
commits.

Local state is not clean:

- 7 modified files.
- 47 deleted tracked files.
- 42 untracked files.
- Many deleted files are old `outputs/`, `ideas/`, and `wayloft/` operational
  artifacts.
- Many untracked files are new `raw/` imports from AIOS / Claude Code memory
  research.

No actual Git merge conflicts were detected with `git ls-files -u`. The
generated Obsidian conflict note was stale and was removed.

## Duplicate / Cache Situation

`projects/annie-intake/wiki-cache/` is a nested wiki clone/cache and was
untracked inside the `annie-intake` repo. It has now been added to that repo's
`.gitignore` so the cache does not get committed accidentally.

## Recommendation

Before using the vault as a new memory-system substrate:

1. Pull/reconcile the 28 remote commits.
2. Decide whether the large deleted `outputs/`, `ideas/`, and `wayloft/` files
   should be permanently removed, moved into AI-OS project folders, or restored.
3. Commit the `CLAUDE.md` slim-router change and new raw imports separately.
4. Keep Obsidian plugin binaries ignored; track only portable app/community
   plugin config.
