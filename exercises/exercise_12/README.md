# Exercise 12 - Practice Debugging (Beginner)

## Goal

Learn how to investigate a runtime error in VBA by introducing a mistake on purpose and using the editor's debugging tools to locate it.

---

## Part A - Create the Example Error

### 1. Open the VBA Editor

* Press **Alt + F11**

---

### 2. Insert a module if needed

In the VBA Editor:

1. Select your workbook
2. Click **Insert -> Module**

---

### 3. Type the test macro

Enter this code:

```vba
Sub DebugExample()
    Worksheets("WrongName").Range("A1").Value = "Test"
End Sub
```

This macro is intentionally incorrect.

The worksheet name `WrongName` should not exist in your workbook.

---

## Part B - Run the Macro and Observe the Error

### 4. Save the workbook

Save as:

* `.xlsm`

---

### 5. Run the macro

Click inside `DebugExample`, then:

* press **F5**

Or run it from:

* **Developer -> Macros**

---

### 6. Observe the error message

You should see a runtime error because VBA cannot find:

```vba
Worksheets("WrongName")
```

This is expected for the exercise.

---

## Part C - Use Debugging Tools

### 7. Click `Debug`

When Excel shows the error dialog, click:

* **Debug**

The VBA Editor should highlight the line that caused the problem.

This is one of the most important beginner debugging skills:

* identify the exact line where execution failed

---

### 8. Read the failing line carefully

Look at:

```vba
Worksheets("WrongName").Range("A1").Value = "Test"
```

Ask:

* Does this worksheet exist?
* Is the name spelled correctly?
* Is the error caused by the worksheet, the range, or the value assignment?

---

### 9. Step through code with `F8`

After fixing or rewriting the example, you can use:

* **F8**

This runs the code one line at a time.

Even in a short macro, stepping helps you understand:

* where execution currently is
* which line runs next
* where the failure begins

---

## Part D - Fix the Error

### 10. Replace the wrong worksheet name

Change:

```vba
Worksheets("WrongName").Range("A1").Value = "Test"
```

To a real sheet name, for example:

```vba
Worksheets("Report").Range("A1").Value = "Test"
```

---

### 11. Run the fixed macro again

After correcting the worksheet name:

* run the macro again

Now it should complete without the same runtime error.

---

## Expected Result

You should experience the full debugging cycle:

* run incorrect code
* receive an error
* inspect the highlighted line
* identify the mistake
* correct it
* run successfully again

---

## Part E - Conceptual Layer

Debugging is a normal part of programming.

The purpose of this exercise is not to avoid errors. It is to learn how to respond when they happen.

Common beginner VBA problems include:

* wrong worksheet names
* wrong range references
* missing objects
* typing mistakes in code

Why debugging matters:

* errors are easier to solve when you inspect the exact line
* the VBA editor gives useful clues
* stepping through code helps you understand execution flow

Key insight:

> A runtime error is not just a failure. It is a clue that points you toward the exact place the program needs attention.

---

## Part F - Small Variations to Try

### 12. Use a wrong range on a real sheet

Try experimenting with other kinds of mistakes.

For example, discuss whether this line would fail differently:

```vba
Worksheets("Report").Range("InvalidCell").Value = "Test"
```

This is useful for comparing types of errors.

---

### 13. Add a second correct line

Example:

```vba
Sub DebugExample()
    Worksheets("Report").Range("A1").Value = "Start"
    Worksheets("WrongName").Range("A1").Value = "Test"
End Sub
```

This helps show that a macro may partly run before it fails.

---

### 14. Step through with `F8` from the start

Instead of running straight to the error, press `F8` repeatedly and observe how execution moves line by line.

This is useful for building confidence in the editor.

---

## Part G - Troubleshooting

### 1. No error appears

Cause:

* A worksheet actually exists with the name `WrongName`

Fix:

* Use a different obviously incorrect sheet name

---

### 2. The editor does not highlight the line

Possible cause:

* The macro was interrupted in a different way

Fix:

* Run the macro again and choose **Debug** when the error dialog appears

---

### 3. You changed the code, but the error remains

Cause:

* The worksheet name still does not match a real sheet

Fix:

* Check the exact worksheet tab name

---

### 4. The macro disappears after reopening

Cause:

* The workbook was saved as `.xlsx`

Fix:

* Save as `.xlsm`

---

## Part H - Key Takeaway

This exercise introduces debugging as a practical skill, not just a theory topic.

You are learning how to:

* trigger and inspect a runtime error
* use the `Debug` button
* step through code with `F8`
* correct a faulty object reference

That skill will be essential for every larger VBA project you build.
