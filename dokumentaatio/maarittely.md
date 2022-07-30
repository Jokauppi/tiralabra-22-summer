# Määrittelydokumentti

## Projektin tiedot

Koodin kieli: englanti

Dokumentaation kieli: suomi

Projektin ohjelmointikieli: Python

Hallitsemani kielet:

- Python
- JavaScript/TypeScript
- jossain määrin Java

Opinto-ohjelma: tietojenkäsittelytieteen kandidaatti

## Projektin aihe

Ohjelman tavoitteena on generoida aidon oloinen korkeuskartta siemennumeron avulla muodostetusta satunnaisesta kohinasta muokkaamalla.
Tarkoituksena on muodostaa kohina ansin [simplex noise](https://en.wikipedia.org/wiki/Simplex_noise) -kohina-algoritmilla ja muokata saatua korkeusdataa veden aiheuttamaa eroosiota matkivalla algoritmilla. Syötteenä algoritmeille annetaan kartan siemennumero sekä erilaisia parametreja, joiden mukaan kohina- ja eroosioalgoritmit muuttavat toimintaansa. Kohina-algoritmin paramereilla voidaan vaikuttaa esimerkiksi kartan suuriin pinnanmuotoihin ja yksityiskohtaisuuteen sekä kartan kokoon. Erilaisia kohinakerroksia yhdistämällä voidaan vaikuttaa kartan alkumuotoon. Eroosioalgoritmin syötteillä voidaan vaikuttaa esimerkiksi maastoa muokkaavan elementin vaikutusmatkaan ja voimakkuuteen. Simplex-algoritmi on suoraviivaisempi toteuttaa mutta eroosioalgoritmi ei ole samalla tavalla ennalta määritely ja sen toteutustavassa on huomattavasi enemmän valinnanvapautta.

## Tietorakenteet ja aikavaativuudet

Projektin pääasiallisena tietorakenteena käytetään kaksiulotteista taulukkoa/matriisia, minkä seurauksena tavoitteena on, että algoritmin tila-ja aikavaativuus noudattaisi kartan kokoa ja olla siten O(mn) leveyden m ja korkeuden n mukaan.
