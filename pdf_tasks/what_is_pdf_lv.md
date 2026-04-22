# Kas Ir PDF?

## Kopaina

PDF nozīmē **Portable Document Format**. Tas ir faila formāts, kas paredzēts, lai saglabātu dokumenta vizuālo izskatu un nodrošinātu, ka tas dažādos datoros, operētājsistēmās, printeros un ekrānos izskatās pēc iespējas līdzīgi.

Šis mērķis ir ļoti noderīgs publicēšanai un koplietošanai, bet tas arī izskaidro, kāpēc PDF failus bieži ir grūti analizēt ar kodu:

- PDF ir veidots, lai **attēlotu lapas**, nevis lai piedāvātu tīrus strukturētus datus;
- teksts var būt novietots pēc koordinātām, nevis saglabāts kā loģiskas rindkopas;
- tabulas cilvēkam var izskatīties acīmredzamas pat tad, ja failā nav īstas tabulas struktūras;
- dažos PDF failos ir reāls digitāls teksts, bet citos ir tikai lapas attēli.

Citiem vārdiem, PDF ir ļoti labs prezentēšanai, bet bieži neērts datu ieguvei.

## Kāpēc PDF ir tik izplatīts

PDF tiek plaši lietots, jo tas labi nodrošina:

- izkārtojuma, fontu un lappušu pārtraukumu saglabāšanu;
- teksta, attēlu, diagrammu un vektorgrafikas apvienošanu;
- stabilu drukāšanas rezultātu;
- ērtu formu, pārskatu, rēķinu, rakstu un skenētu dokumentu koplietošanu;
- līdzīgu izskatu dažādās platformās.

Biznesā un izglītībā tas padara PDF par standarta apmaiņas formātu. Programmēšanā un analīzē tas nozīmē, ka fails var izskatīties vienkāršs, lai gan iekšēji tas ir diezgan sarežģīts.

## Kas atrodas PDF faila iekšpusē

Augstā līmenī PDF dokuments parasti satur:

- lapas;
- teksta objektus;
- fontu informāciju;
- attēlus;
- līniju, rāmju un citu formu zīmēšanas instrukcijas;
- metadatus, piemēram, nosaukumu, autoru vai izveides datumu;
- izvēles interaktīvus elementus, piemēram, saites, veidlapu laukus vai anotācijas.

Galvenā ideja ir tāda, ka daudzi PDF faili satur **zīmēšanas instrukcijas**. Lapa būtībā var nozīmēt:

- uzzīmē šo līniju šeit;
- novieto šo vārdu šajās koordinātās;
- ievieto šo attēlu šajā apgabalā;
- izmanto šo fontu un šo izmēru.

Tas būtiski atšķiras no Word dokumenta vai HTML lapas, kur rindkopas, virsraksti un tabulas bieži ir attēlotas daudz skaidrākā struktūrā.

## PDF ne vienmēr nozīmē "teksts"

Ir divi plaši dokumentu tipi, ar kuriem jūs sastapsieties šajā mapē:

- **Digitāls PDF**: failā ir atlasāms teksts. Tādi rīki kā `PyPDF2` vai `pdfplumber` bieži var šo tekstu iegūt tieši.
- **Skenēts PDF**: lapa pārsvarā ir papīra attēls. Teksts cilvēkam ir redzams, bet parastie PDF teksta ieguves rīki to tieši nespēj nolasīt. Šeit nepieciešams [OCR](what_is_ocr_lv.md).

Piemēri mapē `pdf_tasks`:

- `digital_text.pdf` ir digitāla teksta piemērs;
- `table_report.pdf` ir noderīgs tabulu ieguves treniņam;
- `scanned_document.pdf` ir skenēts piemērs, kur tieša teksta ieguve ir ierobežota vai tukša.

## Kāpēc PDF ieguve ir sarežģīta

### 1. Vizuālais izkārtojums nav tas pats, kas loģiskā struktūra

Cilvēks lasa PDF kā teikumus, rindkopas un sadaļas. Programma bieži redz atsevišķus teksta fragmentus, kas novietoti precīzās koordinātās.

Tas rada šādas problēmas:

- vārdi tiek iegūti nepareizā secībā;
- pazūd atstarpes vai parādās liekas atstarpes;
- rindas pārtrūkst teikuma vidū;
- kolonnas saplūst kopā;
- galvenes un kājenes sajaucas ar pamattekstu.

### 2. Lasīšanas secība nav garantēta

Lapa ar divām kolonnām vizuāli parasti tiek lasīta no kreisās kolonnas uz labo. Iekšēji objekti failā var būt saglabāti citā secībā. Parsētājs var izvadīt:

- vispirms virsrakstu;
- tad daļu no otrās kolonnas;
- pēc tam kājeni;
- un tikai tad atlikušo pirmās kolonnas tekstu.

Rezultāts var izskatīties haotisks pat tad, ja PDF fails ir tehniski korekts.

### 3. Tabulas bieži ir tikai vizuāla ilūzija

PDF tabula var būt nekas vairāk kā:

- teksts, kas izlīdzināts rindās;
- dažas uzzīmētas līnijas;
- tukšas atstarpes vizuālai atdalīšanai.

