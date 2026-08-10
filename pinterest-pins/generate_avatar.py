#!/usr/bin/env python3
"""Generate a simple LearnStack profile avatar (square, 500x500)."""
from pathlib import Path

import cairosvg

OUT = Path(__file__).parent / "output"
OUT.mkdir(exist_ok=True)

BRAND = "#0e7c6b"
WHITE = "#fdfdfb"

SVG = f"""<svg width="500" height="500" viewBox="0 0 500 500" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="500" fill="{BRAND}"/>
  <!-- stacked books / "learn stack" motif -->
  <rect x="130" y="290" width="240" height="34" rx="6" fill="{WHITE}"/>
  <rect x="150" y="248" width="200" height="34" rx="6" fill="{WHITE}" opacity="0.85"/>
  <rect x="170" y="206" width="160" height="34" rx="6" fill="{WHITE}" opacity="0.7"/>
  <text x="250" y="180" font-family="Georgia, serif" font-size="64" font-weight="700"
        fill="{WHITE}" text-anchor="middle">LS</text>
</svg>"""


def main():
    svg_path = OUT / "avatar.svg"
    svg_path.write_text(SVG, encoding="utf-8")
    png_path = OUT / "avatar.png"
    cairosvg.svg2png(url=str(svg_path), write_to=str(png_path), output_width=500, output_height=500)
    print(f"avatar.png -> {png_path}")


if __name__ == "__main__":
    main()
