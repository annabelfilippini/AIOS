#!/usr/bin/env python3
"""Read-only audit of a working directory for an existing agent/client setup.

Usage:
    python3 audit-existing-folder.py [path]

The script prints JSON and never modifies files.
"""

import json
import sys
from pathlib import Path


def safe_count_lines(path: Path) -> int:
    try:
        return len(path.read_text(encoding="utf-8").splitlines())
    except Exception:
        return 0


def list_md(directory: Path) -> list[str]:
    if not directory.is_dir():
        return []
    return sorted(path.stem for path in directory.glob("*.md") if path.is_file())


def list_subdirs(directory: Path) -> list[str]:
    if not directory.is_dir():
        return []
    return sorted(path.name for path in directory.iterdir() if path.is_dir())


def settings_has_hooks(path: Path) -> bool:
    if not path.is_file():
        return False
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return bool(data.get("hooks", {}))
    except Exception:
        return False


def first_existing(paths: list[Path]) -> Path | None:
    for path in paths:
        if path.is_file():
            return path
    return None


def audit(root: Path) -> dict:
    agent_dirs = [root / ".claude", root / ".codex", root / ".agents"]
    data_dir = root / "data"
    outputs_dir = root / "outputs"

    instruction_file = first_existing([
        root / "AGENTS.md",
        root / "CLAUDE.md",
        root / ".claude" / "CLAUDE.md",
        root / ".codex" / "AGENTS.md",
    ])

    skills = []
    for agent_dir in agent_dirs:
        skills.extend(list_subdirs(agent_dir / "skills"))

    rules = []
    for agent_dir in agent_dirs:
        rules.extend(list_md(agent_dir / "rules"))

    agents = []
    for agent_dir in agent_dirs:
        agents.extend(list_md(agent_dir / "agents"))

    detections = {
        "instruction_file": {
            "exists": instruction_file is not None,
            "path": str(instruction_file.relative_to(root)) if instruction_file else None,
            "lines": safe_count_lines(instruction_file) if instruction_file else 0,
        },
        "settings": {
            "claude_settings_exists": (root / ".claude" / "settings.json").is_file(),
            "claude_settings_has_hooks": settings_has_hooks(root / ".claude" / "settings.json"),
        },
        "skills": {
            "count": len(skills),
            "names": sorted(set(skills)),
        },
        "agents": {
            "count": len(agents),
            "names": sorted(set(agents)),
        },
        "rules": {
            "count": len(rules),
            "names": sorted(set(rules)),
        },
        "data_namespaces": list_subdirs(data_dir),
        "outputs": list_md(outputs_dir),
        "raw_dropzone": {
            "exists": (data_dir / "raw_dropzone").is_dir(),
            "file_count": (
                len(list((data_dir / "raw_dropzone").iterdir()))
                if (data_dir / "raw_dropzone").is_dir()
                else 0
            ),
        },
        "converted": {
            "exists": (data_dir / "converted").is_dir(),
            "file_count": (
                len(list((data_dir / "converted").iterdir()))
                if (data_dir / "converted").is_dir()
                else 0
            ),
        },
    }

    has_existing_setup = (
        detections["instruction_file"]["exists"]
        or detections["settings"]["claude_settings_exists"]
        or detections["skills"]["count"] > 0
        or detections["agents"]["count"] > 0
        or detections["rules"]["count"] > 0
        or len(detections["data_namespaces"]) > 0
        or len(detections["outputs"]) > 0
    )

    return {
        "mode": "audit-existing" if has_existing_setup else "greenfield",
        "root": str(root),
        "detections": detections,
    }


def main() -> None:
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path.cwd()
    print(json.dumps(audit(root), indent=2))


if __name__ == "__main__":
    main()
