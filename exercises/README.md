Below is a **structured, step-by-step workbook exercise set** designed to accompany the 5-hour module. Each exercise builds incrementally, with **clear instructions, expected outcomes, and instructor notes**. The sequence assumes a single Excel workbook (`VBA_Exercises.xlsm`) with multiple sheets.

---

# **Workbook Structure (Preparation)**

Create a macro-enabled workbook with the following sheets:

* `RawData`
* `CleanData`
* `Report`
* `Playground`

Populate `RawData` with simple tabular data:

| Name  | Department | Sales | Date       |
| ----- | ---------- | ----- | ---------- |
| Anna  | HR         | 120   | 01.01.2026 |
| John  | IT         | 300   | 02.01.2026 |
| Maria | Sales      | 250   | 03.01.2026 |

---

# **Exercise 1 — Record Your First Macro (Beginner)**

**Goal:** Understand automation via recording

## Steps

1. Go to **Developer → Record Macro**
2. Name: `FormatTable`
3. Perform:

   * Select entire table
   * Make headers bold
   * Apply borders
   * AutoFit columns
4. Stop recording

## Run

* Clear formatting
* Run macro again

## Expected Result

* Table formatted automatically

## Instructor Notes

* Emphasize: “You just created code without coding”

---

# **Exercise 2 — Inspect and Understand Generated Code**

## Steps

1. Press **Alt + F11**
2. Locate `FormatTable` macro
3. Identify:

   * `.Select`
   * `Selection`

## Task

* Highlight lines that refer to selection

## Discussion Questions

* What happens if a different range is selected?
* Why is this fragile?

---

# **Exercise 3 — Remove `.Select` (Critical Skill)**

## Original Code (example)

```vba
Range("A1:D10").Select
Selection.Font.Bold = True
```

## Task

Rewrite as:

```vba
Range("A1:D10").Font.Bold = True
```

## Steps

1. Replace all `.Select` patterns
2. Run macro again

## Expected Result

* Same output, cleaner logic

## Key Insight

* Direct referencing = robust automation

---

# **Exercise 4 — Writing Your First Custom Macro**

## Goal

Write a macro from scratch

## Task

Create:

```vba
Sub WriteHello()
    Range("A1").Value = "Hello, VBA"
End Sub
```

## Steps

1. Insert new module
2. Write code manually
3. Run macro

## Expected Result

* Cell A1 updated

---

# **Exercise 5 — Understanding the Object Model**

## Goal

Use Workbook → Worksheet → Range explicitly

## Task

Write:

```vba
Sub WriteToSheet()
    Worksheets("CleanData").Range("A1").Value = "Processed"
End Sub
```

## Steps

1. Ensure correct sheet name
2. Run macro

## Expected Result

* Value appears in `CleanData`

## Instructor Emphasis

* Avoid relying on “active sheet”

---

# **Exercise 6 — Copy Data Between Sheets**

## Goal

Basic automation workflow

## Task

```vba
Sub CopyData()
    Worksheets("RawData").Range("A1:D10").Copy _
        Destination:=Worksheets("CleanData").Range("A1")
End Sub
```

## Steps

1. Clear `CleanData`
2. Run macro

## Expected Result

* Data copied

---

# **Exercise 7 — Clean Data (Real Task)**

## Goal

Simulate real administrative work

## Task

Write macro:

* Delete column B (Department)
* Add header “Processed” in column E
* Fill E2:E10 with "Yes"

## Example Solution

```vba
Sub CleanData()

    Dim ws As Worksheet
    Set ws = Worksheets("CleanData")

    ws.Columns("B").Delete
    ws.Range("E1").Value = "Processed"
    ws.Range("E2:E10").Value = "Yes"

End Sub
```

---

# **Exercise 8 — Sorting Data**

## Goal

Automate ordering

## Task

Sort by Sales column

```vba
Sub SortData()

    Dim ws As Worksheet
    Set ws = Worksheets("CleanData")

    ws.Range("A1:D10").Sort Key1:=ws.Range("C1"), Header:=xlYes

End Sub
```

## Expected Result

* Sorted by Sales

---

# **Exercise 9 — Generate a Simple Report**

## Goal

Create business output

## Task

* Copy cleaned data to `Report`
* Add title
* Add timestamp

```vba
Sub GenerateReport()

    Dim src As Worksheet, dst As Worksheet

    Set src = Worksheets("CleanData")
    Set dst = Worksheets("Report")

    dst.Cells.Clear

    dst.Range("A1").Value = "Sales Report"
    dst.Range("A2").Value = "Generated: " & Now

    src.Range("A1:D10").Copy Destination:=dst.Range("A4")

End Sub
```

---

# **Exercise 10 — User Input (Interactive VBA)**

## Goal

Add flexibility

## Task

Ask user for report title

```vba
Sub ReportWithInput()

    Dim title As String
    title = InputBox("Enter report title")

    Worksheets("Report").Range("A1").Value = title

End Sub
```

---

# **Exercise 11 — Combine into Workflow**

## Goal

Build full automation

## Task

Create macro:

```vba
Sub FullWorkflow()

    Call CopyData
    Call CleanData
    Call SortData
    Call GenerateReport

    MsgBox "Report completed!"

End Sub
```

## Expected Result

* One-click process

---

# **Exercise 12 — Debugging Practice**

## Task

Introduce error:

```vba
Worksheets("WrongName").Range("A1").Value = "Test"
```

## Steps

1. Run macro → observe error
2. Use:

   * Debug
   * Step through (F8)

## Goal

* Understand runtime errors

---

# **Exercise 13 — Capstone Task (Integrated)**

## Assignment

Create:

### “One-Click Monthly Report”

### Requirements

* Copy raw data
* Clean it
* Sort by Sales
* Generate report
* Ask for report title
* Add timestamp
* Show completion message

---

# **Instructor Control Points**

At each stage verify:

* No `.Select` usage
* Proper object referencing
* Code readability

---

# **Optional Advanced Exercises**

* Loop through rows:

```vba
For i = 2 To 10
    If Cells(i, 3).Value > 200 Then
        Cells(i, 3).Font.Bold = True
    End If
Next i
```

* Export to CSV
* Send report via Outlook

---

# **Pedagogical Progression**

| Stage | Skill                       |
| ----- | --------------------------- |
| 1–3   | Recording + cleaning macros |
| 4–6   | Writing basic VBA           |
| 7–9   | Real workflows              |
| 10–11 | Interactivity + integration |
| 12–13 | Debugging + independence    |

---

# **Key Outcome**

By completing these exercises, participants move from:

> “Excel user” → “Workflow automator”

> “I click buttons” → “I write code that clicks buttons”