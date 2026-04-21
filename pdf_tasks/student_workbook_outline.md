<!-- CELL: markdown -->
# PDF dokumentu analīze ar Python

Šī piezīmju grāmata ir studentu darba versija kursa tēmai **"PDF dokumentu analīze ar Python"**.

Notebook ir veidots kā vadīts praktiskais materiāls 5 akadēmiskajām stundām:
- PDF failu struktūras iepazīšana;
- teksta ekstraktēšana ar `PyPDF2`;
- tabulu iegūšana ar `pdfplumber`;
- OCR pieeja skenētiem dokumentiem;
- batch apstrāde un mini projekts.

Darba princips:
- lasiet īsos skaidrojumus;
- pildiet `# TODO` vietas;
- saglabājiet rezultātus mapē `pdf_tasks/outputs`;
- nodarbības beigās sagatavojiet īsu secinājumu par izvēlēto pieeju.

<!-- CELL: markdown -->
## Mācību rezultāti

Pēc šī notebook izpildes students spēj:
- atšķirt digitāli ģenerētu PDF no skenēta PDF;
- atvērt PDF dokumentu un noteikt lapu skaitu;
- iegūt tekstu no PDF ar `PyPDF2`;
- izvilkt tabulas ar `pdfplumber`;
- saprast, kad jālieto OCR un kādi ir tā ierobežojumi;
- automatizēt vairāku PDF failu apstrādi mapē.

<!-- CELL: markdown -->
## 5 akadēmisko stundu plāns

### 1. ak. st. Ievads un PDF struktūra
- failu tipi;
- darba vides sagatavošana;
- pirmā PDF analīze.

### 2. ak. st. Teksta ekstraktēšana
- viena lapa;
- viss dokuments;
- teksta tīrīšana un saglabāšana.

### 3. ak. st. Tabulu ekstraktēšana
- tabulu atrašana;
- pārveide par `DataFrame`;
- eksportēšana uz `.csv`.

### 4. ak. st. OCR tehnoloģijas
- skenēts PDF;
- OCR rezultāta kvalitāte;
- salīdzinājums ar digitālu PDF.

### 5. ak. st. Batch apstrāde un mini projekts
- vairāku PDF failu apstrāde;
- rezultātu kopsavilkums;
- patstāvīgs mini projekts.

<!-- CELL: markdown -->
## 0. Sagatavošana

Pirms darba sākšanas:
- pārliecinieties, ka pieejamas bibliotēkas `PyPDF2`, `pdfplumber`, `pandas`;
- OCR sadaļai papildus vajadzīgas `pytesseract`, `pdf2image`, `Pillow`;
- lokālā Windows vidē OCR parasti vajadzīga arī atsevišķa `Tesseract OCR` instalācija.

Ieteicamā datu struktūra:
- `pdf_tasks/digital_text.pdf`
- `pdf_tasks/table_report.pdf`
- `pdf_tasks/scanned_document.pdf`
- `pdf_tasks/scanned_document_page1.png`
- `pdf_tasks/batch/`

<!-- CELL: code -->
## Ja vajag, atkomentējiet šo rindu bibliotēku uzstādīšanai Jupyter vidē.
## !pip install PyPDF2 pdfplumber pandas pytesseract pdf2image pillow

<!-- CELL: code -->
from __future__ import annotations

from collections import Counter
from pathlib import Path
import re
import shutil

import pandas as pd

from IPython.display import Markdown, display

try:
    from PyPDF2 import PdfReader
except ImportError:
    PdfReader = None

try:
    import pdfplumber
except ImportError:
    pdfplumber = None

try:
    import pytesseract
except ImportError:
    pytesseract = None

try:
    from pdf2image import convert_from_path
except ImportError:
    convert_from_path = None

try:
    from PIL import Image
except ImportError:
    Image = None

<!-- CELL: code -->
PDF_ROOT = Path("pdf_tasks")
OUTPUT_DIR = PDF_ROOT / "outputs"
BATCH_DIR = PDF_ROOT / "batch"
SCANNED_IMAGE_FALLBACK = PDF_ROOT / "scanned_document_page1.png"

