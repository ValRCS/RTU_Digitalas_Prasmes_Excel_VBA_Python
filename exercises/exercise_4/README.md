# Exercise 4 - Write Your First Custom Macro (Beginner)

## Goal

Write a simple VBA procedure from scratch instead of relying on the macro recorder.

---

## Part A - Open the VBA Editor

### 1. Open Excel's VBA environment

* In Excel, press **Alt + F11**

---

### 2. Insert a new module

In the VBA Editor:

1. Select your workbook in the Project Explorer
2. Click **Insert -> Module**

Excel creates a new standard module where you can write your own code.

---

## Part B - Type the Macro Manually

### 3. Enter the code

Type this code exactly:

```vba
Sub WriteHello()
    Worksheets("Playground").Range("A1").Value = "Hello, VBA"
End Sub
```

What this means:

* `Sub WriteHello()` starts a macro named `WriteHello`
* `Worksheets("Playground")` identifies the target worksheet
* `.Range("A1").Value = "Hello, VBA"` writes text into cell `A1`
* `End Sub` ends the macro

---

### 4. Check the syntax carefully

Make sure:

* `Sub` is spelled correctly
* the macro name is `WriteHello`
* `Worksheets("Playground")` includes the correct sheet name
* `Range("A1")` includes quotation marks
* the text `"Hello, VBA"` also includes quotation marks

---

## Part C - Run the Macro

### 5. Save the workbook

Save as:

* `.xlsm`

If the workbook is saved as `.xlsx`, the macro code will not be preserved.

---

### 6. Run from the VBA Editor

Click anywhere inside the `WriteHello` procedure, then:

* press **F5**

Or use:

* **Run -> Run Sub/UserForm**

---

### 7. Check the worksheet

Return to Excel, open the `Playground` sheet, and inspect cell `A1`.

You should see:

* `Hello, VBA`

---

## Expected Result

Cell `A1` on the `Playground` sheet is updated automatically by your own handwritten VBA code.

---

## Part D - Conceptual Layer

This is different from the earlier recorded exercises.

Before:

* Excel generated code based on your clicks

Now:

* you write the instructions yourself

That is a major shift.

Recorded macro:

* describes actions Excel observed

Custom macro:

* expresses exactly what you want the program to do

Key insight:

> Writing even one line of VBA manually means you are no longer just recording automation. You are programming it.

---

## Part E - Small Variations to Try

### 8. Change the text

Modify the line:

```vba
Worksheets("Playground").Range("A1").Value = "Hello, VBA"
```

For example:

```vba
Worksheets("Playground").Range("A1").Value = "My first macro"
```

Run it again and observe the new result.

---

### 9. Write to another cell

Try changing `A1` to `B2`:

```vba
Worksheets("Playground").Range("B2").Value = "Hello, VBA"
```

This helps confirm that:

* `Worksheets(...)` chooses the target worksheet
* `Range(...)` chooses the target cell
* `.Value` sets the content of that cell

---

## Part F - Troubleshooting

### 1. Nothing happens when you run the macro

Check:

* The cursor is inside the `WriteHello` procedure when you press **F5**
* Macros are enabled
* You are looking at the `Playground` worksheet

---

### 2. You get a syntax error

Look for:

* missing quotation marks
* a missing or incorrect worksheet name in `Worksheets("Playground")`
* missing parentheses in `Range("A1")`
* missing `End Sub`

---

### 3. The macro disappears after reopening the file

Cause:

* The workbook was saved as `.xlsx`

Fix:

* Save as `.xlsm`

---

### 4. The value appears in the wrong place

Cause:

* The cell reference was changed accidentally
* Or the worksheet name was changed accidentally

Fix:

* Recheck `Worksheets("Playground").Range("A1")`

---

## Part G - Instructor Notes

### Core statement

> This is your first handwritten VBA procedure.

Important ideas introduced here:

* a macro is a `Sub`
* Excel worksheets can be addressed directly with `Worksheets(...)`
* Excel objects can be addressed directly with `Range(...)`
* code can modify worksheet values without any manual clicking

---

## Part H - Key Takeaway

This exercise is simple on purpose.

It establishes the core pattern used in almost all later VBA work:

* identify an object
* choose a property
* assign a value

Example:

```vba
Worksheets("Playground").Range("A1").Value = "Hello, VBA"
```

Once this pattern is clear, more advanced macros become much easier to understand and write.
