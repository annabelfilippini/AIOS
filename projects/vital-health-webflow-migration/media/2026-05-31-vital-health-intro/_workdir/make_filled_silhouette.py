#!/usr/bin/env python3
"""Turn the dark-green line drawing of the hummingbird into a solid filled
white silhouette on a transparent background.

Approach:
  1. Read alpha channel of bird-final-transparent.png (the line is opaque,
     everything else is transparent).
  2. Apply morphological closing to seal small line gaps so flood-fill from
     the outside doesn't leak into the bird interior.
  3. Flood-fill from each canvas corner to mark "outside" pixels.
  4. Everything not marked outside = bird body. Paint pure white.
  5. Soften the silhouette edge with a light alpha-based smoothing.
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter

SRC = Path(__file__).resolve().parent.parent.parent.parent / "logo-options" / "bird-final-transparent.png"
OUT = SRC.parent / "bird-filled-deep-forest.png"
FILL = (22, 56, 32, 255)  # deep_forest #163820


def flood_fill_outside(mask: np.ndarray) -> np.ndarray:
    """Return a boolean array where True = pixels reachable from the canvas
    border without crossing the mask. Iterative scanline-style flood fill."""
    h, w = mask.shape
    visited = np.zeros_like(mask, dtype=bool)
    stack = []

    # Seed every border pixel that isn't part of the line.
    for x in range(w):
        if not mask[0, x]:
            stack.append((0, x))
        if not mask[h - 1, x]:
            stack.append((h - 1, x))
    for y in range(h):
        if not mask[y, 0]:
            stack.append((y, 0))
        if not mask[y, w - 1]:
            stack.append((y, w - 1))

    while stack:
        y, x = stack.pop()
        if y < 0 or y >= h or x < 0 or x >= w:
            continue
        if visited[y, x] or mask[y, x]:
            continue
        visited[y, x] = True
        stack.append((y + 1, x))
        stack.append((y - 1, x))
        stack.append((y, x + 1))
        stack.append((y, x - 1))
    return visited


def main() -> None:
    img = Image.open(SRC).convert("RGBA")
    arr = np.array(img)
    alpha = arr[:, :, 3]

    # Step 1: solid mask of drawn pixels.
    mask = alpha > 40

    # Step 2: morphological closing to seal small gaps in the outline.
    # PIL doesn't have closing directly, so we cast to image and dilate+erode.
    mask_img = Image.fromarray((mask * 255).astype("uint8"))
    dilated = mask_img.filter(ImageFilter.MaxFilter(5))
    closed = dilated.filter(ImageFilter.MinFilter(5))
    closed_arr = np.array(closed) > 127

    # Step 3: flood-fill outside region.
    outside = flood_fill_outside(closed_arr)

    # Step 4: anything NOT outside is the bird silhouette.
    silhouette = ~outside

    # Step 5: build RGBA output in the chosen fill color.
    out = np.zeros_like(arr)
    out[silhouette] = list(FILL)

    # Light alpha smoothing for a clean edge.
    out_img = Image.fromarray(out, "RGBA")
    alpha_band = out_img.split()[3].filter(ImageFilter.GaussianBlur(0.6))
    out_img.putalpha(alpha_band)

    out_img.save(OUT, "PNG")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
