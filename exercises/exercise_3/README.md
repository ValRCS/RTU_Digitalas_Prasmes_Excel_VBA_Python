# Exercise 3 - Remove `.Select` (Beginner)

## Goal

Replace recorded-style VBA with direct object references so the macro becomes cleaner, easier to read, and more reliable.

---

## Part A - Start From Recorded Code

### 1. Open the VBA Editor

* In Excel, press **Alt + F11**

---

### 2. Find the `FormatTable` macro

* In the Project Explorer, expand your workbook
* Open **Modules**
* Locate the macro you recorded earlier

---

### 3. Identify the pattern you want to remove

Recorded code often looks like this:

```vba
Range("A1:D10").Select
Selection.Font.Bold = True
```

This pattern means:

* first select a range
* then apply formatting to the current selection

---

## Part B - Rewrite the Code

### 4. Replace selection-based formatting with direct references

Rewrite:

```vba
Range("A1:D10").Select
Selection.Font.Bold = True
```

As:

```vba
Range("A1:D10").Font.Bold = True
```

This version acts directly on the range instead of changing the selection first.

---

### 5. Apply the same idea to similar lines

Look for other patterns such as:

```vba
Range("A1:D10").Select
Selection.Borders.LineStyle = xlContinuous
```

Rewrite them as:

```vba
Range("A1:D10").Borders.LineStyle = xlContinuous
```

Another example:

```vba
Columns("A:D").Select
Selection.Columns.AutoFit
```

Can often become:

```vba
Columns("A:D").AutoFit
```

---

### 6. Remove unnecessary `.Select` lines

After you rewrite a `Selection` action to act directly on the target range, the related `.Select` line is usually no longer needed.

Goal:

* keep the action
* remove the selection step

---

## Part C - Example Cleanup

### 7. Compare before and after

Before:

```vba
Range("A1:D10").Select
Selection.Font.Bold = True
Selection.Borders.LineStyle = xlContinuous
Selection.Columns.AutoFit
```

Cleaner version:

```vba
Range("A1:D10").Font.Bold = True
Range("A1:D10").Borders.LineStyle = xlContinuous
Columns("A:D").AutoFit
```

Possible improvement:

```vba
With Range("A1:D10")
    .Font.Bold = True
    .Borders.LineStyle = xlContinuous
End With

Columns("A:D").AutoFit
```

---

## Part D - Test the Macro

### 8. Save your changes

* Press **Ctrl + S**

Make sure the workbook is saved as:

* `.xlsm`

---

### 9. Run the macro again

In Excel:

1. Return to the worksheet
2. Clear the formatting if needed
3. Run `FormatTable`

---

### 10. Compare the result

Check whether the output is still the same:

* headers are bold
* borders are applied
* columns are adjusted correctly

If the result is unchanged, your cleanup worked.

---

## Expected Result

You should see the same formatted table as before, but the code should now be:

* shorter
* easier to understand
* less dependent on the active selection

---

## Part E - Conceptual Layer

Selection-based code tells Excel to behave as if a user is clicking around the workbook.

Direct-reference code tells Excel exactly which object to modify.

Selection-based style:

```vba
Range("A1:D10").Select
Selection.Font.Bold = True
```

Object-based style:

```vba
Range("A1:D10").Font.Bold = True
```

Key insight:

> Good VBA usually works by referencing workbook objects directly, not by depending on what happens to be selected.

---

## Part F - Troubleshooting

### 1. The macro no longer works

Check:

* The range reference is correct
* You did not remove a line that still served a real purpose
* The code still belongs inside the same `Sub ... End Sub` block

---

### 2. AutoFit behaves differently

That can happen if the recorded macro used a column selection first.

Try using:

```vba
Columns("A:D").AutoFit
```

Instead of:

```vba
Range("A1:D10").Columns.AutoFit
```

---

### 3. You still see some `.Select` lines

That is fine if you are not yet sure how to rewrite every case.

The goal of this exercise is to remove the obvious and unnecessary ones first.

---

### 4. The macro still depends on the active sheet

Yes. Removing `.Select` is an important improvement, but fully reliable code usually also names the worksheet explicitly.

That idea comes in later exercises.

---

## Part G - Key Takeaway

This exercise introduces your first real code cleanup step.

You are learning to:

* simplify recorded VBA
* reduce fragility
* express intent more clearly

That shift, from `Selection` to direct references, is one of the most important habits in beginner VBA.
