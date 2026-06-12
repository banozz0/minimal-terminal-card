#!/usr/bin/env python3
"""Small helper CLI for minimal-terminal-card assets.

Commands:
  list-templates
  render <svg> [--out <png>]
  render-dir <dir>
  validate [paths...]
  contact-sheet [--dir examples] [--out examples/example-contact-sheet.svg]

The renderer prefers macOS qlmanage, then rsvg-convert, then inkscape.
"""
from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = ROOT / "templates"
EXAMPLES = ROOT / "examples"
THREADS = ROOT / "threads"
SIZE = 1600
MIN_FONT = 17
MAX_TEXT_CHARS = 56
MAX_TEXT_NODES = 95
SAFE_MARGIN = 92


def rel(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(ROOT))
    except Exception:
        return str(path)


def list_templates(_: argparse.Namespace) -> int:
    for path in sorted(TEMPLATES.glob("*.svg")):
        print(rel(path))
    return 0


def _render_with_qlmanage(svg: Path, png: Path) -> bool:
    if not shutil.which("qlmanage"):
        return False
    with tempfile.TemporaryDirectory() as tmp:
        tmpdir = Path(tmp)
        proc = subprocess.run(
            ["qlmanage", "-t", "-s", str(SIZE), "-o", str(tmpdir), str(svg)],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
        )
        made = tmpdir / f"{svg.name}.png"
        if proc.returncode == 0 and made.exists():
            png.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(made, png)
            return True
        print(proc.stdout.strip(), file=sys.stderr)
    return False


def render_one(svg: Path, png: Path) -> str:
    if _render_with_qlmanage(svg, png):
        return "qlmanage"
    if shutil.which("rsvg-convert"):
        subprocess.run(["rsvg-convert", "-w", str(SIZE), "-h", str(SIZE), "-o", str(png), str(svg)], check=True)
        return "rsvg-convert"
    if shutil.which("inkscape"):
        subprocess.run(["inkscape", str(svg), "--export-type=png", f"--export-filename={png}", "--export-width=1600", "--export-height=1600"], check=True)
        return "inkscape"
    raise SystemExit("No renderer found: install qlmanage (macOS), rsvg-convert, or inkscape.")


def render_cmd(args: argparse.Namespace) -> int:
    svg = Path(args.svg).resolve()
    png = Path(args.out).resolve() if args.out else svg.with_suffix(".png")
    renderer = render_one(svg, png)
    print(f"rendered {rel(svg)} -> {rel(png)} via {renderer}")
    return 0


def svg_size(path: Path) -> tuple[int | None, int | None]:
    root = ET.parse(path).getroot()
    def clean(value: str | None) -> int | None:
        if not value:
            return None
        m = re.match(r"^(\d+)", value)
        return int(m.group(1)) if m else None
    return clean(root.attrib.get("width")), clean(root.attrib.get("height"))


