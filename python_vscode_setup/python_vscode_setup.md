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

## 🍎 macOS (M1/M2/M3)

1. Atveriet: https://www.python.org/downloads/macos/
2. Lejupielādējiet Python 3.x (universal installer)
3. Instalējiet

Pārbaude:
```
python3 --version
```

⚠️ macOS vienmēr izmantojiet `python3`, nevis `python`

## Pamatojums

Šis solis ir nepieciešams, jo bez Python instalācijas nav iespējams palaist Python programmas vai izmantot bibliotēkas datu apstrādei. Windows vidē `Add Python to PATH` ļauj vienkārši izsaukt Python no komandrindas, savukārt macOS vidē `python3` palīdz izvairīties no konflikta ar sistēmas Python interpretatoru vai tā neesamību.

---

# 2. Visual Studio Code uzstādīšana

👉 https://code.visualstudio.com/

Instalējiet un atveriet.

## Pamatojums

Visual Studio Code ir darba vide, kurā būs ērti rakstīt, palaist un labot Python kodu. Bez redaktora un tā integrācijas rīkiem darbs ar projektiem, failiem un notebook būtu ievērojami neērtāks.

---

# 3. Extensions uzstādīšana

VS Code instalējiet:

- Python (Microsoft)
- Jupyter (Microsoft)

## Pamatojums

Šie paplašinājumi piešķir VS Code atbalstu Python sintaksei, koda palaišanai, interpretatora izvēlei un Jupyter notebook darbībai. Bez tiem VS Code būtu tikai vispārīgs teksta redaktors, nevis pilnvērtīga Python darba vide.

---

# 4. Git uzstādīšana

## 🪟 Windows 10/11

1. Atveriet: https://git-scm.com/download/win
2. Lejupielāde parasti sāksies automātiski
3. Instalācijas laikā varat atstāt noklusējuma iestatījumus
4. Pēc instalēšanas pārbaudiet:

```
git --version
```

## 🍎 macOS

Vienkāršākais variants:

```
xcode-select --install
```

Tas uzstādīs Apple Command Line Tools, kur parasti ietilpst arī `git`.

Pārbaude:

```
git --version
```

Ja nepieciešams, Git var iegūt arī no: https://git-scm.com/download/mac

## Pamatojums

Git ir versiju kontroles rīks, kas ļauj lejupielādēt projektus no GitHub, sekot līdzi izmaiņām un droši saglabāt koda versijas. Tas ir īpaši noderīgi, ja strādājat ar kursa materiāliem, koplietojamiem projektiem vai vēlaties izmantot GitHub Copilot un citus GitHub rīkus pilnvērtīgāk.

---

# 5. GitHub Copilot paplašinājums

Ja vēlaties izmantot AI palīdzību koda rakstīšanā, VS Code var instalēt:

- GitHub Copilot
- GitHub Copilot Chat

## Uzstādīšana

1. Atveriet VS Code sadaļu Extensions
2. Atrodiet `GitHub Copilot`
3. Nospiediet `Install`
4. Pierakstieties ar savu GitHub kontu

⚠️ GitHub Copilot lietošanai ir nepieciešams GitHub konts. Dažos gadījumos nepieciešams arī aktīvs GitHub Copilot plāns vai izmēģinājuma piekļuve.

## Pamatojums

GitHub Copilot var palīdzēt ātrāk rakstīt kodu, ģenerēt piemērus, skaidrot kļūdas un piedāvāt nākamos soļus darbā ar Python. Tas neaizstāj izpratni par kodu, bet var ievērojami paātrināt mācīšanos un ikdienas darbu.

---

# 6. Projekta mapes izveide

Izveidojiet mapi:
```
python_excel_lesson
```

Atveriet VS Code:
File → Open Folder

## Pamatojums

Atsevišķa projekta mape uztur visus failus vienuviet un palīdz izvairīties no jucekļa starp dažādiem darbiem. Atverot tieši šo mapi VS Code vidē, rīki var korekti piesaistīt virtuālo vidi, failus un projekta iestatījumus.

