#!/usr/bin/env python3
"""Build a simple branded proposal PDF from Markdown.

This script is intentionally small and dependency-light. It converts the subset
of Markdown Annabel uses for proposals into styled HTML, then asks Chrome to
print the HTML to PDF.
"""

from __future__ import annotations

import argparse
import html
import re
import shutil
import subprocess
import sys
from pathlib import Path


def inline_md(text: str) -> str:
    escaped = html.escape(text)
    escaped = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(r"\*(.+?)\*", r"<em>\1</em>", escaped)
    escaped = re.sub(
        r"\[([^\]]+)\]\(([^)]+)\)",
        r'<a href="\2">\1</a>',
        escaped,
    )
    return escaped


def table_to_html(lines: list[str]) -> str:
    rows: list[list[str]] = []
    for line in lines:
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        rows.append(cells)
    if len(rows) < 2:
        return ""

    header = rows[0]
    body = rows[2:] if set("".join(rows[1])) <= set("-: ") else rows[1:]
    out = ["<table>", "<thead><tr>"]
    out.extend(f"<th>{inline_md(cell)}</th>" for cell in header)
    out.append("</tr></thead><tbody>")
    for row in body:
        out.append("<tr>")
        out.extend(f"<td>{inline_md(cell)}</td>" for cell in row)
        out.append("</tr>")
    out.append("</tbody></table>")
    return "\n".join(out)


def markdown_to_html(markdown: str) -> str:
    lines = markdown.splitlines()
    out: list[str] = []
    paragraph: list[str] = []
    list_type: str | None = None

    def flush_paragraph() -> None:
        nonlocal paragraph
        if paragraph:
            out.append(f"<p>{inline_md(' '.join(paragraph))}</p>")
            paragraph = []

    def close_list() -> None:
        nonlocal list_type
        if list_type:
            out.append(f"</{list_type}>")
            list_type = None

    i = 0
    while i < len(lines):
        line = lines[i].rstrip()
        stripped = line.strip()

        if not stripped:
            flush_paragraph()
            close_list()
            i += 1
            continue

        if stripped.startswith("|") and "|" in stripped[1:]:
            flush_paragraph()
            close_list()
            table_lines = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                table_lines.append(lines[i])
                i += 1
            out.append(table_to_html(table_lines))
            continue

        heading = re.match(r"^(#{1,4})\s+(.+)$", stripped)
        if heading:
            flush_paragraph()
            close_list()
            level = len(heading.group(1))
            out.append(f"<h{level}>{inline_md(heading.group(2))}</h{level}>")
            i += 1
            continue

        if stripped == "---":
            flush_paragraph()
            close_list()
            out.append("<hr>")
            i += 1
            continue

        bullet = re.match(r"^[-*]\s+(.+)$", stripped)
        numbered = re.match(r"^\d+\.\s+(.+)$", stripped)
        if bullet or numbered:
            flush_paragraph()
            wanted = "ul" if bullet else "ol"
            if list_type != wanted:
                close_list()
                out.append(f"<{wanted}>")
                list_type = wanted
            text = (bullet or numbered).group(1)
            out.append(f"<li>{inline_md(text)}</li>")
            i += 1
            continue

        close_list()
        paragraph.append(stripped)
        i += 1

    flush_paragraph()
    close_list()
    return "\n".join(out)


def chrome_path() -> str | None:
    candidates = [
        "google-chrome",
        "google-chrome-stable",
        "chromium",
        "chromium-browser",
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
    ]
    for candidate in candidates:
        found = shutil.which(candidate) if "/" not in candidate else candidate
        if found and Path(found).exists():
            return found
    return None


def build_html(body: str, title: str, brand: str, logo: str | None) -> str:
    logo_html = ""
    if logo:
        logo_uri = Path(logo).expanduser().resolve().as_uri()
        logo_html = f'<img class="logo" src="{logo_uri}" alt="">'

    return f"""<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>{html.escape(title)}</title>
<style>
@page {{ margin: 0.6in; }}
body {{
  font-family: Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  color: #1f2933;
  font-size: 10pt;
  line-height: 1.4;
}}
.header {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 2px solid {brand};
  padding-bottom: 12px;
  margin-bottom: 18px;
}}
.logo {{ max-height: 42px; max-width: 120px; object-fit: contain; }}
h1 {{ font-size: 14pt; color: {brand}; margin: 0 0 12px; }}
h2 {{ font-size: 12pt; color: {brand}; margin: 20px 0 8px; }}
h3 {{ font-size: 10.5pt; color: {brand}; margin: 16px 0 6px; }}
p {{ margin: 0 0 8px; }}
ul, ol {{ margin: 0 0 10px 18px; padding: 0; }}
li {{ margin: 0 0 4px; }}
hr {{ border: 0; border-top: 1px solid #d7ddd4; margin: 14px 0; }}
table {{ border-collapse: collapse; width: 100%; margin: 8px 0 12px; font-size: 9.5pt; }}
th {{ background: #f5efe0; color: {brand}; text-align: left; }}
th, td {{ border: 1px solid #d7ddd4; padding: 6px 8px; vertical-align: top; }}
a {{ color: {brand}; }}
strong {{ color: #111827; }}
</style>
</head>
<body>
<div class="header"><h1>{html.escape(title)}</h1>{logo_html}</div>
{body}
</body>
</html>
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Build proposal PDF from markdown")
    parser.add_argument("markdown", type=Path)
    parser.add_argument("pdf", type=Path)
    parser.add_argument("--title", default=None)
    parser.add_argument("--brand", default="#1f4d2a")
    parser.add_argument("--logo", default=None)
    parser.add_argument("--html-out", type=Path, default=None)
    args = parser.parse_args()

    source = args.markdown.read_text()
    first_heading = re.search(r"^#\s+(.+)$", source, re.MULTILINE)
    title = args.title or (first_heading.group(1) if first_heading else args.markdown.stem)
    body_source = re.sub(r"^#\s+.+\n?", "", source, count=1, flags=re.MULTILINE)
    body = markdown_to_html(body_source)
    output_html = build_html(body, title, args.brand, args.logo)

    html_path = args.html_out or args.pdf.with_suffix(".html")
    html_path.write_text(output_html)

    chrome = chrome_path()
    if not chrome:
        print("Could not find Chrome or Chromium. HTML written to:", html_path, file=sys.stderr)
        return 2

    args.pdf.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [
            chrome,
            "--headless",
            "--disable-gpu",
            f"--print-to-pdf={args.pdf}",
            html_path.as_uri(),
        ],
        check=True,
    )
    print(args.pdf)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
