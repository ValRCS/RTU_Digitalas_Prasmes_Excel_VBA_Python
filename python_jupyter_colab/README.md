# Python, Jupyter Notebook un Google Colab — ievads Excel lietotājiem

## 1. Kāpēc vispār Python?

Ja līdz šim esat strādājuši galvenokārt ar Excel, tad Python var uztvert kā nākamo soli:

- Excel → manuāls darbs ar datiem  
- VBA → automatizācija Excel ietvaros  
- Python → darbs ar datiem neatkarīgi no Excel  

**Galvenā ideja:**  
Python ļauj jums automatizēt ne tikai Excel, bet visu datu apstrādes procesu kopumā.

---

## 2. Excel vs Python domāšanas veids

| Excel | Python |
|------|--------|
| Darbs ar šūnām | Darbs ar datu tabulām |
| Manuāli soļi | Automātiski skripti |
| Faila līmenis | Datu plūsma (pipeline) |
| Klikšķi | Kods |

Python pieeja:
> Vienreiz uzraksti → palaid atkārtoti → iegūsti to pašu rezultātu

---

## 3. Kas ir Jupyter Notebook?

Jupyter Notebook ir vide, kur:

- rakstīt Python kodu
- uzreiz redzēt rezultātu
- pievienot paskaidrojumus

To var uztvert kā:
> Word dokuments + Excel + kods vienā vietā

---

## 4. Notebook struktūra

Notebook sastāv no **šūnām (cells)**.

### 4.1 Code šūnas

Tās satur Python kodu.

Piemērs:

```python
x = 10
x * 2
```

Rezultāts parādās uzreiz zem koda.

---

### 4.2 Markdown šūnas

Tās satur tekstu (skaidrojumus, virsrakstus).

Piemērs:

```markdown
## Datu ielāde
Šajā solī mēs ielādējam Excel failu.
```

---

## 5. Kas ir Google Colab?

Google Colab ir Jupyter Notebook versija, kas darbojas pārlūkā.

### Priekšrocības:

- Nav jāinstalē Python
- Strādā uzreiz
- Var dalīties kā Google Docs
- Strādā arī uz vājākiem datoriem

---

## 6. Tipiska darba plūsma Python vidē

1. Ielādē datus (Excel, CSV)
2. Apskata struktūru
3. Attīra un filtrē
4. Analizē
5. Veido grafikus
6. Saglabā rezultātu

---

## 7. Excel darbības → Python analogi

| Excel | Python |
|------|--------|
| Atvērt failu | pandas.read_excel() |
| Filtrēt | df[...] |
| Pivot tabula | groupby() |
| Diagramma | matplotlib / seaborn |
| Saglabāt | to_excel() |

---

## 8. Kāpēc izmantot Notebook?

- Var soli pa solim redzēt, kas notiek
- Viegli eksperimentēt
- Viegli dokumentēt darbu
- Viegli atkārtot analīzi

---

## 9. Svarīgākais princips

Python + Jupyter/Colab ļauj veidot:

> reproducējamu datu analīzi

Tas nozīmē:
- tas pats kods → tas pats rezultāts
- mazāk kļūdu
- vieglāk uzturēt

---

## 10. Kopsavilkums

- Python = universāls rīks datu apstrādei
- Jupyter = darba vide
- Colab = Jupyter bez instalācijas
- Code šūnas = darbības
- Markdown šūnas = paskaidrojumi

---

## 11. Nākamais solis

Praksē jūs:
- ielādēsiet Excel failu
- veiksiet filtrēšanu
- izveidosiet kopsavilkumu
- saglabāsiet rezultātu

Tas viss notiks Jupyter Notebook vai Google Colab vidē, kas ļaus jums redzēt katru soli un rezultātu uzreiz.