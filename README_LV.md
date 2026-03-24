# RTU_Digitalas_Prasmes_Excel_VBA_Python

Materiāli RTU Digitālās prasmes kursam pieaugušajiem profesionāļiem ar praktisku fokusu uz Excel automatizāciju ar VBA un pāreju uz Python.

## Kursa galvenā lapa

- https://digitalasprasmes.lv/danalize/

## Saturs

### Sāciet šeit

- `README.md`
  - Galvenais ievadfails angļu valodā studentiem, kuri kursu sāk pirmo reizi vai pie tā atgriežas vēlāk.
- `README_LV.md`
  - Šī paša pārskata versija latviešu valodā.
- `LICENSE`
  - Repozitorijs ir publicēts ar MIT licenci, tāpēc materiālus un kodu var izmantot, pielāgot un papildināt, ievērojot atsauci uz autoru.

### `components/` - Sākuma materiāli praktiskam darbam

- `VBA_Excel_Automation_Workbook_Template.xlsm`
  - Sākuma Excel darbgrāmata praktiskajiem uzdevumiem.
  - Izmantojiet šo versiju, ja vēlaties paši importēt VBA kodu un iziet vingrinājumus soli pa solim.
- `All_Exercises_04_to_11.bas`
  - VBA modulis ar galvenajiem repozitorijā pieejamajiem vingrinājumu makro.
  - Makro aptver vērtību ierakstīšanu lapās, datu kopēšanu, datu tīrīšanu, kārtošanu, atskaites ģenerēšanu, `InputBox` izmantošanu un pilnas darbplūsmas palaišanu.
- `components/README.md`
  - Iesācējiem paredzēta instrukcija, kā importēt `.bas` failu Excel vidē un droši notestēt makro.
- `components/README_LV.md`
  - Tās pašas instrukcijas latviešu valodā.

### `complete_workbook/` - Pabeigts piemērs

- `VBA_Excel_Automation_Workbook_Template_With_Macros.xlsm`
  - Gatava darbgrāmata, kurā VBA modulis jau ir iestrādāts.
  - Izmantojiet šo versiju, ja vēlaties uzreiz apskatīt, palaist un rediģēt strādājošus makro bez importa soļa.
- `complete_workbook/README.md`
  - Soli pa solim apraksts, kā atvērt gatavo darbgrāmatu, rediģēt makro un pārbaudīt izmaiņas.
- `complete_workbook/README_LV.md`
  - Tās pašas instrukcijas latviešu valodā.

### `vba_guides/` - Ātrās atsauces materiāli

- `README.md`
  - VBA iesācēju špikeris angļu valodā.
  - Noder ātram atgādinājumam par sintaksi, mainīgajiem, cikliem, nosacījumiem, diapazoniem un pamata automatizācijas paņēmieniem.
- `README_LV.md`
  - VBA iesācēju špikeris latviešu valodā.
  - Noder studentiem, kuri vēlas atkārtot jēdzienus latviski.

### Repozitorija pašreizējais stāvoklis

- Šobrīd repozitorijs galvenokārt ir vērsts uz kursa Excel un VBA daļu.
- Pilnīgākie materiāli pašlaik ir darbgrāmatu veidnes, koplietotais VBA modulis un VBA ceļveži angļu un latviešu valodā.
- VBA vingrinājumi pieņem, ka darbgrāmatā ir lapas ar nosaukumiem `RawData`, `CleanData`, `Report` un `Playground`, tāpēc šos nosaukumus nevajadzētu mainīt, ja vien vienlaikus netiek labots arī kods.
- Repozitorija nosaukumā ir minēts Python, taču pašreiz redzamie materiāli pārsvarā ir orientēti uz VBA.

### Ieteicamais mācību ceļš

- Ja kursu sākat no nulles, sāciet ar `components/` un paši izmēģiniet makro importēšanu un palaišanu.
- Ja pie materiāla atgriežaties pēc pārtraukuma, vispirms pārskatiet `vba_guides/README_LV.md` vai `vba_guides/README.md`, pēc tam atveriet gatavo darbgrāmatu mapē `complete_workbook/`.
- Ja vēlaties eksperimentēt droši, sāciet ar vienkāršām izmaiņām, piemēram, izvades teksta, mērķa šūnu vai atskaišu virsrakstu maiņu, pirms pārveidojat visu darbplūsmu.