PDF_ROOT.mkdir(parents=True, exist_ok=True)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
BATCH_DIR.mkdir(parents=True, exist_ok=True)

pdf_files = sorted(PDF_ROOT.glob("*.pdf"))

print(f"PDF faili mapē {PDF_ROOT}: {len(pdf_files)}")
for path in pdf_files:
    print("-", path.name)

<!-- CELL: markdown -->
## 1. Palīgfunkcijas

Šajā sadaļā ir sagataves funkcijām, kuras izmantosiet vairākās nodaļās. Daļu varat lietot uzreiz, bet pie dažām ir atstātas `# TODO` vietas, lai papildinātu tās nodarbības gaitā.

<!-- CELL: code -->
def normalize_text(text: str) -> str:
    """Vienkārša PDF teksta normalizācija."""
    if not text:
        return ""

    text = text.replace("\xa0", " ")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def safe_page_count(pdf_path: Path) -> int | None:
    if PdfReader is None:
        return None

    try:
        reader = PdfReader(str(pdf_path))
        return len(reader.pages)
    except Exception:
        return None


def guess_pdf_type(file_name: str) -> str:
    """Ļoti vienkārša heuristika tikai mācību nolūkiem."""
    name = file_name.lower()
    if "scan" in name or "ocr" in name:
        return "scanned"
    if "table" in name or "report" in name:
        return "table-heavy"
    return "digital-text"

<!-- CELL: markdown -->
# 1. ak. st. PDF faila atvēršana un struktūras izpēte

## Uzdevums
Izvēlieties vienu PDF failu no mapes `pdf_tasks` un:
- ielādējiet to ar `PyPDF2`;
- nosakiet lapu skaitu;
- izdrukājiet pirmo lapu numurus vai metadatus;
- mēģiniet noteikt, vai tas ir digitāls vai skenēts dokuments.

<!-- CELL: code -->
# TODO:
# 1. izvēlieties vienu PDF failu no saraksta pdf_files
# 2. piešķiriet to mainīgajam sample_pdf

sample_pdf = next((path for path in pdf_files if "digital" in path.name.lower()), pdf_files[0] if pdf_files else None)
sample_pdf

<!-- CELL: code -->
if PdfReader is None:
    print("PyPDF2 nav pieejams. Uzstādiet bibliotēku un atkārtojiet mēģinājumu.")
elif sample_pdf is None:
    print("Mapē pdf_tasks nav neviena PDF faila.")
else:
    reader = PdfReader(str(sample_pdf))
    print("Fails:", sample_pdf.name)
    print("Lapu skaits:", len(reader.pages))
    print("Minējums par tipu:", guess_pdf_type(sample_pdf.name))

    # TODO:
    # izdrukājiet papildu informāciju par dokumentu, piemēram:
    # - reader.metadata
    # - pirmo 1-2 lapu īsu priekšskatījumu

<!-- CELL: code -->
if PdfReader is None or sample_pdf is None:
    pass
else:
    # TODO:
    # izgājiet cauri lapām un izdrukājiet katras lapas kārtas numuru.
    # Papildus varat pārbaudīt, vai extract_text() atgriež saturu.
    for page_number, page in enumerate(reader.pages, start=1):
        page_text = page.extract_text() or ""
        print(f"Lapa {page_number}: teksta garums = {len(page_text)}")

<!-- CELL: markdown -->
### Kontroljautājumi

- Vai no dokumenta izdevās iegūt tekstu uzreiz?
- Vai iegūtais teksts bija labi strukturēts?
- Kā pēc rezultāta var atšķirt digitālu PDF no skenēta PDF?

<!-- CELL: markdown -->
# 2. ak. st. Teksta ekstraktēšana ar PyPDF2

## Uzdevums
No digitāla PDF dokumenta:
- iegūstiet tekstu no pirmās lapas;
- iegūstiet tekstu no visa dokumenta;
- veiciet vienkāršu teksta tīrīšanu;
- saglabājiet rezultātu `.txt` failā.

<!-- CELL: code -->
if PdfReader is None or sample_pdf is None:
    first_page_text = ""
