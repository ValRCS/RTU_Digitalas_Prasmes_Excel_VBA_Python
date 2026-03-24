# Complete Workbook with Macros inside

This workbook already has the same componenents as /components folder but the macros are already INSIDE (embedded) the workbook

Below is a **clear, procedural guide** for editing a macro, written for someone with no prior VBA experience. It focuses on *what to click, what to change, and how to verify the result*.

---

# **Editing a Macro in Excel (Step-by-Step)**

## **Step 1 — Open Your Workbook**

1. Open:

   ```
   VBA_Excel_Automation_Workbook_Template.xlsm
   ```
2. Click **Enable Content** if prompted

---

## **Step 2 — Open the VBA Editor**

Press:

```
Alt + F11
```

You will now see a new window (VBA Editor).

---

## **Step 3 — Locate the Macro**

On the left (Project Explorer), find:

```
VBAProject (VBA_Excel_Automation_Workbook_Template.xlsm)
 └── Modules
      └── All_Exercises_04_to_11
```

Click:

```
All_Exercises_04_to_11
```

On the right, you will see code.

---

## **Step 4 — Identify a Macro**

Macros look like this:

```vba
Sub WriteHello()
    Range("A1").Value = "Hello, VBA"
End Sub
```

* `Sub WriteHello()` → macro name
* `End Sub` → end of macro

Everything between them is what you can edit.

---

# **Step 5 — Make a Simple Edit**

### Example: Change the message

**Before:**

```vba
Range("A1").Value = "Hello, VBA"
```

**After:**

```vba
Range("A1").Value = "Hello, Student"
```

---

## **Step 6 — Save Changes**

Press:

```
Ctrl + S
```

---

## **Step 7 — Run the Edited Macro**

1. Go back to Excel:

   ```
   Alt + F11
   ```
2. Press:

   ```
   Alt + F8
   ```
3. Select:

   ```
   WriteHello
   ```
4. Click:

   ```
   Run
   ```

### Expected Result

Cell `A1` now shows:

```
Hello, Student
```

---

# **Second Example — Change Target Cell**

### Before:

```vba
Range("A1").Value = "Hello"
```

### After:

```vba
Range("B2").Value = "Hello"
```

**Result:** Output appears in cell `B2` instead

---

# **Third Example — Edit a Real Macro**

Find this macro:

```vba
Sub GenerateReport()
```

Change:

```vba
dst.Range("A1").Value = "Sales Report"
```

To:

```vba
dst.Range("A1").Value = "Weekly Sales Report"
```

---

# **Common Beginner Mistakes**

## 1. Editing Outside the Macro

Wrong:

```vba
Sub WriteHello()
End Sub

Range("A1").Value = "Hello"
```

✔ Always edit **between** `Sub` and `End Sub`

---

## 2. Breaking Quotes

Wrong:

```vba
Range("A1").Value = Hello
```

✔ Correct:

```vba
Range("A1").Value = "Hello"
```

---

## 3. Misspelling Sheet Names

```vba
Worksheets("Report ")
```

→ Extra space = error

---

## 4. Forgetting to Save

Changes are lost unless you press:

```
Ctrl + S
```

---

# **How to Safely Experiment (Recommended)**

Use the `Playground` sheet:

* Try edits there
* Avoid breaking main workflow macros

---

# **Optional — Step Through Code (Very Useful)**

1. Click inside a macro
2. Press:

   ```
   F8
   ```
3. Code runs **line by line**

You can see:

* what line executes
* where errors occur

---

# **Mental Model**

Editing a macro = modifying instructions Excel follows.

Think:

> “Change the steps → change the behavior”

---

# **Minimal Workflow Summary**

```
Alt+F11 → find macro → edit code → Ctrl+S → Alt+F8 → Run
```

---

# **What Students Should Practice**

* Change text output
* Change cell references
* Modify report titles
* Adjust ranges

---

# **Next Skill (Logical Progression)**

* Combine macros
* Add user input (InputBox)
* Create buttons to run macros without VBA editor

