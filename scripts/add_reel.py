#!/usr/bin/env python3
"""
CLI helper to add and organize coding reels into reels.json and rebuild CATALOG.md.
"""

import argparse
import datetime
import json
import os
import re
import subprocess
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(BASE_DIR, "reels.json")
CATALOG_FILE = os.path.join(BASE_DIR, "CATALOG.md")

CATEGORIES = {
    "dsa": "Data Structures & Algorithms",
    "system-design": "System Design & Architecture",
    "clean-code": "Clean Code & Craftsmanship",
    "python": "Python Gems",
    "web-dev": "Web Development",
    "tools-workflow": "Developer Tools & Workflows",
    "interview-prep": "Interview & Career Insights",
    "misc": "Miscellaneous Tips"
}


def load_reels():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []


def save_reels(reels):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(reels, f, indent=2, ensure_ascii=False)


def fetch_metadata_ytdlp(url):
    """Attempt to extract reel title and uploader via yt-dlp if installed."""
    try:
        result = subprocess.run(
            ["yt-dlp", "--dump-json", "--skip-download", url],
            capture_output=True,
            text=True,
            timeout=15
        )
        if result.returncode == 0 and result.stdout:
            info = json.loads(result.stdout)
            title = info.get("title") or info.get("description", "").split("\n")[0]
            uploader = info.get("uploader") or info.get("channel") or ""
            return {"title": title[:80] if title else "", "creator": uploader}
    except Exception:
        pass
    return {}


def rebuild_catalog(reels):
    lines = [
        "# 📚 The Better Code Catalog",
        "",
        "> Bite-sized engineering knowledge extracted from developer reels.",
        "",
        "---",
        "",
        "## Table of Contents",
        ""
    ]

    for cat_id, cat_title in CATEGORIES.items():
        anchor = re.sub(r"[^a-z0-9\- ]", "", cat_title.lower()).replace(" ", "-")
        lines.append(f"- [{cat_title}](#{anchor})")

    lines.append("")
    lines.append("---")
    lines.append("")

    # Group reels by category
    by_category = {k: [] for k in CATEGORIES}
    for reel in reels:
        cat = reel.get("category", "misc")
        if cat not in by_category:
            by_category["misc"].append(reel)
        else:
            by_category[cat].append(reel)

    for cat_id, cat_title in CATEGORIES.items():
        lines.append(f"## {cat_title}")
        entries = by_category[cat_id]
        if not entries:
            lines.append("*No entries yet.*")
            lines.append("")
            lines.append("---")
            lines.append("")
            continue

        for r in entries:
            title = r.get("title", "Untitled Reel")
            url = r.get("url", "#")
            creator = r.get("creator", "")
            creator_badge = f" · *by @{creator}*" if creator else ""
            lines.append(f"### [{title}]({url}){creator_badge}")

            takeaways = r.get("takeaways", [])
            if isinstance(takeaways, str):
                takeaways = [takeaways]
            if takeaways:
                lines.append("**Key Takeaways:**")
                for t in takeaways:
                    lines.append(f"- {t}")

            code = r.get("code_snippet")
            if code and code.strip():
                lang = r.get("language", "")
                lines.append(f"\n```{lang}\n{code.strip()}\n```")

            lines.append("")
        lines.append("---")
        lines.append("")

    with open(CATALOG_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(lines).strip() + "\n")
    print(f"✅ Catalog rebuilt with {len(reels)} reel(s) at {CATALOG_FILE}")


def main():
    parser = argparse.ArgumentParser(description="Add and manage reels in Better Code")
    parser.add_argument("--url", help="Instagram reel URL")
    parser.add_argument("--title", help="Title or concept name")
    parser.add_argument("--category", choices=list(CATEGORIES.keys()), default="misc", help="Reel category")
    parser.add_argument("--creator", default="", help="Creator handle (e.g. neetcode, fireship)")
    parser.add_argument("--takeaways", nargs="*", help="Key takeaway bullet points")
    parser.add_argument("--code", default="", help="Code snippet string or file path")
    parser.add_argument("--build", action="store_true", help="Only rebuild CATALOG.md")
    args = parser.parse_args()

    reels = load_reels()

    if args.build:
        rebuild_catalog(reels)
        return

    if not args.url:
        print("💡 Interactive Reel Entry")
        url = input("Reel URL: ").strip()
        if not url:
            print("Error: URL is required.")
            sys.exit(1)

        print("\nCategories:")
        for idx, (k, name) in enumerate(CATEGORIES.items(), 1):
            print(f"  {idx}. {k} ({name})")
        cat_choice = input(f"Select category (default misc): ").strip()
        category = cat_choice if cat_choice in CATEGORIES else "misc"

        meta = fetch_metadata_ytdlp(url)
        suggested_title = meta.get("title", "")
        title = input(f"Title [{suggested_title}]: ").strip() or suggested_title or "Coding Tip"

        suggested_creator = meta.get("creator", "")
        creator = input(f"Creator handle [{suggested_creator}]: ").strip() or suggested_creator

        takeaway = input("Key takeaway: ").strip()
        takeaways = [takeaway] if takeaway else []

        code = input("Code snippet (optional, press Enter to skip): ").strip()
    else:
        url = args.url
        category = args.category
        meta = fetch_metadata_ytdlp(url) if not args.title or not args.creator else {}
        title = args.title or meta.get("title", "Coding Tip")
        creator = args.creator or meta.get("creator", "")
        takeaways = args.takeaways or []
        code = args.code
        if code and os.path.exists(code):
            with open(code, "r", encoding="utf-8") as f:
                code = f.read()

    new_reel = {
        "id": f"reel_{len(reels) + 1:03d}",
        "title": title,
        "url": url,
        "creator": creator,
        "category": category,
        "takeaways": takeaways,
        "code_snippet": code,
        "date_added": datetime.date.today().isoformat()
    }

    reels.append(new_reel)
    save_reels(reels)
    print(f"✨ Added reel '{title}' ({category})")
    rebuild_catalog(reels)


if __name__ == "__main__":
    main()
