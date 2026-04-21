# Installation Instructions for PDF + OCR Workbook on Windows 10/11

Verified and written for **Windows 10 / Windows 11** and current as of **April 21, 2026**.

This guide installs everything needed for the materials in `pdf_tasks`, including:

- Python
- a project virtual environment
- Jupyter Notebook / JupyterLab
- PDF libraries: `PyPDF2`, `pdfplumber`, `pandas`
- OCR Python libraries: `pytesseract`, `pdf2image`, `Pillow`
- OCR system tools: **Tesseract OCR**
- PDF rendering tool required by `pdf2image`: **Poppler**

## 1. What this workbook uses

The student workbook in this folder currently uses these Python packages:

- `PyPDF2`
- `pdfplumber`
- `pandas`
- `pytesseract`
- `pdf2image`
- `Pillow`

It also needs these non-Python tools for OCR:

- `Tesseract OCR`
- `Poppler for Windows`

## 2. Windows compatibility

According to the current Python 3.14 Windows documentation, **Python 3.14 supports Windows 10 and newer**, which includes Windows 11. In practice, that makes Windows 10 and Windows 11 the right targets for this setup.

## 3. Recommended installation approach

For April 2026, the current official Python recommendation on Windows is to use the **Python Install Manager** from `python.org` or the Microsoft Store.

Recommended workflow:

1. Install Python.
2. Open PowerShell in the project root.
3. Create and activate a virtual environment.
4. Install the Python packages.
5. Install Tesseract OCR.
6. Install Poppler for Windows.
7. Verify that Python, Tesseract, and Poppler are all available.

## 4. Install Python on Windows 10/11

### Option A: Recommended official route

