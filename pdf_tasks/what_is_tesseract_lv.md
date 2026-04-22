# Kas Ir Tesseract?

## Kopaina

Tesseract ir **atvērtā koda OCR dzinis**. Oficiālā Tesseract dokumentācija to raksturo kā teksta atpazīšanas dzini, ko var izmantot no komandrindas vai caur API.

Tā uzdevums ir paskatīties uz attēlu, kurā ir drukāts teksts, un izveidot mašīnlasāmu rezultātu.

Šis rezultāts var būt:

- vienkāršs teksts;
- izkārtojumam bagātāks OCR rezultāts, piemēram, hOCR vai TSV;
- meklējams PDF rezultāts;
- OCR izvade, kuru pēc tam tīra vai analizē Python vidē.

## Kāpēc Tesseract ir svarīgs PDF darbplūsmās

Tesseract kļūst svarīgs tad, kad dokuments cilvēkam ir salasāms, bet teksts tajā nav jau glīti saglabāts digitālā formā.

Tas parasti notiek ar:

- skenētiem PDF failiem;
- fotografētām lapām;
- ekrānattēliem;
- arhīvu materiāliem;
- izdrukātiem dokumentiem, kas pārvērsti attēlos.

Praktiskā PDF darbplūsmā Tesseract bieži strādā pēc Poppler vai cita renderēšanas soļa:

1. PDF lapas pārvērš attēlos.
2. Uz šiem attēliem palaiž Tesseract.
3. OCR rezultātu iztīra, validē un analizē.

## Ko Tesseract spēj darīt

Tesseract ir labs šādiem uzdevumiem:

- atpazīt drukātu tekstu no attēliem;
- strādāt ar daudzām valodām, izmantojot valodu modeļus;
- radīt teksta, hOCR, TSV un meklējama PDF izvadi;
- tikt izmantots skriptos, notebook failos un batch apstrādē.

Tas ir plaši lietots, jo ir atvērtā koda, skriptojams un tam ir nobriedusi komandrindas saskarne.

## Kas Tesseract nav

Tesseract **nav** PDF renderētājs.

Šī atšķirība ir ļoti svarīga. Saskaņā ar oficiālo ievades formātu dokumentāciju:

- Tesseract lasa attēlu formātus;
- Tesseract **neatbalsta** PDF failu lasīšanu kā ievadi;
- Tesseract var veidot PDF kā izvades formātu.

Tātad, ja jūsu ievade ir PDF fails, parasti vispirms vajag citu rīku, kas lapas pārvērš attēlos.

## Tesseract un valodu dati

Tesseract nevar labi strādāt bez pareizajiem valodu modeļiem.

Praksē tas nozīmē:

- vajag pašu OCR dzini;
- vajag arī atbilstošus `.traineddata` valodu failus;
- precizitāte ir atkarīga no tā, vai izvēlētie valodu dati atbilst reālajam dokumentam.

Daudzvalodu darbā tas ir īpaši svarīgi. Ja dokumentā ir latviešu vārdi, diakritiskās zīmes vai jaukts valodu saturs, OCR konfigurācijai tas ir jāņem vērā.

## Galvenie izaicinājumi, lietojot Tesseract

### 1. Sajukums par PDF ievadi

Viens no biežākajiem maldīgajiem pieņēmumiem ir tāds, ka Tesseract var tieši atvērt jebkuru PDF failu un veikt OCR. Oficiālā dokumentācija norāda, ka PDF nav atbalstīts ievades formāts.

Tas nozīmē, ka darbplūsma bieži ir šāda:

- vispirms PDF pārvērš attēlos;
- tikai pēc tam veic OCR.

Ja šis solis tiek izlaists, studenti bieži domā, ka Tesseract nestrādā, lai gan īstā problēma ir nepareizs ievades tips.

### 2. Attēla kvalitāte nosaka OCR kvalitāti

Tesseract ir ļoti jutīgs pret saņemtā attēla kvalitāti.

Biežas problēmas:

- izplūdums;
- zema izšķirtspēja;
- zems kontrasts;
- skenera troksnis;
- ēnas;
- sašķiebtas lapas;
- agresīva saspiešana.

Slikta ievades kvalitāte tieši noved pie sliktāka atpazīšanas rezultāta.

### 3. Valodas un modeļu izvēle

OCR kvalitāte lielā mērā ir atkarīga no izvēlētajiem valodu datiem.

Tipiskas problēmas:

- tikai angļu valodas izmantošana neangļu tekstam;
- trūkstoši `traineddata` faili;
- nepareiza valodu kombinācija;
- gaidas par labiem rezultātiem specifiskiem simboliem bez atbilstošiem modeļiem.

Valodas konfigurācija nav sīkums. Tā bieži ir viens no galvenajiem OCR veiksmes vai neveiksmes faktoriem.

### 4. Sarežģīts izkārtojums

Tesseract var labi atpazīt vārdus un vienlaikus grūtāk tikt galā ar dokumenta struktūru.

Sarežģīti izkārtojumi ir:

- daudzkolonnu lapas;
- tabulas;
- veidlapas;
- paraksti pie attēliem;
- piezīmes, galvenes un kājenes;
- jaukti teksta un grafikas bloki.

Dzīnis var vārdus noteikt pareizi, bet izvadīt tos neērtā vai nepareizā secībā.

### 5. Līdzīgi simboli

