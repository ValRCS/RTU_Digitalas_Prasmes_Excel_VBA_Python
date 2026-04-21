from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTLINE_PATH = ROOT / "pdf_tasks" / "student_workbook_outline.md"
OUTPUT_PATH = ROOT / "pdf_tasks" / "student_workbook_pdf_analize_lv.ipynb"
REFERENCE_NOTEBOOK = ROOT / "notebooks" / "student_workbook_latvia_excel_datasets.ipynb"


CELL_MARKER = re.compile(r"<!-- CELL: (markdown|code) -->\s*")
CODE_FENCE = re.compile(r"^\s*```(?:python)?\s*$")


def load_reference_metadata() -> dict:
    if not REFERENCE_NOTEBOOK.exists():
        return {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {
                "name": "python",
                "version": "3",
            },
        }

    notebook = json.loads(REFERENCE_NOTEBOOK.read_text(encoding="utf-8"))
    return notebook.get("metadata", {})


def to_source_lines(text: str) -> list[str]:
    if not text:
        return []

    lines = text.splitlines(keepends=True)
    if lines and not lines[-1].endswith("\n"):
        lines[-1] += "\n"
    return lines


def strip_code_fences(text: str) -> str:
    lines = text.splitlines()
    if len(lines) >= 2 and CODE_FENCE.match(lines[0]) and CODE_FENCE.match(lines[-1]):
        return "\n".join(lines[1:-1]).strip("\n")
    return text.strip("\n")


def parse_outline(outline_text: str) -> list[dict]:
    parts = CELL_MARKER.split(outline_text)

    cells: list[dict] = []
    for idx in range(1, len(parts), 2):
        cell_type = parts[idx]
        content = parts[idx + 1].lstrip("\n")

        if cell_type == "code":
            source_text = strip_code_fences(content)
            cell = {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": to_source_lines(source_text),
            }
        else:
            cell = {
                "cell_type": "markdown",
                "metadata": {},
                "source": to_source_lines(content.rstrip()),
            }

        cells.append(cell)

    return cells


def build_notebook() -> dict:
    outline_text = OUTLINE_PATH.read_text(encoding="utf-8")
    cells = parse_outline(outline_text)
    metadata = load_reference_metadata()

    return {
        "cells": cells,
        "metadata": metadata,
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def main() -> None:
    notebook = build_notebook()
    OUTPUT_PATH.write_text(
        json.dumps(notebook, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"Notebook generated: {OUTPUT_PATH}")
    print(f"Cell count: {len(notebook['cells'])}")


if __name__ == "__main__":
    main()
