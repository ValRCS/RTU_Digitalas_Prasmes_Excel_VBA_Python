# Installation Instructions for PDF + OCR Libraries and Tools on Windows 10/11

Written for **Windows 10 / Windows 11** and current as of **April 21, 2026**.

This file assumes:

- **Python 3.14 is already installed**
- `python` is already available on `PATH`
- you are working in this repository:
  - `D:\Github\RTU_Digitalas_Prasmes_Excel_VBA_Python`

This guide focuses only on the setup needed for the PDF and OCR workbook in `pdf_tasks`:

- virtual environment setup for this project
- Jupyter
- PDF libraries
- OCR Python libraries
- Tesseract OCR
- Poppler for Windows
- language files
- verification and troubleshooting

## 1. What this workbook needs

The student workbook in `pdf_tasks` currently uses these Python packages:

- `PyPDF2`
- `pdfplumber`
- `pandas`
- `pytesseract`
- `pdf2image`
- `Pillow`
- `jupyterlab`
- `notebook`
- `ipykernel`

It also needs these non-Python tools:

- **Tesseract OCR**
- **Poppler for Windows**

## 2. Project folder

Open **PowerShell** and move to the repository root:

```powershell
cd D:\Github\RTU_Digitalas_Prasmes_Excel_VBA_Python
```

Confirm the `pdf_tasks` folder exists:

```powershell
Get-ChildItem .\pdf_tasks
```

## 3. Create a virtual environment

Even if Python 3.14 is already installed globally, use a project virtual environment for this workbook.

Create it:

```powershell
python -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

After activation, your prompt should usually show `(.venv)`.

### If PowerShell blocks activation

Run this for the current terminal session only:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

## 4. Upgrade packaging tools

With `.venv` active:

```powershell
python -m pip install --upgrade pip setuptools wheel
```

## 5. Install Jupyter

The workbook is a Jupyter notebook, so install Jupyter first:

```powershell
python -m pip install jupyterlab notebook ipykernel
```

Optional check:

```powershell
python -m jupyter --version
```

## 6. Install the PDF libraries

Install the PDF-related libraries used by the workbook:

```powershell
python -m pip install PyPDF2 pdfplumber pandas
```

### Note on `PyPDF2` vs `pypdf`

The workbook currently imports `PyPDF2`, so install `PyPDF2` for compatibility.

However, the PyPI project page for `PyPDF2` states that `PyPDF2 3.0.x` is the last PyPDF2 line and development continues in **`pypdf`**.

If you want the actively maintained successor available too:

```powershell
python -m pip install pypdf
```

For this workbook:

- keep `PyPDF2` installed because the notebook uses it;
- optionally install `pypdf` for newer experiments or future migration.

## 7. Install the OCR-related Python libraries

Install OCR Python packages:

```powershell
python -m pip install pytesseract pdf2image Pillow
```

What they do:

- `pytesseract`: Python wrapper around Tesseract OCR
- `pdf2image`: converts PDF pages into images
- `Pillow`: image support used by OCR workflows

## 8. Install Tesseract OCR on Windows

### Recommended Windows route

The current Tesseract installation guidance says that on Windows the practical standard is to use the **UB Mannheim precompiled binaries**.

Steps:

1. Open:
   - [tesseractocr.org](https://tesseractocr.org/)
2. Follow the Windows installer link to the UB Mannheim build.
3. Run the installer.

### Recommended install location

Use the default location unless you have a reason to change it:

```text
C:\Program Files\Tesseract-OCR
```

### During installation

If the installer offers language/component choices, install at least:

- English
- Latvian
- orientation/script detection data if offered

Useful Tesseract language codes:

- `eng`
- `lav`

### Add Tesseract to PATH

Add this folder to your Windows `Path`:

```text
C:\Program Files\Tesseract-OCR
```

Then completely restart:

- PowerShell
- Command Prompt
- VS Code
- any Jupyter server already running

### Verify Tesseract

In a fresh PowerShell window:

```powershell
tesseract --version
where.exe tesseract
```

## 9. Install Poppler for Windows

`pdf2image` requires Poppler tools such as `pdftoppm` and `pdftocairo`.

The `pdf2image` project page explicitly states that Windows users need to build or download Poppler for Windows, and it specifically recommends the **`oschwartz10612`** Windows package.

### Recommended route

1. Open:
   - [oschwartz10612/poppler-windows releases](https://github.com/oschwartz10612/poppler-windows/releases/)
2. Download the latest release ZIP.
3. Extract it to a stable location, for example:

```text
C:\Tools\poppler
```

After extraction, the Poppler executables are typically in a `bin` directory, often:

```text
C:\Tools\poppler\Library\bin
```

### Add Poppler to PATH

Add the Poppler `bin` folder to Windows `Path`.

Example:

```text
C:\Tools\poppler\Library\bin
```

Then reopen PowerShell.

### Verify Poppler

Run:

```powershell
pdftoppm -h
pdftocairo -h
where.exe pdftoppm
where.exe pdftocairo
```

If these work, `pdf2image` should usually work without extra configuration.

## 10. Optional: install language data manually

If your Tesseract installer did not include the languages you need, the official Tesseract language-data documentation lists trained data files such as:

- `eng.traineddata`
- `lav.traineddata`

Official language data is published in:

- `tessdata`
- `tessdata_fast`
- `tessdata_best`

For classroom use, the simplest practical route is:

1. download the required `.traineddata` file;
2. place it in the Tesseract `tessdata` folder, typically:

```text
C:\Program Files\Tesseract-OCR\tessdata
```

Verify installed languages:

```powershell
tesseract --list-langs
```

You should see at least:

- `eng`
- `lav` if Latvian was installed

## 11. Install everything in one go

After activating `.venv`, this command installs all required Python packages for the workbook:

```powershell
python -m pip install --upgrade pip setuptools wheel
python -m pip install jupyterlab notebook ipykernel PyPDF2 pdfplumber pandas pytesseract pdf2image Pillow pypdf
```

This command does **not** install:

- Tesseract OCR
- Poppler

Those must still be installed separately as Windows tools.

## 12. Verification checklist

With `.venv` active, run:

```powershell
python --version
python -m pip --version
python -m jupyter --version
tesseract --version
pdftoppm -h
```

Then verify Python imports:

```powershell
python -c "import PyPDF2, pdfplumber, pandas, pytesseract, pdf2image, PIL; print('Python imports OK')"
```

Check OCR language visibility:

```powershell
python -c "import pytesseract; print(pytesseract.get_languages(config=''))"
```

## 13. Start Jupyter

From the repository root, with `.venv` active:

```powershell
python -m jupyter lab
```

or:

```powershell
python -m notebook
```

Then open:

- `pdf_tasks/student_workbook_pdf_analize_lv.ipynb`

## 14. Windows path fixes in Python code

### If `pytesseract` cannot find Tesseract

Use an explicit path:

```python
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

