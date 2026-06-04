#!/usr/bin/env python3
"""Generate 6 (or N) carousel photos via gpt-image-1.

Reads inputs.yaml (for brand vocabulary + which slides to render) and
prompts/photo-prompts.yaml (for the 6 base prompts). Writes PNGs to
<working-dir>/raw/.

Usage:
    python generate_photos.py /path/to/inputs.yaml [--working-dir .] [--slides 1,3,5]

If --slides is omitted, generates all configured slides (1..num_slides).
Requires OPENAI_API_KEY in env or .env in working-dir.

Wraps viz-image-gen's `generate_image_gpt.py` if available — falls back to direct
openai.images.generate() call.
"""
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML is required. Run: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

try:
    from dotenv import load_dotenv
    DOTENV_OK = True
except ImportError:
    DOTENV_OK = False


def load_env(working_dir: Path):
    if DOTENV_OK:
        for p in [working_dir / ".env", working_dir.parent / ".env", working_dir.parent.parent / ".env"]:
            if p.exists():
                load_dotenv(p)
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("ERROR: OPENAI_API_KEY not set. Add to .env or export it.", file=sys.stderr)
        sys.exit(2)
    # Reality-check per AI-OS rule: a key starting with 'sk-' should be >40 chars.
    if api_key.startswith("sk-") and len(api_key) < 40:
        print(f"ERROR: OPENAI_API_KEY looks like a template stub (length {len(api_key)}). Verify the actual value.", file=sys.stderr)
        sys.exit(2)
    return api_key


def build_prompt(slide_prompt_data: dict, photos_config: dict) -> str:
    """Compose subject_prompt + style_suffix using brand vocabulary."""
    style_template = "{mood_phrase}, {light_phrase}, {palette_phrase}, {hard_rules}"
    style_suffix = style_template.format(
        mood_phrase=photos_config.get("mood_phrase", "documentary still-life photography, shallow depth of field, slight film grain"),
        light_phrase=photos_config.get("light_phrase", "soft natural window light from upper-left"),
        palette_phrase=photos_config.get("palette_phrase", "cream and warm color palette"),
        hard_rules=photos_config.get("hard_rules", "no text, no logos, no faces, no people identifiable, photographed editorially for a wellness brand, 2:3 portrait composition"),
    )
    return f"{slide_prompt_data['subject_prompt'].strip()}\n\n{style_suffix}"


def generate(prompt: str, out_path: Path, api_key: str):
    from openai import OpenAI
    client = OpenAI(api_key=api_key)
    print(f"  → gpt-image-1: {out_path.name}")
    response = client.images.generate(
        model="gpt-image-1",
        prompt=prompt,
        size="1024x1536",
        quality="high",
        n=1,
    )
    import base64
    img_b64 = response.data[0].b64_json
    out_path.write_bytes(base64.b64decode(img_b64))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("inputs", help="Path to inputs.yaml")
    ap.add_argument("--working-dir", default=None)
    ap.add_argument("--slides", default=None, help="Comma-separated list of slide numbers (default: all)")
    args = ap.parse_args()

    inputs_path = Path(args.inputs).resolve()
    with open(inputs_path) as f:
        config = yaml.safe_load(f)

    working_dir = Path(args.working_dir).resolve() if args.working_dir else inputs_path.parent
    raw_dir = working_dir / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)

    api_key = load_env(working_dir)

    photos_config = config.get("photos", {})
    cfg = config.get("config", {})
    num_slides = cfg.get("num_slides", 6)

    # Load base prompts
    prompts_path = Path(__file__).resolve().parent.parent / "prompts" / "photo-prompts.yaml"
    with open(prompts_path) as f:
        prompts = yaml.safe_load(f)

    # Decide slide list
    if args.slides:
        slide_nums = [int(s.strip()) for s in args.slides.split(",")]
    else:
        # Mirror render_slides.py drop priority: 4 → 5 → 3 if num_slides < 6
        slide_nums = list(range(1, 7))
        if num_slides < 6:
            drop_priority = [4, 5, 3]
            to_drop = drop_priority[: 6 - num_slides]
            slide_nums = [n for n in slide_nums if n not in to_drop]

    for n in slide_nums:
        slide_prompt_data = prompts["slides"][n]
        out_path = raw_dir / slide_prompt_data["filename"]
        if out_path.exists():
            print(f"  ✓ {out_path.name} already exists, skipping (delete to regen)")
            continue
        prompt = build_prompt(slide_prompt_data, photos_config)
        generate(prompt, out_path, api_key)

    print(f"\nDone. Photos in {raw_dir}/")


if __name__ == "__main__":
    main()
