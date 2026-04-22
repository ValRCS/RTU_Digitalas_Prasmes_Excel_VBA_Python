# Kas Ir OCR?

## Kopaina

OCR nozīmē **Optical Character Recognition** jeb optisko rakstzīmju atpazīšanu. Tas ir process, kurā teksts, kas redzams attēlā, tiek pārvērsts mašīnlasāmā tekstā.

Ja jūs ekrānā redzat burtus, bet programma tos nevar nokopēt kā tekstu, ļoti iespējams, ka trūkstošais solis ir OCR.

Darbā ar PDF OCR kļūst nepieciešams tad, kad dokuments ir skenēts, nevis īsts digitāla teksta PDF. Skenēta lapa var izskatīties kā parasts dokuments, bet tehniski tā bieži ir tikai papīra attēls. OCR mēģina no šī attēla atgūt rakstzīmes.

## Kāpēc OCR ir svarīgs

OCR ir svarīgs tāpēc, ka daudzi reāli dokumenti pie mums nonāk kā:

- skenēti līgumi;
- fotografētas piezīmes;
- izdrukātas veidlapas, kas saglabātas PDF formātā;
- veci arhīvu materiāli;
- čeki un rēķini;
- pārskati no skeneriem vai daudzfunkciju iekārtām.

Bez OCR šādus failus ir grūti meklēt, analizēt, apkopot vai pārvērst strukturētos datos.

## OCR salīdzinājumā ar parasto PDF teksta ieguvi

Tieša PDF teksta ieguve un OCR risina atšķirīgas problēmas:

- **Tiešā ieguve** nolasa tekstu, kas PDF failā jau ir saglabāts.
- **OCR** mēģina atpazīt tekstu no lapas attēla.

Ja `PyPDF2` vai līdzīgs rīks jau spēj iegūt tīru tekstu, OCR var nebūt vajadzīgs. Ja ieguve atgriež tukšu vai sliktu rezultātu, jo lapa ir attēla tipa, OCR ir pareizais nākamais solis.

Šajā mapē:

- `digital_text.pdf` galvenokārt ir tiešās teksta ieguves piemērs;
- `scanned_document.pdf` un `scanned_document_page1.png` ir OCR orientēti piemēri.

## Kā OCR darbojas augstā līmenī

OCR parasti seko šādai plūsmai:

1. Ielādē attēlu vai pārveido PDF lapas par attēliem.
2. Vajadzības gadījumā uzlabo attēla kvalitāti.
3. Atrod vietas lapā, kurās atrodas teksts.
4. Atpazīst burtus, vārdus un skaitļus.
5. Atjauno rindas vai teksta blokus.
6. Vajadzības gadījumā pielieto valodas noteikumus vai pēcapstrādi.

Python vidē izplatīta pieeja ir:

- izmantot `pdf2image`, lai PDF lapas pārvērstu attēlos;
- izmantot `Pillow` vienkāršai attēlu apstrādei;
- izmantot `pytesseract`, lai palaistu OCR ar Tesseract.

## OCR nav oriģinālās struktūras pilnīga atjaunošana

OCR bieži spēj atgūt redzamo tekstu, taču tas parasti nespēj perfekti atjaunot dokumenta sākotnējo struktūru.

Piemēram, OCR var nepilnīgi saprast:

- virsrakstu hierarhiju;
- tabulu robežas;
- lasīšanas secību sarežģītos daudzkolonnu izkārtojumos;
- vai skaitlis pieder vienai vai otrai kolonnai;
- vai konkrēta rinda ir kājene, paraksts zem attēla vai pamatteksts.

Tāpēc OCR rezultātam gandrīz vienmēr vajag pārbaudi un tīrīšanu.

## Galvenie OCR izaicinājumi

### 1. Attēla kvalitāte

OCR kvalitāte ļoti stipri ir atkarīga no ievades attēla kvalitātes. Biežas problēmas ir:

- izplūdums;
- zema izšķirtspēja;
- ēnas;
- zems kontrasts;
- saspiešanas artefakti;
- skenera svītras vai putekļi;
- pārgaismotas vai pārāk tumšas lapas.

Ja rakstzīmes ir neskaidras, atpazīšanas kļūdu skaits strauji pieaug.

### 2. Rotācija un šķībums

Skenētās lapas bieži ir nedaudz sašķiebtas. Pat neliels leņķis var pasliktināt rindu noteikšanu un rakstzīmju atpazīšanu.

Tipiskas sekas:

- teksta rindas slīd uz augšu vai uz leju;
- kolonnas tiek interpretētas kļūdaini;
- vārdu sadalīšana kļūst nestabila.

Pirmsapstrāde, piemēram, taisnošana vai rotācijas korekcija, var būtiski uzlabot rezultātu.

### 3. Troksnis un fona tekstūra

OCR vislabāk darbojas tad, ja teksts skaidri atdalās no fona. Grūtības rodas ar:

- pelēku papīra tekstūru;
- zīmogiem;
- rokraksta piezīmēm;
- locījumu ēnām;
- rūtiņu vai līniju fonu;
- trokšņainām kopijām.

OCR dzinis var šos elementus sajaukt ar rakstzīmēm vai sapludināt ar tuvumā esošo tekstu.

