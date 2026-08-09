#!/usr/bin/env python3
"""Static site builder: converts content/*.md into site/ HTML pages."""
import re
import shutil
from datetime import date
from pathlib import Path

import markdown

ROOT = Path(__file__).parent
CONTENT = ROOT / "content"
ASSETS = ROOT / "assets"
OUT = ROOT / "docs"

SITE_NAME = "LearnStack"
SITE_TAGLINE = "Honest reviews of AI-powered learning tools"
SITE_URL = "https://yameyaku.com"
CUSTOM_DOMAIN = "yameyaku.com"
# Google Analytics 4 の測定ID(例: "G-XXXXXXXXXX")。空なら埋め込まない
GA_MEASUREMENT_ID = "G-VQHSDY43D3"

PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="stylesheet" href="{root}style.css">
{analytics}</head>
<body>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="{root}index.html">{site_name}</a>
    <span class="tagline">{tagline}</span>
  </div>
</header>
<main class="wrap">
{body}
</main>
<footer class="site-footer">
  <div class="wrap">
    <p>&copy; {year} {site_name}. Some links on this site are affiliate links —
    see the disclosure at the top of each review. We never accept payment for
    rankings, and every review lists the product's weaknesses alongside its strengths.</p>
  </div>
</footer>
</body>
</html>
"""


ANALYTICS = ""
if GA_MEASUREMENT_ID:
    ANALYTICS = (
        f'<script async src="https://www.googletagmanager.com/gtag/js?id={GA_MEASUREMENT_ID}"></script>'
        '<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}'
        f"gtag('js',new Date());gtag('config','{GA_MEASUREMENT_ID}');</script>"
    )


def parse_front_matter(text: str):
    meta = {}
    if text.startswith("---"):
        end = text.index("\n---", 3)
        for line in text[3:end].strip().splitlines():
            if ":" in line:
                key, val = line.split(":", 1)
                meta[key.strip()] = val.strip()
        text = text[end + 4:]
    return meta, text.lstrip("\n")


def render_markdown(body: str) -> str:
    html = markdown.markdown(body, extensions=["tables", "fenced_code"])
    # テーブルは横スクロール可能なラッパーで包む(モバイル対策)
    html = html.replace("<table>", '<div class="table-wrap"><table>')
    html = html.replace("</table>", "</table></div>")
    return html


def build():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    shutil.copy(ASSETS / "style.css", OUT / "style.css")
    (OUT / ".nojekyll").write_text("")
    if CUSTOM_DOMAIN:
        (OUT / "CNAME").write_text(CUSTOM_DOMAIN + "\n")
    (OUT / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n")

    articles = []
    for md_file in sorted(CONTENT.glob("*.md")):
        meta, body = parse_front_matter(md_file.read_text(encoding="utf-8"))
        slug = meta.get("slug", md_file.stem)
        title = meta.get("title") or re.search(r"^# (.+)$", body, re.M).group(1)
        page_dir = OUT / slug
        page_dir.mkdir()
        (page_dir / "index.html").write_text(PAGE.format(
            title=f"{title} | {SITE_NAME}",
            description=meta.get("description", ""),
            body=f'<article class="post">{render_markdown(body)}</article>',
            root="../", site_name=SITE_NAME, tagline=SITE_TAGLINE, analytics=ANALYTICS,
            year=date.today().year,
        ), encoding="utf-8")
        articles.append({**meta, "slug": slug, "title": title})

    articles.sort(key=lambda a: a.get("date", ""), reverse=True)
    cards = "\n".join(
        f'<a class="card" href="{a["slug"]}/index.html">'
        f'<h2>{a["title"]}</h2>'
        f'<p>{a.get("description", "")}</p>'
        f'<span class="date">{a.get("date", "")}</span></a>'
        for a in articles
    )
    intro = (
        '<section class="hero"><h1>Find learning tools that are actually '
        "worth paying for</h1><p>We research AI-powered language apps, online "
        "course platforms, and study tools — then tell you honestly which ones "
        "deliver, which ones don't, and who should skip them entirely.</p></section>"
    )
    (OUT / "index.html").write_text(PAGE.format(
        title=f"{SITE_NAME} — {SITE_TAGLINE}",
        description="Honest, research-driven reviews of AI learning tools, "
                    "language apps, and online course platforms.",
        body=f'{intro}<section class="cards">{cards}</section>',
        root="", site_name=SITE_NAME, tagline=SITE_TAGLINE, analytics=ANALYTICS,
        year=date.today().year,
    ), encoding="utf-8")
    urls = [f"{SITE_URL}/"] + [f"{SITE_URL}/{a['slug']}/" for a in articles]
    entries = "\n".join(f"  <url><loc>{u}</loc></url>" for u in urls)
    (OUT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{entries}\n</urlset>\n")
    print(f"Built {len(articles)} article(s) -> {OUT}")


if __name__ == "__main__":
    build()
