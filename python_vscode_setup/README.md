# 🧰 Python + Visual Studio Code uzstādīšana (Windows + macOS, 2026)

## 🎯 Mērķis

Pēc šīs uzstādīšanas jūs spēsiet:
- palaist Python programmas
- strādāt ar Jupyter notebook (.ipynb)
- apstrādāt Excel failus ar Python (`pandas`, `openpyxl`)

---

# 1. Python uzstādīšana

## 🪟 Windows 10/11

1. Atveriet: https://www.python.org/downloads/
2. Lejupielādējiet Python 3.x
3. Instalācijas laikā:
   ☑ Add Python to PATH
4. Install Now

Pārbaude (atverot cmd vai powershell):
```
python --version
```
vai:
```
py --version
```

---

## 🍎 macOS (M1/M2/M3)

1. Atveriet: https://www.python.org/downloads/macos/
2. Lejupielādējiet Python 3.x (universal installer)
3. Instalējiet

Pārbaude:
```
python3 --version
```

⚠️ macOS vienmēr izmantojiet `python3`, nevis `python`

---

# 2. Visual Studio Code uzstādīšana

👉 https://code.visualstudio.com/

Instalējiet un atveriet.

---

# 3. Extensions uzstādīšana

VS Code instalējiet:

- Python (Microsoft)
- Jupyter (Microsoft)

---

# 4. Projekta mapes izveide

Izveidojiet mapi:
```
python_excel_lesson
```

Atveriet VS Code:
File → Open Folder

---

# 5. Virtuālā vide (.venv)

## 🪟 Windows

```
python -m venv .venv
```

Aktivizācija:
```
.\.venv\Scripts\Activate.ps1
```

Ja nestrādā:
```
.venv\Scripts\activate.bat
```

---

## 🍎 macOS

```
python3 -m venv .venv
```

Aktivizācija:
```
source .venv/bin/activate
```

---

# 6. Interpreter izvēle VS Code

Ctrl + Shift + P (Mac: Cmd + Shift + P)

```
Python: Select Interpreter
```

Izvēlieties:
```
.venv
```

---

# 7. Bibliotēku uzstādīšana

## 🪟 Windows
```
python -m pip install pandas openpyxl jupyter matplotlib
```

## 🍎 macOS
```
python3 -m pip install pandas openpyxl jupyter matplotlib
```

---

# 8. Python tests

Izveidojiet `test.py`:

```
print("Python darbojas!")
import pandas
import openpyxl
print("Bibliotēkas darbojas!")
```

## 🪟 Windows
```
python test.py
```

## 🍎 macOS
```
python3 test.py
```

---

# 9. Notebook tests

Izveidojiet `.ipynb` failu un palaidiet:

```
import pandas as pd
print("Notebook darbojas")
```

⚠️ Kernel jābūt `.venv`

---

# 10. Excel tests

```
import pandas as pd

df = pd.DataFrame({
    "Department": ["IT", "HR", "Finance"],
    "Amount": [1200, 800, 1500]
})

df.to_excel("test.xlsx", index=False)
```

---

# 11. Biežākās problēmas

## Windows
- python neatrod → izmantojiet `py`
- PowerShell bloķē aktivizāciju → izmantojiet `.bat`

## macOS
- izmanto `python` nevis `python3`
- nav aktivizēts `.venv`

## Abiem
- nepareizs interpreter
- notebook kernel neatbilst `.venv`

---

# 12. Komandu kopsavilkums

## Windows
```
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install pandas openpyxl jupyter matplotlib
```

## macOS
```
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install pandas openpyxl jupyter matplotlib
```

---

# 13. Galvenā ideja

Python:
- automatizē Excel darbu
- samazina kļūdas
- ietaupa laiku

---

# 14. Minimālais darba princips

1. Atver projektu
2. Aktivizē `.venv`
3. Instalē bibliotēkas
4. Palaiž kodu
5. Iegūst Excel rezultātu