OCR bieži jauc savā starpā vizuāli līdzīgas rakstzīmes, piemēram:

- `O` un `0`;
- `I`, `l` un `1`;
- `S` un `5`;
- `B` un `8`.

Šādas kļūdas ir īpaši dārgas identifikatoros, rēķinu numuros, datumos, kodos un vārdos.

### 6. Tabulas ir sarežģītas

Tesseract var atpazīt tekstu tabulas šūnās, bet tas nevar uzticami atjaunot pašu tabulas struktūru.

Biežas problēmas:

- kolonnas saplūst;
- rindas sadalās;
- virsraksti attālinās no saviem datiem;
- skaitliskās vērtības nonāk nepareizā vietā.

Tāpēc OCR teksta ieguve un strukturēta tabulu ieguve nav viens un tas pats uzdevums.

### 7. Ātruma un kvalitātes kompromisi

OCR iestatījumi ietekmē gan darbības laiku, gan kvalitāti.

Piemēri:

- lielākas izšķirtspējas attēli var uzlabot atpazīšanu, bet palēnina apstrādi;
- daudzu valodu OCR var būt precīzāks jauktiem dokumentiem, bet lēnāks;
- daudzu lapu batch apstrāde var kļūt dārga laikā un atmiņā.

Tas ir svarīgi gan mācību uzdevumos, gan reālās produkcijas darbplūsmās.

### 8. OCR rezultātam joprojām vajag pēcapstrādi

Pat tad, ja Tesseract strādā labi, neapstrādātais rezultāts bieži vien ir jātīra.

Tipiski tīrīšanas uzdevumi:

- atstarpju labošana;
- salauztu rindu apvienošana;
- acīmredzamu atpazīšanas kļūdu filtrēšana;
- datumu, kodu vai identifikatoru validēšana ar šabloniem;
- svarīgo lauku manuāla pārbaude.

Tesseract dod spēcīgu sākumpunktu, bet negarantē perfekti gatavu tekstu.

## Kā Tesseract iederas šajā repozitorijā

Mapes `pdf_tasks` kontekstā Tesseract ir noderīgs tad, ja:

- tiešā teksta ieguve no PDF ir tukša vai slikta;
- dokuments ir acīmredzami skenēts;
- vajag OCR no lapas attēla, piemēram, `scanned_document_page1.png`;
- PDF lapa vispirms ir pārvērsta attēlā un tagad tai vajag teksta atpazīšanu.

Īsumā:

- Poppler palīdz sagatavot lapas attēlu;
- Tesseract palīdz nolasīt šajā attēlā esošo tekstu.

## Praktiska pieeja

Lemjot, vai jums vajag Tesseract, uzdodiet sev jautājumus:

1. Vai avota dokuments ir attēlu tipa, nevis īsts digitāls teksts?
2. Vai parastā PDF teksta ieguve jau nedod lietojamu rezultātu?
3. Vai man ir uzinstalēti pareizie valodu dati?
4. Vai lapas kvalitāte ir pietiekami laba OCR darbam?
5. Kā es pārbaudīšu OCR rezultātu?

Šie jautājumi parasti ir svarīgāki par jebkuru vienu OCR komandu.

## Oficiālie resursi

Tālāk ir norādīti autoritatīvi, projekta uzturēti resursi:

- Oficiālā Tesseract lietotāja rokasgrāmata: [https://tesseract-ocr.github.io/tessdoc/](https://tesseract-ocr.github.io/tessdoc/)
- Oficiālā instalēšanas pamācība: [https://tesseract-ocr.github.io/tessdoc/Installation.html](https://tesseract-ocr.github.io/tessdoc/Installation.html)
- Oficiālā komandrindas lietošanas pamācība: [https://tesseract-ocr.github.io/tessdoc/Command-Line-Usage.html](https://tesseract-ocr.github.io/tessdoc/Command-Line-Usage.html)
- Oficiālā ievades formātu lapa: [https://tesseract-ocr.github.io/tessdoc/InputFormats.html](https://tesseract-ocr.github.io/tessdoc/InputFormats.html)
- Oficiālais `traineddata` pārskats: [https://tesseract-ocr.github.io/tessdoc/Data-Files.html](https://tesseract-ocr.github.io/tessdoc/Data-Files.html)
- Oficiālā pirmkoda repozitorija lapa: [https://github.com/tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract)
- Oficiālie valodu datu repozitoriji: [https://github.com/tesseract-ocr/tessdata](https://github.com/tesseract-ocr/tessdata), [https://github.com/tesseract-ocr/tessdata_fast](https://github.com/tesseract-ocr/tessdata_fast), [https://github.com/tesseract-ocr/tessdata_best](https://github.com/tesseract-ocr/tessdata_best)

## Kopsavilkums

Tesseract ir OCR dzinis, kas pārvērš attēlos redzamu tekstu mašīnlasāmā rezultātā. Tas ir spēcīgs un plaši lietots rīks, bet vislabāk darbojas tad, ja ievades attēls ir sagatavots rūpīgi un valodu dati ir pareizi konfigurēti.

Galvenā ideja ir šāda:

- **Tesseract lasa tekstu no attēliem; tas neaizstāj atsevišķu PDF atvēršanas vai renderēšanas soli**.

Tieši tāpēc reālās PDF analīzes darbplūsmās Tesseract bieži tiek lietots kopā ar Poppler.
