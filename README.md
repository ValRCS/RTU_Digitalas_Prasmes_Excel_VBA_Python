# RTU_Digitalas_Prasmes_Excel_VBA_Python

Materials for the RTU Digitalas Prasmes course for adult professionals, with a practical focus on Excel automation through VBA and a transition path toward Python, Jupyter Notebook, and Google Colab.

## Course Main Page

- https://digitalasprasmes.lv/danalize/

## Instructor

- Valdis Saulespurens
- Lector, Riga Technical University - Faculty of Computer Science, Information Technology and Energy
- E-mail: valdis.saulespurens at rtu.lv

## Repository Overview

The repository currently contains:

- VBA starter materials, macro modules, and completed Excel workbook examples
- Guided exercises for Excel/VBA practice
- Python notebooks for visualization and Excel-data workflows
- Python setup notes for VS Code, Jupyter Notebook, and Google Colab
- Synthetic Excel datasets for Python-based practice
- Instructor-facing notes, historical context, and slide decks
- Class-session snapshots and helper scripts

## Top-Level Structure

### Start Here

- `README.md`
  - English top-level orientation file.
- `README_LV.md`
  - Latvian top-level orientation file.
- `LICENSE`
  - MIT License for reuse and adaptation with attribution.
- `TOOLS.md`
  - Short overview of the software and services used to build the repository materials.

### Introductory Slides

- `intro_vba_excel.pdf`
  - Introductory slide deck for the Excel VBA lesson.
- `intro_vba_excel.pptx`
  - Editable PowerPoint source of the same material.

### `components/` - VBA Starter Materials

- `components/VBA_Excel_Automation_Workbook_Template.xlsm`
  - Starter workbook for importing VBA code manually.
- `components/All_Exercises_04_to_11.bas`
  - Main VBA exercise module for the workbook-based practice flow.
- `components/sort_events_monitor.bas`
  - Additional VBA example module related to event sorting and monitoring.
- `components/report.docx`
  - Supporting document used with the workbook materials.
- `components/README.md`
  - English guide for importing `.bas` modules and testing macros.
- `components/README_LV.md`
  - Latvian version of the same guide.

### `complete_workbook/` - Finished Workbook Example

- `complete_workbook/VBA_Excel_Automation_Workbook_Template_With_Macros.xlsm`
  - Completed workbook with macros already embedded.
- `complete_workbook/README.md`
  - English guide for opening, editing, and testing the completed workbook.
- `complete_workbook/README_LV.md`
  - Latvian version of the same guide.

### `exercises/` - Guided VBA Practice

- `exercises/README.md`
  - Main exercise track for Excel/VBA practice.
- `exercises/exercise_1/` to `exercises/exercise_13/`
  - Step-by-step exercises that move from introductory macro recording to more complete workflow tasks.

### `vba_guides/` - VBA Quick Reference

- `vba_guides/README.md`
  - English VBA beginner cheatsheet.
- `vba_guides/README_LV.md`
  - Latvian VBA beginner cheatsheet.
- `vba_guides/undo/README.md`
  - Additional note focused on undo-related behavior and limitations in VBA workflows.

### `history/` - Background and Context

- `history/README.md`
  - Background reading on VBA and newer automation approaches.
- `history/VBA_and_Modern_Automation.pdf`
  - Presentation version of the same topic.
- `history/VBA_and_Modern_Automation.pptx`
  - Editable PowerPoint source.

### `for_instructors/` - Instructor-Oriented Notes

- `for_instructors/README.md`
  - Instructor-facing conceptual overview of VBA, Excel's object model, teaching patterns, and common pitfalls.

### `notebooks/` - Python Notebooks and Notebook Assets

- `notebooks/README.md`
  - Notes for running notebooks locally in VS Code with `.venv`.
- `notebooks/python_vizualizacija_student_lv.ipynb`
  - Latvian student notebook for visualization practice.
- `notebooks/python_vizualizacija_student_lv_clear.ipynb`
  - Cleaner starter version of the student notebook.
- `notebooks/python_vizualizacija_teacher_lv.ipynb`
  - Latvian teacher notebook with worked examples.
- `notebooks/student_workbook_latvia_excel_datasets.ipynb`
  - Local notebook for dataset-based Excel practice.
- `notebooks/student_workbook_latvia_excel_datasets_colab.ipynb`
  - Google Colab version of the same student notebook.
- `notebooks/teacher_solution_latvia_excel_datasets.ipynb`
  - Local teacher solution notebook for the dataset workflow.
- `notebooks/teacher_solution_latvia_excel_datasets_colab.ipynb`
  - Google Colab version of the teacher solution.
