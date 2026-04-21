from __future__ import annotations

import csv
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


ROOT = Path(__file__).resolve().parent
BATCH_DIR = ROOT / "batch"
OUTPUT_DIR = ROOT / "outputs"

DIGITAL_TEXT_PATH = ROOT / "digital_text.pdf"
TABLE_REPORT_PATH = ROOT / "table_report.pdf"
SCANNED_PDF_PATH = ROOT / "scanned_document.pdf"
SCANNED_PNG_PATH = ROOT / "scanned_document_page1.png"

DIGITAL_TEXT_SOURCE_PATH = ROOT / "digital_text_source.txt"
TABLE_SOURCE_PATH = ROOT / "table_report_source.csv"
SCANNED_REFERENCE_PATH = ROOT / "scanned_document_reference.txt"
MANIFEST_PATH = ROOT / "pdf_dataset_manifest.json"
BATCH_EXPECTED_PATH = ROOT / "batch_expected_summary.csv"


DIGITAL_PAGES = [
    {
        "title": "Digital workbook example",
        "body": [
            "This PDF is designed for PyPDF2 text extraction exercises.",
            "Students can inspect page counts, metadata, and paragraph text without needing OCR.",
            "The document mixes short headings, complete sentences, and repeated keywords such as data, report, and student.",
            "Use this file when the notebook asks for a digital text sample.",
        ],
    },
    {
        "title": "Lesson notes",
        "body": [
            "Page two contains enough text to test multi-page extraction and simple cleaning steps.",
            "Typical tasks include joining pages, counting words, and saving the result to a text file.",
            "Because the text layer is present, extraction should work directly with PyPDF2.",
            "Students can compare this result with the OCR example later in the workbook.",
        ],
    },
    {
        "title": "Reflection prompts",
        "body": [
            "Which library worked best for this document type?",
            "How much cleanup was needed after extraction?",
            "Which repeated words describe the document most clearly?",
            "These questions are intentionally simple so the sample stays predictable for automated checks.",
        ],
    },
]

TABLE_COLUMNS = ["Month", "Group", "Submitted", "AverageScore", "Late", "Notes"]
TABLE_ROWS = [
    ["January", "A1", "24", "8.9", "1", "Strong practical work"],
    ["February", "A1", "22", "8.4", "2", "Two late reports"],
    ["March", "B2", "26", "9.1", "0", "Clean table extraction target"],
    ["April", "B2", "25", "8.8", "1", "Minor formatting changes"],
    ["May", "C3", "23", "8.6", "3", "Follow up on missing files"],
]

SCANNED_LINES = [
    "OCR sample document",
    "",
    "Student: Marta Ozola",
    "Course: Digital document analysis",
    "Attendance: 18 of 20 sessions",
    "Result: completed with distinction",
    "",
    "Scanned copies require OCR because the text layer is missing.",
]


def ensure_directories() -> None:
    BATCH_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def build_styles() -> tuple[ParagraphStyle, ParagraphStyle]:
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        "WorkbookTitle",
        parent=styles["Heading1"],
        fontName="Helvetica-Bold",
        fontSize=18,
        leading=22,
        textColor=colors.HexColor("#1F3A5F"),
        spaceAfter=10,
    )
    body_style = ParagraphStyle(
        "WorkbookBody",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=11,
        leading=16,
        spaceAfter=8,
    )
    return title_style, body_style


def create_digital_pdf(path: Path, pages: list[dict[str, list[str] | str]]) -> None:
    title_style, body_style = build_styles()
    doc = SimpleDocTemplate(
        str(path),
        pagesize=A4,
        leftMargin=18 * mm,
        rightMargin=18 * mm,
        topMargin=18 * mm,
        bottomMargin=18 * mm,
        title="Digital workbook example",
        author="OpenAI Codex",
    )

    story = []
    for page_index, page in enumerate(pages):
        story.append(Paragraph(str(page["title"]), title_style))
        for paragraph in page["body"]:
            story.append(Paragraph(paragraph, body_style))
        if page_index != len(pages) - 1:
            story.append(Spacer(1, 8))
            story.append(PageBreak())

    doc.build(story)


