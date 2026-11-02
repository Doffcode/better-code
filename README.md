# Better Code 🚀

> A curated, high-yield vault of bite-sized coding reels, developer tips, system design insights, and algorithmic concepts gathered from Instagram.

Turn passive reel scrolling into actionable engineering knowledge. Every saved reel is cataloged with key takeaways, code snippets, creator credits, and categorized by topic for quick revision.

---

## 🗂️ Categories

- **[Data Structures & Algorithms (`dsa`)](CATALOG.md#data-structures--algorithms)**: Visual tricks, time complexity optimizations, pattern recognition.
- **[System Design & Architecture (`system-design`)](CATALOG.md#system-design--architecture)**: Scalability patterns, caching, database trade-offs, real-world case studies.
- **[Clean Code & Software Craftsmanship (`clean-code`)](CATALOG.md#clean-code)**: Refactoring, design patterns, naming conventions, SOLID principles.
- **[Python Gems (`python`)](CATALOG.md#python-gems)**: Pythonic idioms, hidden standard library modules, performance optimizations.
- **[Web Development (`web-dev`)](CATALOG.md#web-development)**: Modern CSS, JavaScript/TypeScript quirks, backend APIs, browser mechanics.
- **[Developer Tools & Workflows (`tools-workflow`)](CATALOG.md#developer-tools--workflows)**: Git mastery, CLI shortcuts, Docker tips, terminal productivity.
- **[Interview & Career Insights (`interview-prep`)](CATALOG.md#interview--career-insights)**: Tricky conceptual questions, mindset, and behavioral advice.

---

## 📖 Catalog

All cataloged reels and notes are maintained in **[CATALOG.md](CATALOG.md)** and machine-readable in **[reels.json](reels.json)**.

---

## 🛠️ Adding a New Reel

You can manually add entries to `reels.json` or run the helper script:

```bash
# Add a reel interactively
python3 scripts/add_reel.py

# Or pass parameters directly
python3 scripts/add_reel.py --url "https://www.instagram.com/reel/xyz..." --category "dsa" --title "Two Pointer Pattern Explained" --takeaways "Use two pointers when array is sorted to reach O(N) time."
```

The script automatically validates entries and updates `CATALOG.md`.

---

## 🤝 Contributing

Found a high-value reel that teaches a core programming concept well? Submit an issue or a PR with the reel link, category, and key takeaways!