Tas nozīmē, ka bibliotēkai ir jāmin:

- kur sākas un beidzas rindas;
- kuras šūnas pieder kurai kolonnai;
- vai uzzīmētais rāmis ir tabulas robeža vai tikai dekorācija.

Tāpēc tabulu ieguve var neizdoties pat tad, ja cilvēkam tabula šķiet ļoti vienkārša.

### 4. Fonti un kodējumi var būt neparasti

Daži PDF faili izmanto iegultos fontus, pielāgotas simbolu kartes, ligatūras vai neparastus kodējumus. Tas var radīt:

- nepareizus simbolus;
- trūkstošus diakritiskos burtus;
- negaidīti saliktus vai sadalītus vārdus;
- kopētu tekstu, kas atšķiras no redzamā teksta.

Šī problēma ir īpaši svarīga daudzvalodu dokumentos vai tekstos ar specifiskiem simboliem.

### 5. Vienā lapā var būt teksts, grafika un attēli

Viena lapa var saturēt:

- atlasāmu tekstu;
- logotipus un diagrammas;
- ieskenētus parakstus;
- rastra attēlus;
- vektorgrafiku;
- anotācijas.

Iegūšanas rīkam ir jāizlemj, ko saglabāt, ko ignorēt un kā apvienot dažādus satura veidus.

### 6. Skenēti PDF faili uzvedas citādi

Ja lapa ir tikai attēls, tieša PDF teksta ieguve var atgriezt:

- neko;
- ļoti maz teksta;
- bezjēdzīgas rakstzīmes no slēptiem OCR slāņiem.

Šādā gadījumā vajag OCR, kas savukārt ievieš savus kļūdu avotus, piemēram, izplūdumu, zemu kontrastu, šķību lapu un atpazīšanas kļūdas.

### 7. Reālās dzīves PDF faili ir nekonsekventi

Divi faili ar paplašinājumu `.pdf` var uzvesties pilnīgi atšķirīgi:

- viens var būt tīrs digitāls teksts;
- viens var būt papīra lapu fotogrāfija;
- viens var saturēt labi strukturētu tabulu;
- viens var būt sarežģīts pārskats ar grafikiem un peldošām etiķetēm;
- viens var būt šifrēts, bojāts, pagriezts vai slikti ģenerēts.

Tāpēc PDF apstrādes plūsmām vajag testēšanu, validēšanu un rezerves pieejas.

## Biežākie izaicinājumi Python darbplūsmās

Kad studenti strādā ar PDF failiem Python vidē, visbiežāk rodas šādas grūtības:

- `extract_text()` atgriež tukšu rezultātu skenētiem failiem;
- rindkopu teksts zaudē formatējumu;
- tabulu kolonnas nobīdās vai saplūst;
- atkārtotas galvenes parādās katrā lapā;
- lappušu numuri sajaucas ar galveno saturu;
- rindu pārtraukumi rada trokšņainu tekstu turpmākai analīzei;
- dažām lapām vajag OCR, bet citām ne;
- dažādas bibliotēkas vienam un tam pašam failam dod atšķirīgus rezultātus.

Tipiski rīki šajā tēmā:

- `PyPDF2` vienkāršai lapu piekļuvei un teksta ieguvei;
- `pdfplumber` izkārtojuma pārbaudei un darbam ar tabulām;
- `pandas` iegūto tabulu tīrīšanai;
- OCR rīki attēlu tipa lapām.

## Praktiska pieeja darbam ar PDF

Apstrādājot PDF failu, nevajag sākt ar pieņēmumu, ka tas ir tīrs teksts. Labāk vispirms uzdot jautājumus:

1. Vai tas ir digitāls PDF vai skenēts PDF?
2. Vai man vajag parastu tekstu, tabulas, metadatus vai visu kopā?
3. Vai dokuments ir vienkolonnas, daudzkolonnu vai vizuāli sarežģīts?
4. Vai OCR vajag visām lapām vai tikai daļai?
5. Kā es pārbaudīšu, vai iegūtais rezultāts ir pareizs?

Šāds domāšanas veids ir svarīgāks par jebkuru vienu bibliotēku.

## Ieteicamā darbplūsma

Šai kursa tēmai saprātīga darbplūsma ir šāda:

1. Atvērt failu un apskatīt lapu skaitu un metadatus.
2. Vispirms izmēģināt tiešu teksta ieguvi.
3. Pārbaudīt, vai rezultāts ir salasāms un pilnīgs.
4. Ja dokumentā ir tabulas, pārbaudīt tabulām piemērotu rīku.
5. Ja fails ir skenēts, pāriet uz OCR.
6. Pirms analīzes iztīrīt un validēt iegūto rezultātu.

## Kopsavilkums

PDF ir vizuālajam attēlojumam orientēts formāts. Tas ir lieliski piemērots dokumenta izskata saglabāšanai, bet tieši šī pati īpašība bieži apgrūtina automātisku satura ieguvi.

Galvenā atziņa ir vienkārša:

- **labs vizuālais izskats negarantē vieglu mašīnlasāmu satura ieguvi**.

Tieši tāpēc PDF analīze bieži apvieno pārbaudi, satura ieguvi, tīrīšanu, validēšanu un dažkārt arī OCR.
