#!/usr/bin/env python3
"""
migrate_quest.py — Migre un fichier .md de quête vers le LMS :
  - télécharge les images distantes et les stocke localement
  - remplace les URLs par des chemins locaux
  - convertit les blocs custom (tabs, alert, youtube) en composants MDX
  - ajoute un frontmatter cohérent
  - écrit le résultat dans src/content/quests/

Usage:
    python3 scripts/migrate_quest.py <fichier.md>

Génère :
    src/content/quests/<stem>.mdx
    public/assets/<stem>/images/img_NN.<ext>
"""

import re
import sys
import urllib.request
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

# ── Patterns ──────────────────────────────────────────────────────────────────

IMAGE_PATTERN   = re.compile(r'(!\[[^\]]*\])\((https?://[^)]+)\)')
TABS_PATTERN    = re.compile(r'`{3,4}tabs\n(.*?)`{3,4}', re.DOTALL)
ALERT_PATTERN   = re.compile(r'`{3,4}alert\s+(\w+)\n(.*?)`{3,4}', re.DOTALL)
YOUTUBE_PATTERN = re.compile(r'`{3,4}youtube\n\s*(https?://\S+)\s*\n`{3,4}', re.DOTALL)


# ── Helpers ───────────────────────────────────────────────────────────────────

def guess_ext(url: str, content_type: str | None) -> str:
    suffix = Path(urlparse(url).path).suffix
    if suffix:
        return suffix.lstrip(".")
    if content_type:
        mapping = {
            "image/jpeg": "jpg", "image/png": "png",
            "image/gif": "gif",  "image/webp": "webp",
            "image/svg+xml": "svg",
        }
        return mapping.get(content_type.split(";")[0].strip(), "bin")
    return "bin"


def extract_title(content: str, fallback: str) -> str:
    for line in content.splitlines():
        stripped = line.strip()
        if stripped.startswith("# "):
            return stripped[2:].strip()
    return fallback


# ── Conversions custom → MDX ──────────────────────────────────────────────────

def convert_tabs(match: re.Match) -> str:
    inner = match.group(1)
    # Découpe par !--- Label
    parts = re.split(r'!---\s*(.+)\n', inner)
    # parts : [preamble, label1, content1, label2, content2, ...]
    tabs: list[tuple[str, str]] = []
    i = 1
    while i + 1 <= len(parts) - 1:
        label   = parts[i].strip()
        content = parts[i + 1].strip()
        tabs.append((label, content))
        i += 2

    if not tabs:
        return inner  # bloc malformé, on conserve tel quel

    lines = ["<Tabs>"]
    for label, content in tabs:
        lines.append(f'<Tab label="{label}">')
        lines.append("")
        lines.append(content)
        lines.append("")
        lines.append("</Tab>")
    lines.append("</Tabs>")
    return "\n".join(lines)


def convert_alert(match: re.Match) -> str:
    alert_type = match.group(1).lower()
    content    = match.group(2).strip()
    return f'<Alert type="{alert_type}">\n\n{content}\n\n</Alert>'


def convert_youtube(match: re.Match) -> str:
    url = match.group(1).strip()
    return f'<YoutubeEmbed url="{url}" />'


# ── Pipeline principal ────────────────────────────────────────────────────────

def migrate(md_path: str):
    src = Path(md_path).resolve()
    if not src.exists():
        sys.exit(f"Erreur : fichier introuvable — {src}")

    stem         = src.stem
    project_root = Path.cwd()

    out_path        = project_root / "src" / "content" / "quests" / (stem + ".mdx")
    images_dir      = project_root / "public" / "assets" / stem / "images"
    assets_url_base = f"/assets/{stem}/images"

    images_dir.mkdir(parents=True, exist_ok=True)

    content = src.read_text(encoding="utf-8")

    # 1. Téléchargement des images distantes
    img_counter = 0
    replaced    = 0
    errors      = 0

    def download(match: re.Match) -> str:
        nonlocal img_counter, replaced, errors
        img_tag, url = match.group(1), match.group(2)
        img_counter += 1
        label = f"img_{img_counter:02d}"
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=15) as resp:
                ext  = guess_ext(url, resp.headers.get("Content-Type"))
                data = resp.read()
            filename = f"{label}.{ext}"
            (images_dir / filename).write_bytes(data)
            replaced += 1
            print(f"  ✓ {label} ← {url[:70]}")
            return f"{img_tag}({assets_url_base}/{filename})"
        except Exception as exc:
            errors += 1
            print(f"  ✗ {label} ERREUR — {exc}")
            return match.group(0)

    content = IMAGE_PATTERN.sub(download, content)

    # 2. Conversion des blocs custom → composants MDX
    content = TABS_PATTERN.sub(convert_tabs, content)
    content = ALERT_PATTERN.sub(convert_alert, content)
    content = YOUTUBE_PATTERN.sub(convert_youtube, content)

    # 3. Frontmatter
    title = extract_title(content, fallback=stem)
    frontmatter = (
        f'---\n'
        f'title: "{title}"\n'
        f'description: "migrated content"\n'
        f'tags: []\n'
        f'publishedAt: {date.today().isoformat()}\n'
        f'difficulty: easy\n'
        f'draft: true\n'
        f'---\n\n'
    )

    out_path.write_text(frontmatter + content, encoding="utf-8")

    print(f"\nTerminé →")
    print(f"  {out_path}")
    print(f"  {images_dir}/")
    print(f"  · {replaced} image(s) téléchargée(s), {errors} erreur(s)")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage : python3 scripts/migrate_quest.py <fichier.md>")
    migrate(sys.argv[1])
