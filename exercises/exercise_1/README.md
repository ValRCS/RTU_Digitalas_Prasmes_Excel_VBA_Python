

# Exercise 1 — Record Your First Macro (Beginner)

## Goal

Understand **automation via recording** and recognize that Excel actions can be converted into **repeatable executable procedures (VBA macros)**.

---

# Part A — Setup

## 1. Enable Developer Tab

* Go to **File → Options → Customize Ribbon**
* Enable **Developer**
* Click **OK**

---

# Part B — Prepare Data

## 2. Create Example Table

| Name  | Department | Salary |
| ----- | ---------- | ------ |
| Anna  | HR         | 1200   |
| John  | IT         | 1500   |
| Maria | Finance    | 1400   |

Constraints:

* No blank rows inside the dataset
* Headers must be in row 1

---

# Part C — Record Macro

## 3. Start Recording

* Developer → **Record Macro**

| Field    | Value         |
| -------- | ------------- |
| Name     | `FormatTable` |
| Store in | This Workbook |

Click **OK**

---

# Part D — Perform Actions

## 4. Select Table

* Click inside table
* Press **Ctrl + A**

---

## 5. Bold Headers

* Select first row
* Click **Bold**

---

## 6. Apply Borders

* Select entire table
* Home → **Borders → All Borders**

---

## 7. AutoFit Columns

* Select columns
* Home → Format → **AutoFit Column Width**

---

## 8. Stop Recording

* Developer → **Stop Recording**

---

# Part E — Run Macro

## 9. Reset Formatting

* Home → Clear → **Clear Formats**

---

## 10. Run Macro

* Developer → **Macros**
* Select `FormatTable`
* Click **Run**

---

# Expected Result

Fully formatted table:

* Bold headers
* Borders
* Proper column widths

---

# Part F — Conceptual Layer

The recorder generated VBA instructions such as:

```vba
Selection.Font.Bold = True
Selection.Borders.LineStyle = xlContinuous
Selection.Columns.AutoFit
```

Key insight:

> Macros operate on **objects** (often `Selection`) and execute **step-by-step procedural logic**.

---

# Part G — Troubleshooting

### 1. Developer Tab Missing

Enable via Excel Options

---

### 2. Macros Disabled

* File → Options → Trust Center
* Enable macros or click **Enable Content**

---

### 3. Lost Macro After Saving

Save as:

* **.xlsm**

---

### 4. Incorrect Formatting

Cause:

* Wrong selection during recording

Fix:

* Re-record carefully

---

### 5. Partial Execution

Cause:

* Macro depends on specific selection state

---

### 6. Security Warnings

Explain corporate macro restrictions

---

# Part H — Instructor Notes

## Core Statement

> “You created code without writing code.”

---

## Key Concepts

* Automation = repeatable actions
* Macro = recorded procedure
* VBA = execution layer
* Recorder = literal, not intelligent

---

# Part I — Related Topics — Bonus

This section deepens conceptual understanding and introduces **first practical customization pathway**.

---

## 1. Absolute vs Relative References (Critical Concept)

### Absolute (Default Behavior)

Recorder generates code tied to exact positions.

Example behavior:

* Always formats **A1:C4**, regardless of selection

**Problem:**

* Not reusable

---

### Relative References (Better for Generalization)

To enable:

* Developer → **Use Relative References**
* Then record macro again

Now:

* Macro acts relative to current selection

---

### Teaching Insight

| Type     | Behavior    | Use Case           |
| -------- | ----------- | ------------------ |
| Absolute | Fixed cells | Reports, templates |
| Relative | Dynamic     | Reusable tools     |

---

## 2. Selection vs Direct Object Referencing

### Selection-Based Code (Recorder Default)

```vba
Selection.Font.Bold = True
```

**Issues:**

* Fragile
* Depends on user state

---

### Direct Referencing (Better Practice)

```vba
Range("A1:C4").Font.Bold = True
```

Or more robust:

```vba
ActiveSheet.UsedRange.Font.Bold = True
```

---

### Teaching Point

> Selection-based macros simulate user behavior; object-based macros express intent.

---

## 3. Cleaning Recorded Code

Recorded macros are:

* Verbose
* Redundant
* Inefficient

---

### Typical Recorded Output

```vba
Select id="tswhm0"
Selection.Font.Bold = True
Selection.Borders(xlEdgeLeft).LineStyle = xlContinuous
Selection.Borders(xlEdgeRight).LineStyle = xlContinuous
```

---

### Cleaner Version

```vba
With Selection
    .Font.Bold = True
    .Borders.LineStyle = xlContinuous
End With
```

---

### Teaching Point

> Refactoring transforms recorded scripts into maintainable programs.

---

## 4. Assigning Macro to a Button (Practical Automation)

This is the **first step toward real usability**.

---

### Method A — Form Control Button (Recommended for Beginners)

#### Step-by-Step

1. Go to:

   * Developer → **Insert**

2. Under **Form Controls**:

   * Select **Button (Form Control)**

3. Click anywhere on worksheet to place button

4. Excel immediately prompts:

   * Assign Macro → select `FormatTable`
   * Click **OK**

---

### Rename Button

* Right-click button → **Edit Text**
* Example:

  * “Format Table”

---

### Test

* Clear formatting
* Click button
* Macro executes

---

### Method B — Assign Macro to Existing Shape

#### Steps:

1. Insert shape:

   * Insert → Shapes → Rectangle (or any)

2. Right-click shape → **Assign Macro**

3. Select:

   * `FormatTable`

4. Click **OK**

---

### Advantages

| Method      | When to Use            |
| ----------- | ---------------------- |
| Form Button | Simple UI, quick setup |
| Shape       | Custom UI, dashboards  |

---

### Common Issues

#### 1. Button does nothing

Cause:

* Macro not assigned

Fix:

* Right-click → Assign Macro

---

#### 2. Macro security blocks execution

Fix:

* Enable content

---

#### 3. Button disappears or moves

Cause:

* Sheet layout changes

Fix:

* Right-click → Format Control → Properties → "Don't move or size with cells"

---

### Instructor Emphasis

> This is the transition from “tool user” → “tool builder”.

---

### Conceptual Upgrade

You are now:

* Encapsulating logic
* Creating reusable UI triggers
* Building interactive Excel tools

---

# Related Topics (Extended Context)

* Event-driven VBA (button click events)
* UserForms vs worksheet controls
* Modular macro design
* Macro security policies in enterprises

---

## Time Allocation

| Section                   | Time      |
| ------------------------- | --------- |
| Recording                 | 10 min    |
| Running + troubleshooting | 10–15 min |
| Bonus topics              | 15–25 min |

