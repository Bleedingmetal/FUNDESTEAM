import os
import pathlib
from collections import defaultdict

EXCLUDE_DIRS = {"node_modules", "venv", ".git", "dist", "build"}

# Optional mapping for "nice" language names
EXT_LANG_MAP = {
    ".ts": "TypeScript",
    ".js": "JavaScript",
    ".py": "Python",
    ".css": "CSS",
    ".html": "HTML",
    ".json": "JSON",
    ".md": "Markdown",
    ".txt": "Text",
    ".bat": "Batch",
}

stats = defaultdict(lambda: {"files": 0, "lines": 0, "words": 0, "chars": 0})
totals = {"files": 0, "lines": 0, "words": 0, "chars": 0}

for root, dirs, files in os.walk("."):
    dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]

    for fname in files:
        fpath = os.path.join(root, fname)
        ext = pathlib.Path(fname).suffix.lower()
        lang = EXT_LANG_MAP.get(ext, f"*{ext}" if ext else "Other")

        try:
            with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
                text = f.read()
        except Exception:
            continue  # skip binary/unreadable files

        lines = text.count("\n") + 1 if text else 0
        words = len(text.split())
        chars = len(text)

        stats[lang]["files"] += 1
        stats[lang]["lines"] += lines
        stats[lang]["words"] += words
        stats[lang]["chars"] += chars

        totals["files"] += 1
        totals["lines"] += lines
        totals["words"] += words
        totals["chars"] += chars

# Print summary
print(f"{'Language':<12} {'Files':>6} {'Lines':>10} {'Words':>10} {'Chars':>12}")
print("-" * 52)
for lang, data in stats.items():
    print(f"{lang:<12} {data['files']:>6} {data['lines']:>10} {data['words']:>10} {data['chars']:>12}")

print("-" * 52)
print(f"{'TOTAL':<12} {totals['files']:>6} {totals['lines']:>10} {totals['words']:>10} {totals['chars']:>12}")