def png_size(path: Path) -> tuple[int | None, int | None]:
    if shutil.which("sips"):
        proc = subprocess.run(["sips", "-g", "pixelWidth", "-g", "pixelHeight", str(path)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        nums = [int(x) for x in re.findall(r"pixel(?:Width|Height): (\d+)", proc.stdout)]
        if len(nums) >= 2:
            return nums[0], nums[1]
    # Minimal PNG header fallback.
    with path.open("rb") as f:
        data = f.read(24)
    if data.startswith(b"\x89PNG\r\n\x1a\n"):
        return int.from_bytes(data[16:20], "big"), int.from_bytes(data[20:24], "big")
    return None, None


def validate_svg(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        tree = ET.parse(path)
    except Exception as exc:
        return [f"invalid XML: {exc}"]
    w, h = svg_size(path)
    if (w, h) != (SIZE, SIZE):
        errors.append(f"SVG size is {w}x{h}, expected {SIZE}x{SIZE}")
    text = path.read_text(encoding="utf-8")
    for banned in ["World Cup", "FIFA", "ESPN", "FOX", "Harry", "Sven", "Banozz", "banozz"]:
        if banned.lower() in text.lower():
            errors.append(f"public-cleanliness banned term present: {banned}")
    font_sizes = [int(x) for x in re.findall(r"font-size:(\d+)px", text)]
    too_small = [x for x in font_sizes if x < MIN_FONT]
    if too_small:
        errors.append(f"font size below {MIN_FONT}px: {sorted(set(too_small))}")
    root = tree.getroot()
    ns = "{http://www.w3.org/2000/svg}"
    texts = ["".join(t.itertext()).strip() for t in root.iter(f"{ns}text")]
    long = [t for t in texts if len(t) > MAX_TEXT_CHARS and "{{" not in t]
    if long:
        errors.append(f"text node over {MAX_TEXT_CHARS} chars: {long[0]!r}")
    if len(texts) > MAX_TEXT_NODES:
        errors.append(f"too many text nodes: {len(texts)} > {MAX_TEXT_NODES}; split to 2 cards")
    return errors


def validate_cmd(args: argparse.Namespace) -> int:
    paths = [Path(p) for p in args.paths] if args.paths else sorted(EXAMPLES.glob("*.svg")) + sorted(TEMPLATES.glob("*.svg"))
    failed = 0
    for path in paths:
        if path.suffix.lower() == ".svg":
            errors = validate_svg(path)
        elif path.suffix.lower() == ".png":
            w, h = png_size(path)
            errors = [] if (w, h) == (SIZE, SIZE) else [f"PNG size is {w}x{h}, expected {SIZE}x{SIZE}"]
        else:
            continue
        if errors:
            failed += 1
            print(f"FAIL {rel(path)}")
            for err in errors:
                print(f"  - {err}")
        else:
            print(f"OK   {rel(path)}")
    return 1 if failed else 0


def contact_sheet_cmd(args: argparse.Namespace) -> int:
    source_dir = Path(args.dir).resolve() if getattr(args, "dir", None) else EXAMPLES
    out = Path(args.out).resolve()
    pngs = sorted(p for p in source_dir.glob("*.png") if p.name != out.with_suffix(".png").name)
    if not pngs:
        raise SystemExit(f"No PNG files found in {source_dir}")
    cell = 360
    gap = 32
    cols = 3
    width = 1600
    height = 1600
    items = []
    for i, png in enumerate(pngs):
        col = i % cols
        row = i // cols
        x = 100 + col * (cell + gap + 72)
        y = 210 + row * (cell + 68)
        label = png.stem.replace("-", " ")[:34]
        items.append(f'<image href="{png.name}" x="{x}" y="{y}" width="{cell}" height="{cell}"/>')
        items.append(f'<text x="{x}" y="{y+cell+34}" class="mono cap muted">{label}</text>')
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <defs><style>.mono{{font-family:ui-monospace,'SF Mono','IBM Plex Mono',Menlo,Consolas,monospace}}.fg{{fill:#eeeeee}}.muted{{fill:#9a9a9a}}.dim{{fill:#626262}}.thin{{stroke:#bdbdbd;stroke-width:1.5;fill:none}}.title{{font-size:42px;font-weight:650}}.cap{{font-size:20px;font-weight:520}}</style></defs>
  <rect width="{width}" height="{height}" fill="#050505"/>
  <rect x="60" y="60" width="{width-120}" height="{height-120}" class="thin" opacity=".65"/>
  <text x="100" y="126" class="mono title fg">{args.title}</text>
  <text x="100" y="164" class="mono cap dim">{args.subtitle or f'{len(pngs)} rendered cards · generated contact sheet'}</text>
  {chr(10).join(items)}
</svg>'''
    out.write_text(svg, encoding="utf-8")
    print(f"wrote {rel(out)} with {len(pngs)} cards from {rel(source_dir)}")
    return 0


def render_dir_cmd(args: argparse.Namespace) -> int:
    directory = Path(args.dir).resolve()
    svgs = sorted(directory.glob("*.svg"))
    if not svgs:
        raise SystemExit(f"No SVG files found in {directory}")
    for svg in svgs:
        if svg.name.endswith("contact-sheet.svg"):
            continue
        renderer = render_one(svg, svg.with_suffix(".png"))
        print(f"rendered {rel(svg)} via {renderer}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("list-templates").set_defaults(func=list_templates)
    p = sub.add_parser("render")
    p.add_argument("svg")
    p.add_argument("--out")
    p.set_defaults(func=render_cmd)
    p = sub.add_parser("validate")
    p.add_argument("paths", nargs="*")
    p.set_defaults(func=validate_cmd)
    p = sub.add_parser("render-dir")
    p.add_argument("dir")
    p.set_defaults(func=render_dir_cmd)
    p = sub.add_parser("contact-sheet")
    p.add_argument("--dir", default=str(EXAMPLES), help="Directory of PNG files to include")
    p.add_argument("--out", default=str(EXAMPLES / "example-contact-sheet.svg"))
    p.add_argument("--title", default="minimal terminal card examples")
    p.add_argument("--subtitle", default=None)
    p.set_defaults(func=contact_sheet_cmd)
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
