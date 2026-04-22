# Kas Ir Poppler?

## Kopaina

Poppler ir **atvērtā koda PDF renderēšanas bibliotēka**. Projekta oficiālā mājaslapa to raksturo kā PDF renderēšanas bibliotēku, kas balstīta uz xpdf-3.0 kodu bāzi.

Praktiski tas nozīmē, ka Poppler prot:

- atvērt PDF failus;
- interpretēt PDF lapu saturu;
- renderēt lapas attēlos;
- nodrošināt API izstrādātājiem;
- piedāvāt komandrindas rīkus biežākajiem PDF uzdevumiem.

Poppler ir svarīgs PDF darbplūsmās, jo daudzi rīki PDF lapu paši tieši nelasa. Tā vietā tie paļaujas uz Poppler, kas vispirms lapu uzzīmē jeb renderē.

## Kāpēc Poppler ir svarīgs Python darbplūsmās

Python projektos studenti ar Poppler bieži sastopas netieši. Tipisks piemērs ir `pdf2image`, kas parasti fonā izmanto Poppler utilītas, piemēram, `pdftoppm` vai `pdftocairo`, lai PDF lapas pārvērstu attēlos.

Tas ir svarīgi, jo daudzas OCR darbplūsmas izskatās šādi:

1. Ar Poppler PDF lapas pārvērš attēlos.
2. Ar OCR rīku, piemēram, [Tesseract](what_is_tesseract_lv.md), no šiem attēliem atpazīst tekstu.

Tātad Poppler parasti ir **PDF puse** šajā darbplūsmā, bet Tesseract ir **OCR puse**.

## Ko Poppler spēj darīt

Poppler bieži izmanto šādiem uzdevumiem:

- renderēt PDF lapu attēlā;
- nolasīt PDF metadatus;
- iegūt tekstu no digitāliem PDF failiem;
- iegūt iegultos attēlus;
- pārveidot PDF lapas citos formātos;
- nodrošināt atbalstu programmām, kas attēlo PDF dokumentus.

Oficiālajā Poppler pirmkoda kokā ir komandrindas utilītas, piemēram:

- `pdftoppm`;
- `pdftocairo`;
- `pdftotext`;
- `pdfinfo`;
- `pdfimages`;
- `pdffonts`.

Tieši šie rīki bieži ir tas, ko lietotājs reāli instalē savā sistēmā.

## Kas Poppler nav

Poppler **nav** OCR dzinis.

Šī atšķirība ir svarīga:

- Poppler var renderēt skenētu PDF lapu attēlā;
- Poppler dažkārt var iegūt tekstu, ja PDF jau satur digitālu tekstu;
- Poppler nevar "izlasīt" tekstu no tīri attēlu tipa lapas tādā veidā, kā to dara OCR dzinis.

Ja PDF ir tikai skenējums, Poppler var palīdzēt iegūt kvalitatīvu lapas attēlu, bet burtu atpazīšanai joprojām vajag OCR.

## Poppler un skenēti PDF faili

Šeit iesācēji bieži apjūk. Skenēts PDF var izskatīties kā parasts dokuments, bet iekšēji tas var būt tikai attēlu kopa.

Šādā gadījumā:

- Poppler ir noderīgs, lai atvērtu PDF un pārvērstu katru lapu par attēlu;
- Poppler viens pats neatgūst teksta saturu;
- pēc renderēšanas ir vajadzīgs OCR rīks.

Tieši tāpēc Poppler ir tik izplatīts OCR darbplūsmās.

## Galvenie izaicinājumi, lietojot Poppler

### 1. Bibliotēkas un utilītu sajaukšana

Cilvēki bieži saka "instalēt Poppler", lai gan patiesībā var būt domāts:

- instalēt Poppler bibliotēku;
- instalēt Poppler komandrindas utilītas;
- instalēt operētājsistēmas pakotni, kas šos rīkus apvieno.

Precīzs pakotnes nosaukums ir atkarīgs no platformas, tāpēc ideja ir vienkārša, bet instalēšanas detaļas atšķiras.

### 2. Instalēšana un ceļu konfigurācija

Daudzi Python apvalki paši Poppler neiekļauj. Tie sagaida, ka Poppler jau būs pieejams sistēmā.

Biežākās problēmas:

- Poppler ir uzinstalēts, bet nav sistēmas `PATH`;
- apvalks nevar atrast `pdftoppm` vai `pdftocairo`;
- Windows vidē binārie faili ir mapē, par kuru Python kods neko nezina;
- Jupyter, terminālis un IDE izmanto atšķirīgu vidi.

### 3. Renderēšana nav OCR

Biežs nepareizs pieņēmums ir, ka PDF lapas pārvēršana attēlā jau nozīmē teksta iegūšanu. Tā nav.

