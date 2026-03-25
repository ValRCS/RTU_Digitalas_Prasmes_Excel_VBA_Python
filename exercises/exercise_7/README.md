# Exercise 7 - Clean Data (Beginner)

## Goal

Simulate a small real-world data cleanup task by modifying worksheet structure and filling a new status column with VBA.

---

## Part A - Prepare the Workbook

### 1. Check the worksheet name

Make sure your workbook contains a worksheet named exactly:

* `CleanData`

This name must match the VBA code.

---

### 2. Check the data range

Before running the macro, `CleanData` should contain sample data in roughly this layout:

| Name  | Department | Sales | Date       |
| ----- | ---------- | ----- | ---------- |
| Anna  | HR         | 120   | 01.01.2026 |
| John  | IT         | 300   | 02.01.2026 |
| Maria | Sales      | 250   | 03.01.2026 |

The important part is that:

* column `B` contains `Department`
* rows `2` to `10` contain data you can update

---

## Part B - Enter the Macro

### 3. Open the VBA Editor

* Press **Alt + F11**

---

### 4. Insert a module if needed

In the VBA Editor:

1. Select your workbook in the Project Explorer
2. Click **Insert -> Module**

---

### 5. Type the cleanup macro

Enter this code:

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

### 6. Read the code step by step

This line creates a worksheet variable:

```vba
Dim ws As Worksheet
```

This line assigns the worksheet object:

```vba
Set ws = Worksheets("CleanData")
```

These lines perform the cleanup:

```vba
ws.Columns("B").Delete
ws.Range("E1").Value = "Processed"
ws.Range("E2:E10").Value = "Yes"
```

Meaning:

* delete column `B`
* add the header `Processed` in `E1`
* fill cells `E2:E10` with `Yes`

---

## Part C - Run the Macro

### 7. Save the workbook

Save as:

* `.xlsm`

---

### 8. Run `CleanData`

You can run it in either place.

In the VBA Editor:

* click inside the procedure
* press **F5**

In Excel:

1. Go to **Developer -> Macros**
2. Select `CleanData`
3. Click **Run**

---

### 9. Check the result

Inspect the `CleanData` worksheet after the macro runs.

You should see:

* column `B` has been deleted
* `E1` contains `Processed`
* `E2:E10` contains `Yes`

---

## Expected Result

The worksheet is restructured and marked as processed:

* the `Department` column is removed
* a new status header is added
* the status values are filled automatically

---

## Part D - Conceptual Layer

This exercise introduces a more realistic automation pattern:

* use a worksheet variable
* apply multiple changes to the same worksheet
* treat the worksheet as a working object

Instead of repeating:

```vba
Worksheets("CleanData").Range("A1").Value = "..."
```

You can first assign the worksheet once:

```vba
Set ws = Worksheets("CleanData")
```

Then reuse it:

```vba
ws.Columns("B").Delete
ws.Range("E1").Value = "Processed"
ws.Range("E2:E10").Value = "Yes"
```

Why this is useful:

* the code becomes shorter
* the target worksheet stays clear
* the macro is easier to expand later

Key insight:

> Worksheet variables make repeated actions on the same sheet cleaner and easier to manage.

---

## Part E - Small Variations to Try

### 10. Change the processed text

Try:

```vba
ws.Range("E2:E10").Value = "Done"
```

This shows that the structure stays the same even when the value changes.

---

### 11. Add a different header

Try:

```vba
ws.Range("E1").Value = "Status"
```

This helps separate the idea of:

* a column header
* the values written below it

---

### 12. Write to a different range

If your cleaned data now ends in column `C` or `D` after deleting column `B`, think about whether `E` is still the best location for the new status column.

This is useful for discussing:

* fixed cell references
* layout changes after column deletion

---

## Part F - Troubleshooting

### 1. Subscript out of range error

Cause:

* The worksheet `CleanData` does not exist or is spelled differently

Fix:

* Check the exact worksheet name

---

### 2. The wrong column was deleted

Cause:

* The source layout was different from the expected layout

Fix:

* Confirm that `Department` is really in column `B` before running the macro

---

### 3. The `Processed` column seems far to the right

Cause:

* After deleting a column, the worksheet layout shifts, but the code still writes to column `E`

That is not an error in the macro. It is simply using a fixed target range.

---

### 4. Only some rows were filled

Cause:

* The code only fills `E2:E10`

Fix:

* Extend the range if your dataset is larger

Example:

```vba
ws.Range("E2:E20").Value = "Yes"
```

---

## Part G - Key Takeaway

This exercise introduces the idea of using VBA for simple data transformation rather than just formatting or copying.

You are practicing how to:

* delete worksheet content structurally
* add a new field
* populate a range with one command
* reuse a worksheet variable for multiple actions

That is an important step toward building real cleanup workflows in Excel VBA.