---

# 7. Virtuālā vide (.venv)

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

## Pamatojums

Virtuālā vide izolē projekta bibliotēkas no citām datorā uzstādītajām pakotnēm. Tas novērš versiju konfliktus un nodrošina, ka projekts strādā paredzami gan šodien, gan vēlāk.

---

# 8. Interpreter izvēle VS Code

Ctrl + Shift + P (Mac: Cmd + Shift + P)

```
Python: Select Interpreter
```

Izvēlieties:
```
.venv
```

## Pamatojums

Šis solis liek VS Code izmantot tieši projekta virtuālajā vidē esošo Python interpretatoru. Pretējā gadījumā redaktors var izmantot citu Python versiju, kurā nav vajadzīgo bibliotēku, un kods nedarbosies pareizi.

---

# 9. Bibliotēku uzstādīšana

## 🪟 Windows
```
python -m pip install pandas openpyxl jupyter matplotlib
```

## 🍎 macOS
```
python3 -m pip install pandas openpyxl jupyter matplotlib
```

## Pamatojums

Bibliotēkas ir nepieciešamas, lai veiktu praktiskos uzdevumus: `pandas` datu apstrādei, `openpyxl` Excel failiem, `jupyter` notebook videi un `matplotlib` vizualizācijām. Bez šī soļa Python būtu uzstādīts, bet tam trūktu rīku reālam darbam ar datiem.

---

# 10. Python tests

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

## Pamatojums

Tests pārbauda gan pašu Python darbību, gan to, vai bibliotēkas ir uzstādītas korekti un importējas bez kļūdām. Tas ļauj problēmas pamanīt uzreiz, pirms sākat strādāt ar lielākiem uzdevumiem.

---

# 11. Notebook tests

Izveidojiet `.ipynb` failu un palaidiet:

```
import pandas as pd
print("Notebook darbojas")
```

⚠️ Kernel jābūt `.venv`

## Pamatojums

Šis solis pārbauda, vai Jupyter notebook vide darbojas kopā ar izvēlēto Python vidi. Pareizs kernel (kodols) ir svarīgs, jo citādi notebook var tikt palaista ar citu interpretatoru un neredzēt projektam uzstādītās bibliotēkas.

---

# 12. Excel tests

```
import pandas as pd

df = pd.DataFrame({
    "Department": ["IT", "HR", "Finance"],
    "Amount": [1200, 800, 1500]
})

df.to_excel("test.xlsx", index=False)
```

## Pamatojums

Excel tests apstiprina, ka `pandas` un `openpyxl` spēj ne tikai ielādēties, bet arī izveidot reālu `.xlsx` failu. Tas ir būtiski, jo kursa uzdevumos galvenais mērķis ir automatizēt darbu ar Excel datiem.

---

# 13. Biežākās problēmas

## Windows
- python neatrod → izmantojiet `py`
- PowerShell bloķē aktivizāciju → izmantojiet `.bat`

## macOS
- izmanto `python` nevis `python3`
- nav aktivizēts `.venv`

## Abiem
- nepareizs interpreter
- notebook kernel neatbilst `.venv`

## Pamatojums

Biežāko problēmu saraksts palīdz ātri diagnosticēt tipiskās kļūdas, nepatērējot lieku laiku nejaušai risinājumu meklēšanai. Īpaši sākumā tas samazina risku iestrēgt vienkāršos konfigurācijas jautājumos.

---

# 14. Komandu kopsavilkums

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

## Pamatojums

Komandu kopsavilkums kalpo kā īsa atgādne, kuru var izmantot atkārtoti arī nākamajos projektos. Tas paātrina darba sākšanu un samazina iespēju sajaukt darbību secību.

---

# 15. Galvenā ideja

Python:
- automatizē Excel darbu
- samazina kļūdas
- ietaupa laiku

---

# 16. Minimālais darba princips

1. Atver projektu
2. Aktivizē `.venv`
3. Instalē bibliotēkas
4. Palaiž kodu
5. Iegūst Excel (vai citus) rezultātus



