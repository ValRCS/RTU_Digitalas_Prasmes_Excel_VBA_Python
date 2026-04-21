from __future__ import annotations

import json
from pathlib import Path
from textwrap import dedent


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_PATH = ROOT / "pdf_tasks" / "student_workbook_pdf_analize_lv_colab.ipynb"


def md(text: str) -> dict:
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": to_source(text),
    }


def code(text: str) -> dict:
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": to_source(text),
    }


def to_source(text: str) -> list[str]:
    text = dedent(text).strip("\n")
    if not text:
        return []
    lines = text.splitlines(keepends=True)
    if lines and not lines[-1].endswith("\n"):
        lines[-1] += "\n"
    return lines


def build_notebook() -> dict:
    cells = [
        md(
            """
            # PDF dokumentu analīze ar Python (Google Colab)

            [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ValRCS/RTU_Digitalas_Prasmes_Excel_VBA_Python/blob/main/pdf_tasks/student_workbook_pdf_analize_lv_colab.ipynb)

            Šī ir **Google Colab draudzīga** un pilnībā izpildāma studentu workbook versija tēmai **"PDF dokumentu analīze ar Python"**.

            Atšķirībā no lokālās studentu versijas, šajā notebook:

            - visas nepieciešamās bibliotēkas tiek uzstādītas Colab vidē;
            - tiek uzstādīti arī OCR rīki `Tesseract` un `Poppler`;
            - tiek automātiski lejupielādēti sagatavotie faili no repozitorija mapes `pdf_tasks`;
            - koda šūnas ir pilnībā aizpildītas un izpildāmas no sākuma līdz beigām.

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

            Google Colab šeit palīdz, jo lielu daļu no šīs tehniskās sagatavošanas var automatizēt ar dažām uzstādīšanas šūnām notebook sākumā.
            """
        ),
        md(
            """
            ## Darba plūsma Google Colab vidē

            Ieteicams izpildīt šūnas tieši šādā secībā:

            1. uzstādīt sistēmas rīkus OCR un PDF apstrādei;
            2. uzstādīt Python bibliotēkas;
            3. lejupielādēt `pdf_tasks` piemērfailus no GitHub;
            4. importēt bibliotēkas un ielādēt datus;
            5. iziet cauri sadaļām par tekstu, tabulām, OCR un batch apstrādi.

            Piezīme:

            - Colab faili glabājas tikai sesijas laikā;
            - ja vēlaties saglabāt rezultātus ārpus Colab, lejupielādējiet tos sesijas beigās.
            """
        ),
        md(
            """
            ## 0. Sistēmas rīku uzstādīšana Colab vidē

            OCR un PDF lapu renderēšanai Colab nepietiek tikai ar Python bibliotēkām.

            Šajā šūnā ar termināļa komandām tiks uzstādīti:

            - `tesseract-ocr` OCR dzinējs;
            - `tesseract-ocr-lav` latviešu valodas atbalsts;
            - `poppler-utils`, kas vajadzīgs `pdf2image`.
            """
        ),
        code(
            """
            !apt-get update -qq
            !apt-get install -y -qq tesseract-ocr tesseract-ocr-lav poppler-utils
            """
        ),
        md(
            """
            ## 1. Python bibliotēku uzstādīšana Colab vidē

            Šajā šūnā tiks uzstādītas visas notebook izmantotās Python bibliotēkas:

            - `PyPDF2`
            - `pdfplumber`
            - `pandas`
            - `pytesseract`
            - `pdf2image`
            - `Pillow`

            Ja Colab paziņo par nepieciešamu runtime restartu, palaidiet pārējās šūnas vēlreiz pēc restartēšanas.
            """
        ),
        code(
            """
            !pip install -q --disable-pip-version-check PyPDF2 pdfplumber pandas pytesseract pdf2image Pillow
            """
        ),
        md(
            """
            ## 2. Sagatavoto `pdf_tasks` failu lejupielāde no repozitorija

            Lai notebook darbotos pilnībā arī Colab vidē, šī šūna lejupielādēs visus vajadzīgos failus no GitHub:

            - galvenos PDF piemērus;
            - to salīdzināšanas/reference failus;
            - batch piemērus;
            - manifestu ar aprakstu par datu kopu.
            """
        ),
        code(
            """
            !mkdir -p pdf_tasks/batch pdf_tasks/outputs

            from pathlib import Path
            from urllib.request import urlretrieve

            BASE_RAW = "https://raw.githubusercontent.com/ValRCS/RTU_Digitalas_Prasmes_Excel_VBA_Python/main/pdf_tasks"

            ASSET_PATHS = [
                "pdf_dataset_manifest.json",
                "batch_expected_summary.csv",
                "digital_text.pdf",
                "digital_text_source.txt",
                "table_report.pdf",
                "table_report_source.csv",
                "scanned_document.pdf",
                "scanned_document_page1.png",
                "scanned_document_reference.txt",
                "batch/digital_brief.pdf",
                "batch/attendance_report.pdf",
                "batch/scan_archive_copy.pdf",
                "batch/scan_archive_copy_page1.png",
            ]

            root = Path("pdf_tasks")

            for rel_path in ASSET_PATHS:
                target = root / rel_path
                target.parent.mkdir(parents=True, exist_ok=True)
                url = f"{BASE_RAW}/{rel_path}"
                urlretrieve(url, target)
                print("Downloaded:", rel_path)
            """
        ),
        md(
            """
            ## 3. Importi un vides pārbaude

            Šajā šūnā:

            - importēsim bibliotēkas;
            - pārbaudīsim, vai notebook tiešām darbojas Google Colab vidē;
            - izdrukāsim daļu no uzstādīto rīku versijām.
            """
        ),
        code(
            """
            from __future__ import annotations

            import json
            import re
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

            IN_COLAB = "google.colab" in sys.modules

            print("Running in Colab:", IN_COLAB)
            print("Python version:", sys.version.split()[0])
            print("Tesseract path:", subprocess.run(["which", "tesseract"], capture_output=True, text=True).stdout.strip())
            print("pdftoppm path:", subprocess.run(["which", "pdftoppm"], capture_output=True, text=True).stdout.strip())
            """
        ),
        md(
            """
            ## 4. Ceļi un palīgfunkcijas

            Šeit definējam:

            - ceļus uz `pdf_tasks` failiem;
            - teksta tīrīšanas funkcijas;
            - PDF lapu skaita iegūšanu;
            - teksta ekstraktēšanu;
            - tabulu ekstraktēšanu;
            - OCR funkciju skenētiem PDF.
            """
        ),
        code(
            """
            pd.set_option("display.max_colwidth", 120)

            PDF_ROOT = Path("pdf_tasks")
            BATCH_DIR = PDF_ROOT / "batch"
            OUTPUT_DIR = PDF_ROOT / "outputs"

            MANIFEST_PATH = PDF_ROOT / "pdf_dataset_manifest.json"
            BATCH_EXPECTED_PATH = PDF_ROOT / "batch_expected_summary.csv"

            OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


            def normalize_text(text: str) -> str:
                if not text:
                    return ""
                text = text.replace("\\xa0", " ")
                text = re.sub(r"[ \\t]+", " ", text)
                text = re.sub(r"\\n{3,}", "\\n\\n", text)
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
                return normalize_text("\\n\\n".join(parts))


            def extract_text_with_pdfplumber(pdf_path: Path) -> str:
                with pdfplumber.open(pdf_path) as pdf:
                    parts = [(page.extract_text() or "") for page in pdf.pages]
                return normalize_text("\\n\\n".join(parts))


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
                    images = convert_from_path(str(pdf_path), first_page=1, last_page=1)
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
            """
        ),
        md(
            """
            ## 5. Pieejamie faili

            Apskatīsim, kādi faili tika lejupielādēti no `pdf_tasks`.
            """
        ),
        code(
            """
            print("Primary inputs:")
            for item in manifest["primary_inputs"]:
                print("-", item["path"], "| kind:", item["kind"], "| pages:", item["page_count"])

            print("\\nBatch inputs:")
            for item in manifest["batch_inputs"]:
                print("-", item["file_name"], "| kind:", item["pdf_type_guess"], "| pages:", item["page_count"])

            print("\\nManifest notes:")
            for note in manifest["notes"]:
                print("-", note)
            """
        ),
        md(
            """
            # 1. ak. st. PDF faila atvēršana un struktūras izpēte

            Šajā akadēmiskajā stundā studenti iepazīstas ar pašu PDF dokumentu kā datu avotu. Mērķis nav vēl veikt dziļu analīzi, bet saprast, kā Python redz dokumentu:

            - vai dokumentam ir vairākas lapas;
            - vai dokumentam ir teksta slānis;
            - kādu metadatu informāciju var nolasīt;
            - cik daudz teksta katrā lapā vispār ir pieejams.

            **Izmantotie rīki**

            - `PyPDF2.PdfReader` dokumenta atvēršanai;
            - `reader.pages` lapu sarakstam;
            - `reader.metadata` dokumenta metadatiem;
            - `page.extract_text()` sākotnējam teksta pārbaudījumam.

            **Ko darīs koda šūnas**

            - atvērs `digital_text.pdf`;
            - parādīs lapu skaitu un metadatus;
            - izies cauri katrai lapai;
            - parādīs, cik rakstzīmju katrā lapā iespējams iegūt.
            """
        ),
        code(
            """
            digital_pdf = get_primary_asset("digital-text")
            digital_reader = PdfReader(str(digital_pdf))

            print("Fails:", digital_pdf.name)
            print("Lapu skaits:", len(digital_reader.pages))
            print("Metadati:", digital_reader.metadata)

            for page_number, page in enumerate(digital_reader.pages, start=1):
                page_text = page.extract_text() or ""
                print(f"Lapa {page_number}: teksta garums = {len(page_text)}")
            """
        ),
        md(
            """
            ## Refleksija un dokumentācija pēc 1. ak. st.

            **Refleksijas jautājumi**

            - Kā pēc `extract_text()` rezultāta var spriest, vai PDF ir digitāli ģenerēts?
            - Kāda ir atšķirība starp lapu skaitu, metadatiem un pašu satura ekstraktēšanu?
            - Kurā brīdī būtu jāsāk domāt par OCR, nevis par parastu PDF teksta nolasīšanu?

            **Autoritatīvi avoti tālākai lasīšanai**

            - [PyPDF2 dokumentācija: sākumlapa](https://pypdf2.readthedocs.io/en/3.x/)
            - [PyPDF2 dokumentācija: metadata](https://pypdf2.readthedocs.io/en/3.0.0/user/metadata.html)
            - [pypdf dokumentācija: PdfReader klase](https://pypdf.readthedocs.io/en/stable/modules/PdfReader.html)
            """
        ),
        md(
            """
            # 2. ak. st. Teksta ekstraktēšana ar PyPDF2

            Šajā akadēmiskajā stundā fokuss ir uz teksta ieguvi no digitāli ģenerēta PDF. Šis ir tipisks scenārijs, kad dokumentā jau eksistē teksta slānis un OCR nav vajadzīgs.

            **Izmantotie rīki**

            - `page.extract_text()` vienas lapas tekstam;
            - iepriekš definētā `extract_text_with_pypdf2()` funkcija visa dokumenta tekstam;
            - `normalize_text()` vienkāršai pēcapstrādei;
            - `Counter` biežāko vārdu skaitīšanai;
            - `pandas.DataFrame` rezultātu pārskatāmam attēlojumam.

            **Ko darīs koda šūnas**

            - parādīs pirmās lapas teksta priekšskatījumu;
            - savāks tekstu no visām lapām vienā blokā;
            - iztīrīs liekās atstarpes un tukšās rindas;
            - saglabās rezultātu `.txt` failā;
            - salīdzinās iegūto tekstu ar reference tekstu;
            - aprēķinās biežāk sastopamos vārdus.
            """
        ),
        code(
            """
            first_page_text = digital_reader.pages[0].extract_text() or ""
            print(first_page_text[:1000])
            """
        ),
        code(
            """
            clean_text = extract_text_with_pypdf2(digital_pdf)
            text_output_path = OUTPUT_DIR / "sample_pdf_text_colab.txt"
            text_output_path.write_text(clean_text, encoding="utf-8")

            source_text = normalize_text((PDF_ROOT / "digital_text_source.txt").read_text(encoding="utf-8"))
            similarity_ratio = SequenceMatcher(None, clean_text.lower(), source_text.lower()).ratio()

            print("Saglabāts:", text_output_path)
            print("Iegūtā teksta garums:", len(clean_text))
            print("Reference teksta garums:", len(source_text))
            print("Līdzības koeficients:", round(similarity_ratio, 4))

            display(Markdown("### Teksta priekšskatījums"))
            print(clean_text[:1500])
            """
        ),
        code(
            """
            words = re.findall(r"[A-Za-zĀ-ž0-9]{3,}", clean_text.lower())
            top_words = pd.DataFrame(Counter(words).most_common(15), columns=["word", "count"])
            top_words
            """
        ),
        md(
            """
            ## Refleksija un dokumentācija pēc 2. ak. st.

            **Refleksijas jautājumi**

            - Vai ekstraktētais teksts pilnībā sakrita ar reference tekstu?
            - Kādas kļūdas parasti parādās PDF teksta ekstraktēšanā: rindkopas, atstarpes, secība, galvenes?
            - Kāpēc teksta pēcapstrāde ir gandrīz vienmēr vajadzīga arī digitāliem PDF?

            **Autoritatīvi avoti tālākai lasīšanai**

            - [pypdf dokumentācija: Extract Text from a PDF](https://pypdf.readthedocs.io/en/stable/user/extract-text.html)
            - [PyPDF2 dokumentācija: sākumlapa un user guide](https://pypdf2.readthedocs.io/en/3.x/)
            - [pandas dokumentācija: DataFrame.to_csv](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html)
            """
        ),
        md(
            """
            # 3. ak. st. Tabulu ekstraktēšana ar `pdfplumber`

            Šajā akadēmiskajā stundā uzsvars ir uz strukturētu datu ieguvi no PDF. Tabulas ir sarežģītākas nekā vienkāršs teksts, jo PDF formātā tabula bieži ir tikai vizuāli izkārtots saturs.

            **Izmantotie rīki**

            - `pdfplumber.open()` PDF lapu objektu apstrādei;
            - `page.extract_table()` lielākās tabulas iegūšanai;
            - `pandas.DataFrame` tabulas strukturēšanai;
            - `DataFrame.to_csv()` eksportam.

            **Ko darīs koda šūnas**

            - atvērs `table_report.pdf`;
            - mēģinās iegūt pirmo tabulu no pirmās lapas;
            - pārvērtīs tabulas datus par `DataFrame`;
            - saglabās rezultātu CSV formātā;
            - salīdzinās iegūto tabulu ar oriģinālo `table_report_source.csv`.
            """
        ),
        code(
            """
            table_pdf = get_primary_asset("table-heavy")
            extracted_table_df = extract_first_table(table_pdf)
            extracted_table_df
            """
        ),
        code(
            """
            table_output_path = OUTPUT_DIR / "table_extract_colab.csv"
            extracted_table_df.to_csv(table_output_path, index=False, encoding="utf-8")

            expected_table_df = pd.read_csv(PDF_ROOT / "table_report_source.csv")
            extracted_compare_df = extracted_table_df.astype(str).reset_index(drop=True)
            expected_compare_df = expected_table_df.astype(str).reset_index(drop=True)
            exact_match = extracted_compare_df.equals(expected_compare_df)

            print("Saglabāts:", table_output_path)
            print("Rindu skaits:", len(extracted_table_df))
            print("Kolonnu skaits:", len(extracted_table_df.columns))
            print("Sakrīt ar reference CSV:", exact_match)

            display(Markdown("### Reference CSV"))
            display(expected_table_df)
            """
        ),
        md(
            """
            ## Refleksija un dokumentācija pēc 3. ak. st.

            **Refleksijas jautājumi**

            - Vai tabula tika atrasta automātiski bez papildu parametriem?
            - Kādas problēmas būtu iespējamas reālos PDF: sapludinātas šūnas, tukšas kolonnas, nobīdīti virsraksti?
            - Kad ar `extract_table()` pietiek, un kad būtu vajadzīga dziļāka tabulas debugēšana?

            **Autoritatīvi avoti tālākai lasīšanai**

            - [pdfplumber PyPI apraksts](https://pypi.org/project/pdfplumber/)
            - [pdfplumber GitHub dokumentācija un piemēri](https://github.com/jsvine/pdfplumber)
            - [pandas dokumentācija: DataFrame.to_csv](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html)
            """
        ),
        md(
            """
            # 4. ak. st. OCR tehnoloģijas skenētiem PDF

            Šajā akadēmiskajā stundā tiek aplūkota situācija, kurā PDF satur tikai attēlu vai skenētu lapu. Šādā gadījumā parasta teksta ekstraktēšana dod maz vai neko, un jāizmanto OCR.

            **Izmantotie rīki**

            - `pdf2image.convert_from_path()` PDF lapas pārvēršanai attēlā;
            - `PIL.Image` attēla glabāšanai un attēlošanai;
            - `pytesseract.image_to_string()` teksta atpazīšanai;
            - `normalize_text()` OCR rezultāta tīrīšanai.

            **Ko darīs koda šūnas**

            - atvērs `scanned_document.pdf`;
            - pārvērtīs pirmo lapu par attēlu;
            - palaidīs OCR ar valodām `eng+lav`;
            - saglabās OCR rezultātu teksta failā;
            - salīdzinās OCR rezultātu ar reference tekstu.
            """
        ),
        code(
            """
            scanned_entry = get_primary_entry("scanned")
            scanned_pdf = PDF_ROOT / scanned_entry["path"]
            scanned_fallback = PDF_ROOT / scanned_entry["fallback_image"]

            scanned_image, clean_ocr_text = ocr_pdf_first_page(scanned_pdf, fallback_image=scanned_fallback, lang="eng+lav")

            print("Fails:", scanned_pdf.name)
            print("OCR teksta garums:", len(clean_ocr_text))
            display(scanned_image)
            """
        ),
        code(
            """
            ocr_output_path = OUTPUT_DIR / "scanned_document_ocr_colab.txt"
            ocr_output_path.write_text(clean_ocr_text, encoding="utf-8")

            scanned_reference = normalize_text((PDF_ROOT / "scanned_document_reference.txt").read_text(encoding="utf-8"))
            ocr_similarity = SequenceMatcher(None, clean_ocr_text.lower(), scanned_reference.lower()).ratio()

            print("Saglabāts:", ocr_output_path)
            print("Reference garums:", len(scanned_reference))
            print("OCR līdzība pret reference tekstu:", round(ocr_similarity, 4))

            display(Markdown("### OCR rezultāts"))
            print(clean_ocr_text)

            display(Markdown("### Reference teksts"))
            print(scanned_reference)
            """
        ),
        md(
            """
            ## Refleksija un dokumentācija pēc 4. ak. st.

            **Refleksijas jautājumi**

            - Cik labi OCR rezultāts sakrita ar reference tekstu?
            - Kā OCR kvalitāti ietekmē skenējuma kvalitāte, kontrasts un valodas modelis?
            - Kāpēc OCR ir atsevišķs solis un nevis vienkārši "tas pats, tikai PDF formātā"?

            **Autoritatīvi avoti tālākai lasīšanai**

            - [pytesseract PyPI dokumentācija](https://pypi.org/project/pytesseract/)
            - [Tesseract User Manual](https://tesseract-ocr.github.io/tessdoc/)
            - [pdf2image PyPI dokumentācija](https://pypi.org/project/pdf2image/)
            """
        ),
        md(
            """
            # 5. ak. st. Batch apstrāde vairākiem PDF failiem

            Šajā akadēmiskajā stundā tiek savienots viss iepriekš apgūtais vienā automatizētā darba plūsmā. Mērķis ir vienā ciklā apstrādāt vairākus PDF failus ar dažādu tipu saturu.

            **Izmantotie rīki**

            - `Path.glob()` failu atlasīšanai mapē;
            - `guess_pdf_type()` dokumenta tipa minēšanai;
            - `process_batch_pdf()` vienotas apstrādes funkcijai;
            - `pandas.DataFrame` kopsavilkuma tabulai;
            - `DataFrame.merge()` rezultātu salīdzināšanai ar reference aprakstu.

            **Ko darīs koda šūnas**

            - atradīs visus PDF failus mapē `pdf_tasks/batch`;
            - katram failam noteiks tipu un lapu skaitu;
            - mēģinās iegūt tekstu vai tabulas informāciju;
            - saglabās rezultātu kopsavilkuma CSV failā;
            - salīdzinās iegūtos rezultātus ar sagaidāmo `batch_expected_summary.csv`.
            """
        ),
        code(
            """
            batch_files = sorted(BATCH_DIR.glob("*.pdf"))
            summary_rows = [process_batch_pdf(path) for path in batch_files]
            summary_df = pd.DataFrame(summary_rows)

            batch_output_path = OUTPUT_DIR / "batch_summary_colab.csv"
            summary_df.to_csv(batch_output_path, index=False, encoding="utf-8")

            print("Saglabāts:", batch_output_path)
            summary_df
            """
        ),
        code(
            """
            expected_batch_df = pd.read_csv(BATCH_EXPECTED_PATH)

            comparison_df = summary_df.merge(
                expected_batch_df,
                on=["file_name", "pdf_type_guess"],
                how="left",
                suffixes=("_actual", "_expected"),
            )

            comparison_df["page_count_ok"] = comparison_df["page_count_actual"] == comparison_df["page_count_expected"]
            comparison_df["text_min_ok"] = comparison_df["text_chars"] >= comparison_df["expected_text_chars_min"]
            comparison_df["table_min_ok"] = comparison_df["table_rows"] >= comparison_df["expected_table_rows_min"]

            comparison_df[
                [
                    "file_name",
                    "pdf_type_guess",
                    "page_count_actual",
                    "page_count_expected",
                    "text_chars",
                    "expected_text_chars_min",
                    "table_rows",
                    "expected_table_rows_min",
                    "page_count_ok",
                    "text_min_ok",
                    "table_min_ok",
                ]
            ]
            """
        ),
        md(
            """
            ## Refleksija un dokumentācija pēc 5. ak. st.

            **Refleksijas jautājumi**

            - Kā batch apstrāde palīdzētu reālā biroja vai datu analīzes darbā?
            - Kādi riski parādās, ja mapē ir dažādu tipu PDF faili?
            - Kā jūs paplašinātu šo pipeline, lai tā automātiski izvēlētos arī OCR gadījumus?

            **Autoritatīvi avoti tālākai lasīšanai**

            - [Python 3.14 dokumentācija: pathlib](https://docs.python.org/3/library/pathlib.html)
            - [pandas user guide: Merge, join, concatenate and compare](https://pandas.pydata.org/docs/user_guide/merging.html)
            - [pandas API: merge](https://pandas.pydata.org/docs/reference/api/pandas.merge.html)
            """
        ),
        md(
            """
            # 6. Mini projekts ar automātisku pieejas izvēli

            Lai notebook būtu pilnībā izpildāms, šajā daļā mini projekts tiek realizēts automātiski:

            - izvēlamies vienu PDF failu;
            - nosakām piemērotāko pieeju;
            - saglabājam rezultātu;
            - izdrukājam īsu kopsavilkumu.
            """
        ),
        code(
            """
            def run_mini_project(pdf_path: Path) -> dict:
                pdf_type = guess_pdf_type(pdf_path.name)

                if pdf_type == "digital-text":
                    output_path = OUTPUT_DIR / f"{pdf_path.stem}_mini_text.txt"
                    result_text = extract_text_with_pypdf2(pdf_path)
                    output_path.write_text(result_text, encoding="utf-8")
                    return {
                        "file_name": pdf_path.name,
                        "method": "text",
                        "output_file": str(output_path),
                        "status": "done",
                        "chars": len(result_text),
                    }

                if pdf_type == "table-heavy":
                    output_path = OUTPUT_DIR / f"{pdf_path.stem}_mini_table.csv"
                    result_df = extract_first_table(pdf_path)
                    result_df.to_csv(output_path, index=False, encoding="utf-8")
                    return {
                        "file_name": pdf_path.name,
                        "method": "table",
                        "output_file": str(output_path),
                        "status": "done",
                        "rows": len(result_df),
                    }

                fallback = PDF_ROOT / "scanned_document_page1.png"
                _, result_text = ocr_pdf_first_page(pdf_path, fallback_image=fallback, lang="eng+lav")
                output_path = OUTPUT_DIR / f"{pdf_path.stem}_mini_ocr.txt"
                output_path.write_text(result_text, encoding="utf-8")
                return {
                    "file_name": pdf_path.name,
                    "method": "ocr",
                    "output_file": str(output_path),
                    "status": "done",
                    "chars": len(result_text),
                }


            project_pdf = get_primary_asset("scanned")
            project_result = run_mini_project(project_pdf)
            project_result
            """
        ),
        md(
            """
            ## Iegūtie rezultāti

            Šajā sesijā tika izveidoti rezultātu faili mapē `pdf_tasks/outputs`.

            Tie parasti ietver:

            - ekstraktēto tekstu no digitāla PDF;
            - tabulas CSV failu;
            - OCR rezultātu;
            - batch kopsavilkumu;
            - mini projekta rezultātu.
            """
        ),
        code(
            """
            output_files = sorted(OUTPUT_DIR.glob("*"))
            pd.DataFrame(
                [{"file_name": path.name, "size_bytes": path.stat().st_size} for path in output_files]
            )
            """
        ),
        md(
            """
            ## Papildu piezīme par Colab

            Colab darba vide ir īslaicīga. Ja vēlaties saglabāt izveidotos rezultātu failus lokāli, varat tos lejupielādēt.
            """
        ),
        code(
            """
            if IN_COLAB:
                from google.colab import files
                print("Lai lejupielādētu kādu failu, izmantojiet:")
                print("files.download('pdf_tasks/outputs/sample_pdf_text_colab.txt')")
                print("files.download('pdf_tasks/outputs/table_extract_colab.csv')")
                print("files.download('pdf_tasks/outputs/scanned_document_ocr_colab.txt')")
                print("files.download('pdf_tasks/outputs/batch_summary_colab.csv')")
            else:
                print("Šī lejupielādes palīdzība ir paredzēta Google Colab videi.")
            """
        ),
        md(
            """
            ## Noslēguma secinājumi

            Pēc šī notebook izpildes var secināt:

            - **digitāliem PDF** labi strādā `PyPDF2`;
            - **tabulu PDF** gadījumā noderīgs ir `pdfplumber`;
            - **skenētiem dokumentiem** vajadzīga OCR pieeja ar `pytesseract`;
            - **batch apstrāde** ļauj vienā plūsmā apstrādāt vairākus dažādu tipu dokumentus.
            """
        ),
        md(
            """
            ## Plašāka informācija un atsauces

            Ja vēlaties šo tēmu apgūt dziļāk, zemāk ir pārbaudīti un autoritatīvi resursi, kuros var lasīt vairāk par konkrētajiem rīkiem un pieejām.

            ### PDF lasīšana, struktūra un teksta ekstraktēšana

            - [PyPDF2 dokumentācija](https://pypdf2.readthedocs.io/en/3.x/)
            - [pypdf dokumentācija: Extract Text from a PDF](https://pypdf.readthedocs.io/en/stable/user/extract-text.html)
            - [pypdf dokumentācija: PdfReader klase](https://pypdf.readthedocs.io/en/stable/modules/PdfReader.html)

            ### Tabulu ekstraktēšana no PDF

            - [pdfplumber oficiālais projekts GitHub](https://github.com/jsvine/pdfplumber)
            - [pdfplumber PyPI lapa](https://pypi.org/project/pdfplumber/)

            ### OCR un skenētu dokumentu apstrāde

            - [pytesseract PyPI lapa](https://pypi.org/project/pytesseract/)
            - [Tesseract User Manual](https://tesseract-ocr.github.io/tessdoc/)
            - [pdf2image PyPI lapa](https://pypi.org/project/pdf2image/)

            ### Darbs ar datiem un rezultātu saglabāšana

            - [pandas dokumentācija: DataFrame.to_csv](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html)
            - [pandas dokumentācija: merge](https://pandas.pydata.org/docs/reference/api/pandas.merge.html)
            - [pandas user guide: Merge, join, concatenate and compare](https://pandas.pydata.org/docs/user_guide/merging.html)

            ### Failu ceļi un Python pamatbibliotēka

            - [Python 3 dokumentācija: pathlib](https://docs.python.org/3/library/pathlib.html)

            ### Ko ieteicams lasīt vispirms

            Ja mērķis ir ātri sākt praktisku darbu:

            1. izlasiet `pypdf` vai `PyPDF2` teksta ekstraktēšanas sadaļu;
            2. pēc tam apskatiet `pdfplumber` tabulu ekstraktēšanu;
            3. tad izlasiet `Tesseract` un `pytesseract` dokumentāciju OCR sadaļai;
            4. beigās nostipriniet rezultātu saglabāšanu ar `pandas`.
            """
        ),
    ]

    return {
        "cells": cells,
        "metadata": {
            "colab": {
                "name": OUTPUT_PATH.name,
                "provenance": [],
            },
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {
                "name": "python",
                "version": "3",
            },
        },
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