def create_table_pdf(path: Path, heading: str, rows: list[list[str]]) -> None:
    title_style, body_style = build_styles()
    doc = SimpleDocTemplate(
        str(path),
        pagesize=A4,
        leftMargin=16 * mm,
        rightMargin=16 * mm,
        topMargin=16 * mm,
        bottomMargin=16 * mm,
        title=heading,
        author="OpenAI Codex",
    )

    table = Table([TABLE_COLUMNS, *rows], repeatRows=1)
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#D9E8FB")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.HexColor("#183153")),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
                ("FONTSIZE", (0, 0), (-1, -1), 9),
                ("LEADING", (0, 0), (-1, -1), 11),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F7FAFD")]),
                ("ALIGN", (2, 1), (4, -1), "CENTER"),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
            ]
        )
    )

    story = [
        Paragraph(heading, title_style),
        Paragraph(
            "The first page contains a grid-based table intended for pdfplumber extraction tests.",
            body_style,
        ),
        Spacer(1, 6),
        table,
    ]
    doc.build(story)


def load_font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = [
        "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/calibri.ttf",
        "C:/Windows/Fonts/tahoma.ttf",
    ]
    for candidate in candidates:
        if Path(candidate).exists():
            return ImageFont.truetype(candidate, size=size)
    return ImageFont.load_default()


def create_scanned_assets(pdf_path: Path, png_path: Path, lines: list[str]) -> None:
    image = Image.new("RGB", (1654, 2339), "white")
    draw = ImageDraw.Draw(image)
    title_font = load_font(48)
    body_font = load_font(34)

    draw.rectangle([(80, 80), (1574, 2259)], outline=(0, 0, 0), width=3)
    draw.text((120, 140), lines[0], fill=(0, 0, 0), font=title_font)

    y = 260
    for line in lines[1:]:
        if line:
            draw.text((120, y), line, fill=(0, 0, 0), font=body_font)
            y += 70
        else:
            y += 40

    image.save(png_path)
    image.save(pdf_path, "PDF", resolution=150.0)


def write_text_source(path: Path, pages: list[dict[str, list[str] | str]]) -> None:
    chunks = []
    for page in pages:
        chunks.append(str(page["title"]))
        chunks.extend(page["body"])
        chunks.append("")
    path.write_text("\n".join(chunks).strip() + "\n", encoding="utf-8")


