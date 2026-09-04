from pathlib import Path
from urllib.parse import unquote
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
errors: list[str] = []

for document in ROOT.rglob("*.md"):
    text = document.read_text(encoding="utf-8")
    for raw in LINK.findall(text):
        target = raw.strip().split()[0].strip("<>")
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        path_part = unquote(target.split("#", 1)[0])
        if not path_part:
            continue
        resolved = (document.parent / path_part).resolve()
        try:
            resolved.relative_to(ROOT.resolve())
        except ValueError:
            errors.append(f"{document.relative_to(ROOT)}: link escapes repository: {target}")
            continue
        if not resolved.exists():
            errors.append(f"{document.relative_to(ROOT)}: missing target: {target}")

if errors:
    print("\n".join(sorted(set(errors))))
    sys.exit(1)
print("PASS: internal Markdown links resolve inside the repository")
