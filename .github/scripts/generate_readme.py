#!/usr/bin/env python3
"""
Auto-generates the folder table inside python/basic/concepts/README.md.

For every subfolder inside CONCEPTS_DIR that contains a README.md,
this pulls:
  - the first '# Title' line  -> Topic column
  - the first '> blockquote'  -> Covers column
and rebuilds the table between the AUTO-GENERATED-CONTENT markers.

Run manually:
    python .github/scripts/generate_readme.py

Runs automatically via .github/workflows/update-concepts-readme.yml
"""

import re
from pathlib import Path

# Path from repo root to the concepts folder
CONCEPTS_DIR = Path("basic/concepts")
README_PATH = CONCEPTS_DIR / "README.md"

START_MARKER = "<!-- AUTO-GENERATED-CONTENT:START -->"
END_MARKER = "<!-- AUTO-GENERATED-CONTENT:END -->"


def get_title_and_summary(readme_path: Path):
    text = readme_path.read_text(encoding="utf-8")

    title_match = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else readme_path.parent.name

    summary_match = re.search(r"^>\s+(.+)$", text, re.MULTILINE)
    summary = summary_match.group(1).strip() if summary_match else "—"

    return title, summary


def build_table():
    rows = []
    if not CONCEPTS_DIR.exists():
        return rows

    for folder in sorted(CONCEPTS_DIR.iterdir()):
        if not folder.is_dir() or folder.name.startswith("."):
            continue
        folder_readme = folder / "README.md"
        if not folder_readme.exists():
            continue
        title, summary = get_title_and_summary(folder_readme)
        rows.append(f"| [`{folder.name}/`](./{folder.name}) | {title} | {summary} |")

    return rows


def update_readme():
    if not README_PATH.exists():
        raise FileNotFoundError(f"{README_PATH} not found")

    content = README_PATH.read_text(encoding="utf-8")

    if START_MARKER not in content or END_MARKER not in content:
        raise ValueError(
            f"README.md must contain {START_MARKER} and {END_MARKER} markers"
        )

    table_rows = build_table()
    table = "| Folder | Topic | Covers |\n|---|---|---|\n" + "\n".join(table_rows)

    new_block = f"{START_MARKER}\n{table}\n{END_MARKER}"

    updated_content = re.sub(
        f"{re.escape(START_MARKER)}.*?{re.escape(END_MARKER)}",
        new_block,
        content,
        flags=re.DOTALL,
    )

    README_PATH.write_text(updated_content, encoding="utf-8")
    print(f"Updated {README_PATH} with {len(table_rows)} folder(s).")


if __name__ == "__main__":
    update_readme()
