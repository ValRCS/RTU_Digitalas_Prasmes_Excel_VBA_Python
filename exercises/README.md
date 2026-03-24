# Excel VBA Exercises

Use this folder to practice the main Excel VBA skills from the course, from recording your first macro to building a simple automated workflow.

## Before You Start

Choose the workbook that matches how you want to study:

* If you want a ready-to-run workbook with macros already included, open [`VBA_Excel_Automation_Workbook_Template_With_Macros.xlsm`](../complete_workbook/VBA_Excel_Automation_Workbook_Template_With_Macros.xlsm).
* If you want to build the solution more manually, start with [`VBA_Excel_Automation_Workbook_Template.xlsm`](../components/VBA_Excel_Automation_Workbook_Template.xlsm).

For the first exercise, you can also follow the detailed walkthrough in [`exercise_1/README.md`](./exercise_1/README.md).

Keep these worksheet names unchanged unless you also update the VBA code:

* `RawData`
* `CleanData`
* `Report`
* `Playground`

## Workbook Setup

If you need to prepare the workbook yourself, populate `RawData` with simple sample data such as:

| Name  | Department | Sales | Date       |
| ----- | ---------- | ----- | ---------- |
| Anna  | HR         | 120   | 01.01.2026 |
| John  | IT         | 300   | 02.01.2026 |
| Maria | Sales      | 250   | 03.01.2026 |

## Exercise Path

### Exercise 1: Record Your First Macro

Goal: understand how Excel actions can be recorded as reusable VBA steps.

What to do:

1. Go to **Developer -> Record Macro**.
2. Name the macro `FormatTable`.
3. Select the table, make the headers bold, apply borders, and AutoFit the columns.
4. Stop recording.
5. Clear the formatting and run the macro again.

What you should see:

* The table is formatted automatically.

Detailed version: [`exercise_1/README.md`](./exercise_1/README.md)

### Exercise 2: Inspect the Generated Code

Goal: see what Excel recorded for you.

What to do:

1. Press **Alt + F11**.
2. Locate the `FormatTable` macro.
3. Identify lines that use `.Select` and `Selection`.
4. Ask yourself what would happen if a different range were selected before running the macro.

What you should learn:

* Recorded macros often depend on the current selection, which makes them fragile.

### Exercise 3: Remove `.Select`

Goal: replace recorded-style code with direct object references.

Original code:

```vba
Range("A1:D10").Select
Selection.Font.Bold = True
```

Rewrite it as:

```vba
Range("A1:D10").Font.Bold = True
```

What to do:

1. Replace `.Select` patterns where possible.
2. Run the macro again.

What you should see:

* The result stays the same, but the code is cleaner and more reliable.

### Exercise 4: Write Your First Custom Macro

Goal: write a simple macro from scratch.

Task:

```vba
Sub WriteHello()
    Range("A1").Value = "Hello, VBA"
End Sub
```

What to do:

1. Insert a new module.
2. Type the code manually.
3. Run the macro.

What you should see:

* Cell `A1` is updated.

### Exercise 5: Understand the Object Model

Goal: work explicitly with workbook objects instead of relying on whatever is active.

Task:

```vba
Sub WriteToSheet()
    Worksheets("CleanData").Range("A1").Value = "Processed"
End Sub
```

What to do:

1. Check that the worksheet name is exactly `CleanData`.
2. Run the macro.

What you should see:

* The value appears in `CleanData`.

### Exercise 6: Copy Data Between Sheets

Goal: automate a basic multi-sheet task.

Task:

```vba
Sub CopyData()
    Worksheets("RawData").Range("A1:D10").Copy _
        Destination:=Worksheets("CleanData").Range("A1")
End Sub
```

What to do:

1. Clear `CleanData`.
2. Run the macro.

What you should see:

* The data from `RawData` is copied into `CleanData`.

### Exercise 7: Clean Data

Goal: simulate a small real-world cleanup task.

Task:

* Delete column `B` (`Department`)
* Add the header `Processed` in column `E`
* Fill `E2:E10` with `Yes`

Example solution:

```vba
Sub CleanData()

    Dim ws As Worksheet
    Set ws = Worksheets("CleanData")

    ws.Columns("B").Delete
    ws.Range("E1").Value = "Processed"
    ws.Range("E2:E10").Value = "Yes"

End Sub
```

### Exercise 8: Sort Data

Goal: automate ordering and preparation of data.

Task:

Sort by the `Sales` column.

```vba
Sub SortData()

    Dim ws As Worksheet
    Set ws = Worksheets("CleanData")

    ws.Range("A1:D10").Sort Key1:=ws.Range("C1"), Header:=xlYes

End Sub
```

What you should see:

* The table is sorted by `Sales`.

### Exercise 9: Generate a Simple Report

Goal: produce an output sheet automatically.

Task:

* Copy cleaned data to `Report`
* Add a title
* Add a timestamp

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

### Exercise 10: Add User Input

Goal: make your macro interactive.

Task:

Ask the user for a report title.

```vba
Sub ReportWithInput()

    Dim title As String
    title = InputBox("Enter report title")

    Worksheets("Report").Range("A1").Value = title

End Sub
```

### Exercise 11: Combine the Workflow

Goal: connect several smaller macros into one larger process.

Task:

```vba
Sub FullWorkflow()

    Call CopyData
    Call CleanData
    Call SortData
    Call GenerateReport

    MsgBox "Report completed!"

End Sub
```

What you should see:

* One macro runs the full process from start to finish.

### Exercise 12: Practice Debugging

Goal: learn how to investigate runtime errors.

Task:

Introduce this error on purpose:

```vba
Worksheets("WrongName").Range("A1").Value = "Test"
```

What to do:

1. Run the macro and observe the error.
2. Use **Debug**.
3. Step through the code with **F8**.

What you should learn:

* Small mistakes such as a wrong worksheet name can break a macro, and the VBA editor helps you locate the problem.

### Exercise 13: Capstone Task

Goal: build a complete mini-automation project.

Assignment: create a "One-Click Monthly Report" macro that:

* Copies raw data
* Cleans it
* Sorts by `Sales`
* Generates a report
* Asks for a report title
* Adds a timestamp
* Shows a completion message

## How to Check Your Progress

As you work through the exercises, try to confirm that your code:

* Avoids unnecessary `.Select` and `Selection` usage
* Refers to worksheets and ranges clearly
* Still works after you rerun it
* Is readable enough that you can explain it to someone else

## Optional Stretch Exercises

If you finish early or want extra practice, try one of these:

* Loop through rows and bold sales values above 200:

```vba
For i = 2 To 10
    If Cells(i, 3).Value > 200 Then
        Cells(i, 3).Font.Bold = True
    End If
Next i
```

* Export a report to CSV
* Send a report through Outlook

## Learning Outcome

By the end of this set, you should be able to move from recording simple Excel actions to writing and combining your own VBA procedures for repeatable work.