### If `pdf2image` cannot find Poppler

Pass the Poppler `bin` folder explicitly:

```python
from pdf2image import convert_from_path

images = convert_from_path(
    r"pdf_tasks\data\scanned_document.pdf",
    poppler_path=r"C:\Tools\poppler\Library\bin",
)
```

## 15. Common Windows errors and fixes

### `pip` is not recognized

Fix:

- activate the virtual environment;
- use:

```powershell
python -m pip --version
```

instead of plain `pip`.

### `TesseractNotFoundError`

Fix:

- install Tesseract;
- add `C:\Program Files\Tesseract-OCR` to `Path`;
- reopen PowerShell and VS Code;
- or set `pytesseract.pytesseract.tesseract_cmd` explicitly.

### `PDFInfoNotInstalledError` or Poppler-related `pdf2image` errors

Fix:

- install Poppler for Windows;
- add its `bin` folder to `Path`;
- or pass `poppler_path=...` in Python.

### `Error opening data file ... .traineddata`

Fix:

- install the missing Tesseract language file;
- place it in the `tessdata` directory;
- confirm with:

```powershell
tesseract --list-langs
```

### PowerShell blocks `.ps1` activation

Fix:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

## 16. Suggested smoke test

Once everything is installed:

```powershell
cd D:\Github\RTU_Digitalas_Prasmes_Excel_VBA_Python
.\.venv\Scripts\Activate.ps1
python -c "from PyPDF2 import PdfReader; print('PyPDF2 OK')"
python -c "import pdfplumber, pandas; print('pdfplumber/pandas OK')"
python -c "import pytesseract, pdf2image, PIL; print('OCR Python libs OK')"
tesseract --version
pdftoppm -h
python -m jupyter lab
```

If all of these work, the environment is ready for the workbook.

## 17. References

Primary sources used for these instructions:

- [Python: Installing Python Modules](https://docs.python.org/3/installing/)
- [PyPI: pdfplumber](https://pypi.org/project/pdfplumber/)
- [PyPI: PyPDF2](https://pypi.org/project/PyPDF2/)
- [PyPI: pypdf](https://pypi.org/project/pypdf/)
- [PyPI: pytesseract](https://pypi.org/project/pytesseract/)
- [PyPI: pdf2image](https://pypi.org/project/pdf2image/)
- [Tesseract OCR official site](https://tesseractocr.org/)
- [Tesseract official language data documentation](https://tesseract-ocr.github.io/tessdoc/Data-Files.html)
- [Recommended Poppler for Windows package](https://github.com/oschwartz10612/poppler-windows)

## 18. Notes on interpretation

Two practical judgments in this guide are based on the sources above:

- **Inference:** because this file assumes Python 3.14 is already installed and available on `PATH`, the remaining setup should focus on virtualenv, libraries, and external OCR/PDF tooling rather than Python installation itself.
- **Inference:** on Windows, the most reliable practical setup for `pdf2image` is to install a packaged Poppler build and either add its `bin` folder to `Path` or pass `poppler_path` explicitly.
