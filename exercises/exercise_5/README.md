# Exercise 5 - Understand the Object Model (Beginner)

## Goal

Work explicitly with workbook objects instead of relying on whichever sheet or cell happens to be active.

---

## Part A - Understand the Target

### 1. Review the macro

This exercise uses the following code:

```vba
Sub WriteToSheet()
    Worksheets("CleanData").Range("A1").Value = "Processed"
End Sub
```

This macro does not depend on the current selection. It names the worksheet and the cell directly.

---

### 2. Check the worksheet name

In Excel, confirm that your workbook contains a worksheet named exactly:

* `CleanData`

This name must match the VBA code exactly.

If the sheet has a different name, either:

* rename the sheet to `CleanData`
* or update the VBA code to match the real sheet name

---

## Part B - Enter the Code

### 3. Open the VBA Editor

* In Excel, press **Alt + F11**

---

### 4. Insert a module if needed

If you do not already have a suitable module:

1. Select your workbook in the Project Explorer
2. Click **Insert -> Module**

---

### 5. Type the macro

Enter this code:

```vba
Sub WriteToSheet()
    Worksheets("CleanData").Range("A1").Value = "Processed"
End Sub
```

Read it from left to right:

* `Worksheets("CleanData")` identifies the worksheet
* `.Range("A1")` identifies the target cell
* `.Value = "Processed"` writes the value into that cell

---

## Part C - Run the Macro

### 6. Save the workbook

Save as:

* `.xlsm`

---

### 7. Run `WriteToSheet`

In the VBA Editor:

* click inside the procedure
* press **F5**

Or in Excel:

1. Go to **Developer -> Macros**
2. Select `WriteToSheet`
3. Click **Run**

---

### 8. Check the result

Open the `CleanData` worksheet and inspect cell `A1`.

You should see:

* `Processed`

---

## Expected Result

The value appears in `CleanData!A1` even if some other worksheet or cell was active before the macro started.

---

## Part D - Conceptual Layer

This exercise introduces a core VBA idea:

* Excel workbooks contain objects
* worksheets are objects
* ranges are objects
* code becomes more reliable when you refer to those objects directly

Compare these two styles.

Fragile style:

```vba
Range("A1").Value = "Processed"
```

Better style:

```vba
Worksheets("CleanData").Range("A1").Value = "Processed"
```

Why the second version is better:

* it clearly identifies the target worksheet
* it does not depend on the active sheet
* it is easier to understand later

Key insight:

> Good VBA code usually tells Excel exactly which object to use.

---

## Part E - Small Variations to Try

### 9. Write to another cell on the same sheet

Try:

```vba
Worksheets("CleanData").Range("B2").Value = "Checked"
```

This shows that you can keep the worksheet fixed and change only the target cell.

---

### 10. Write to a different worksheet

If your workbook also contains `Report`, try:

```vba
Worksheets("Report").Range("A1").Value = "Ready"
```

This helps reinforce that:

* the worksheet object can change
* the overall code pattern stays the same

---

## Part F - Troubleshooting

### 1. Subscript out of range error

Cause:

* The worksheet name in the code does not match the actual worksheet name

Fix:

* Check spelling, spaces, and capitalization in `CleanData`

---

### 2. The value appears on the wrong sheet

Cause:

* The code was edited to use a different worksheet name

Fix:

* Recheck `Worksheets("CleanData")`

---

### 3. The macro does not save

Cause:

* The workbook is stored as `.xlsx`

Fix:

* Save as `.xlsm`

---

### 4. You used `Sheet1` or `ActiveSheet` instead

That may still work in some cases, but it is less clear for beginners.

For this exercise, use:

```vba
Worksheets("CleanData").Range("A1").Value = "Processed"
```

So the target is explicit.

---

## Part G - Key Takeaway

This exercise moves you from simple cell actions toward structured Excel automation.

You are learning to think in terms of:

* workbook objects
* worksheet objects
* range objects

That object-based thinking is the foundation for writing reliable multi-sheet VBA later in the course.
