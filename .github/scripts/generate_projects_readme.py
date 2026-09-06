#!/usr/bin/env python3
"""
Auto-generates the project table inside projects/README.md.

For every subfolder inside PROJECTS_DIR that contains a README.md,
this pulls:
  - the first '# Title' line   -> Project name shown in the table
  - the first '> blockquote'   -> Description column
  - a line starting with 'Status:' -> Status column (defaults to "In Progress" if missing)

Run manually:
    python .github/scripts/generate_projects_readme.py
"""

import re
from pathlib import Path

PROJECTS_DIR = Path("projects")
README_PATH = PROJECTS_DIR / "README.md"

START_MARKER = "<!-- AUTO-GENERATED-CONTENT:START -->"
END_MARKER = "<!-- AUTO-GENERATED-CONTENT:END -->"

DEFAULT_STATUS = "🚧 In Progress"


def get_project_info(readme_path: Path):
    text = readme_path.read_text(encoding="utf-8")

    title_match = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else readme_path.parent.name

    desc_match = re.search(r"^>\s+(.+)$", text, re.MULTILINE)
    description = desc_match.group(1).strip() if desc_match else "—"

    status_match = re.search(r"^Status:\s*(.+)$", text, re.MULTILINE)
    status = status_match.group(1).strip() if status_match else DEFAULT_STATUS

    return title, description, status


def build_table():
    rows = []
    if not PROJECTS_DIR.exists():
        return rows

    for folder in sorted(PROJECTS_DIR.iterdir()):
        if not folder.is_dir() or folder.name.startswith("."):
            continue
        folder_readme = folder / "README.md"
        if not folder_readme.exists():
            continue
        title, description, status = get_project_info(folder_readme)
        rows.append(f"| [{title}]({folder.name}) | {description} | {status} |")

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
    table = "| Project | Description | Status |\n|---|---|---|\n" + "\n".join(table_rows)

    new_block = f"{START_MARKER}\n{table}\n{END_MARKER}"

    updated_content = re.sub(
        f"{re.escape(START_MARKER)}.*?{re.escape(END_MARKER)}",
        new_block,
        content,
        flags=re.DOTALL,
    )

    README_PATH.write_text(updated_content, encoding="utf-8")
    print(f"Updated {README_PATH} with {len(table_rows)} project(s).")


if __name__ == "__main__":
    update_readme()
