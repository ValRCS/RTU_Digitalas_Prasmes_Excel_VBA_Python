# Exercise 10 - Add User Input (Beginner)

## Goal

Make a macro interactive by asking the user for a value and writing that value into the worksheet.

---

## Part A - Understand the Task

### 1. Review the macro idea

This exercise introduces a simple `InputBox`.

The user types a report title, and the macro writes that title into the `Report` sheet.

---

### 2. Check the worksheet name

Make sure your workbook contains a worksheet named:

* `Report`

The code uses that worksheet name directly.

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

### 5. Type the macro

Enter this code:

```vba
Sub ReportWithInput()

    Dim title As String
    title = InputBox("Enter report title")

    If title = "" Then
        title = "Sales Report"
    End If

    Worksheets("Report").Range("A1").Value = title

End Sub
```

---

### 6. Read the code step by step

This line creates a text variable:

```vba
Dim title As String
```

This line asks the user for input:

```vba
title = InputBox("Enter report title")
```

These lines provide a default title if the user leaves the box empty or clicks **Cancel**:

```vba
If title = "" Then
    title = "Sales Report"
End If
```

This line writes the entered value into the worksheet:

```vba
Worksheets("Report").Range("A1").Value = title
```

Meaning:

* ask the user to enter text
* store that text in `title`
* use `Sales Report` if no title is entered
* place it into `Report!A1`

---

## Part C - Run the Macro

### 7. Save the workbook

Save as:

* `.xlsm`

---

### 8. Run `ReportWithInput`

In the VBA Editor:

* click inside the procedure
* press **F5**

Or in Excel:

1. Go to **Developer -> Macros**
2. Select `ReportWithInput`
3. Click **Run**

---

### 9. Enter a title when prompted

When the input box appears, type something like:

* `March Sales Summary`

Then click **OK**.

---

### 10. Check the result

Open the `Report` worksheet and inspect cell `A1`.

You should see the exact title you entered.

---

## Expected Result

The macro asks for a report title and writes the user's input into `Report!A1`.

If the user enters nothing, the macro uses `Sales Report`.

---

## Part D - Conceptual Layer

This exercise is important because it makes the macro interactive.

Earlier macros used only fixed values, such as:

```vba
Range("A1").Value = "Hello, VBA"
```

Now the value comes from the user at runtime:

```vba
title = InputBox("Enter report title")
If title = "" Then
    title = "Sales Report"
End If
Worksheets("Report").Range("A1").Value = title
```

Why this matters:

* the same macro can be reused with different input
* users do not need to edit code just to change a title
* automation becomes more flexible

Key insight:

> Input boxes let a macro collect simple decisions from the user while it runs.

---

## Part E - Small Variations to Try

### 11. Use a different prompt

Try:

```vba
title = InputBox("Enter monthly report title")
```

This shows that the message displayed to the user is fully customizable.

---

### 12. Write the title to a different cell

Try:

```vba
Worksheets("Report").Range("B2").Value = title
```

This helps reinforce that the input and the target location are separate decisions.

---

### 13. Add extra text before the user input

Try:

```vba
Worksheets("Report").Range("A1").Value = "Report: " & title
```

This introduces basic string combination in VBA.

---

## Part F - Troubleshooting

### 1. Subscript out of range error

Cause:

* The worksheet `Report` does not exist or is named differently

Fix:

* Check the exact worksheet name

---

### 2. The cell stays blank

With the provided version in `All_Exercises_04_to_11.bas`, the cell should not stay blank just because the input was empty.

If the input is empty, the macro uses:

```vba
"Sales Report"
```

If the cell is blank, check whether the fallback `If title = "" Then ...` block was removed or changed.

---

### 3. The text appears in the wrong place

Cause:

* The target cell reference was changed

Fix:

* Recheck:

```vba
Worksheets("Report").Range("A1").Value = title
```

---

### 4. The macro disappears after saving

Cause:

* The workbook was saved as `.xlsx`

Fix:

* Save as `.xlsm`

---

## Part G - Key Takeaway

This exercise introduces one of the simplest forms of user interaction in VBA.

You are learning how to:

* declare a variable
* collect input with `InputBox`
* reuse that value in worksheet output

That makes your macro more flexible and prepares you for more interactive workflows later in the course.