else:
    first_page_text = reader.pages[0].extract_text() or ""

print(first_page_text[:1000])

<!-- CELL: code -->
# TODO:
# 1. iegūstiet tekstu no visām lapām
# 2. apvienojiet to vienā teksta blokā
# 3. normalizējiet tekstu ar normalize_text()

all_page_texts = []

if PdfReader is not None and sample_pdf is not None:
    for page in reader.pages:
        all_page_texts.append(page.extract_text() or "")

full_text = "\n\n".join(all_page_texts)
clean_text = normalize_text(full_text)

print(clean_text[:1500])

<!-- CELL: code -->
text_output_path = OUTPUT_DIR / "sample_pdf_text.txt"

# TODO:
# saglabājiet clean_text failā text_output_path

if clean_text:
    text_output_path.write_text(clean_text, encoding="utf-8")

print("Saglabāts:", text_output_path)

<!-- CELL: code -->
# TODO:
# Aprēķiniet biežāk sastopamos vārdus.
# Ieteikums:
# 1. pārvērtiet tekstu mazajos burtos
# 2. atdaliet vārdus ar regex
# 3. izmantojiet Counter

words = re.findall(r"[A-Za-zĀ-ž0-9]{3,}", clean_text.lower())
top_words = Counter(words).most_common(15)
top_words

<!-- CELL: markdown -->
### Starpsecinājums

Pierakstiet īsi:
- kuras kļūdas parādījās ekstraktētajā tekstā;
- vai bija problēmas ar rindkopām, atstarpēm vai diakritiskajām zīmēm;
- vai šim dokumentam `PyPDF2` pieeja ir pietiekama.

<!-- CELL: markdown -->
# 3. ak. st. Tabulu ekstraktēšana ar pdfplumber

## Uzdevums
Atrodiet PDF failu, kurā ir tabula, un:
- atveriet to ar `pdfplumber`;
- mēģiniet iegūt pirmo tabulu;
- pārveidojiet to par `pandas DataFrame`;
- iztīriet rezultātu un eksportējiet uz `.csv`.

<!-- CELL: code -->
table_candidates = [path for path in pdf_files if "table" in path.name.lower() or "report" in path.name.lower()]
table_pdf = table_candidates[0] if table_candidates else None
table_pdf

<!-- CELL: code -->
if pdfplumber is None:
    print("pdfplumber nav pieejams. Uzstādiet bibliotēku un atkārtojiet mēģinājumu.")
elif table_pdf is None:
    print("Mapē pdf_tasks nav atrasts PDF ar tabulām.")
else:
    with pdfplumber.open(table_pdf) as pdf:
        first_page = pdf.pages[0]
        extracted_table = first_page.extract_table()

    extracted_table[:5] if extracted_table else "Tabula netika atrasta"

<!-- CELL: code -->
# TODO:
# 1. pārvērtiet extracted_table par DataFrame
# 2. izmantojiet pirmo rindu kā kolonnu nosaukumus, ja tas ir piemēroti
# 3. iztīriet tukšās rindas

table_df = pd.DataFrame()

if isinstance(extracted_table, list) and extracted_table:
    header = extracted_table[0]
    rows = extracted_table[1:]
    table_df = pd.DataFrame(rows, columns=header)
    table_df = table_df.dropna(how="all")

table_df.head()

<!-- CELL: code -->
table_output_path = OUTPUT_DIR / "table_extract.csv"

# TODO:
# iztīriet kolonnu nosaukumus un saglabājiet DataFrame CSV failā

if not table_df.empty:
    table_df.columns = [str(col).strip() for col in table_df.columns]
    table_df.to_csv(table_output_path, index=False, encoding="utf-8")

print("Saglabāts:", table_output_path)

<!-- CELL: markdown -->
### Tabulu kvalitātes pārbaude

Pārbaudiet:
- vai visas kolonnas ir pareizi nosauktas;
- vai nav pazudušas rindas;
- vai nav tukšu kolonnu;
- vai tabula nav jātīra vēl papildus.

<!-- CELL: markdown -->
# 4. ak. st. OCR tehnoloģijas skenētiem PDF

