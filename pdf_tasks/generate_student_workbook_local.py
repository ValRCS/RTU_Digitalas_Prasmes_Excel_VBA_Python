from __future__ import annotations

import json
from pathlib import Path
from textwrap import dedent


ROOT = Path(__file__).resolve().parents[1]
SOURCE_PATH = ROOT / "pdf_tasks" / "student_workbook_pdf_analize_lv_colab.ipynb"
OUTPUT_PATH = ROOT / "pdf_tasks" / "student_workbook_pdf_analize_lv_local.ipynb"


def to_source(text: str) -> list[str]:
    text = dedent(text).strip("\n")
    if not text:
        return []
    lines = text.splitlines(keepends=True)
    if lines and not lines[-1].endswith("\n"):
        lines[-1] += "\n"
    return lines


def set_cell_source(cell: dict, text: str) -> None:
    cell["source"] = to_source(text)


def replace_in_all_cells(notebook: dict, old: str, new: str) -> None:
    for cell in notebook["cells"]:
        source = "".join(cell.get("source", []))
        if old in source:
            cell["source"] = to_source(source.replace(old, new))


def build_notebook() -> dict:
    notebook = json.loads(SOURCE_PATH.read_text(encoding="utf-8"))
    cells = notebook["cells"]

    set_cell_source(
        cells[0],
        """
        # PDF dokumentu analīze ar Python (Lokālā Windows vide)

        Šī ir **lokāli izpildāma** studentu workbook versija tēmai **"PDF dokumentu analīze ar Python"**.

        Šī notebook ir paredzēta darbam:

        - Windows 10/11 vidē;
        - ar **Python 3.14**;
        - ar aktīvu projekta virtuālo vidi **`.venv`**;
        - Jupyter Notebook vai JupyterLab vidē.

        Atšķirībā no Google Colab versijas, šajā notebook:

        - netiek lejupielādēti faili no GitHub, jo tiek izmantoti lokālie `pdf_tasks` faili;
        - netiek mēģināts automātiski instalēt Windows sistēmas rīkus kā `Tesseract` un `Poppler`;
        - tiek pieņemts, ka strādājat repozitorijā ar jau sagatavotu lokālo vidi;
        - Python bibliotēkas var uzstādīt tieši aktīvajā `.venv`, izmantojot notebook šūnas.

        ## Ievads

        Šī notebook mērķis ir soli pa solim parādīt, kā ar Python analizēt dažādu tipu PDF dokumentus:

        - digitāli ģenerētus PDF ar teksta slāni;
        - PDF failus ar tabulām;
        - skenētus PDF dokumentus, kuriem vajadzīga OCR pieeja;
        - vairāku failu batch apstrādi vienā darba plūsmā.

        Praktiski mēs mēģinām sasniegt vienu galveno mērķi: izvēlēties pareizo rīku pareizajam PDF tipam un iegūt rezultātu, ko pēc tam var saglabāt kā tekstu, tabulu vai kopsavilkuma atskaiti.

        Šajā tēmā lielākā daļa grūtību parasti nav pašā Python sintaksē, bet gan tehniskajā sagatavošanā:

        - pareizo bibliotēku uzstādīšanā;
        - ārējo rīku, piemēram, `Tesseract` un `Poppler`, pieejamībā;
        - atšķirībā starp digitālu PDF un skenētu PDF;
        - datu kvalitātes problēmās pēc ekstraktēšanas vai OCR.

        Lokālā vide dod vairāk kontroles pār failiem un rezultātu saglabāšanu, taču prasa vairāk uzmanības sākotnējai Windows konfigurācijai.
        """,
    )

    set_cell_source(
        cells[1],
        """
        ## Darba plūsma lokālajā Windows vidē

        Ieteicams izpildīt šūnas tieši šādā secībā:

        1. pārbaudīt, ka Jupyter izmanto projekta `.venv` Python interpretatoru;
        2. pārbaudīt, ka `Tesseract` un `Poppler` ir pieejami Windows vidē;
        3. ja vajag, uzstādīt Python bibliotēkas aktīvajā `.venv`;
        4. pārbaudīt, ka `pdf_tasks` lokālie faili ir pieejami;
        5. iziet cauri sadaļām par tekstu, tabulām, OCR un batch apstrādi.

        Piezīme:

        - lokālajā vidē rezultātu faili saglabāsies diskā mapē `pdf_tasks/outputs`;
        - ja trūkst ārējo OCR rīku, izmantojiet [INSTALL_instructions_en.md](INSTALL_instructions_en.md).
        """,
    )

    set_cell_source(
        cells[2],
        """
        ## 0. Sistēmas rīku pārbaude lokālajā Windows vidē

        OCR un PDF lapu renderēšanai lokālajā Windows vidē nepietiek tikai ar Python bibliotēkām.

        Šai notebook versijai svarīgi ir divi ārējie rīki:

        - `Tesseract OCR`
        - `Poppler for Windows`

        Šajā sadaļā notebook tos **neinstalē automātiski**, bet pārbauda, vai tie ir pieejami. Ja kāds no tiem trūkst, izmantojiet:

        - [INSTALL_instructions_en.md](INSTALL_instructions_en.md)

        Tur ir detalizētas Windows 10/11 uzstādīšanas instrukcijas.
        """,
    )

    set_cell_source(
        cells[3],
        r"""
        import platform
        import shutil
        import subprocess

        print("Platforma:", platform.platform())

        for command_name in ["tesseract", "pdftoppm", "pdftocairo"]:
            print(f"{command_name} PATH meklēšana ->", shutil.which(command_name))

        if platform.system() == "Windows":
            for command_name in ["tesseract", "pdftoppm", "pdftocairo"]:
                result = subprocess.run(
                    ["where.exe", command_name],
                    capture_output=True,
                    text=True,
                )
                lines = [line for line in result.stdout.splitlines() if line.strip()]
                print(f"where.exe {command_name} ->", lines if lines else "nav atrasts")

        print("\nJa kāds no rīkiem nav atrasts, skatiet INSTALL_instructions_en.md.")
        """,
    )

    set_cell_source(
        cells[4],
        """
        ## 1. Python bibliotēku uzstādīšana lokālajā `.venv`

        Šajā notebook tiek pieņemts, ka:

        - Python 3.14 jau ir uzstādīts;
        - Jupyter darbojas projekta `.venv` vidē.

        Ja nepieciešams, nākamā šūna uzstādīs notebook izmantotās Python bibliotēkas **pašreizējā Python kernelī**:

        - `PyPDF2`
        - `pdfplumber`
        - `pandas`
        - `pytesseract`
        - `pdf2image`
        - `Pillow`

        Pēc uzstādīšanas dažās Jupyter vidēs var būt nepieciešams pārrunāt šūnas no jauna, bet runtime restarts lokāli parasti nav vajadzīgs.
        """,
    )

    set_cell_source(
        cells[5],
        """
        import sys

        print("Aktīvais Python interpretators:")
        print(sys.executable)

        !{sys.executable} -m pip install -q --disable-pip-version-check PyPDF2 pdfplumber pandas pytesseract pdf2image Pillow
        """,
    )

    set_cell_source(
        cells[6],
        """
        ## 2. Lokālo `pdf_tasks` failu pārbaude

        Atšķirībā no Colab versijas, šī notebook izmanto jau esošos lokālos failus mapē `pdf_tasks`.

        Tāpēc šajā šūnā:

        - netiek nekas lejupielādēts;
        - tiek pārbaudīts, vai visi vajadzīgie faili tiešām eksistē;
        - tiek parādīts, kuri faili būs izmantoti workbook gaitā.

        Ja kāds no failiem trūkst, izmantojiet repozitorijā esošo ģeneratoru:

        - `pdf_tasks/generate_pdf_datasets.py`
        """,
    )

    set_cell_source(
        cells[7],
        """
        from pathlib import Path

        cwd = Path.cwd()
        candidate_roots = [cwd / "pdf_tasks", cwd]
        detected_root = None

        for candidate in candidate_roots:
            if (candidate / "pdf_dataset_manifest.json").exists():
                detected_root = candidate
                break

        if detected_root is None:
            raise FileNotFoundError(
                "Neizdevās atrast pdf_tasks datu mapi. Palaidiet notebook no repozitorija saknes vai no pdf_tasks mapes."
            )

        required_paths = [
            detected_root / "pdf_dataset_manifest.json",
            detected_root / "batch_expected_summary.csv",
            detected_root / "digital_text.pdf",
            detected_root / "digital_text_source.txt",
            detected_root / "table_report.pdf",
            detected_root / "table_report_source.csv",
            detected_root / "scanned_document.pdf",
            detected_root / "scanned_document_page1.png",
            detected_root / "scanned_document_reference.txt",
            detected_root / "batch" / "digital_brief.pdf",
            detected_root / "batch" / "attendance_report.pdf",
            detected_root / "batch" / "scan_archive_copy.pdf",
        ]

        missing_paths = [path for path in required_paths if not path.exists()]

        print("Detected PDF_ROOT:", detected_root.resolve())
        if missing_paths:
            print("Trūkstošie faili:")
            for path in missing_paths:
                print("-", path)
            raise FileNotFoundError("Trūkst viens vai vairāki pdf_tasks faili.")
        else:
            print("Visi nepieciešamie faili ir pieejami.")
        """,
    )

    set_cell_source(
        cells[8],
        """
        ## 3. Importi un vides pārbaude lokālajā Windows vidē

        Šajā šūnā:

        - importēsim bibliotēkas;
        - pārbaudīsim, ka strādājam lokālajā vidē, nevis Colab;
        - izdrukāsim aktīvā Python interpretatora ceļu;
        - pārbaudīsim, vai `Tesseract` un `Poppler` ir atrodamas komandas vai ceļi.
        """,
    )

    set_cell_source(
        cells[9],
        """
        from __future__ import annotations

        import json
        import re
        import shutil
        import subprocess
        import sys
        from collections import Counter
        from difflib import SequenceMatcher
        from pathlib import Path

        import pandas as pd
        import pdfplumber
        import pytesseract
        from PIL import Image
        from PyPDF2 import PdfReader
        from pdf2image import convert_from_path
        from IPython.display import Markdown, display

        IN_COLAB = False
        LOCAL_WINDOWS = sys.platform.startswith("win")

        print("Running in Colab:", IN_COLAB)
        print("Running on Windows:", LOCAL_WINDOWS)
        print("Python version:", sys.version.split()[0])
        print("Python executable:", sys.executable)
        print("Tesseract on PATH:", shutil.which("tesseract"))
        print("pdftoppm on PATH:", shutil.which("pdftoppm"))
        """,
    )

    set_cell_source(
        cells[10],
        """
        ## 4. Ceļi un palīgfunkcijas

        Šeit definējam:

        - lokālās `pdf_tasks` mapes noteikšanu;
        - teksta tīrīšanas funkcijas;
        - PDF lapu skaita iegūšanu;
        - teksta ekstraktēšanu;
        - tabulu ekstraktēšanu;
        - OCR funkciju skenētiem PDF;
        - Windows palīgfunkcijas `Tesseract` un `Poppler` atrašanai.
        """,
    )

    set_cell_source(
        cells[11],
        r"""
        pd.set_option("display.max_colwidth", 120)


        def resolve_pdf_root() -> Path:
            cwd = Path.cwd()
            candidates = [cwd / "pdf_tasks", cwd]
            for candidate in candidates:
                if (candidate / "pdf_dataset_manifest.json").exists():
                    return candidate
            raise FileNotFoundError(
                "Neizdevās noteikt pdf_tasks mapi. Palaidiet notebook no repozitorija saknes vai no pdf_tasks mapes."
            )


        def find_tesseract_exe() -> Path | None:
            path_match = shutil.which("tesseract")
            if path_match:
                return Path(path_match)

            candidates = [
                Path(r"C:\Program Files\Tesseract-OCR\tesseract.exe"),
                Path(r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"),
            ]
            for candidate in candidates:
                if candidate.exists():
                    return candidate
            return None


        def find_poppler_bin() -> Path | None:
            pdftoppm_match = shutil.which("pdftoppm")
            if pdftoppm_match:
                return Path(pdftoppm_match).parent

            candidates = [
                Path(r"C:\Tools\poppler\Library\bin"),
                Path(r"C:\Program Files\poppler\Library\bin"),
                Path(r"C:\Program Files (x86)\poppler\Library\bin"),
            ]
            for candidate in candidates:
                if (candidate / "pdftoppm.exe").exists():
                    return candidate
            return None


        PDF_ROOT = resolve_pdf_root()
        BATCH_DIR = PDF_ROOT / "batch"
        OUTPUT_DIR = PDF_ROOT / "outputs"

        MANIFEST_PATH = PDF_ROOT / "pdf_dataset_manifest.json"
        BATCH_EXPECTED_PATH = PDF_ROOT / "batch_expected_summary.csv"

        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

        TESSERACT_EXE = find_tesseract_exe()
        POPPLER_BIN = find_poppler_bin()

        if TESSERACT_EXE is not None:
            pytesseract.pytesseract.tesseract_cmd = str(TESSERACT_EXE)

        print("PDF_ROOT:", PDF_ROOT.resolve())
        print("TESSERACT_EXE:", TESSERACT_EXE)
        print("POPPLER_BIN:", POPPLER_BIN)


        def normalize_text(text: str) -> str:
            if not text:
                return ""
            text = text.replace("\xa0", " ")
            text = re.sub(r"[ \t]+", " ", text)
            text = re.sub(r"\n{3,}", "\n\n", text)
            return text.strip()


        def load_manifest() -> dict:
            return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))


        def get_primary_asset(kind: str) -> Path:
            manifest = load_manifest()
            for item in manifest["primary_inputs"]:
                if item["kind"] == kind:
                    return PDF_ROOT / item["path"]
            raise KeyError(f"Primary asset not found for kind={kind!r}")


        def get_primary_entry(kind: str) -> dict:
            manifest = load_manifest()
            for item in manifest["primary_inputs"]:
                if item["kind"] == kind:
                    return item
            raise KeyError(f"Primary asset not found for kind={kind!r}")


        def pdf_page_count(pdf_path: Path) -> int:
            return len(PdfReader(str(pdf_path)).pages)


        def extract_text_with_pypdf2(pdf_path: Path) -> str:
            reader = PdfReader(str(pdf_path))
            parts = [(page.extract_text() or "") for page in reader.pages]
            return normalize_text("\n\n".join(parts))


        def extract_text_with_pdfplumber(pdf_path: Path) -> str:
            with pdfplumber.open(pdf_path) as pdf:
                parts = [(page.extract_text() or "") for page in pdf.pages]
            return normalize_text("\n\n".join(parts))


        def extract_first_table(pdf_path: Path) -> pd.DataFrame:
            with pdfplumber.open(pdf_path) as pdf:
                table = pdf.pages[0].extract_table()

            if not table:
                return pd.DataFrame()

            header = [str(col).strip() if col is not None else "" for col in table[0]]
            rows = table[1:]
            df = pd.DataFrame(rows, columns=header)
            df = df.dropna(how="all")

            for column in df.columns:
                df[column] = df[column].map(lambda value: str(value).strip() if value is not None else "")

            return df


        def guess_pdf_type(file_name: str) -> str:
            name = file_name.lower()
            if "scan" in name or "ocr" in name:
                return "scanned"
            if "table" in name or "report" in name or "attendance" in name:
                return "table-heavy"
            return "digital-text"


        def ocr_pdf_first_page(pdf_path: Path, fallback_image: Path | None = None, lang: str = "eng+lav") -> tuple[Image.Image, str]:
            try:
                kwargs = {"first_page": 1, "last_page": 1}
                if POPPLER_BIN is not None:
                    kwargs["poppler_path"] = str(POPPLER_BIN)
                images = convert_from_path(str(pdf_path), **kwargs)
                image = images[0]
            except Exception:
                if fallback_image is None or not fallback_image.exists():
                    raise
                image = Image.open(fallback_image)

            text = pytesseract.image_to_string(image, lang=lang)
            return image, normalize_text(text)


        def process_batch_pdf(pdf_path: Path) -> dict:
            pdf_type = guess_pdf_type(pdf_path.name)
            page_count = pdf_page_count(pdf_path)

            pypdf2_text = extract_text_with_pypdf2(pdf_path)
            pdfplumber_text = extract_text_with_pdfplumber(pdf_path)
            best_text = pypdf2_text if len(pypdf2_text) >= len(pdfplumber_text) else pdfplumber_text

            table_df = extract_first_table(pdf_path) if pdf_type == "table-heavy" else pd.DataFrame()

            status = "ok"
            notes = ""
            if pdf_type == "scanned":
                status = "ocr-needed"
                notes = "PyPDF2 and pdfplumber see little or no text. OCR is the correct next step."

            return {
                "file_name": pdf_path.name,
                "pdf_type_guess": pdf_type,
                "page_count": page_count,
                "text_chars": len(best_text),
                "table_rows": int(len(table_df)) if not table_df.empty else 0,
                "status": status,
                "notes": notes,
            }


        manifest = load_manifest()
        manifest
        """,
    )

    set_cell_source(
        cells[12],
        """
        ## 5. Pieejamie lokālie faili

        Apskatīsim, kādi faili tika atrasti lokālajā `pdf_tasks` mapē.
        """,
    )

    set_cell_source(
        cells[38],
        """
        ## Papildu piezīme par lokālo Jupyter vidi

        Šī notebook darbojas lokāli, tāpēc rezultātu faili saglabājas uz diska. Jūs varat tos:

        - atvērt JupyterLab failu pārlūkā;
        - apskatīt File Explorer;
        - izmantot citās Python programmās vai nākamajās notebook šūnās.
        """,
    )

    set_cell_source(
        cells[39],
        """
        print("Rezultātu faili saglabāti mapē:")
        print(OUTPUT_DIR.resolve())

        print("\\nPilnie ceļi uz izveidotajiem failiem:")
        for path in output_files:
            print("-", path.resolve())
        """,
    )

    replace_in_all_cells(notebook, "sample_pdf_text_colab.txt", "sample_pdf_text_local.txt")
    replace_in_all_cells(notebook, "table_extract_colab.csv", "table_extract_local.csv")
    replace_in_all_cells(notebook, "scanned_document_ocr_colab.txt", "scanned_document_ocr_local.txt")
    replace_in_all_cells(notebook, "batch_summary_colab.csv", "batch_summary_local.csv")
    replace_in_all_cells(notebook, "student_workbook_pdf_analize_lv_colab.ipynb", "student_workbook_pdf_analize_lv_local.ipynb")

    notebook["metadata"] = {
        "kernelspec": {
            "display_name": ".venv (3.14.3)",
            "language": "python",
            "name": "python3",
        },
        "language_info": {
            "codemirror_mode": {"name": "ipython", "version": 3},
            "file_extension": ".py",
            "mimetype": "text/x-python",
            "name": "python",
            "nbconvert_exporter": "python",
            "pygments_lexer": "ipython3",
            "version": "3.14.3",
        },
    }

    return notebook


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
