# Exercise 6 - Copy Data Between Sheets (Beginner)

## Goal

Automate a basic multi-sheet task by copying data from one worksheet to another with VBA.

---

## Part A - Prepare the Workbook

### 1. Check the worksheet names

Make sure your workbook contains these sheets:

* `RawData`
* `CleanData`

The macro depends on those exact names.

---

### 2. Check the source data

In `RawData`, make sure you have data in the range `A1:D10`.

Example structure:

| Name  | Department | Sales | Date       |
| ----- | ---------- | ----- | ---------- |
| Anna  | HR         | 120   | 01.01.2026 |
| John  | IT         | 300   | 02.01.2026 |
| Maria | Sales      | 250   | 03.01.2026 |

It does not have to match exactly, but the range should contain data to copy.

---

### 3. Clear the destination sheet

Open `CleanData` and remove any old content in the area where the copied data will be placed.

This makes the result easier to see.

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

### 6. Type the code

Enter this macro:

```vba
Sub CopyData()
    Worksheets("RawData").Range("A1:D10").Copy _
        Destination:=Worksheets("CleanData").Range("A1")
End Sub
```

How to read it:

* `Worksheets("RawData")` identifies the source sheet
* `.Range("A1:D10")` identifies the source range
* `.Copy` copies that range
* `Destination:=Worksheets("CleanData").Range("A1")` tells Excel where to paste it

---

## Part C - Run the Macro

### 7. Save the workbook

Save as:

* `.xlsm`

---

### 8. Run `CopyData`

You can run it in either place.

In the VBA Editor:

* click inside the procedure
* press **F5**

In Excel:

1. Go to **Developer -> Macros**
2. Select `CopyData`
3. Click **Run**

---

### 9. Check `CleanData`

Open the `CleanData` worksheet and confirm that the data from `RawData!A1:D10` now starts at:

* `CleanData!A1`

---

## Expected Result

The contents of `RawData!A1:D10` are copied into `CleanData!A1:D10`.

---

## Part D - Conceptual Layer

This is one of the first macros in the course that works across worksheets.

It introduces an important VBA pattern:

* identify a source object
* identify a destination object
* perform an action between them

Core idea:

```vba
Worksheets("RawData").Range("A1:D10").Copy _
    Destination:=Worksheets("CleanData").Range("A1")
```

Why this is useful:

* you do not need to select either sheet manually
* the code is explicit about where data comes from
* the code is explicit about where data goes

Key insight:

> Reliable VBA automation usually names both the source and the destination clearly.

---

## Part E - Small Variations to Try

### 10. Copy to a different starting cell

Try changing the destination to:

```vba
Worksheets("CleanData").Range("B2")
```

Example:

```vba
Sub CopyData()
    Worksheets("RawData").Range("A1:D10").Copy _
        Destination:=Worksheets("CleanData").Range("B2")
End Sub
```

This helps you see how the destination anchor controls the placement.

---

### 11. Copy a smaller range

Try:

```vba
Worksheets("RawData").Range("A1:B5").Copy _
    Destination:=Worksheets("CleanData").Range("A1")
```

This confirms that the copied area depends entirely on the source range you specify.

---

## Part F - Troubleshooting

### 1. Subscript out of range error

Cause:

* `RawData` or `CleanData` does not match the actual worksheet name

Fix:

* Check sheet names carefully

---

### 2. Nothing visible appears in `CleanData`

Check:

* The destination really starts at `A1`
* `RawData!A1:D10` actually contains data
* You are viewing the correct worksheet

---

### 3. Old data remains below or beside the copied area

That is normal.

This macro copies data into the target range, but it does not automatically clear everything else on the sheet.

If needed, clear `CleanData` before running the macro.

---

### 4. The workbook loses the macro after closing

Cause:

* The file was saved as `.xlsx`

Fix:

* Save as `.xlsm`

---

## Part G - Key Takeaway

This exercise introduces the basic structure of worksheet-to-worksheet automation.

You are practicing how to:

* refer to multiple worksheets explicitly
* copy structured ranges
* build repeatable workbook workflows

This pattern becomes the basis for later cleanup, sorting, and reporting exercises.
