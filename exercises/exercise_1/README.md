# Exercise 1 - Record Your First Macro (Beginner)

## Goal

Understand automation via recording and recognize that Excel actions can be converted into repeatable VBA procedures.

---

## Part A - Setup

### 1. Enable the Developer tab

* Go to **File -> Options -> Customize Ribbon**
* Under **Main Tabs**, enable **Developer**
* Click **OK**

This matches current Excel for Windows desktop.

---

## Part B - Prepare Data

### 2. Create an example table

| Name  | Department | Salary |
| ----- | ---------- | ------ |
| Anna  | HR         | 1200   |
| John  | IT         | 1500   |
| Maria | Finance    | 1400   |

Constraints:

* No blank rows inside the dataset
* Headers must be in row 1

---

## Part C - Record the Macro

### 3. Start recording

* Go to **Developer -> Record Macro**

Use these settings:

| Field    | Value         |
| -------- | ------------- |
| Name     | `FormatTable` |
| Store in | This Workbook |

Click **OK**.

---

## Part D - Perform Actions

### 4. Select the table

* Click inside the table
* Press **Ctrl + A**

---

### 5. Bold the headers

* Select the header row
* Click **Bold** on the Home tab

---

### 6. Apply borders

* Select the table
* Go to **Home -> Borders -> All Borders**

---

### 7. AutoFit the columns

* Select the columns used by the table
* Go to **Home -> Format -> AutoFit Column Width**

---

### 8. Stop recording

* Go to **Developer -> Stop Recording**

---

## Part E - Run the Macro

### 9. Reset the formatting

* Go to **Home -> Clear -> Clear Formats**

---

### 10. Run the macro

* Go to **Developer -> Macros**
* Select `FormatTable`
* Click **Run**

---

## Expected Result

The table is formatted automatically with:

* bold headers
* borders
* adjusted column widths

---

## Part F - Conceptual Layer

The recorder usually generates VBA instructions such as:

```vba
Selection.Font.Bold = True
Selection.Borders.LineStyle = xlContinuous
Selection.Columns.AutoFit
```

Key insight:

> Macros operate on Excel objects, often `Selection`, and execute step-by-step procedural logic.

---

## Part G - Troubleshooting

### 1. Developer tab is missing

Fix:

* Go to **File -> Options -> Customize Ribbon**
* Enable **Developer**

---

### 2. Macros are disabled

You have two common current options in Excel for Windows:

* Click **Enable Content** on the security warning bar if Excel offers it
* Or go to **Developer -> Macro Security**

You can also use:

* **File -> Options -> Trust Center -> Trust Center Settings -> Macro Settings**

Keep in mind that **Disable all macros with notification** is the default and recommended general setting in current Excel.

---

### 3. The macro is missing after saving

Fix:

* Save the workbook as `.xlsm`

---

### 4. The formatting is incorrect

Cause:

* The wrong range was selected during recording

Fix:

* Record the macro again more carefully

---

### 5. The macro only works in some cases

Cause:

* Recorded macros often depend on the current selection state

---

### 6. Security warnings appear

That is normal in current Excel.

Excel protects users from untrusted macro-enabled files. In managed environments, macro behavior may also be restricted by organization policy.

---

## Part H - Instructor Notes

### Core statement

> You created code without writing code.

---

### Key concepts

* Automation = repeatable actions
* Macro = recorded procedure
* VBA = execution layer
* Recorder = literal, not intelligent

---

## Part I - Related Topics - Bonus

This section deepens conceptual understanding and introduces a practical customization path.

---

### 1. Absolute vs relative references

#### Absolute references

By default, the recorder often generates code tied to exact cell positions.

Example behavior:

* Always formats `A1:C4`, regardless of where the user starts

Problem:

* Less reusable

---

#### Relative references

To enable them:

* Go to **Developer -> Use Relative References**
* Record the macro again

Now:

* The macro acts relative to the current active cell

---

#### Teaching insight

| Type     | Behavior    | Use Case           |
| -------- | ----------- | ------------------ |
| Absolute | Fixed cells | Reports, templates |
| Relative | Dynamic     | Reusable tools     |

---

### 2. Selection vs direct object references

#### Selection-based code

```vba
Selection.Font.Bold = True
```

Issues:

* Fragile
* Depends on user state

---

#### Direct references

```vba
Range("A1:C4").Font.Bold = True
```

Or:

```vba
ActiveSheet.UsedRange.Font.Bold = True
```

Teaching point:

> Selection-based macros simulate user behavior; object-based macros express intent.

---

### 3. Cleaning recorded code

Recorded macros are often:

* verbose
* redundant
* inefficient

---

#### Typical recorded output

```vba
Range("A1:C4").Select
Selection.Font.Bold = True
Selection.Borders(xlEdgeLeft).LineStyle = xlContinuous
Selection.Borders(xlEdgeRight).LineStyle = xlContinuous
```

---

#### Cleaner version

```vba
With Range("A1:C4")
    .Font.Bold = True
    .Borders.LineStyle = xlContinuous
End With
```

Teaching point:

> Refactoring transforms recorded scripts into maintainable programs.

---

### 4. Assigning the macro to a button

This is the first step toward real usability.

Current Excel note:

* Use **Form Controls** for this exercise
* Avoid **ActiveX controls** here, because Microsoft has them disabled by default in current Microsoft 365 and Office 2024 desktop builds unless users change security settings

---

#### Method A - Form Control button

1. Go to **Developer -> Insert**
2. Under **Form Controls**, select **Button (Form Control)**
3. Click on the worksheet to place the button
4. When Excel prompts you, assign the macro `FormatTable`
5. Click **OK**

---

#### Rename the button

* Right-click the button
* Choose **Edit Text**
* Rename it to something like `Format Table`

---

#### Test

* Clear the table formatting
* Click the button
* Confirm that the macro runs

---

#### Method B - Assign a macro to a shape

1. Go to **Insert -> Shapes**
2. Insert a shape such as a rectangle
3. Right-click the shape
4. Choose **Assign Macro**
5. Select `FormatTable`
6. Click **OK**

---

#### Advantages

| Method      | When to Use            |
| ----------- | ---------------------- |
| Form Button | Simple UI, quick setup |
| Shape       | Custom UI, dashboards  |

---

#### Common issues

##### 1. The button does nothing

Cause:

* No macro is assigned

Fix:

* Right-click the button or shape and choose **Assign Macro**

---

##### 2. Macro security blocks execution

Fix:

* Use the workbook only from a trusted source
* Enable content only when appropriate

---

##### 3. The button moves when the sheet layout changes

Fix:

* Right-click the button
* Choose **Format Control -> Properties**
* Select **Don't move or size with cells**

---

#### Instructor emphasis

> This is the transition from tool user to tool builder.

---

#### Conceptual upgrade

You are now:

* encapsulating logic
* creating reusable UI triggers
* building interactive Excel tools

---

### Related topics

* Event-driven VBA
* UserForms vs worksheet controls
* Modular macro design
* Macro security policies in organizations

---

#### Time allocation

| Section                   | Time      |
| ------------------------- | --------- |
| Recording                 | 10 min    |
| Running + troubleshooting | 10-15 min |
| Bonus topics              | 15-25 min |
