#!/usr/bin/env python3
"""
Embed whoami-illusion.gif into whoami-full.svg as a data URI.
GitHub README blocks external image refs in SVGs but allows data: URIs,
so the GIF will show inside the card when you use this generated SVG.

Run from repo root: python3 scripts/embed-whoami-gif.py
"""
import base64
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
GIF_PATH = REPO_ROOT / "assets" / "whoami-illusion.gif"
SVG_PATH = REPO_ROOT / "assets" / "whoami-full.svg"

def main():
    if not GIF_PATH.exists():
        print(f"Missing {GIF_PATH}")
        return 1
    gif_b64 = base64.b64encode(GIF_PATH.read_bytes()).decode("ascii")
    data_uri = f"data:image/gif;base64,{gif_b64}"

    svg = SVG_PATH.read_text(encoding="utf-8")
    # Replace file reference with data URI (GitHub allows data: in SVGs)
    if "whoami-illusion.gif" not in svg:
        print("SVG does not reference whoami-illusion.gif")
        return 1
    new_svg = svg.replace('href="whoami-illusion.gif"', f'href="{data_uri}"').replace(
        'xlink:href="whoami-illusion.gif"', f'xlink:href="{data_uri}"'
    )
    SVG_PATH.write_text(new_svg, encoding="utf-8")
    print(f"Updated {SVG_PATH} with embedded GIF (data URI).")
    return 0

if __name__ == "__main__":
    exit(main())
