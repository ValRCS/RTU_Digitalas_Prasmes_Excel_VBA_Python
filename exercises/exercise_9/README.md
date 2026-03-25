# Exercise 9 - Generate a Simple Report (Beginner)

## Goal

Produce a report worksheet automatically by clearing old output, adding report metadata, and copying cleaned data into a presentation sheet.

---

## Part A - Prepare the Workbook

### 1. Check the worksheet names

Make sure your workbook contains these worksheets:

* `CleanData`
* `Report`

The macro uses both names directly.

---

### 2. Check the source data

Before running the macro, confirm that `CleanData` contains data in:

* `A1:E10`

This will be the source range copied into the report.

---

### 3. Understand the destination sheet

The `Report` sheet will be used as an output area.

This macro will:

* clear the sheet
* place a title in `A1`
* place a timestamp in `A2`
* copy the main table starting at `A4`
* AutoFit columns `A:E` on the report

---

## Part B - Enter the Macro

### 4. Open the VBA Editor

* Press **Alt + F11**

---

### 5. Insert a module if needed

In the VBA Editor:

1. Select your workbook
2. Click **Insert -> Module**

---

### 6. Type the macro

Enter this code:

```vba
Sub GenerateReport()

    Dim src As Worksheet, dst As Worksheet

    Set src = Worksheets("CleanData")
    Set dst = Worksheets("Report")

    dst.Cells.Clear

    dst.Range("A1").Value = "Sales Report"
    dst.Range("A2").Value = "Generated: " & Now

    src.Range("A1:E10").Copy Destination:=dst.Range("A4")
    dst.Columns("A:E").AutoFit

End Sub
```

---

### 7. Read the code step by step

This line declares two worksheet variables:

```vba
Dim src As Worksheet, dst As Worksheet
```

These lines define the source and destination sheets:

```vba
Set src = Worksheets("CleanData")
Set dst = Worksheets("Report")
```

This line removes old report content:

```vba
dst.Cells.Clear
```

These lines add report header information:

```vba
dst.Range("A1").Value = "Sales Report"
dst.Range("A2").Value = "Generated: " & Now
```

This line copies the cleaned table into the report:

```vba
src.Range("A1:E10").Copy Destination:=dst.Range("A4")
```

This line adjusts the report columns:

```vba
dst.Columns("A:E").AutoFit
```

---

## Part C - Run the Macro

### 8. Save the workbook

Save as:

* `.xlsm`

---

### 9. Run `GenerateReport`

In the VBA Editor:

* click inside the procedure
* press **F5**

Or in Excel:

1. Go to **Developer -> Macros**
2. Select `GenerateReport`
3. Click **Run**

---

### 10. Check the `Report` sheet

After running the macro, inspect the `Report` worksheet.

You should see:

* `Sales Report` in cell `A1`
* a generated timestamp in `A2`
* copied data beginning at `A4`
* report columns adjusted automatically

---

## Expected Result

The `Report` sheet becomes a clean output page with:

* a title
* a timestamp
* a copied data table
* readable column widths

This gives you a basic automated reporting layout.

---

## Part D - Conceptual Layer

This exercise combines several useful VBA actions into one procedure:

* define source and destination worksheets
* clear old output
* write summary information
* copy data into a new layout

That makes it more realistic than earlier one-step macros.

Why this matters:

* reports often need a fixed structure
* output sheets should be refreshed cleanly
* automation becomes more useful when it produces a reusable result

Key insight:

> A report macro is not just about copying data. It is about preparing a complete output sheet.

---

## Part E - Small Variations to Try

### 11. Change the report title

Try:

```vba
dst.Range("A1").Value = "Monthly Sales Report"
```

This shows how the report can be customized easily.

---

### 12. Move the table lower on the sheet

Try changing:

```vba
dst.Range("A4")
```

To:

```vba
dst.Range("A6")
```

This helps you see how the destination anchor affects report layout.

---

### 13. Copy a different source range

If your cleaned data extends further down, update:

```vba
src.Range("A1:E10")
```

For example:

```vba
src.Range("A1:E20")
```

This reinforces that the copied range is fully controlled by the code.

---

## Part F - Troubleshooting

### 1. Subscript out of range error

Cause:

* `CleanData` or `Report` does not match the actual worksheet name

Fix:

* Check the exact sheet names

---

### 2. Old content disappears from `Report`

That is expected.

This line clears the sheet on purpose:

```vba
dst.Cells.Clear
```

The macro is designed to rebuild the report from scratch each time.

---

### 3. No data appears below the title

Check:

* `CleanData!A1:E10` contains data
* the copy line still points to the correct source range
* you are looking at the `Report` worksheet

---

### 4. The timestamp changes every time

That is expected.

`Now` returns the current date and time at the moment the macro runs.

---

## Part G - Key Takeaway

This exercise introduces report-building as a structured VBA task.

You are practicing how to:

* separate source and output sheets
* clear and rebuild a destination sheet
* add metadata such as a title and timestamp
* copy a prepared table into a report layout

This becomes a key part of end-to-end Excel automation.
