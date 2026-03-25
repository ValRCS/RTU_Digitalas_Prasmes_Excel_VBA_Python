# Exercise 8 - Sort Data (Beginner)

## Goal

Automate the sorting of worksheet data so Excel can reorder a table by a chosen column with VBA.

---

## Part A - Prepare the Workbook

### 1. Check the worksheet name

Make sure your workbook contains a worksheet named:

* `CleanData`

The macro uses that worksheet name directly.

---

### 2. Check the data layout

Before sorting, make sure `CleanData` contains a table in the range:

* `A1:E10`

And that:

* row `1` contains headers
* the `Sales` values are in column `C`
* the `Processed` field is in column `E`

Example:

| Name  | Department | Sales | Date       |
| ----- | ---------- | ----- | ---------- |
| Anna  | HR         | 120   | 01.01.2026 |
| John  | IT         | 300   | 02.01.2026 |
| Maria | Sales      | 250   | 03.01.2026 |

---

## Part B - Enter the Macro

### 3. Open the VBA Editor

* Press **Alt + F11**

---

### 4. Insert a module if needed

In the VBA Editor:

1. Select your workbook
2. Click **Insert -> Module**

---

### 5. Type the sorting macro

Enter this code:

```vba
Sub SortData()

    Dim ws As Worksheet
    Set ws = Worksheets("CleanData")

    ws.Range("A1:E10").Sort Key1:=ws.Range("C1"), Order1:=xlAscending, Header:=xlYes

End Sub
```

---

### 6. Read the code step by step

This line stores the worksheet in a variable:

```vba
Set ws = Worksheets("CleanData")
```

This line sorts the table:

```vba
ws.Range("A1:E10").Sort Key1:=ws.Range("C1"), Order1:=xlAscending, Header:=xlYes
```

Meaning:

* sort the range `A1:E10`
* use column `C` as the key
* sort in ascending order
* treat the first row as headers

---

## Part C - Run the Macro

### 7. Save the workbook

Save as:

* `.xlsm`

---

### 8. Run `SortData`

In the VBA Editor:

* click inside the procedure
* press **F5**

Or in Excel:

1. Go to **Developer -> Macros**
2. Select `SortData`
3. Click **Run**

---

### 9. Check the result

Return to `CleanData` and inspect the table order.

You should see:

* the rows reordered by `Sales`
* the header row remaining at the top

---

## Expected Result

The table in `CleanData` is sorted by the values in the `Sales` column.

---

## Part D - Conceptual Layer

This exercise introduces a common preparation step in automation:

* take a range
* apply a sorting rule
* preserve the header row

Core code:

```vba
ws.Range("A1:E10").Sort Key1:=ws.Range("C1"), Order1:=xlAscending, Header:=xlYes
```

Important idea:

* `Key1` identifies the column Excel should use for sorting
* `Order1:=xlAscending` makes the sort order explicit
* `Header:=xlYes` tells Excel not to mix the header row into the data sort

Why this matters:

* sorted data is easier to review
* sorted data is easier to report on
* sorting is a common part of automated workflows

Key insight:

> Sorting with VBA means defining both the full table range and the exact column that controls the order.

---

## Part E - Small Variations to Try

### 10. Sort by a different column

If you want to sort by `Name` instead, try:

```vba
ws.Range("A1:E10").Sort Key1:=ws.Range("A1"), Order1:=xlAscending, Header:=xlYes
```

This shows how the sort key changes the output order.

---

### 11. Expand the range

If your dataset is larger than row `10`, update the range.

Example:

```vba
ws.Range("A1:E20").Sort Key1:=ws.Range("C1"), Order1:=xlAscending, Header:=xlYes
```

This reinforces that the macro only sorts the range you specify.

---

### 12. Observe ascending behavior

The provided solution in `All_Exercises_04_to_11.bas` sets ascending order explicitly.

That means for numeric sales values, smaller numbers appear first.

This is a useful discussion point for later improvements.

---

## Part F - Troubleshooting

### 1. The header row was sorted with the data

Cause:

* `Header:=xlYes` was removed or changed
* Or the sort range no longer includes the full table correctly

Fix:

* Keep:

```vba
Header:=xlYes
```

---

### 2. The wrong order appears

Cause:

* The key column does not match the intended field

Fix:

* Recheck whether `Sales` is really in column `C`

---

### 3. Some rows were not sorted

Cause:

* The actual table is larger than `A1:E10`

Fix:

* Expand the sorted range to cover the full dataset

---

### 4. Subscript out of range error

Cause:

* The worksheet name `CleanData` does not match the workbook

Fix:

* Check the exact sheet name

---

## Part G - Key Takeaway

This exercise introduces VBA sorting as a repeatable data-preparation step.

You are learning to:

* define a table range
* choose a sort key
* preserve headers
* automate a common spreadsheet operation

This becomes an important building block for reporting and workflow automation later in the course.
