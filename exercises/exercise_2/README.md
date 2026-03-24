# Exercise 2 - Inspect the Generated Code (Beginner)

## Goal

Understand what Excel recorded inside your macro and recognize why recorded code often depends on the current selection.

---

## Part A - Open the VBA Editor

### 1. Open the editor

* In Excel, press **Alt + F11**

---

### 2. Find your recorded macro

* In the Project Explorer, expand your workbook
* Open **Modules**
* Find the macro named `FormatTable`

If you do not see the Project Explorer:

* Press **Ctrl + R**

---

## Part B - Read the Recorded Macro

### 3. Read the code from top to bottom

Look through the macro line by line and notice that Excel usually records very literal actions.

You may see lines similar to:

```vba
Range("A1:D10").Select
Selection.Font.Bold = True
Selection.Borders.LineStyle = xlContinuous
Selection.Columns.AutoFit
```

---

### 4. Identify lines that use `.Select`

Mark every line where Excel first selects a cell, range, row, or column.

Examples:

```vba
Range("A1:D10").Select
Rows("1:1").Select
Columns("A:D").Select
```

---

### 5. Identify lines that use `Selection`

Mark every line that applies formatting or actions to whatever is currently selected.

Examples:

```vba
Selection.Font.Bold = True
Selection.Borders.LineStyle = xlContinuous
Selection.Columns.AutoFit
```

---

## Part C - Think About Reliability

### 6. Ask what each line depends on

For every `Selection` line, ask:

* What is selected at this moment?
* Which earlier line made that selection?
* Would this still work if the wrong cell or sheet were active?

---

### 7. Predict what could go wrong

Think about these cases:

* A different range is selected before the macro runs
* The user clicks another worksheet first
* The selection changes in the middle of the macro

Key question:

> What happens if the macro expects one selection state, but Excel is currently in another?

---

### 8. Optional test

Try this carefully in Excel:

1. Select a different cell or range than before
2. Run `FormatTable`
3. Observe whether the macro still behaves exactly as expected

---

## Expected Result

You should be able to point to the fragile parts of the recorded macro and explain that:

* `.Select` changes the active selection
* `Selection` acts on whatever is currently selected
* This makes recorded macros harder to trust and reuse

---

## Part D - Conceptual Layer

Recorded macros often simulate user behavior instead of expressing intent directly.

Selection-based style:

```vba
Range("A1:D10").Select
Selection.Font.Bold = True
```

Why this is fragile:

* It depends on the active worksheet and selection state
* It is harder to read
* It is easier to break when the workbook changes

Better direction for the next exercise:

```vba
Range("A1:D10").Font.Bold = True
```

Key insight:

> Recorded macros are useful for learning, but they usually need cleanup before they become reliable code.

---

## Part E - Troubleshooting

### 1. Cannot find the macro

Check:

* The workbook was saved as `.xlsm`
* The macro was recorded in **This Workbook**
* You are looking inside **Modules**

---

### 2. Project Explorer is missing

Fix:

* Press **Ctrl + R**

---

### 3. The code looks different from the example

That is normal.

Excel records actions based on exactly what you clicked, selected, and formatted.

---

### 4. Macro does not fail, but still looks fragile

That is also normal.

Some recorded macros work in simple cases, but they remain dependent on selection state and are not robust.

---

## Part F - Key Takeaway

The purpose of this exercise is not to rewrite the macro yet.

The purpose is to notice that recorded VBA often contains:

* `.Select`
* `Selection`
* hidden dependence on the active sheet and current cursor position

This observation prepares you for the next step: removing `.Select` and writing cleaner object-based VBA.
