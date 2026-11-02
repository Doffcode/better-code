# Better Code: Handoff & Architecture Guide

Curated knowledge base of coding-focused Instagram reels, transforming short-form educational videos into permanent, structured engineering notes, cheat sheets, and code snippets.

## Repository Details
- **Repo**: `Doffcode/better-code` (GitHub)
- **Local Path**: `/home/shiva/Projects/better-code`
- **Visibility**: Public

## File Structure
- `reels.json`: Single source of truth containing all indexed reels, takeaways, code snippets, tags, and creator metadata.
- `CATALOG.md`: Generated, human-readable markdown categorized by topics (DSA, System Design, Clean Code, Python, Web Dev, Tools/Workflow, Interview Prep).
- `scripts/add_reel.py`: Python CLI tool to ingest reels, extract metadata (via yt-dlp if reachable), and regenerate `CATALOG.md`.
- `README.md`: Overview and documentation.

## Common Workflows
- **Add Reel**: `python3 scripts/add_reel.py`
- **Regenerate Catalog**: `python3 scripts/add_reel.py --build`
