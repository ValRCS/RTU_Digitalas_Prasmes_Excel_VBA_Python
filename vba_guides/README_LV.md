# 📊 VBA Excel vidē — Iesācēju špikeris

> Praktisks VBA sintakses un semantikas pārskats Excel vidē  
> Paredzēts iesācējiem automatizācijā un skriptēšanā

---

## 🚀 Kas tas ir

Šis repozitorijs satur **strukturētu, viegli saprotamu VBA špikeru**, kas paredzēts:

- pieaugušo izglītībai
- lietotājiem bez programmēšanas pieredzes
- Excel lietotājiem, kas vēlas automatizēt darbus

Fokuss: **praktiska pielietošana, nevis teorija**

---

## 📚 Saturs

- VBA pamatsintakse
- Mainīgie un datu tipi
- Nosacījumi un cikli
- Excel objektu modelis
- Darbs ar šūnām un diapazoniem
- Tipiski automatizācijas piemēri
- Mini piemēri

---

## ⚡ Ātrais sākums

### 1. Atver VBA redaktoru
- Nospied `Alt + F11`

### 2. Izveido moduli
- `Insert → Module`

### 3. Ielīmē un palaid

```vb
Sub HelloWorld()
    MsgBox "Sveika, pasaule!"
End Sub
```

---

## 🧠 Pamatideja

Domā par Excel šādi:

```
Excel → Darbgrāmata → Darblapa → Šūna (Range)
```

Viss VBA darbs būtībā nozīmē manipulēt ar:

- šūnām
- lapām
- failiem

---

## 🧩 Sintakses pamati

### Mainīgie

```vb
Dim name As String
Dim count As Long
Dim price As Double
Dim isDone As Boolean
```

### Piešķiršana

```vb
name = "Anna"
count = 10
```

---

## 🔀 Nosacījumi

```vb
If score >= 50 Then
    MsgBox "Ieskaitīts"
Else
    MsgBox "Nav ieskaitīts"
End If
```

---

## 🔁 Cikli

### For cikls

```vb
Dim i As Long

For i = 1 To 10
    Cells(i, 1).Value = i
Next i
```

---

## 📦 Procedūras un funkcijas

### Sub (veic darbību)

```vb
Sub ShowMessage()
    MsgBox "Sveiki"
End Sub
```

### Function (atgriež vērtību)

```vb
Function Add(a As Double, b As Double) As Double
    Add = a + b
End Function
```

---

## 📊 Darbs ar Excel

### Ierakstīt šūnā

```vb
Range("A1").Value = "Sveiki"
```

### Nolasīt šūnas vērtību

```vb
Dim x As Variant
x = Range("A1").Value
```

---

## 📌 Labā prakse: vienmēr norādi lapu

❌ Slikti:

```vb
Range("A1").Value = "Teksts"
```

✅ Pareizi:

```vb
Worksheets("Sheet1").Range("A1").Value = "Teksts"
```

---

## 🔄 Cikls pa rindām

```vb
Dim i As Long
Dim lastRow As Long

lastRow = Cells(Rows.Count, 1).End(xlUp).Row

For i = 2 To lastRow
    Cells(i, 2).Value = "Apstrādāts"
Next i
```

---

## 🧰 With bloks

```vb
With Range("A1")
    .Value = "Virsraksts"
    .Font.Bold = True
End With
```

---

## 💬 Lietotāja ievade

```vb
Dim name As String
name = InputBox("Ievadi savu vārdu:")
MsgBox "Sveiks, " & name
```

---

## ⚠️ Kļūdu apstrāde

```vb
On Error GoTo ErrorHandler

' riskants kods

Exit Sub

ErrorHandler:
MsgBox "Kļūda: " & Err.Description
```

---

## 🧪 Mini piemērs

```vb
Sub ProcessData()

    Dim ws As Worksheet
    Dim lastRow As Long
    Dim i As Long

    Set ws = Worksheets("Sheet1")
    lastRow = ws.Cells(ws.Rows.Count, 1).End(xlUp).Row

    For i = 2 To lastRow
        ws.Cells(i, 2).Value = "Apstrādāts"
    Next i

    MsgBox "Pabeigts"

End Sub
```

---

## ❗ Tipiskas kļūdas

- Aizmirst `Set` objektiem
- Nenorāda konkrētu darblapu
- Bezgalīgi cikli
- `Integer` vietā vajadzētu `Long`
- Sajauc `=` nozīmi

---

## 🧭 Mācību ceļš

1. Ieraksti makro
2. Izlasi kodu
3. Nedaudz to izmaini
4. Raksti vienkāršus makro
5. Apvieno ciklus + nosacījumus + diapazonus

---

## 🛠 Ieteicamie rīki (2026)

- Excel VBA redaktors (`Alt + F11`)
- VS Code (`.bas` failiem)
- GitHub

---

## 🎯 Noslēgums

VBA nav moderna valoda, bet tā ir:

- praktiska
- cieši integrēta Excel
- plaši izmantota

Ja apgūsi:

- mainīgos
- ciklus
- nosacījumus
- darbu ar šūnām

— tu spēsi automatizēt lielāko daļu Excel uzdevumu.

---

## 📄 Licence

Brīvai izglītības lietošanai

---

## 👨‍🏫 Kursa konteksts

Izstrādāts kursam:

**VBA Excel automatizācijai**

