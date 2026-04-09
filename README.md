# RTU_Digitalas_Prasmes_Excel_VBA_Python

Materials for the RTU Digitalas Prasmes course for adult professionals, with a practical focus on Excel automation through VBA and a transition path toward Python.

## Course Main Page

- https://digitalasprasmes.lv/danalize/

## Instructor

* Valdis Saulespurens
* Lector, Riga Technical University - Faculty of Computer Science, Information Technology and Energy
* E-mail valdis.saulespurens at above mentioned rtu.lv

## Contents

### Start Here

- `README.md`
  - The top-level orientation file for students who are new to the course or returning after a break.
- `README_LV.md`
  - A Latvian-language version of the same top-level orientation.
- `LICENSE`
  - The repository is shared under the MIT License, so the teaching materials and code can be reused and adapted with attribution.
- `TOOLS.md`
  - A short overview of the software and services used to build the repository materials.

### Introductory Slides and Lecture Material

- `intro_vba_excel.pdf`
  - A ready-to-read slide deck for the introductory Excel VBA lesson.
  - Best for students who want a quick conceptual overview before opening Excel.
- `intro_vba_excel.pptx`
  - The editable PowerPoint source of the same introductory material.

### `components/` - Starter Materials for Practice

- `VBA_Excel_Automation_Workbook_Template.xlsm`
  - A starter Excel workbook prepared for practice.
  - Use this version if you want to import VBA code yourself and work through the exercises step by step.
- `All_Exercises_04_to_11.bas`
  - A VBA module containing the main exercise macros currently included in the repository.
  - The macros cover writing values to sheets, copying data, cleaning data, sorting, generating a report, using `InputBox`, and running the full workflow.
- `components/README.md`
  - A beginner-oriented guide for importing the `.bas` file into Excel and testing the macros safely.
- `components/README_LV.md`
  - A Latvian-language version of the same import guide.

### `complete_workbook/` - Finished Example

- `VBA_Excel_Automation_Workbook_Template_With_Macros.xlsm`
  - A completed workbook where the VBA module is already embedded.
  - Use this version if you want to inspect, run, and modify working macros without the extra import step.
- `complete_workbook/README.md`
  - A step-by-step guide for opening the finished workbook, editing macros, and testing changes.
- `complete_workbook/README_LV.md`
  - A Latvian-language version of the same editing guide.

### `exercises/` - Guided Practice

- `exercises/README.md`
  - The main exercise track for practicing the course material from macro recording up to a small end-to-end workflow.
  - Useful if you want a more structured sequence than the standalone workbook and module files.
- `exercises/exercise_1/README.md`
  - A detailed beginner walkthrough for recording a first macro and understanding what the recorder generates.

### `notebooks/` - Python Notebooks

- `notebooks/python_vizualizacija_student_lv.ipynb`
  - Latvian student notebook for Python visualization practice.
  - Open in Google Colab: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ValRCS/RTU_Digitalas_Prasmes_Excel_VBA_Python/blob/main/notebooks/python_vizualizacija_student_lv.ipynb)
- `notebooks/python_vizualizacija_teacher_lv.ipynb`
  - Latvian teacher notebook with the corresponding worked example.
  - Open in Google Colab: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ValRCS/RTU_Digitalas_Prasmes_Excel_VBA_Python/blob/main/notebooks/python_vizualizacija_teacher_lv.ipynb)

### `vba_guides/` - Quick Reference Material

- `README.md`
  - An English-language VBA beginner cheatsheet.
  - Useful when you need a quick reminder about syntax, variables, loops, conditions, ranges, or basic automation patterns.
- `README_LV.md`
  - A Latvian-language version of the VBA beginner cheatsheet.
  - Useful for students who prefer reviewing concepts in Latvian.

### `history/` - Broader Context

- `history/README.md`
  - Background reading on the history of VBA and its place among newer Office automation technologies.
  - Useful for students who want conceptual context, not only hands-on practice.
- `history/VBA_and_Modern_Automation.pdf`
  - A presentation version of the historical and strategic overview.
- `history/VBA_and_Modern_Automation.pptx`
  - The editable PowerPoint source of the same material.

### Current Repository State

- The repository currently focuses mainly on the Excel and VBA part of the course.
- The repository now includes several types of learning material: introductory slides, workbook templates, guided exercises, quick-reference guides, and historical context material.
- The VBA exercises currently assume workbook sheets such as `RawData`, `CleanData`, `Report`, and `Playground`, so students should keep those sheet names unchanged unless they are also updating the code.
- The repository name mentions Python, but the visible materials in the current version are primarily VBA-oriented.
- Some of the newer exercise and history materials are currently documented in English only.

### Suggested Study Path

- If you are new to the course, start with `intro_vba_excel.pdf`, then review `vba_guides/`, and only then move into `exercises/` or `components/`.
- If you want a structured practice sequence, use `exercises/README.md` as the main path and refer to the workbook files when needed.
- If you are returning and want a fast refresher, open the cheatsheet in `vba_guides/` and then review the finished workbook in `complete_workbook/`.
- If you want broader context on why VBA still matters, read `history/README.md` or the related slides in `history/`.
- If you want to experiment safely, begin with simple edits such as changing output text, target cells, or report titles before modifying the full workflow.