## Uzdevums
Izmantojiet skenētu PDF dokumentu un:
- pārvērtiet pirmo lapu attēlā;
- mēģiniet iegūt tekstu ar OCR;
- iztīriet rezultātu;
- salīdziniet OCR tekstu ar `PyPDF2` ekstrakciju.

Svarīgi:
- šī daļa strādās tikai tad, ja OCR bibliotēkas un `Tesseract OCR` ir uzstādīts;
- ja vide vēl nav gatava, šo sadaļu var izmantot kā skolotāja demonstrāciju.

<!-- CELL: code -->
scanned_candidates = [path for path in pdf_files if "scan" in path.name.lower() or "ocr" in path.name.lower()]
scanned_pdf = scanned_candidates[0] if scanned_candidates else None
scanned_pdf

<!-- CELL: code -->
# Ja strādājat Windows vidē un Tesseract nav PATH mainīgajā,
# norādiet tā atrašanās vietu:
#
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

poppler_available = any(shutil.which(tool) for tool in ["pdftoppm", "pdftocairo"])
ocr_rendering_ready = convert_from_path is not None and poppler_available
ocr_ready = pytesseract is not None and Image is not None and (
    ocr_rendering_ready or SCANNED_IMAGE_FALLBACK.exists()
)
print("OCR bibliotēkas pieejamas:", ocr_ready)
print("Poppler rīki pieejami:", poppler_available)
print("PNG fallback pieejams:", SCANNED_IMAGE_FALLBACK.exists())

<!-- CELL: code -->
ocr_images = []

if not ocr_ready:
    print("OCR vide nav pilnībā sagatavota.")
elif ocr_rendering_ready and scanned_pdf is not None:
    # TODO:
    # pēc vajadzības norādiet poppler_path, ja convert_from_path to prasa.
    ocr_images = convert_from_path(scanned_pdf, first_page=1, last_page=1)
    display(ocr_images[0])
elif Image is not None and SCANNED_IMAGE_FALLBACK.exists():
    with Image.open(SCANNED_IMAGE_FALLBACK) as fallback_image:
        ocr_images = [fallback_image.copy()]
    print("Izmantots PNG fallback, jo Poppler nav pieejams.")
    display(ocr_images[0])
else:
    print("Nav atrasts skenēta PDF piemērs vai tā PNG fallback.")

<!-- CELL: code -->
ocr_text = ""

if ocr_ready and ocr_images:
    # TODO:
    # izmēģiniet latviešu vai angļu valodas modeli, ja tas pieejams.
    # Piemēri:
    # - pytesseract.image_to_string(ocr_images[0], lang="eng")
    # - pytesseract.image_to_string(ocr_images[0], lang="lav")
    ocr_text = pytesseract.image_to_string(ocr_images[0])

clean_ocr_text = normalize_text(ocr_text)
print(clean_ocr_text[:1500])

<!-- CELL: code -->
# TODO:
# salīdziniet OCR rezultātu ar PyPDF2 extract_text() rezultātu.
# Pierakstiet:
# - kurš variants deva vairāk teksta;
# - kurš variants bija precīzāks;
# - kādas kļūdas OCR ieviesa.

comparison = {
    "scanned_pdf_text_chars": 0,
    "ocr_text_chars": len(clean_ocr_text),
}

if PdfReader is not None and scanned_pdf is not None:
    scanned_reader = PdfReader(str(scanned_pdf))
    scanned_pdf_text = "\n\n".join(page.extract_text() or "" for page in scanned_reader.pages)
    comparison["scanned_pdf_text_chars"] = len(normalize_text(scanned_pdf_text))

comparison

<!-- CELL: markdown -->
### OCR ierobežojumi

Pierakstiet vismaz 3 novērojumus:
- kā skenējuma kvalitāte ietekmēja rezultātu;
- vai OCR sajauca rakstzīmes;
- vai saglabājās dokumenta sākotnējais izkārtojums.

<!-- CELL: markdown -->
# 5. ak. st. Batch apstrāde vairākiem PDF failiem

