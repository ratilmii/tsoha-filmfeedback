# FilmFeedback

Sovelluksen avulla käyttäjä voi selata tietoja elokuvista, mm. ohjaaja, päärooleissa esiintyvät näyttelijät, genre, ensi-ilta, sekä tiivistelmä juonesta. Käyttäjä voi myös arvioida elokuvan joko pelkästään tähdillä, tai kirjoittamalla lisäksi sanallisen arvostelun. Jokainen käyttäjä on joko peruskäyttäjä tai ylläpitäjä.

Sovelluksen ominaisuuksia ovat:

* Käyttäjä voi luoda uuden tunnuksen ja käyttää tätä tunnusta kirjautuakseen sisään ja ulos
* Käyttäjä näkee listan elokuvista joko aakkosjärjestyksessä, tai ilmestymispäivän tai tähtimäärän mukaan järjestettynä.
* Käyttäjä voi myös hakea tiettyä elokuvaa nimen tai genren perusteella. Elokuva voi kuulua yhteen tai useampaan genreen.
* Käyttäjä voi antaa elokuvalle arvion tähdillä (min. puoli, maks. viisi) ja halutessaan kirjoittaa sanallisen arvostelun.
* Käyttäjä voi lukea muiden kirjoittamia arvosteluja ja antaa niille ylä- tai alapeukun.
* Sanalliset arvostelut näkyvät elokuvien sivuilla, järjestettynä peukutusten perusteella (joko laskevassa tai nousevassa järjestyksessä).
* Tähtimäärät näkyvät elokuvien sivuilla sekä keskiarvona että jakaumana.
* Ylläpitäjä voi lisätä tai poistaa elokuvia, sekä muokata olemassaolevien elokuvien tietoja.
* Ylläpitäjä voi tarvittaessa poistaa käyttäjien antamia arvosteluja, sekä antaa porttikieltoja.

Tällä hetkellä kaikki listatuista ominaisuuksista eivät ole vielä valmiina, mutta perustoiminnallisuus on kunnossa.

# Käyttöohjeet

Aivan aluksi ohjeet sovelluksen paikalliseen käynnistykseen:

Kloonaa tämä repositorio omalle koneellesi ja siirry sen juurikansioon. Luo kansioon .env-tiedosto ja määritä sen sisältö seuraavanlaiseksi:

```
DATABASE_URL=<tietokannan-paikallinen-osoite>
SECRET_KEY=<salainen-avain>
```

tietokannan paikallinen osoite on todennäköisesti luokkaa:

```
postgresql:///user
```

missä user on käyttäjänimesi. Salainen avain puolestaan voidaan luoda esim. komennoilla:

```
python3
import secrets
secrets.token_hex(16)
```

Aktivoi lopuksi virtuaaliympäristö, asenna riippuvuudet ja määritä tietokantojen skeema komennoilla:

```
python3 -m venv venv
source venv/bin/activate
pip install -r ./requirements.txt

psql < schema.sql
```

Ja nyt voit käynnistää sovelluksen komennolla:

```
flask run
```

## Esitiedot

Sovellukseen on lisätty valmiiksi kymmenen elokuvaa tietoineen, jotta sovelluksen käyttöä voi testata. Käyttäjätunnuksia ei ole valmiina yhtään.

## Aloitus

Sovellus avautuu etusivulle, jossa on tervetulotoivotus, sekä painikkeet elokuvalistaan pääsyä tai sisäänkirjautumista varten. Käyttäjä voi selata elokuvia ja niiden arvosteluja ilman sisäänkirjautumista, mutta oman arvostelun voi lisätä vasta kirjautuneena.

## Tunnuksen luonti ja kirjautuminen

Kun käyttäjä painaa "login"-nappia, avautuu kirjautumissivu. Oletuksena on, että käyttäjä on jo rekisteröitynyt, mutta mikäli käyttäjä on uusi tulokas, on sivun alalaidassa linkki rekisteröintisivulle, joka on muuten samanlainen, kuin kirjautumissivu, mutta salasana tulee syöttää kahteen kertaan.

Kun käyttäjä on joko kirjautunut tai rekisteröitynyt uudeksi käyttäjäksi, palauttaa sovellus hänet etusivulle, jossa näkyy nyt tieto siitä, millä nimellä käyttäjä on kirjautunut.

Salasanat on tallennettu tietokantaan hash-muodossa.

## Elokuvalista

Elokuvat ovat listassa linkkeinä joista painamalla käyttäjä pääsee yksittäisten elokuvien omille sivuille, joissa on listaa perusteellisempaa tietoa ja mahdollisuus antaa elokuvalle arvostelu ja lukea muiden antamia arvosteluja.

## Elokuvasivu

Elokuvan omalla sivulla on tietoa mm. sen ohjaajasta, julkaisuvuodesta, genreistä ja näyttelijöistä. Jokainen elokuva voi kuulua yhteen tai useampaan genreen ja sisältää listan sen tärkeimmistä näyttelijöistä.

Elokuvan sivulla on myös sen saama keskimääräinen arvosana "tähtinä", joita voi antaa puolen tähden välein aina viiteen saakka. Sivun alalaidassa on vielä lista elokuvan saamista arvosteluista, käyttäjän antama arvostelu ensimmäisenä omassa osiossaan. Muiden käyttäjien arvosteluissa on näkyvissä käyttäjänimi, tähtimäärä ja kirjallinen arvostelu. Mikäli käyttäjä ei ole vielä arvostellut elokuvaa, oman arvostelun kohdalla on valikko tähtiarvosanan valitsemista varten ja tekstikenttä arvostelun kirjoittamista varten.

Mikäli käyttäjä ei ole kirjautunut sisään, on oman arvostelun kohdalla nappi josta pääsee kirjautumissivulle.

## Lopetus

Käyttäjä voi kirjautua ulos ja palata myöhemmin takaisin, tiedot säilyvät.

## Jatkosuunnitelmat

* Ulkoasun parantaminen, CSS ja mahdollisesti Javascript-kirjautumisruutu
* arvostelujen plus- ja miinuspisteet
* elokuvien ja arvostelujen lajittelu ja järjestäminen eri seikkojen perusteella
* elokuvien määrän lisääminen ja hakumahdollisuus mm. nimen tai julkaisuvuoden mukaan
