# RTU_Digitalas_Prasmes_Excel_VBA_Python

Materiāli RTU Digitālās prasmes kursam pieaugušajiem profesionāļiem ar praktisku fokusu uz Excel automatizāciju ar VBA un pāreju uz Python.

## Kursa galvenā lapa

- https://digitalasprasmes.lv/danalize/

## Pasniedzējs

- Valdis Saulespurens
- Lektors, Rīgas Tehniskā universitāte - Datorzinātnes, informācijas tehnoloģijas un enerģētikas fakultāte
- E-pasts: valdis.saulespurens iepriekš minētajā rtu.lv domēnā

## Saturs

### Sāciet šeit

- `README.md`
  - Galvenais ievadfails angļu valodā studentiem, kuri kursu sāk pirmo reizi vai pie tā atgriežas vēlāk.
- `README_LV.md`
  - Šī paša pārskata versija latviešu valodā.
- `LICENSE`
  - Repozitorijs ir publicēts ar MIT licenci, tāpēc materiālus un kodu var izmantot, pielāgot un papildināt, ievērojot atsauci uz autoru.
- `TOOLS.md`
  - Īss pārskats par programmām un pakalpojumiem, kas izmantoti repozitorija materiālu veidošanā.

### Ievada slaidi un lekciju materiāli

- `intro_vba_excel.pdf`
  - Gatavs slaidu komplekts ievadam Excel VBA tēmā.
  - Noder studentiem, kuri pirms praktiskā darba vēlas ātru konceptuālu pārskatu.
- `intro_vba_excel.pptx`
  - Tā paša ievadmateriāla rediģējamā PowerPoint versija.

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

### `exercises/` - Vadīti praktiskie uzdevumi

- `exercises/README.md`
  - Galvenais vingrinājumu ceļš kursa prasmju trenēšanai no pirmā ierakstītā makro līdz nelielai pilnai darbplūsmai.
  - Noder, ja vēlaties strukturētāku secību nekā tikai atsevišķi darbgrāmatu un moduļu faili.
- `exercises/exercise_1/README.md`
  - Detalizēts iesācēju ceļvedis pirmajam ierakstītajam makro un makro ierakstītāja ģenerētā koda izpratnei.

### `vba_guides/` - Ātrās atsauces materiāli

- `README.md`
  - VBA iesācēju špikeris angļu valodā.
  - Noder ātram atgādinājumam par sintaksi, mainīgajiem, cikliem, nosacījumiem, diapazoniem un pamata automatizācijas paņēmieniem.
- `README_LV.md`
  - VBA iesācēju špikeris latviešu valodā.
  - Noder studentiem, kuri vēlas atkārtot jēdzienus latviski.

### `history/` - Plašāks konteksts

- `history/README.md`
  - Papildmateriāls par VBA vēsturi un tās vietu līdzās jaunākām Office automatizācijas tehnoloģijām.
  - Noder studentiem, kuri vēlas ne tikai praktisku darbu, bet arī plašāku priekšstatu par vidi.
- `history/VBA_and_Modern_Automation.pdf`
  - Vēsturiskā un stratēģiskā pārskata prezentācijas versija.
- `history/VBA_and_Modern_Automation.pptx`
  - Tā paša materiāla rediģējamā PowerPoint versija.

### Repozitorija pašreizējais stāvoklis

- Šobrīd repozitorijs galvenokārt ir vērsts uz kursa Excel un VBA daļu.
- Repozitorijā tagad ir vairāku veidu mācību materiāli: ievada slaidi, darbgrāmatu veidnes, vadīti vingrinājumi, ātrās atsauces materiāli un vēsturiskais konteksts.
- VBA vingrinājumi pieņem, ka darbgrāmatā ir lapas ar nosaukumiem `RawData`, `CleanData`, `Report` un `Playground`, tāpēc šos nosaukumus nevajadzētu mainīt, ja vien vienlaikus netiek labots arī kods.
- Repozitorija nosaukumā ir minēts Python, taču pašreiz redzamie materiāli pārsvarā ir orientēti uz VBA.
- Daļa no jaunākajiem vingrinājumu un vēstures materiāliem pašlaik ir dokumentēti tikai angļu valodā.

### Ieteicamais mācību ceļš

- Ja kursu sākat no nulles, sāciet ar `intro_vba_excel.pdf`, pēc tam pārskatiet `vba_guides/`, un tikai tad pārejiet pie `exercises/` vai `components/`.
- Ja vēlaties strukturētu praktisko ceļu, izmantojiet `exercises/README.md` kā galveno secību un nepieciešamības gadījumā atsaucieties uz darbgrāmatu failiem.
- Ja pie materiāla atgriežaties pēc pārtraukuma, vispirms pārskatiet `vba_guides/README_LV.md` vai `vba_guides/README.md`, pēc tam atveriet gatavo darbgrāmatu mapē `complete_workbook/`.
- Ja vēlaties plašāku izpratni par to, kāpēc VBA joprojām ir nozīmīga, izlasiet `history/README.md` vai apskatiet ar to saistītos slaidus mapē `history/`.
- Ja vēlaties eksperimentēt droši, sāciet ar vienkāršām izmaiņām, piemēram, izvades teksta, mērķa šūnu vai atskaišu virsrakstu maiņu, pirms pārveidojat visu darbplūsmu.