Poppler risina renderēšanas problēmu. OCR risina rakstzīmju atpazīšanas problēmu. Skenētu dokumentu gadījumā bieži vajag abus.

### 4. Teksta ieguvei joprojām ir PDF ierobežojumi

Pat izmantojot Poppler teksta utilītas, PDF ieguve joprojām manto tipiskās PDF problēmas:

- salauzta lasīšanas secība;
- saplūdušas kolonnas;
- dīvainas atstarpes;
- atkārtotas galvenes un kājenes;
- trūkstoša vai neskaidra tabulu struktūra;
- fontu un kodējumu problēmas.

Poppler var ļoti palīdzēt, bet tas maģiski nepārvērš katru PDF par tīri strukturētiem datiem.

### 5. Izšķirtspējas un veiktspējas kompromisi

Kad Poppler renderē lapas attēlos, izvēlētā DPI vērtība ir svarīga.

- zema DPI ir ātrāka, bet OCR kvalitāte var kristies;
- augsta DPI var uzlabot atpazīšanu, bet patērē vairāk atmiņas, vietas un laika.

Šis kompromiss ir īpaši redzams batch apstrādē un lielos daudzlapu PDF failos.

### 6. Reālās dzīves PDF faili ir nekonsekventi

Poppler ir jātiek galā ar daudziem sarežģītiem failiem:

- bojāti PDF faili;
- šifrēti PDF faili;
- neparasti fonti;
- sarežģīta vektorgrafika;
- jaukti teksta un attēlu izkārtojumi;
- lieli pārskati ar grafiskiem elementiem.

Tie paši iestatījumi dažādos dokumentos var dot pilnīgi atšķirīgus rezultātus.

### 7. Atšķirības starp platformām

Linux, macOS un Windows vidēs instalēšanas stāsts var būt atšķirīgs. Dažas sistēmas piedāvā Poppler pakotnes tieši, citās vajag atsevišķus bināros failus vai norādīt papildu ceļus.

Tā nav īsti Poppler dizaina kļūda, bet studentiem tā ir ļoti bieža praktiska grūtība.

## Kā Poppler iederas šajā repozitorijā

Mapes `pdf_tasks` kontekstā Poppler ir īpaši svarīgs tad, ja vajag:

- pārvērst PDF lapas attēlos OCR vajadzībām;
- pārbaudīt vai konvertēt PDF pirms tālākas analīzes;
- lietot rīkus, kas paļaujas uz `pdftoppm` vai `pdftocairo`.

Piemēram:

- digitāls PDF var ļaut iegūt tekstu tieši ar tādiem rīkiem kā `PyPDF2`;
- skenēts PDF vispirms var prasīt Poppler balstītu renderēšanu attēlos;
- pēc tam šos attēlus var nodot Tesseract OCR apstrādei.

## Praktiska pieeja

Lemjot, vai jums vajag Poppler, uzdodiet sev jautājumus:

1. Vai man vajag renderēt PDF lapas attēlos?
2. Vai es izmantoju rīku, piemēram, `pdf2image`, kuram vajadzīgas Poppler utilītas?
3. Vai PDF ir skenēts, tāpēc pirms OCR man vajag attēlu?
4. Vai es mēģinu pārbaudīt metadatus, fontus vai PDF iekšējos attēlus?

Ja atbilde uz kādu no šiem jautājumiem ir "jā", Poppler bieži būs daļa no risinājuma.

## Oficiālie resursi

Tālāk ir norādīti autoritatīvi, projekta uzturēti resursi:

- Oficiālā Poppler projekta lapa: [https://poppler.freedesktop.org/](https://poppler.freedesktop.org/)
- Oficiālā API dokumentācija: [https://poppler.freedesktop.org/api/cpp/](https://poppler.freedesktop.org/api/cpp/)
- Oficiālais pirmkoda pārlūks: [https://cgit.freedesktop.org/poppler/poppler/tree/](https://cgit.freedesktop.org/poppler/poppler/tree/)
- Oficiālā utilītu direktorija pirmkodā: [https://cgit.freedesktop.org/poppler/poppler/tree/utils](https://cgit.freedesktop.org/poppler/poppler/tree/utils)
- Oficiālā laidienu lapa: [https://poppler.freedesktop.org/releases.html](https://poppler.freedesktop.org/releases.html)

## Kopsavilkums

Poppler ir PDF renderēšanas un utilītu rīkkopa. Tā palīdz programmām atvērt, pārbaudīt un renderēt PDF failus, bet tā pati par sevi nav OCR dzinis.

Galvenā ideja ir šāda:

- **Poppler palīdz strādāt ar PDF lapām; OCR rīki palīdz nolasīt tekstu no šo lapu attēliem**.

Tieši tāpēc Poppler un Tesseract praktiskās PDF analīzes darbplūsmās bieži parādās kopā.