- `notebooks/*.csv` and `notebooks/*.png`
  - Supporting CSV input files and generated chart examples used by the notebooks.

### `python_jupyter_colab/` - Python and Colab Introduction

- `python_jupyter_colab/README.md`
  - Introductory notes on Python, Jupyter Notebook, and Google Colab for Excel users.

### `python_vscode_setup/` - Local Python Setup

- `python_vscode_setup/README.md`
  - Setup guide for Python, Git, VS Code, extensions, and notebook work.
- `python_vscode_setup/python_vscode_setup.md`
  - Extended version of the same setup notes.

### `resources/` - Supporting Learning Notes

- `resources/python_jupyter_colab_resources_lv.md`
  - Latvian supporting notes and reference material for Python/Jupyter/Colab work.

### `latvia_gov_excel_datasets/` - Synthetic Excel Practice Data

- `latvia_gov_excel_datasets/README.txt`
  - Short description of the dataset pack.
- `latvia_gov_excel_datasets/1_budget_reports/`
- `latvia_gov_excel_datasets/2_procurement_data/`
- `latvia_gov_excel_datasets/3_employee_registry/`
- `latvia_gov_excel_datasets/4_municipality_data/`
- `latvia_gov_excel_datasets/5_mixed_quality_data/`
- `latvia_gov_excel_datasets/6_reporting_template/`
- `latvia_gov_excel_datasets/7_chart_data/`
  - Synthetic Excel files for Python-based Excel automation and analysis practice.
- `latvia_gov_excel_datasets.zip`
  - Zipped copy of the dataset pack.

### `presentations/` - Additional Slide Material

- `presentations/Grid_to_Pipeline.pdf`
  - Presentation about moving from spreadsheet-style work toward a pipeline mindset.
- `presentations/Grid_to_Pipeline.pptx`
  - Editable PowerPoint source.

### `work_in_class/` - Class Session Snapshots

- `work_in_class/README.md`
  - Top-level placeholder for class work.
- `work_in_class/work_2026_03_25_900am/`
  - Dated class session folder with VBA exercises and notes.
- `work_in_class/class250326_afternoon/`
  - Another dated class session folder with VBA modules and notes.

### `scripts/` - Helper Scripts

- `scripts/python_env_check.py`
  - Helper script for checking whether the Python environment is ready.
- `scripts/create_excel_spreadsheets.py`
  - Helper script for generating Excel spreadsheets used in practice material.

### `img/` - Repository Images

- `img/Excel_Python_Jupyter_Colab.png`
  - Supporting image used in documentation or teaching material.

### Output Folders

- `student_outputs/`
  - Reserved location for student-generated outputs during exercises.
- `teacher_outputs/`
  - Reserved location for teacher-generated outputs or reference results.

These output folders may be empty in the repository until someone runs the related exercises or notebook workflows.

## Current Repository State

- The repository now includes both a substantial VBA track and a visible Python follow-on track.
- The Excel/VBA materials remain the most structured guided path for beginners, especially through `components/`, `complete_workbook/`, `exercises/`, and `vba_guides/`.
- The Python side now includes notebook-based practice, setup notes, synthetic datasets, and local or Colab variants of the same learning flow.
- Some materials are in English, some in Latvian, and some topics have both language versions while others currently do not.

## Suggested Study Paths

### If You Are New to Excel VBA

1. Start with `intro_vba_excel.pdf`.
2. Review `vba_guides/README.md` or `vba_guides/README_LV.md`.
3. Use `components/README.md` or `components/README_LV.md` to import macros into the starter workbook.
4. Continue with `exercises/README.md` and the numbered exercise folders.
5. Inspect `complete_workbook/` after you are comfortable with the import workflow.

### If You Want to Move from VBA Toward Python

1. Start with `python_jupyter_colab/README.md`.
2. Review `python_vscode_setup/README.md` if you want a local setup.
3. Open the notebooks in `notebooks/`.
4. Use `latvia_gov_excel_datasets/` together with the student or teacher notebooks.
5. Refer to `resources/python_jupyter_colab_resources_lv.md` for extra supporting notes.

### If You Are Teaching the Course

1. Review `for_instructors/README.md`.
2. Use `history/` and `presentations/` for broader framing and lecture support.
3. Use `work_in_class/` as examples of dated session-specific material.

## Notes

- Many VBA exercises assume workbook sheets such as `RawData`, `CleanData`, `Report`, and `Playground`. Keep those names unchanged unless you are also updating the VBA code.
- Some notebooks are designed for local execution, while others are prepared specifically for Google Colab.
- Local Python work in VS Code commonly uses a project virtual environment such as `.venv`, but that environment is not part of the repository content itself.
