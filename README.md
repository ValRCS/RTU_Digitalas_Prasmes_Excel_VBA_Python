# RTU_Digitalas_Prasmes_Excel_VBA_Python

Materials for the RTU Digitalas Prasmes course for adult professionals, with a practical focus on Excel automation through VBA and a transition path toward Python.

## Course Main Page

- https://digitalasprasmes.lv/danalize/

## Instructor

Valdis Saulespurens
Lector, Riga Technical University - Faculty of Computer Science, Information Technology and Energy
E-mail valdis.saulespurens at above mentioned rtu.lv

## Contents

### Start Here

- `README.md`
  - The top-level orientation file for students who are new to the course or returning after a break.
- `README_LV.md`
  - A Latvian-language version of the same top-level orientation.
- `LICENSE`
  - The repository is shared under the MIT License, so the teaching materials and code can be reused and adapted with attribution.

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

### `vba_guides/` - Quick Reference Material

- `README.md`
  - An English-language VBA beginner cheatsheet.
  - Useful when you need a quick reminder about syntax, variables, loops, conditions, ranges, or basic automation patterns.
- `README_LV.md`
  - A Latvian-language version of the VBA beginner cheatsheet.
  - Useful for students who prefer reviewing concepts in Latvian.

### Current Repository State

- The repository currently focuses mainly on the Excel and VBA part of the course.
- The most complete learning materials at the moment are the workbook templates, the shared VBA module, and the English and Latvian guidance files across the repository.
- The VBA exercises currently assume workbook sheets such as `RawData`, `CleanData`, `Report`, and `Playground`, so students should keep those sheet names unchanged unless they are also updating the code.
- The repository name mentions Python, but the visible materials in the current version are primarily VBA-oriented.

### Suggested Study Path

- If you are new to the course, start with `components/` and practice importing and running the macros yourself.
- If you are returning and want a fast refresher, open the cheatsheet in `vba_guides/` and then review the finished workbook in `complete_workbook/`.
- If you want to experiment safely, begin with simple edits such as changing output text, target cells, or report titles before modifying the full workflow.
