# Exercise 13 - Capstone Task (Beginner)

## Goal

Build a complete mini-automation project that combines the earlier VBA skills into one practical "One-Click Monthly Report" solution.

---

## Part A - Understand the Assignment

### 1. Review the capstone requirements

Create a macro that:

* copies raw data
* cleans it
* sorts by `Sales`
* generates a report
* asks for a report title
* adds a timestamp
* shows a completion message

This is the final exercise because it combines multiple earlier ideas into one end-to-end workflow.

---

### 2. Check the worksheet names

Make sure your workbook contains:

* `RawData`
* `CleanData`
* `Report`

These names must match the code.

---

## Part B - Prepare the Building Blocks

### 3. Confirm the earlier macros

This capstone becomes much easier if you already have working versions of:

* `CopyData`
* `CleanData`
* `SortData`
* `GenerateReport`
* `ReportWithInput`

If one of these does not exist yet, create or fix it first.

---

### 4. Decide how the workflow should run

A practical sequence is:

1. copy raw data
2. clean the copied data
3. sort the cleaned data
4. generate the report structure
5. ask the user for a report title
6. write the custom title into the report
7. show a completion message

This is a useful moment to think about workflow order, not just code syntax.

---

## Part C - Create the Capstone Macro

### 5. Open the VBA Editor

* Press **Alt + F11**

---

### 6. Insert a module if needed

In the VBA Editor:

1. Select your workbook
2. Click **Insert -> Module**

---

### 7. Type a complete capstone version

One possible solution is:

```vba
Sub MonthlyReport()

    Dim title As String

    Call CopyData
    Call CleanData
    Call SortData
    Call GenerateReport

    title = InputBox("Enter report title")
    Worksheets("Report").Range("A1").Value = title
    Worksheets("Report").Range("A2").Value = "Generated: " & Now

    MsgBox "Report completed!"

End Sub
```

---

### 8. Read the capstone logic

This macro:

* runs the core data workflow
* asks the user for a custom report title
* updates the report heading
* refreshes the timestamp
* shows a completion message

This is a compact example of a real automation flow.

---

## Part D - Run the Capstone

### 9. Save the workbook

Save as:

* `.xlsm`

---

### 10. Run `MonthlyReport`

In the VBA Editor:

* click inside the procedure
* press **F5**

Or in Excel:

1. Go to **Developer -> Macros**
2. Select `MonthlyReport`
3. Click **Run**

---

### 11. Enter a report title

When prompted, enter something like:

* `April Sales Overview`

Click **OK**.

---

### 12. Check the final result

Inspect the workbook after the macro finishes.

You should see:

* cleaned and sorted data in `CleanData`
* a report sheet with your chosen title
* a timestamp in `Report`
* a completion message box

---

## Expected Result

One macro performs the complete reporting process from raw data to finished output.

---

## Part E - Conceptual Layer

This capstone exercise is important because it brings together the main beginner VBA patterns from the course:

* direct worksheet references
* copying data between sheets
* cleaning data
* sorting data
* generating reports
* collecting user input
* combining procedures into one workflow

That means this is not just another macro. It is a small automation system.

Why this matters:

* it resembles a real office task
* it shows how separate ideas fit together
* it demonstrates the value of automation clearly

Key insight:

> The real power of VBA appears when small procedures are combined into a complete repeatable workflow.

---

## Part F - Alternative Design Discussion

### 13. Use existing macros versus writing everything inline

There are two reasonable capstone styles.

Style A:

* call earlier macros such as `CopyData`, `CleanData`, and `GenerateReport`

Style B:

* write one larger macro that contains all actions directly

For learning purposes, Style A is usually better because:

* each step stays easier to understand
* errors are easier to isolate
* code can be reused later

---

### 14. Think about title placement

If `GenerateReport` already writes `Sales Report` into `A1`, and the capstone later replaces it with user input, that is fine.

This is useful for discussing:

* default report titles
* user customization
* overwrite behavior

---

## Part G - Small Variations to Try

### 15. Use a default title when the user enters nothing

You can discuss or try a simple improvement:

```vba
If title = "" Then title = "Monthly Report"
```

This is a useful beginner extension.

---

### 16. Add the timestamp on a different line

Try placing the timestamp in:

```vba
Worksheets("Report").Range("A3")
```

This helps you think about layout design inside generated reports.

---

### 17. Rename the macro

You could also call it:

* `OneClickMonthlyReport`
* `RunMonthlyReport`
* `BuildReport`

This is a useful reminder that naming matters in larger projects.

---

## Part H - Troubleshooting

### 1. The capstone macro fails immediately

Cause:

* One of the earlier called macros is missing or broken

Fix:

* Test each earlier macro separately first

---

### 2. The report title is not what you expect

Cause:

* `GenerateReport` writes a default title before the user input replaces it

That is normal if your capstone overwrites cell `A1` afterward.

---

### 3. The timestamp appears to update twice

Cause:

* `GenerateReport` may write one timestamp and the capstone may write another

That is not necessarily wrong, but it is worth understanding.

---

### 4. The final output is incomplete

Cause:

* One of the earlier steps used a fixed range or incorrect sheet name

Fix:

* Review the earlier procedures one by one

---

## Part I - Key Takeaway

This capstone is the transition from isolated practice tasks to a meaningful automation workflow.

You are applying how to:

* build with multiple procedures
* coordinate worksheet operations
* gather user input
* generate a finished output
* design a repeatable one-click process

Completing this exercise means you have moved from beginner VBA actions toward basic end-to-end solution building.
