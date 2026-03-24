# Pilnā darbgrāmata ar jau iestrādātiem makro

Šajā darbgrāmatā jau ir tās pašas komponentes, kas atrodamas mapē `/components`, taču makro jau ir iestrādāti pašā failā.

Zemāk ir skaidra, secīga instrukcija, kā rediģēt makro. Tā ir rakstīta cilvēkam bez iepriekšējas VBA pieredzes un fokusējas uz to, kur nospiest, ko nomainīt un kā pārbaudīt rezultātu.

---

# Makro rediģēšana Excel vidē soli pa solim

## 1. solis - atveriet darbgrāmatu

1. Atveriet:

   ```
   VBA_Excel_Automation_Workbook_Template_With_Macros.xlsm
   ```

2. Ja redzat drošības paziņojumu, nospiediet **Enable Content**.

---

## 2. solis - atveriet VBA redaktoru

Nospiediet:

```
Alt + F11
```

Tiks atvērts jauns logs - **VBA Editor**.

---

## 3. solis - atrodiet makro

Kreisajā pusē, Project Explorer logā, atrodiet:

```
VBAProject (VBA_Excel_Automation_Workbook_Template_With_Macros.xlsm)
└── Modules
    └── All_Exercises_04_to_11
```

Noklikšķiniet uz:

```
All_Exercises_04_to_11
```

Labajā pusē redzēsiet kodu.

---

## 4. solis - atpazīstiet makro

Makro izskatās šādi:

```vba
Sub WriteHello()
    Range("A1").Value = "Hello, VBA"
End Sub
```

- `Sub WriteHello()` ir makro nosaukums
- `End Sub` ir makro beigas

Viss, kas atrodas starp šīm rindām, ir vieta, ko varat rediģēt.

---

## 5. solis - veiciet vienkāršu izmaiņu

### Piemērs: nomainiet ziņojuma tekstu

Pirms:

```vba
Range("A1").Value = "Hello, VBA"
```

Pēc:

```vba
Range("A1").Value = "Hello, Student"
```

---

## 6. solis - saglabājiet izmaiņas

Nospiediet:

```
Ctrl + S
```

---

## 7. solis - palaidiet rediģēto makro

1. Atgriezieties Excel logā:

   ```
   Alt + F11
   ```

2. Nospiediet:

   ```
   Alt + F8
   ```

3. Izvēlieties:

   ```
   WriteHello
   ```

4. Nospiediet:

   ```
   Run
   ```

Sagaidāmais rezultāts:

Šūnā `A1` tagad ir redzams:

```
Hello, Student
```

---

# Otrais piemērs - mērķa šūnas maiņa

Pirms:

```vba
Range("A1").Value = "Hello"
```

Pēc:

```vba
Range("B2").Value = "Hello"
```

Rezultāts:
Izvade tiks ierakstīta šūnā `B2`.

---

# Trešais piemērs - reāla makro pielāgošana

Atrodiet šo makro:

```vba
Sub GenerateReport()
```

Mainiet šo rindu:

```vba
dst.Range("A1").Value = "Sales Report"
```

Uz šo:

```vba
dst.Range("A1").Value = "Weekly Sales Report"
```

---

# Biežākās iesācēju kļūdas

## 1. Rediģēšana ārpus makro

Nepareizi:

```vba
Sub WriteHello()
End Sub

Range("A1").Value = "Hello"
```

Vienmēr rediģējiet tikai starp `Sub` un `End Sub`.

---

## 2. Sabojātas pēdiņas

Nepareizi:

```vba
Range("A1").Value = Hello
```

Pareizi:

```vba
Range("A1").Value = "Hello"
```

---

## 3. Neprecīzi lapu nosaukumi

```vba
Worksheets("Report ")
```

Papildu atstarpe izraisīs kļūdu.

---

## 4. Aizmirst saglabāt

Izmaiņas pazudīs, ja nenospiedīsiet:

```
Ctrl + S
```

---

# Kā droši eksperimentēt

Ieteicams izmantot lapu `Playground`:

- tur varat izmēģināt nelielas izmaiņas
- tā ir drošāka vieta, lai nesabojātu galveno darbplūsmu

---

# Papildus - koda izpilde soli pa solim

1. Ieklikšķiniet makro iekšpusē.
2. Nospiediet:

   ```
   F8
   ```

3. Kods izpildīsies pa vienai rindai.

Tas palīdz redzēt:

- kura rinda tieši izpildās
- kurā vietā rodas kļūda

---

# Domāšanas modelis

Makro rediģēšana nozīmē Excel izpildāmo instrukciju maiņu.

Domājiet šādi:

> Maini soļus -> mainās rezultāts

---

# Īss darbplūsmas kopsavilkums

```
Alt+F11 -> atrodi makro -> rediģē kodu -> Ctrl+S -> Alt+F8 -> palaid
```

---

# Ko studentiem vērts patrenēt

- mainīt izvades tekstu
- mainīt šūnu adreses
- pielāgot atskaites virsrakstus
- koriģēt diapazonus

---

# Nākamais loģiskais solis

- apvienot vairākus makro vienā darbplūsmā
- pievienot lietotāja ievadi ar `InputBox`
- izveidot pogas makro palaišanai bez VBA redaktora
