# Exercise 11 - Combine the Workflow (Beginner)

## Goal

Connect several smaller macros into one larger automated process that runs the full reporting workflow from start to finish.

---

## Part A - Prepare the Workbook

### 1. Check that earlier macros exist

This exercise assumes you already have working versions of:

* `CopyData`
* `CleanData`
* `SortData`
* `GenerateReport`
* `ReportWithInput`

The `FullWorkflow` macro will call them in sequence.

---

### 2. Confirm the worksheet names

Make sure your workbook still contains:

* `RawData`
* `CleanData`
* `Report`

Those sheets are used by the earlier macros.

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
Sub FullWorkflow()

    Call CopyData
    Call CleanData
    Call SortData
    Call GenerateReport
    Call ReportWithInput

    MsgBox "Report completed!", vbInformation

End Sub
```

---

### 6. Read the code step by step

These lines call the earlier procedures:

```vba
Call CopyData
Call CleanData
Call SortData
Call GenerateReport
Call ReportWithInput
```

This means:

* copy the raw data
* clean the copied data
* sort the cleaned data
* generate the report sheet
* ask for a report title and apply it to the report

This line shows a completion message:

```vba
MsgBox "Report completed!", vbInformation
```

---

## Part C - Run the Workflow

### 7. Save the workbook

Save as:

* `.xlsm`

---

### 8. Run `FullWorkflow`

In the VBA Editor:

* click inside the procedure
* press **F5**

Or in Excel:

1. Go to **Developer -> Macros**
2. Select `FullWorkflow`
3. Click **Run**

---

### 9. Check the outcome

After the macro finishes:

* `CleanData` should contain copied and modified data
* `Report` should contain the generated report
* the user should be prompted for a report title
* a message box should appear saying `Report completed!`

---

## Expected Result

One macro run completes the full process instead of requiring you to execute several smaller procedures manually.

---

## Part D - Conceptual Layer

This exercise introduces an important programming idea:

* small macros can be combined into larger workflows

Earlier exercises focused on one task at a time:

* copy
* clean
* sort
* report

Now those steps become one coordinated automation process.

Why this matters:

* the user only runs one macro
* the logic becomes easier to reuse
* larger tasks can be built from smaller tested pieces

Key insight:

> Complex automation becomes manageable when it is built from simple procedures that each do one clear job.

---

## Part E - Small Variations to Try

### 10. Remove the `Call` keyword

In VBA, these lines often also work:

```vba
CopyData
CleanData
SortData
GenerateReport
ReportWithInput
```

This is useful for noticing that `Call` is optional in many simple cases.

---

### 11. Change the message text

Try:

```vba
MsgBox "Workflow finished successfully!"
```

This shows that the workflow can provide user feedback at the end.

---

### 12. Change the order of `ReportWithInput`

The provided solution runs `ReportWithInput` after `GenerateReport`.

Think about what would happen if you moved it:

* before `GenerateReport`
* or kept it after `GenerateReport`

This is a useful discussion about workflow order and overwrite behavior.

---

## Part F - Troubleshooting

### 1. The workflow stops in the middle

Cause:

* One of the called macros contains an error

Fix:

* Test `CopyData`, `CleanData`, `SortData`, `GenerateReport`, and `ReportWithInput` separately first

---

### 2. Sub or Function not defined

Cause:

* One of the macro names is missing or spelled differently

Fix:

* Check the exact names of the called procedures

---

### 3. The final message appears, but the result is wrong

Cause:

* One or more earlier macros ran, but their logic or source ranges were incorrect

Fix:

* Review each procedure individually

This includes checking whether `ReportWithInput` overwrites the report title as expected.

---

### 4. The report looks outdated

Cause:

* A previous macro used a fixed range that did not match the current data

Fix:

* Recheck the ranges used in earlier exercises

---

## Part G - Key Takeaway

This exercise introduces workflow orchestration in VBA.

You are learning how to:

* combine multiple procedures
* automate a longer sequence of steps
* build one-click processes from smaller parts

That is a major step from isolated macros toward practical automation.