### 4. Fonti, simboli un valodas

OCR nav vienādi spēcīgs visiem rakstības stiliem. Precizitāte var kristies, ja dokumentā ir:

- dekoratīvi fonti;
- ļoti mazs teksts;
- neparasti simboli;
- jauktas alfabētu sistēmas;
- matemātiska pieraksta elementi;
- diakritiskās zīmes;
- nozares specifiski saīsinājumi.

Svarīga ir arī valodas konfigurācija. Ja OCR dzinis sagaida angļu valodu, bet dokumentā ir latviešu vārdi vai cits teksts ar diakritiskajām zīmēm, rezultāts var būt sliktāks.

### 5. Tabulas OCR ir sarežģītas

OCR var atpazīt tekstu tabulas iekšpusē, bet tas nenozīmē, ka tas saprot pašu tabulas struktūru.

Biežas kļūmes:

- rindas saplūst kopā;
- kolonnas nobīdās;
- skaitļi tiek piesaistīti nepareiziem virsrakstiem;
- šūnu robežas tiek ignorētas;
- vairāku rindu šūnas pārvēršas netīrā teksta blokā.

Tāpēc OCR viens pats bieži nav pietiekams augstas kvalitātes tabulu ieguvei.

### 6. Jaukta satura lapas

Reālās lapās bieži vienlaikus ir:

- rindkopas;
- logotipi;
- zīmogi;
- paraksti;
- diagrammas;
- tabulas;
- lappušu numuri.

OCR var iegūt visu redzamo tekstu, bet joprojām sajaukt nesaistītas daļas. Galvene, attēla paraksts un kājene var nonākt pamatteksta vidū.

### 7. Līdzīgi simboli

OCR bieži jauc savā starpā līdzīgi izskatošās rakstzīmes, piemēram:

- `O` un `0`;
- `I`, `l` un `1`;
- `S` un `5`;
- `B` un `8`.

Šādas nelielas kļūdas ir īpaši svarīgas vārdos, identifikatoros, rēķinu numuros, datumos un finanšu datos.

### 8. Rokraksts ir atsevišķs sarežģījums

Standarta OCR vislabāk darbojas ar drukātu tekstu. Rokraksts ir daudz grūtāks, jo:

- burti nav konsekventi;
- vārdi pārklājas;
- rindu atstarpes mainās;
- katram cilvēkam ir atšķirīgs rakstības stils.

Daļu rokraksta dažkārt var atpazīt, bet gaidas ir jāuztur zemākas nekā drukāta teksta gadījumā.

## Kāpēc OCR rezultātam vajag pēcapstrādi

Neapstrādāts OCR teksts bieži satur:

- salauztus rindu pārtraukumus;
- trūkstošas vai liekas atstarpes;
- nepareizu interpunkciju;
- saplūdušas kolonnas;
- atkārtotas galvenes un kājenes;
- rakstzīmju aizvietojumus.

Pēcapstrāde var ietvert:

- atstarpju sakārtošanu;
- ticamības vērtējumu filtrēšanu;
- vārdnīcu vai atslēgvārdu pārbaudes;
- regulāro izteiksmju pārbaudes datumiem, kodiem vai identifikatoriem;
- manuālu kritisko lauku pārskatīšanu.

Nopietnās darbplūsmās OCR ir jāuztver kā aptuvens rezultāts, kas ir jāpārbauda.

## Praktiska OCR darbplūsma studentiem

Strādājot mapē `pdf_tasks`, saprātīga pieeja ir šāda:

1. Vispirms pārbaudīt, vai darbojas tiešā PDF teksta ieguve.
2. Ja nē, pārveidot lapu par attēlu.
3. Palaist OCR uz attēla.
4. Salīdzināt OCR rezultātu ar redzamo dokumentu.
5. Atzīmēt atkārtotas atpazīšanas kļūdas.
6. Pirms analīzes vai eksportēšanas iztīrīt rezultātu.

Šis salīdzināšanas solis ir būtisks. OCR kvalitāte ir jāmēra, nevis jāpieņem automātiski.

## Kad OCR ir pareizais rīks

Lietojiet OCR, ja:

- PDF satur skenētu lapu attēlus;
- teksts ir redzams, bet to nevar uzticami atlasīt;
- kopētais teksts ir tukšs vai acīmredzami bojāts;
- dokumenti nāk no skenera, kameras vai arhīva attēlu avota.

Nelietojiet OCR pēc noklusējuma, ja dokumentā jau ir tīrs digitāls teksts. Šādā gadījumā tiešā ieguve parasti ir ātrāka, vienkāršāka un precīzāka.

## Kopsavilkums

OCR pārvērš attēlos redzamu tekstu mašīnlasāmā tekstā. Tas ir ļoti noderīgs rīks, bet tas nav maģija.

Galvenā atziņa ir šāda:

- **OCR palīdz datoram lasīt teksta attēlus, bet rezultātu vienmēr ietekmē attēla kvalitāte, izkārtojuma sarežģītība un atpazīšanas kļūdas**.

PDF analīzē OCR vislabāk uztvert kā rezerves vai papildinošu tehniku skenētiem un attēlu tipa dokumentiem.
