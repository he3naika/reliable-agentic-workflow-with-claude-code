#!/usr/bin/env python3
"""Deterministic markdown -> HTML renderer for the Personal Finance Goal Planner.

Stdlib only, no external markdown library, on purpose: the whole point of
rendering with a script instead of asking the model to hand-write HTML is
that the same markdown input always produces byte-for-byte the same layout.

Supports the small subset of markdown actually used in plan.md: #/##/###
headings, paragraphs, unordered lists (- item), GFM pipe tables, **bold**,
*italic*, [text](url) links, and horizontal rules (---).

Usage:
    python render_html.py --input plan.md --output financial-goal-plan.html --title "Financial Goal Plan"
"""
import argparse
import html
import re
import sys
from pathlib import Path

INLINE_LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
INLINE_BOLD = re.compile(r"\*\*([^*]+)\*\*")
INLINE_ITALIC = re.compile(r"\*([^*]+)\*")

CSS = """
:root {
  color-scheme: light dark;
  --bg: #ffffff; --fg: #1a1a1a; --muted: #5f6b7a; --border: #d9dee3;
  --accent: #1f6feb; --table-stripe: #f5f7fa;
}
@media (prefers-color-scheme: dark) {
  :root { --bg: #14171a; --fg: #e8e8e8; --muted: #9aa5b1; --border: #2c333b; --table-stripe: #1c2126; }
}
body {
  background: var(--bg); color: var(--fg); margin: 0;
  font-family: -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif;
  line-height: 1.55;
}
.doc { max-width: 860px; margin: 0 auto; padding: 2.5rem 1.5rem 4rem; }
h1 { font-size: 1.9rem; border-bottom: 2px solid var(--accent); padding-bottom: 0.5rem; }
h2 { font-size: 1.35rem; margin-top: 2.2rem; color: var(--accent); }
h3 { font-size: 1.1rem; margin-top: 1.6rem; }
p { margin: 0.6rem 0; }
ul { padding-left: 1.4rem; }
li { margin: 0.25rem 0; }
a { color: var(--accent); }
hr { border: none; border-top: 1px solid var(--border); margin: 2rem 0; }
table { border-collapse: collapse; width: 100%; margin: 1rem 0; }
th, td { border: 1px solid var(--border); padding: 0.5rem 0.7rem; text-align: left; }
tr:nth-child(even) td { background: var(--table-stripe); }
"""


def inline(text: str) -> str:
    text = html.escape(text)
    text = INLINE_LINK.sub(r'<a href="\2">\1</a>', text)
    text = INLINE_BOLD.sub(r"<strong>\1</strong>", text)
    text = INLINE_ITALIC.sub(r"<em>\1</em>", text)
    return text


def render_table(lines):
    header = [c.strip() for c in lines[0].strip().strip("|").split("|")]
    body_lines = lines[2:]
    out = ["<table>", "<thead><tr>"]
    out += [f"<th>{inline(c)}</th>" for c in header]
    out.append("</tr></thead><tbody>")
    for line in body_lines:
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        out.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in cells) + "</tr>")
    out.append("</tbody></table>")
    return "\n".join(out)


def markdown_to_html(md: str) -> str:
    lines = md.splitlines()
    out = []
    i = 0
    in_list = False

    def close_list():
        nonlocal in_list
        if in_list:
            out.append("</ul>")
            in_list = False

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            close_list()
            i += 1
            continue

        if stripped == "---":
            close_list()
            out.append("<hr>")
            i += 1
            continue

        heading = re.match(r"^(#{1,3})\s+(.*)$", stripped)
        if heading:
            close_list()
            level = len(heading.group(1))
            out.append(f"<h{level}>{inline(heading.group(2))}</h{level}>")
            i += 1
            continue

        if stripped.startswith("|") and i + 1 < len(lines) and re.match(r"^\|?[\s:-]+\|", lines[i + 1].strip()):
            close_list()
            table_lines = [lines[i]]
            j = i + 1
            while j < len(lines) and lines[j].strip().startswith("|"):
                table_lines.append(lines[j])
                j += 1
            out.append(render_table(table_lines))
            i = j
            continue

        if stripped.startswith("- "):
            if not in_list:
                out.append("<ul>")
                in_list = True
            out.append(f"<li>{inline(stripped[2:])}</li>")
            i += 1
            continue

        close_list()
        out.append(f"<p>{inline(stripped)}</p>")
        i += 1

    close_list()
    return "\n".join(out)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--title", default="Financial Goal Plan")
    args = parser.parse_args()

    md_text = Path(args.input).read_text(encoding="utf-8")
    body = markdown_to_html(md_text)

    doc = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(args.title)}</title>
<style>{CSS}</style>
</head>
<body>
<div class="doc">
{body}
</div>
</body>
</html>
"""
    Path(args.output).write_text(doc, encoding="utf-8")
    print(f"wrote {args.output}")


if __name__ == "__main__":
    sys.exit(main())