1. Open:
   - [python.org/downloads](https://www.python.org/downloads/)
2. Install the current **Python Install Manager**.
3. Open a new **PowerShell** window.
4. Verify:

```powershell
python --version
py --version
```

You can also list installed runtimes with:

```powershell
py list
```

### If `python` or `py` is not recognized

Close and reopen PowerShell first.

If it still does not work:

- check that Python installed correctly;
- check Windows app execution aliases;
- reinstall from `python.org`;
- use the official Python documentation troubleshooting section.

## 5. Open the project in PowerShell

Navigate to the repository root:

```powershell
cd D:\Github\RTU_Digitalas_Prasmes_Excel_VBA_Python
```

Confirm that `pdf_tasks` exists:

```powershell
Get-ChildItem .\pdf_tasks
```

## 6. Create a virtual environment

From the project root:

```powershell
python -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

After activation, you should usually see `(.venv)` at the start of your terminal prompt.

### If PowerShell blocks activation

Run this only for the current terminal session:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

### Alternative for Command Prompt

If you use `cmd.exe` instead of PowerShell:

```bat
.venv\Scripts\activate.bat
```

## 7. Upgrade pip and core packaging tools

With the virtual environment active:

```powershell
python -m pip install --upgrade pip setuptools wheel
```

Use `python -m pip` rather than plain `pip` if you want the most reliable Windows behavior.

## 8. Install Jupyter

This workbook is a `.ipynb` notebook, so install Jupyter first:

```powershell
python -m pip install jupyterlab notebook ipykernel
```

Optional check:

```powershell
python -m jupyter --version
```

## 9. Install the PDF libraries used in this workbook

Install the packages that the workbook directly depends on:

```powershell
python -m pip install PyPDF2 pdfplumber pandas
```

### Important note about `PyPDF2`

The workbook currently imports `PyPDF2`, so install it for compatibility.

However, the PyPI project page states that **PyPDF2 3.0.x is the last PyPDF2 line** and that ongoing development continues in **`pypdf`**. For new standalone projects, `pypdf` is generally the better long-term choice.

If you want to install both for experimentation:

```powershell
python -m pip install pypdf
```

## 10. Install the OCR-related Python libraries

Install OCR Python packages:

```powershell
python -m pip install pytesseract pdf2image Pillow
```

What they do:

- `pytesseract`: Python wrapper around the Tesseract OCR engine
- `pdf2image`: converts PDF pages into images
- `Pillow`: image handling required by OCR workflows

## 11. Install Tesseract OCR on Windows

### Current recommended Windows route

The Tesseract project's current installation page says that on Windows the practical standard is to use the **UB Mannheim precompiled binaries**.

Steps:

1. Open the Tesseract site:
   - [tesseractocr.org](https://tesseractocr.org/)
2. Use the Windows installer link to the UB Mannheim build.
3. Run the installer.

### Recommended install path

Unless you have a strong reason to change it, use:

```text
C:\Program Files\Tesseract-OCR
```

### During installation

If the installer allows language/component selection, select at least:

- English
- Latvian
- orientation/script detection data if offered

Language codes commonly used later in Python:

- `eng` = English
- `lav` = Latvian

### Add Tesseract to PATH

This is the most common Windows issue.

Add this folder to your system `Path`:

```text
C:\Program Files\Tesseract-OCR
```

Then fully close and reopen:

- PowerShell
- Command Prompt
- VS Code
- Jupyter server sessions

### Verify Tesseract

Open a fresh PowerShell window and run:

```powershell
tesseract --version
```

Also check that Windows can find it:

```powershell
where.exe tesseract
```

## 12. Install Poppler for Windows

`pdf2image` does not render PDFs by itself. It wraps Poppler tools such as `pdftoppm` and `pdftocairo`.

The `pdf2image` project page explicitly says that Windows users need to **build or download Poppler for Windows**, and it specifically recommends the **`oschwartz10612` Windows package**.

### Recommended route

1. Open:
   - [oschwartz10612/poppler-windows releases](https://github.com/oschwartz10612/poppler-windows/releases/)
2. Download the latest release ZIP.
3. Extract it to a stable folder, for example:

```text
C:\Tools\poppler
```

After extraction, the binaries should typically be under something like:

```text
C:\Tools\poppler\Library\bin
```

or another `bin` directory inside the extracted package.

### Add Poppler to PATH

Add the Poppler `bin` folder to your system `Path`.

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
```

And optionally:

```powershell
where.exe pdftoppm
where.exe pdftocairo
```

If those commands work, `pdf2image` should usually be able to use Poppler without extra configuration.

## 13. Optional: install language data manually

If your Tesseract installer did not include the languages you need, the official Tesseract documentation lists `.traineddata` files, including:

- `eng` for English
- `lav` for Latvian

Official language data lives in the Tesseract `tessdata`, `tessdata_fast`, and `tessdata_best` repositories.

For most teaching and notebook use, the simplest practical option is:

1. download the required `.traineddata` file;
2. place it into Tesseract's `tessdata` folder, typically:

```text
C:\Program Files\Tesseract-OCR\tessdata
```

Then test available languages:

```powershell
tesseract --list-langs
```

You should see at least:

- `eng`
- `lav` if Latvian was installed

## 14. Install everything in one go

After activating `.venv`, this single command installs all Python dependencies for the workbook:

```powershell
python -m pip install --upgrade pip setuptools wheel
python -m pip install jupyterlab notebook ipykernel PyPDF2 pdfplumber pandas pytesseract pdf2image Pillow pypdf
```

This does **not** install:

- Tesseract OCR
- Poppler

Those still need to be installed separately as Windows tools.

## 15. Quick verification checklist

With `.venv` active, run:

```powershell
python --version
python -m pip --version
python -m jupyter --version
tesseract --version
pdftoppm -h
```

Then test Python imports:

```powershell
python -c "import PyPDF2, pdfplumber, pandas, pytesseract, pdf2image, PIL; print('Python imports OK')"
```

Check OCR languages:

```powershell
python -c "import pytesseract; print(pytesseract.get_languages(config=''))"
```

## 16. Jupyter startup

From the project root, with `.venv` active:

```powershell
python -m jupyter lab
```

or:

```powershell
python -m notebook
```

Then open:

- `pdf_tasks/student_workbook_pdf_analize_lv.ipynb`

## 17. Code snippets for common Windows path issues

### If `pytesseract` cannot find Tesseract

Use an explicit path in the notebook:

```python
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

### If `pdf2image` cannot find Poppler

Pass the Poppler `bin` directory explicitly:

```python
from pdf2image import convert_from_path

images = convert_from_path(
    r"pdf_tasks\data\scanned_document.pdf",
    poppler_path=r"C:\Tools\poppler\Library\bin",
)
```

## 18. Common Windows errors and fixes

### `python` is not recognized

Fix:

- reopen PowerShell after Python install;
- verify Python Install Manager installed correctly;
- run `py --version`;
- reinstall from `python.org` if needed.

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
- add Poppler `bin` to `Path`;
- or pass `poppler_path=...` directly in Python.

### `Error opening data file ... .traineddata`

Fix:

- install the missing Tesseract language file;
- check that the file is inside the `tessdata` directory;
- run `tesseract --list-langs` to verify it is visible.

### PowerShell blocks `.ps1` activation

Fix:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

## 19. Recommended versions policy for this repo

For teaching, the safest approach is:

- use the latest stable Python 3 runtime supported by Windows 10/11;
- install packages into `.venv`;
- prefer `python -m pip`;
- keep `PyPDF2` installed because the workbook imports it;
- optionally also install `pypdf`, because it is the actively developed successor;
- keep Tesseract and Poppler installed outside Python and verify both from PowerShell before opening the notebook.

## 20. Suggested first-run smoke test

Once everything is installed, this is a good minimal test sequence:

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

If all of those work, the workbook environment is ready.

## 21. References

Primary sources used for these instructions:

- [Python: Using Python on Windows](https://docs.python.org/3/using/windows.html)
- [Python: Installing Python Modules](https://docs.python.org/3/installing/)
- [PyPI: pdfplumber](https://pypi.org/project/pdfplumber/)
- [PyPI: PyPDF2](https://pypi.org/project/PyPDF2/)
- [PyPI: pypdf](https://pypi.org/project/pypdf/)
- [PyPI: pytesseract](https://pypi.org/project/pytesseract/)
- [PyPI: pdf2image](https://pypi.org/project/pdf2image/)
- [Tesseract OCR official site](https://tesseractocr.org/)
- [Tesseract official language data documentation](https://tesseract-ocr.github.io/tessdoc/Data-Files.html)
- [Recommended Poppler for Windows package](https://github.com/oschwartz10612/poppler-windows)

## 22. Notes on interpretation

Two practical judgments in this guide are based on the current sources:

- **Inference:** because Python 3.14 officially supports Windows 10 and newer, these instructions are appropriate for both Windows 10 and Windows 11.
- **Inference:** Poppler for Windows is not a Python package, so the most reliable practical setup for `pdf2image` on Windows is to install a packaged Poppler build and either add its `bin` folder to `Path` or pass `poppler_path` explicitly.
