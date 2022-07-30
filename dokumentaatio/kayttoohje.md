# Käyttöohje

## Ympäristö

Projekti on rakennettu pythonilla käyttäen apuna poetryä

## Komennot

Projektin riippuvuudet voi asentaa komennolla

```poetry install```

(Toistaiseksi projektin toteutusta ei aloitettu)

(Seuraavat komennot toimivat vasta komennon ```poetry shell``` ajamisen jälkeen)

projektin käynnistys

```python3 src/```

automaattisten testien ajo

```pytest```

Testikattavuusraportin luonti

```coverage run --branch -m pytest; coverage html```

