Below is a **student-friendly guide** you can include directly in your workbook or slides. It keeps the mental model simple and avoids technical overload.

---

# Undoing Changes in VBA (Important!)

## Key Idea (Must Remember)

> **Macros cannot be undone with Ctrl + Z.**

When you run a macro:

* Excel **forgets its Undo history**
* You **cannot press Ctrl + Z** to go back

This is normal behavior in Excel.

---

# What Should You Do Instead?

You should always have a **“last known good version”** of your data.

There are three simple and reliable ways to do this.

---

# Method 1 — Work on a Copy (Recommended)

## Steps

1. Right-click your worksheet tab
2. Click **Move or Copy…**
3. Check **Create a copy**
4. Click **OK**

Now you have:

* `Sheet1` (original — safe)
* `Sheet1 (2)` (for experiments)

## How to use

* Run your macros on the copy
* If something goes wrong → delete the copy and start again

## Why this is best

* Very safe
* No coding needed
* Works for everything (data + formatting)

---

# Method 2 — Save Before Running a Macro

## Steps

1. Press **Ctrl + S** before running your macro
2. Run your macro
3. If something goes wrong:

   * Close Excel **without saving**
   * Reopen the file

## When to use

* Quick protection
* Before running a new or risky macro

## Limitation

* You lose *all* changes since last save

---

# Method 3 — Backup a Selection (More Advanced)

If you are working only on a small table:

## Step 1 — Save backup

Run this macro:

```vba
Sub SaveBackup()
    Sheets("Backup").Cells.Clear
    Selection.Copy
    Sheets("Backup").Range("A1").PasteSpecial xlPasteAll
End Sub
```

## Step 2 — Run your macro

## Step 3 — Restore if needed

```vba
Sub RestoreBackup()
    Sheets("Backup").Range("A1").CurrentRegion.Copy
    Selection.PasteSpecial xlPasteAll
End Sub
```

## Setup

* Create a sheet named **Backup**
* You can hide it if you want

## When to use

* When working with a specific selected table
* When testing formatting macros

---

# What About Formatting?

Important:

> Formatting (colors, bold, borders, etc.) is NOT automatically restored.

That means:

* If your macro changes formatting
* Excel will NOT remember what it looked like before

So you must:

* Use a backup (Method 1 or 3), or
* Work on a copy

---

# What NOT to Expect

Do **not** expect:

* Ctrl + Z to work after a macro
* Excel to “remember” previous formatting
* Automatic undo like in Word or normal editing

---

# Simple Rule for This Course

Before running any macro:

✔ Save your file
✔ OR work on a copied sheet

If unsure:

✔ Always use a copy of your worksheet

---

# Typical Student Workflow

1. Duplicate worksheet
2. Run macro
3. Check result
4. If wrong → delete sheet and try again

---

# Summary

* VBA macros **cannot be undone normally**
* Always keep a **safe version**
* Best method: **work on a copy of your worksheet**