def write_table_source(path: Path, rows: list[list[str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(TABLE_COLUMNS)
        writer.writerows(rows)


def write_scanned_reference(path: Path, lines: list[str]) -> None:
    path.write_text("\n".join(lines).strip() + "\n", encoding="utf-8")


def create_batch_fixtures() -> list[dict[str, object]]:
    expected_rows: list[dict[str, object]] = []

    digital_path = BATCH_DIR / "digital_brief.pdf"
    create_digital_pdf(digital_path, DIGITAL_PAGES[:2])
    expected_rows.append(
        {
            "file_name": digital_path.name,
            "pdf_type_guess": "digital-text",
            "page_count": 2,
            "expected_text_chars_min": 350,
            "expected_table_rows_min": 0,
            "notes": "Text extraction should work with PyPDF2.",
        }
    )

    table_path = BATCH_DIR / "attendance_report.pdf"
    create_table_pdf(
        table_path,
        "Attendance report",
        [
            ["Week 1", "A1", "12", "8.7", "0", "On schedule"],
            ["Week 2", "A1", "11", "8.4", "1", "One late upload"],
            ["Week 3", "B2", "13", "8.9", "0", "Good consistency"],
            ["Week 4", "B2", "12", "9.0", "0", "Strong submissions"],
        ],
    )
    expected_rows.append(
        {
            "file_name": table_path.name,
            "pdf_type_guess": "table-heavy",
            "page_count": 1,
            "expected_text_chars_min": 50,
            "expected_table_rows_min": 4,
            "notes": "First page should contain an extractable table.",
        }
    )

    scanned_path = BATCH_DIR / "scan_archive_copy.pdf"
    scanned_png_path = BATCH_DIR / "scan_archive_copy_page1.png"
    create_scanned_assets(
        scanned_path,
        scanned_png_path,
        [
            "Archived scan copy",
            "",
            "Document id: ARC-2026-04",
            "Status: manual review required",
            "Reason: source file was stored as an image-only PDF",
        ],
    )
    expected_rows.append(
        {
            "file_name": scanned_path.name,
            "pdf_type_guess": "scanned",
            "page_count": 1,
            "expected_text_chars_min": 0,
            "expected_table_rows_min": 0,
            "notes": "PyPDF2 should see little or no text. OCR is needed.",
        }
    )

    return expected_rows


def write_batch_expected_summary(path: Path, rows: list[dict[str, object]]) -> None:
    fieldnames = [
        "file_name",
        "pdf_type_guess",
        "page_count",
        "expected_text_chars_min",
        "expected_table_rows_min",
        "notes",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_manifest(batch_expected_rows: list[dict[str, object]]) -> None:
    manifest = {
        "root": str(ROOT),
        "primary_inputs": [
            {
                "path": DIGITAL_TEXT_PATH.name,
                "kind": "digital-text",
                "page_count": len(DIGITAL_PAGES),
                "companion": DIGITAL_TEXT_SOURCE_PATH.name,
            },
            {
                "path": TABLE_REPORT_PATH.name,
                "kind": "table-heavy",
                "page_count": 1,
                "companion": TABLE_SOURCE_PATH.name,
            },
            {
                "path": SCANNED_PDF_PATH.name,
                "kind": "scanned",
                "page_count": 1,
                "companion": SCANNED_REFERENCE_PATH.name,
                "fallback_image": SCANNED_PNG_PATH.name,
            },
        ],
        "batch_inputs": batch_expected_rows,
        "notes": [
            "The notebook reads main sample PDFs directly from pdf_tasks.",
            "Batch examples live in pdf_tasks/batch.",
            "The scanned PNG is a fallback for OCR workflows on machines without Poppler.",
        ],
    }
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2), encoding="utf-8")


def main() -> None:
    ensure_directories()
    create_digital_pdf(DIGITAL_TEXT_PATH, DIGITAL_PAGES)
    create_table_pdf(TABLE_REPORT_PATH, "Laboratory submission report", TABLE_ROWS)
    create_scanned_assets(SCANNED_PDF_PATH, SCANNED_PNG_PATH, SCANNED_LINES)

    write_text_source(DIGITAL_TEXT_SOURCE_PATH, DIGITAL_PAGES)
    write_table_source(TABLE_SOURCE_PATH, TABLE_ROWS)
    write_scanned_reference(SCANNED_REFERENCE_PATH, SCANNED_LINES)

    batch_expected_rows = create_batch_fixtures()
    write_batch_expected_summary(BATCH_EXPECTED_PATH, batch_expected_rows)
    write_manifest(batch_expected_rows)

    generated_files = [
        DIGITAL_TEXT_PATH,
        TABLE_REPORT_PATH,
        SCANNED_PDF_PATH,
        SCANNED_PNG_PATH,
        DIGITAL_TEXT_SOURCE_PATH,
        TABLE_SOURCE_PATH,
        SCANNED_REFERENCE_PATH,
        BATCH_EXPECTED_PATH,
        MANIFEST_PATH,
    ]
    generated_files.extend(sorted(BATCH_DIR.glob("*")))

    print("Generated PDF fixtures and companion datasets:")
    for path in generated_files:
        print(f"- {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
