# Komponentes

Komponentes šajā repozitorijā nozīmē atsevišķus failus, kas tiek izmantoti kursa praktiskajā darbā.

## Kā tos apvienot

Zemāk ir precīza, iesācējiem droša instrukcija, kā importēt `.bas` moduli savā Excel darbgrāmatā. Teksts ir rakstīts, pieņemot, ka iepriekšējas VBA pieredzes nav.

---

# `All_Exercises_04_to_11.bas` importēšana Excel darbgrāmatā (.xlsm)

## Priekšnosacījumi

- Jums ir:
  - `VBA_Excel_Automation_Workbook_Template.xlsm`
  - `All_Exercises_04_to_11.bas`
- Datorā ir instalēts Excel (Windows darbvirsmas versija)

---

## 1. solis - atveriet darbgrāmatu

1. Veiciet dubultklikšķi uz:

   ```
   VBA_Excel_Automation_Workbook_Template.xlsm
   ```

2. Ja redzat drošības brīdinājumu dzeltenajā joslā:
   - nospiediet **Enable Content**

Svarīgi:
Makro nedarbosies, kamēr saturs nav atļauts.

---

## 2. solis - atveriet VBA redaktoru

1. Nospiediet:

   ```
   Alt + F11
   ```

2. Tiks atvērts **VBA Editor (VBE)** logs.

---

## 3. solis - atrodiet darbgrāmatu Project logā

Kreisajā pusē, Project Explorer logā, atrodiet:

```
VBAProject (VBA_Excel_Automation_Workbook_Template.xlsm)
```

Ja šo logu neredzat:

- nospiediet `Ctrl + R`, lai to parādītu

---

## 4. solis - importējiet `.bas` moduli

1. Augšējā izvēlnē nospiediet:

   ```
   File -> Import File...
   ```

2. Atrodiet failu:

   ```
   All_Exercises_04_to_11.bas
   ```

3. Nospiediet:

   ```
   Open
   ```

---

## 5. solis - pārbaudiet importu

Pēc importa vajadzētu redzēt:

```
Modules
└── All_Exercises_04_to_11
```

Noklikšķiniet uz moduļa, un labajā pusē vajadzētu parādīties kodam.

---

## 6. solis - saglabājiet darbgrāmatu

1. Nospiediet:

   ```
   Ctrl + S
   ```

Svarīgi:
Failam jāsaglabājas `.xlsm` formātā, jo tas ir makro saturošs fails.

---

## 7. solis - palaidiet makro pārbaudei

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

- šūnā `A1` parādās teksts:

  ```
  Hello, VBA
  ```

---

# Biežākās problēmas un risinājumi

## 1. Makro ir bloķēti

Simptoms:
Nekas nenotiek.

Risinājums:

- nospiediet **Enable Content**
- vai atveriet:

  ```
  File -> Options -> Trust Center -> Macro Settings
  ```

---

## 2. Modulis nav redzams

Risinājums:

- nospiediet `Ctrl + R`
- izvērsiet savas darbgrāmatas koku

---

## 3. Kļūda "Sub or Function not defined"

Iemesls:

- trūkst kāda atkarīga makro daļa

Risinājums:

- pārliecinieties, ka importēts viss modulis, nevis tikai daļa no tā

---

## 4. Kļūdas lapu nosaukumos

Simptoms:

```
Subscript out of range
```

Risinājums:
Pārbaudiet, vai lapu nosaukumi pilnībā sakrīt:

- `RawData`
- `CleanData`
- `Report`
- `Playground`

Bez papildu atstarpēm un ar precīzu rakstību.

---

# Domāšanas modelis

Jūs:

- importējāt **koda moduli (`.bas` failu)**
- kurā ir vairākas `Sub` procedūras jeb makro
- un Excel tagad tās uztver kā palaižamus automatizācijas rīkus

---

# Īss darbplūsmas kopsavilkums

```
Atver darbgrāmatu
-> Alt+F11
-> File -> Import .bas
-> Save
-> Alt+F8 -> Run macro
```
