# Components

Component - meaning meaning partial files that are used in the course

## Combining them

Below is a **precise, beginner-safe procedure** for importing the `.bas` module into your Excel workbook. This is written assuming zero prior VBA experience.

---

# **Importing `All_Exercises_04_to_11.bas` into Excel (.xlsm)**

## **Prerequisites**

* You have:

  * `VBA_Excel_Automation_Workbook_Template.xlsm`
  * `All_Exercises_04_to_11.bas`
* Excel installed (Windows desktop version)

---

# **Step 1 — Open the Workbook**

1. Double-click:

   ```
   VBA_Excel_Automation_Workbook_Template.xlsm
   ```
2. If you see a **security warning** (yellow bar):

   * Click **Enable Content**

**Important:**
Macros will not work unless content is enabled.

---

# **Step 2 — Open the VBA Editor**

1. Press:

   ```
   Alt + F11
   ```
2. This opens the **VBA Editor (VBE)**

---

# **Step 3 — Locate Your Workbook in the Project Window**

On the left side (Project Explorer), find:

```
VBAProject (VBA_Excel_Automation_Workbook_Template.xlsm)
```

If you do not see it:

* Press `Ctrl + R` to show Project Explorer

---

# **Step 4 — Import the .bas Module**

1. In the top menu, click:

   ```
   File → Import File...
   ```

2. Navigate to:

   ```
   All_Exercises_04_to_11.bas
   ```

3. Click:

   ```
   Open
   ```

---

# **Step 5 — Verify Import**

You should now see:

```
Modules
 └── All_Exercises_04_to_11
```

Click it → code should appear on the right.

---

# **Step 6 — Save the Workbook**

1. Press:

   ```
   Ctrl + S
   ```

**Important:**
Keep the file as `.xlsm` (macro-enabled).

---

# **Step 7 — Run a Macro (Test)**

1. Return to Excel:

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

**Expected Result:**

* Cell `A1` changes to:

  ```
  Hello, VBA
  ```

---

# **Common Problems and Fixes**

## **1. Macros Disabled**

**Symptom:** Nothing happens
**Fix:**

* Click **Enable Content**
* Or:

  ```
  File → Options → Trust Center → Macro Settings
  ```

---

## **2. Module Not Visible**

**Fix:**

* Press `Ctrl + R`
* Expand your workbook tree

---

## **3. “Sub or Function not defined”**

**Cause:**

* Missing dependent macros

**Fix:**

* Ensure full module was imported (not partial file)

---

## **4. Sheet Name Errors**

**Symptom:**

```
Subscript out of range
```

**Fix:**
Verify sheet names exactly match:

* `RawData`
* `CleanData`
* `Report`
* `Playground`

(No extra spaces, exact spelling)

---

# **Mental Model (What Just Happened)**

You:

* Imported a **code module (.bas file)**
* Which contains:

  * multiple `Sub` procedures (macros)
* Excel now treats them as:

  * runnable automation tools

---

# **Minimal Workflow Summary**

```
Open workbook
→ Alt+F11
→ File → Import .bas
→ Save
→ Alt+F8 → Run macro
```

---

# **Next Logical Steps (for learners)**

* Edit one macro and re-run it
* Add a new macro manually
* Combine macros into a workflow (`FullWorkflow`)

---

If you want, the next step can be:

* adding a **custom ribbon button**
* or assigning macros to **worksheet buttons for non-technical users**