## Uzdevums
Izveidojiet vienkāršu darba plūsmu, kas:
- iziet cauri PDF failiem mapē `pdf_tasks/batch`;
- nosaka dokumenta tipu;
- mēģina iegūt lapu skaitu un tekstu vai tabulu;
- sagatavo kopsavilkuma tabulu.

<!-- CELL: code -->
batch_files = sorted(BATCH_DIR.glob("*.pdf"))
print(f"Batch mapē atrasti {len(batch_files)} faili.")
for path in batch_files:
    print("-", path.name)

<!-- CELL: code -->
def process_pdf_stub(pdf_path: Path) -> dict:
    """Vienkārša sagatave batch apstrādei."""
    row = {
        "file_name": pdf_path.name,
        "pdf_type_guess": guess_pdf_type(pdf_path.name),
        "page_count": safe_page_count(pdf_path),
        "text_chars": None,
        "table_rows": None,
        "status": "TODO",
        "notes": "",
    }

    # TODO:
    # 1. ja fails ir digital-text, mēģiniet iegūt teksta apjomu
    # 2. ja fails ir table-heavy, mēģiniet iegūt pirmo tabulu un rindas skaitu
    # 3. ja fails ir scanned, atzīmējiet, ka vajadzīga OCR pieeja

    return row

<!-- CELL: code -->
summary_rows = []

for pdf_path in batch_files:
    try:
        summary_rows.append(process_pdf_stub(pdf_path))
    except Exception as exc:
        summary_rows.append(
            {
                "file_name": pdf_path.name,
                "pdf_type_guess": guess_pdf_type(pdf_path.name),
                "page_count": safe_page_count(pdf_path),
                "text_chars": None,
                "table_rows": None,
                "status": "error",
                "notes": str(exc),
            }
        )

summary_df = pd.DataFrame(summary_rows)
summary_df

<!-- CELL: code -->
batch_output_path = OUTPUT_DIR / "batch_summary.csv"

# TODO:
# papildiniet summary_df ar saviem rezultātiem un saglabājiet to CSV failā

summary_df.to_csv(batch_output_path, index=False, encoding="utf-8")
print("Saglabāts:", batch_output_path)

<!-- CELL: markdown -->
# 6. Mini projekts

## Patstāvīgais uzdevums
Izvēlieties vienu PDF dokumentu un izpildiet pilnu analīzes ciklu:
- izvēlieties piemērotāko pieeju;
- iegūstiet tekstu, tabulu vai OCR rezultātu;
- saglabājiet rezultātus;
- sagatavojiet īsu kopsavilkumu.

<!-- CELL: code -->
# TODO:
# norādiet savu mini projekta failu un izvēlēto pieeju

project_pdf = None
project_method = "text"  # "text", "table" vai "ocr"
project_notes = []

project_pdf, project_method

<!-- CELL: code -->
# TODO:
# šeit ievietojiet sava mini projekta galveno apstrādes kodu.
# Ieteikums:
# - atkārtoti izmantojiet helper funkcijas;
# - saglabājiet rezultātu OUTPUT_DIR mapē;
# - apstrādājiet kļūdas ar try/except.

project_result = {
    "file_name": getattr(project_pdf, "name", None),
    "method": project_method,
    "output_file": None,
    "status": "TODO",
}

project_result

<!-- CELL: markdown -->
## Iesniedzamie rezultāti

Nodarbības beigās studentam vajadzētu būt vismaz:
- vienam `.txt` failam ar ekstraktētu tekstu;
- vienam `.csv` failam ar tabulu vai batch kopsavilkumu;
- īsam secinājumu aprakstam par izvēlēto pieeju un rezultātu kvalitāti.

<!-- CELL: markdown -->
## Noslēguma refleksija

Atbildiet īsi uz jautājumiem:
1. Kad pietiek ar `PyPDF2`, un kad tas vairs nav pietiekami?
2. Kādas priekšrocības darbā ar tabulām dod `pdfplumber`?
3. Kādi ir galvenie OCR ierobežojumi?
4. Kā batch apstrāde palīdz reālā darbā ar dokumentiem?
5. Kuru pieeju jūs izvēlētos savam mini projektam un kāpēc?
