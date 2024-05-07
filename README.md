# FilmFeedback

Sovelluksen avulla käyttäjä voi selata tietoja elokuvista, mm. ohjaaja, päärooleissa esiintyvät näyttelijät, genre, julkaisuvuosi, kesto, sekä tiivistelmä juonesta. Käyttäjä voi myös arvioida elokuvan joko pelkästään tähdillä, tai kirjoittamalla lisäksi sanallisen arvostelun. Jokainen käyttäjä on joko peruskäyttäjä tai ylläpitäjä.

Sovelluksen ominaisuuksia ovat:

- [x] Käyttäjä voi luoda uuden tunnuksen ja käyttää tätä tunnusta kirjautuakseen sisään ja ulos.
- [x] Käyttäjä näkee listan elokuvista ilmestymisvuoden mukaan järjestettynä.
- [x] Elokuva voi kuulua yhteen tai useampaan genreen.
- [x] Käyttäjä voi antaa elokuvalle arvion tähdillä (min. puoli, maks. viisi) ja halutessaan kirjoittaa sanallisen arvostelun.
- [x] Käyttäjä voi lukea muiden kirjoittamia arvosteluja.
- [x] Sanalliset arvostelut näkyvät elokuvien sivuilla arvostelujärjestyksessä.
- [x] Tähtimäärät näkyvät elokuvien sivuilla keskiarvona
- [x] Ylläpitäjä voi tarvittaessa poistaa käyttäjien antamia arvosteluja
- [x] Käyttäjä voi poistaa oman arvostelunsa.

Sovelluksen mahdollisia tulevia ominaisuuksia ovat:

- [ ] Käyttäjä voi järjestää elokuvalistan muidenkin kriteerien perusteella, sekä hakea tiettyä elokuvaa nimen tai genren perusteella.
- [ ] Käyttäjä voi antaa muiden antamille arvosteluille ns. ylä- tai alapeukun.
- [ ] Arvostelut voidaan järjestää myös peukutusten perusteella (joko laskevassa tai nousevassa järjestyksessä).
- [ ] Tähtimäärät näkyvät myös jakaumana.
- [ ] Ylläpitäjä voi lisätä tai poistaa elokuvia, sekä muokata olemassaolevien elokuvien tietoja.
- [ ] Ylläpitäjä voi antaa porttikieltoja.

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

## Admin-tunnuksen luonti

Sovelluksen täyttä toiminnallisuutta testatakseen käyttäjän tulee voida luoda admin-tunnus. Tämän sovelluksen puitteissa se toteutetaan niin, että luotuaan ensin tavallisen tunnuksen, sovellusta paikallisesti testaava käyttäjä voi manuaalisesti muokata Users-taulun "is_admin" saraketta haluamalleen käyttäjänimelle (todellisessa käytössä admin-tason tunnuksien luomiselle olisi luonnollisesti täysin oma toiminnallisuutensa).

Kun käyttäjä on luonut itselleen tunnuksen, jonka hän haluaa muuttaa admin-tunnukseksi, tapahtuu se seuraavalla tavalla:

```
psql -d käyttäjän_tietokannan_nimi -c  "UPDATE Users SET is_admin = true WHERE username = 'käyttäjänimi';"
```
missä "käyttäjän_tietokannan_nimi" on käytössä olevan PostgreSQL-tietokannan nimi ja "käyttäjänimi" sen tunnuksen nimi, joka halutaan muuttaa admin-tunnukseksi.

## Elokuvalista

Elokuvat ovat listassa linkkeinä joista painamalla käyttäjä pääsee yksittäisten elokuvien omille sivuille, joissa on listaa perusteellisempaa tietoa ja mahdollisuus antaa elokuvalle arvostelu ja lukea muiden antamia arvosteluja.

## Elokuvasivu

Elokuvan omalla sivulla on tietoa mm. sen ohjaajasta, julkaisuvuodesta, genreistä ja näyttelijöistä. Jokainen elokuva voi kuulua yhteen tai useampaan genreen ja sisältää listan sen tärkeimmistä näyttelijöistä.

Elokuvan sivulla on myös sen saama keskimääräinen arvosana "tähtinä", joita voi antaa puolen tähden välein aina viiteen saakka. Sivun alalaidassa on vielä lista elokuvan saamista arvosteluista, käyttäjän antama arvostelu ensimmäisenä omassa osiossaan. Muiden käyttäjien arvosteluissa on näkyvissä käyttäjänimi, tähtimäärä ja kirjallinen arvostelu. Mikäli käyttäjä ei ole vielä arvostellut elokuvaa, oman arvostelun kohdalla on valikko tähtiarvosanan valitsemista varten ja tekstikenttä arvostelun kirjoittamista varten.

Mikäli käyttäjä ei ole kirjautunut sisään, on oman arvostelun kohdalla nappi josta pääsee kirjautumissivulle.

## Lopetus

Käyttäjä voi kirjautua ulos ja palata myöhemmin takaisin, tiedot säilyvät.

## Jatkosuunnitelmat

Sovelluksesta jäi puuttumaan joitakin haastavammista ominaisuuksista, mutta olen kuitenkin tyytyväinen sen nykytilanteeseen. Voin lisäillä jäljellä olevia ominaisuuksia myöhemmin, mutta perustoiminnallisuus on nyt valmis. Jatkossa olisi mielenkiintoista toteuttaa ainakin osa seuraavista:

* Ulkoasun parantaminen entisestään, tällä hetkellä vasta login- ja register-sivu siistinä
* kuvien lisääminen tietokantaan
* virheilmoitusten yhdenmukaistaminen ja eri virhetilanteiden yksilöllisempi huomioonottaminen (ts. ei vain geneeristä "ei onnistunut" -ilmoitusta, vaan tarkempi ilmoitus siitä, mikä meni pieleen)
* arvostelujen plus- ja miinuspisteet
* arvostelujen muokkaaminen
* elokuvien ja arvostelujen lajittelu ja järjestäminen eri seikkojen perusteella
* elokuvien määrän lisääminen ja hakumahdollisuus mm. nimen tai julkaisuvuoden mukaan
