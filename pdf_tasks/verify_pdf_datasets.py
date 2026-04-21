from __future__ import annotations

import csv
import json
import os
from pathlib import Path

import nbformat
import pdfplumber
import pytesseract
from nbclient import NotebookClient
from PIL import Image
from PyPDF2 import PdfReader


ROOT = Path(__file__).resolve().parent
BATCH_DIR = ROOT / "batch"
NOTEBOOK_PATH = ROOT / "student_workbook_pdf_analize_lv.ipynb"
MANIFEST_PATH = ROOT / "pdf_dataset_manifest.json"


def require_file(path: Path) -> None:
    if not path.exists():
        raise FileNotFoundError(f"Missing required file: {path}")


def assert_true(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def verify_manifest() -> None:
    require_file(MANIFEST_PATH)
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    for item in manifest["primary_inputs"]:
        require_file(ROOT / item["path"])
    for item in manifest["batch_inputs"]:
        require_file(BATCH_DIR / item["file_name"])


def verify_digital_text() -> None:
    pdf_path = ROOT / "digital_text.pdf"
    source_path = ROOT / "digital_text_source.txt"
    require_file(pdf_path)
    require_file(source_path)

    reader = PdfReader(str(pdf_path))
    extracted_text = "\n".join(page.extract_text() or "" for page in reader.pages)
    source_text = source_path.read_text(encoding="utf-8")

    assert_true(len(reader.pages) == 3, "digital_text.pdf should have 3 pages.")
    assert_true("Digital workbook example" in extracted_text, "Digital PDF title was not extracted.")
    assert_true("PyPDF2" in extracted_text, "Digital PDF should include PyPDF2 in extracted text.")
    assert_true(len(extracted_text) >= len(source_text) * 0.7, "Digital PDF extraction is too short.")


def verify_table_report() -> None:
    pdf_path = ROOT / "table_report.pdf"
    csv_path = ROOT / "table_report_source.csv"
    require_file(pdf_path)
    require_file(csv_path)

    with pdfplumber.open(pdf_path) as pdf:
        extracted_table = pdf.pages[0].extract_table()

    with csv_path.open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.reader(handle))

    assert_true(extracted_table is not None, "pdfplumber did not extract a table from table_report.pdf.")
    assert_true(extracted_table[0] == rows[0], "Table header mismatch in table_report.pdf.")
    assert_true(len(extracted_table) >= len(rows), "Extracted table row count is lower than expected.")


def verify_scanned_assets() -> None:
    pdf_path = ROOT / "scanned_document.pdf"
    png_path = ROOT / "scanned_document_page1.png"
    require_file(pdf_path)
    require_file(png_path)

    reader = PdfReader(str(pdf_path))
    extracted_text = "\n".join(page.extract_text() or "" for page in reader.pages).strip()
    assert_true(len(reader.pages) == 1, "scanned_document.pdf should have 1 page.")
    assert_true(len(extracted_text) <= 20, "Scanned PDF should not expose a normal text layer.")

    with Image.open(png_path) as image:
        ocr_text = pytesseract.image_to_string(image)

    normalized_ocr = " ".join(ocr_text.split()).lower()
    assert_true("ocr sample document" in normalized_ocr, "OCR did not recover the scanned title.")
    assert_true("attendance: 18 of 20 sessions" in normalized_ocr, "OCR missed the attendance line.")


def verify_batch_files() -> None:
    expected_path = ROOT / "batch_expected_summary.csv"
    require_file(expected_path)

    with expected_path.open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))

    for row in rows:
        pdf_path = BATCH_DIR / row["file_name"]
        require_file(pdf_path)
        reader = PdfReader(str(pdf_path))
        assert_true(
            len(reader.pages) == int(row["page_count"]),
            f"{pdf_path.name} page count mismatch.",
        )


def verify_notebook_executes() -> None:
    require_file(NOTEBOOK_PATH)
    runtime_dir = Path(os.environ.get("TEMP", str(ROOT))) / "codex_jupyter_runtime"
    runtime_dir.mkdir(exist_ok=True)
    os.environ["JUPYTER_RUNTIME_DIR"] = str(runtime_dir)
    os.environ["JUPYTER_ALLOW_INSECURE_WRITES"] = "true"
    notebook = nbformat.read(NOTEBOOK_PATH, as_version=4)
    client = NotebookClient(
        notebook,
        timeout=180,
        kernel_name="python3",
        resources={"metadata": {"path": str(ROOT.parent)}},
    )
    client.execute()


def main() -> None:
    verify_manifest()
    verify_digital_text()
    verify_table_report()
    verify_scanned_assets()
    verify_batch_files()
    verify_notebook_executes()
    print("Verification complete: PDF fixtures and notebook executed successfully.")


if __name__ == "__main__":
    main()
