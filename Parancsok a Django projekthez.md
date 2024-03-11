# DJANGO ALAPOK

---
> **==App/AFP1_Nagy_Projekt/main/db.sqlite3== --> ezt az adatbázist nem tölti fel Git-re ez mindenkinél egyedi, a lejjebb írt kóddal lehet feltölteni, ha nem generálja le a környezet létre kell hozni**
**VS Code Extensions/==SQLite Viewer== --> az oldal által kezelt adatbázis(db.sqlite3) megjelenítése a VS Code-ban**
**==Command Prompt== terminál megnyitása a VS Code-ban**

---

## BELÉPÉS A FEJLESZTŐI KÖRNYEZETBE

### Mappastruktúra

```plaintext
project --> gyökérmappa
├── project
| ├── settings.py --> függőségek hozzáadása
| └── urls.py --> elérési út függőségek
├── page --> új oldal létrehozása
| ├── models.py --> adatbázisműveletek (új tábla inicializálása)
| ├── urls.py --> elérési út meghatározása
| └── views.py --> megjelenítendő html oldal kezelése
├── static --> statikus elemek (stílus, képek)
| ├── css --> stílus oldalak
| └── img --> képek
├── templates --> html oldalak
| ├── base.html --> sablon az oldalakhoz
| ├── index.html --> főoldal, kiterjeszti a base.html-t
| ├── register.html
| └── login.html
├── db.sqlite3 --> adatbázis
└── manage.py --> kezeli a webszervert
└── requirements.txt
```

- `Scripts\activate` _// belép a python virtuális környezetébe_

```plaintext
Jelenlegi mappa:
    project
```

- `python manage.py runserver` _// a webszerver elindítása_
  - [http://127.0.0.1:8000/](http://127.0.0.1:8000/) _// webszerver elérése a böngészőben_
  - [http://127.0.0.1:8000/page/](http://127.0.0.1:8000/uj_oldal_neve/) _// létrehozott új oldal felületének elérése_
- `Ctrl + C`_// webszerver leállítása_
- `python manage.py migrate` _// a keletkezett változtatások elmentése, amikor a main mappa valamelyik python fájljában (settings.py) változás keletkezik_

---

## ÚJ OLDALAK HOZZÁADÁSA

```plaintext
Jelenlegi mappa:
    project
```

- `python manage.py startapp page` _// új oldal létrehozása, előtte mindig le kell állítani a szervert, majd a tesztelés előtt újra el kell indítani_

```plaintext
Jelenlegi fájl:
    app
    └── page
        └── views.py  --> a html oldal megjelenítése
```

```python
from django.shortcuts import render
from django.http import HttpResponse
def page(request):
    return HttpResponse("Új oldal szövege") # az oldal lekérésekor megjelenő szöveg
    return render(request, 'page.html') # a templates mappában lévő html fájl megjelenítése
```

```plaintext
Jelenlegi fájl:
    project
    └── page
        └── urls.py  --> elérési út, manuálisan kell létrehozni a fájlt
```

```python
from django.urls import path
from . import views
urlpatterns = [
    path('page/', views.page, name='page'), # az elérési útvonal megadása
]
```

> ha új oldalt hozunk létre hozzá kell adni az elérési útját az admin felülethez, hogy a böngésző keresősávjába [http://127.0.0.1:8000/page/](http://127.0.0.1:8000/page/) ilyen alapban rá lehessen keresni és megjelenítse az oldal tartalmát

```plaintext
Jelenlegi fájl:
    project
    └── project
        └── urls.py  --> az előbb létrehozott elérési utak hozzáadása a főprogramhoz
```

```python
from django.contrib import admin
from django.urls import include, path
urlpatterns = [
    path('', include('page.urls')), # új elérési út hozzáadása
    path('admin/', admin.site.urls),
]

```

---

## HTML OLDALAK KEZELÉSE I

> ha az egyes oldalaknak külön html fájlokat akarunk csinálni, akkor a templates mappába kell egy új html fájlt létrehozni

```plaintext
Jelenlegi fájl:
    project --> gyökérmappa
    └──  templates --> html oldalak
        ├── base.html --> sablon az oldalakhoz
        └── page.html --> az új oldal
```

```html
{% extends "base.html" %} --> a sablon meghívása
{% load static %} --> stílus és képek elérése

{% block title %}Cím{% endblock %}

{% block content %} --> html main tartalma

<link rel="stylesheet" href="{% static 'css/page.css' %}" type="text/css"/> --> hivatkozás a saját stílushoz is
{% endblock %}
```

> ezután a main beállításait módosítani kell úgy, hogy érzékelje a page mappát úgy mint egy oldalt

```plaintext
Jelenlegi fájl:
    project
    └── project
        └── settings.py  --> az előbb létrehozott elérési utak hozzáadása a főprogramhoz
```

```python
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'page', # itt kell hozzáadni az új oldalakat
    ]
```

- `python manage.py migrate` --> változtatások mentése

## ADATBÁZIS KEZELÉS

### az adott oldal adatbázisműveletei

```plaintext
Jelenlegi fájl:
    project
    └── page
        └── models.py 
```

```python
from django.db import models
class tabla_neve(models.Model): # új tábla inicializálása
    szoveg = models.CharField(max_length=255) # attribútumok hozzáadása
    szam = models.IntegerField()
    datum = models.DateField()
    idegen_kulcs = models.ForeignKey(masik_tabla_neve, on_delete=models.CASCADE, related_name="hivatkozási név")
    elsodleges_kulcs = models.CharField(max_length=100, primary_key=True) # ha nem adunk meg a rendszer generál egyet automatikusan
    valasztas = models.TextChoices("valaszthato1", "valaszthato2")
```

- `python manage.py makemigrations page` _// tábla létrehozása az adatbázisban_
- `python manage.py migrate` _// módosítások mentése_

#### adatbázis feltöltése elemekkel, ezek módosítása / törlése

- `python manage.py shell` _// a python virtuális környezetében a Python Shell_

> Kilépés: Ctrl + Z gomb lenyomására beír egy ^Z-t erre nyomni kell egy Enter-t

##### új elemek hozzáadása a táblához

```shell
>>> from page.models import tabla_neve # a tabla_neve tábla importálása
>>> tabla_neve.objects.all() # létrehoz egy üres tabla_neve táblát
>>> tabla_eleme = tabla_neve(szoveg='szöveg', szam=123) # egy új elem létrehozása az értékek megadásával
>>> tabla_eleme.save() # az új elem mentése
>>> tabla_neve.objects.all().values() # annak ellenőrzése, hogy a táblába fel-e vitte az új elemet
>>> tabla_eleme1 = tabla_neve(szoveg='szöveg', szam=123) # több elem felvitele a táblázatba
>>> tabla_eleme2 = tabla_neve(szoveg='szöveg', szam=123)
>>> tabla_eleme3 = tabla_neve(szoveg='szöveg', szam=123)
>>> tabla_eleme4 = tabla_neve(szoveg='szöveg', szam=123)
>>> tabla_eleme5 = tabla_neve(szoveg='szöveg', szam=123)
>>> elemek_lista = [tabla_eleme1, tabla_eleme2, tabla_eleme3, tabla_eleme4, tabla_eleme5]  # lista létrehozása
>>> for elem in elemek_lista: # ciklus létrehozása a lista kezelésére
>>>     elem.save() # elemek mentése
```

##### létező elemek módosítása a táblában

```shell
>>> from uj_oldal_neve.models import tabla_neve
>>> adott_elem = tabla_neve.objects.all()[index] # az adott indexű elem kiválasztása (az index helyére egy szám kell)
>>> adott_elem.szoveg # kiírja az adott elem szoveg attribútumának tartalmát
>>> adott_elem.szoveg = "új szöveg" # a kiválasztott elem a táblában lévő szoveg attribútumának megváltoztatása értékadással
>>> adott_elem.save()
```

##### elem törlése a táblából

```shell
>>> from uj_oldal_neve.models import tabla_neve
>>> adott_elem = tabla_neve.objects.all()[index]
>>> adott_elem.delete() # az adott elem törlése a táblából, ki fogja írni, hogy az elem mit tartalmazott
```

#### már meglévő tábla módosítása (új attribútumok hozzáadásával)

```plaintext
Jelenlegi fájl:
    project
    └── page
        └── models.py 
```

```python
from django.db import models
class tabla_neve(models.Model):
    szoveg = models.CharField(max_length=255)
    szam = models.IntegerField()
    datum = models.DateField()
    idegen_kulcs = models.ForeignKey(masik_tabla_neve, on_delete=models.CASCADE, related_name="hivatkozási név")
    elsodleges_kulcs = models.CharField(max_length=100, primary_key=True) // ha nem adunk meg a rendszer generál egyet automatikusan
    valasztas = models.TextChoices("valaszthato1", "valaszthato2")
    uj_szam = models.IntegerField() # új attribútumok hozzáadása
    uj_datum = models.DateField() # új attribútumok hozzáadása
```

- `py manage.py makemigrations page` _// új attribútumok hozzáadása esetén elmenti a változtatásokat (ebben az esetbe meg kell adni egy default értéket, de erre fog figyelmeztetni a program, egy választási lehetőséggel ahol a 2 beírása és Enter lenyomása után kell megadni az alapértéket, ha ezt korábban nem tettük meg)_
- `2` _// 2. lehetőség kiválasztása, majd Enter_
- `py manage.py makemigrations page`

```plaintext
Jelenlegi fájl:
    project
    └── page
        └── models.py 
```

```python
from django.db import models
class tabla_neve(models.Model):
    szoveg = models.CharField(max_length=255)
    szam = models.IntegerField()
    datum = models.DateField()
    idegen_kulcs = models.ForeignKey(masik_tabla_neve, on_delete=models.CASCADE, related_name="hivatkozási név")
    elsodleges_kulcs = models.CharField(max_length=100, primary_key=True) // ha nem adunk meg a rendszer generál egyet automatikusan
    valasztas = models.TextChoices("valaszthato1", "valaszthato2")
    uj_szam = models.IntegerField(null=True) # az előbb beírt parancsok itt adják hozzá a 'null=True' kiegészítést
    uj_datum = models.DateField(null=True)
```

- `python manage.py makemigrations page`
- `python manage.py migrate`
// ezután a meglévő mezőket az előzőekben leírtak szerint lehet az adott attribútumokra vonatkozóan feltölteni *1

## HTML OLDALAK KEZELÉSE II

```plaintext
Jelenlegi fájl:
    project --> gyökérmappa
    └──  templates --> html oldalak
        ├── base.html --> sablon az oldalakhoz
        └── page.html --> az új oldal
```

```html
{% extends "base.html" %}
{% load static %}

{% block title %}Adatbázis elemek kilistázása{% endblock %}

{% block content %}

    {% for elem in lista %} <!-- % elemek közé helyezet kód a Django nyelv logikája --> 
        <li>{{ elem.attributum1 }} {{ elem.attributum2 }}</li>
    {% endfor %}

<link rel="stylesheet" href="{% static 'css/kanban.css' %}" type="text/css"/>
{% endblock %}
```

---

# Modellek (Models)

---

Egy modell az adatokról szóló információk egyetlen, meghatározó forrása. Tartalmazza az adattárolás során szükséges alapvető mezőket és viselkedéseket. Általában minden modell egyetlen adatbázis táblához kapcsolódik.
Az alapok:
+ Minden modell egy Python osztály, ami a django.db.models.Model osztályból származik le.
+ A modell minden attribútuma egy adatbázis mezőt reprezentál.
+ Mindezekkel együtt a Django egy automatikusan generált adatbázis-hozzáférési API-t biztosít; lásd a Lekérdezések készítése részt.

```plaintext
Jelenlegi fájl:
    project
    └── page
        └── models.py 
```

```python
from django.db import models

class Person(models.Model):
    # id --> automatikusan generált
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
```
> A first_name és a last_name a modell mezői. Minden mezőt osztály attribútumként határoznak meg, és minden attribútum egy adatbázis oszlophoz kapcsolódik.

> Amint definiáltad a modelleket, közölnöd kell Djangóval, hogy használni fogod azokat a modelleket. Ezt úgy teheted meg, hogy szerkeszted a beállításfájlt, és a INSTALLED_APPS beállítást módosítod, hogy hozzáadd azon modul nevét, amely tartalmazza a models.py fájlt.
Például, ha az alkalmazásod modellei a myapp.models modulban találhatóak (ez az a csomagstruktúra, amelyet egy alkalmazásnak a manage.py startapp szkript létrehoz), akkor a INSTALLED_APPS beállításnak így kellene kinéznie:

```plaintext
Jelenlegi fájl:
    project
    └── project
        └── settings.py 
```

```python
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'page', # itt kell hozzáadni az új oldalakat
    ]
```

- `python manage.py makemigrations` 
- `python manage.py migrate`

---

## Mezők

A modell legfontosabb része - és az egyetlen kötelező része a modellnek - az adatbázis mezők listája, amelyet definiál. A mezőket osztály attribútumokkal határozzák meg. Ügyelj arra, hogy ne válassz mezőneveket, amelyek ütköznek a modellek API-jával, mint például clean, save vagy delete.

```python
from django.db import models

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()
```

---

### Mező típusok

A Django számos beépített mezőtípust tartalmaz; a teljes listát megtalálhatod a [modellmező referenciában](https://docs.djangoproject.com/en/5.0/ref/models/fields/#model-field-types). Ha a Django beépített mezői nem megfelelőek, könnyen írhatsz saját mezőket; lásd a [Hogyan lehet saját modellmezőket létrehozni](https://docs.djangoproject.com/en/5.0/howto/custom-model-fields/) című részt.

---

## Modellek több fájlban

Teljesen elfogadott egy modellt összekapcsolni egy másik alkalmazásból származóval. Ehhez importáld a kapcsolódó modellt a fájl tetején, ahol a modellt meghatározod. Ezután hivatkozz a másik modell osztályra, amikor szükséges. Például:

```python
from django.db import models
from geography.models import ZipCode

class Restaurant(models.Model):
    # ...
    zip_code = models.ForeignKey(
        ZipCode,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
```

---

## Modellek szervezése egy csomagba

A manage.py startapp parancs létrehoz egy alkalmazás szerkezetet, amely tartalmaz egy models.py fájlt. Ha sok modell van, akkor hasznos lehet őket külön fájlokban szervezni.

Ahhoz, hogy ezt megtehesd, hozz létre egy models csomagot. Távolítsd el a models.py-t, majd hozz létre egy myapp/models/ könyvtárat egy __init__.py fájllal, valamint a fájlokat, amelyekben tárolni kívánod a modelleket. Importálnod kell a modelleket a __init__.py fájlban.

```plaintext
Jelenlegi fájl:
    project --> gyökérmappa
    └── page --> adott oldal
        └──  models --> models csomag
            ├──  organic.py 
            ├──  synthetic.py  
            └── __init__.py --> modellek gyűjteménye
```

Például, ha a models könyvtárban van egy organic.py és egy synthetic.py fájl:

```python
from .organic import Person
from .synthetic import Robot
```

---

## Bővebben a modellekről [itt!](https://docs.djangoproject.com/en/5.0/topics/db/models/)

---

## Lekérdezések Python shell-ben [itt!](https://docs.djangoproject.com/en/5.0/topics/db/queries/)

---

## Migrációk (Migrations)

A migrációk a Django egyik módja annak, hogy átvezessék az általad végzett változtatásokat a modellekben (mező hozzáadása, modell törlése stb.) az adatbázis sémaszerkezetébe. Általában automatikusak, de tudnod kell, mikor kell migrációkat készíteni, mikor kell futtatni őket, és milyen gyakori problémákba ütközhetsz.

```django
python manage.py migrate [app_label] [migration_name]
python manage.py makemigrations [app_label [app_label ...]]
python manage.py sqlmigrate app_label migration_name
python manage.py showmigrations [app_label [app_label ...]]
```

---

### Migráció visszafordítása

A migrációkat vissza lehet fordítani a migrate paranccsal, azzal hogy megadod az előző migráció számát. Például, ha vissza akarod fordítani a books.0003 migrációt:

```python
python manage.py migrate books 0002
```

---

## Használható adatbázisok

Django hivatalosan támogatja az alábbi adatbázisokat:
+ PostgreSQL
+ MariaDB
+ MySQL
+ Oracle
+ SQLite

Ezenkívül számos adatbázis háttérendszer van, amelyeket harmadik felek biztosítanak:
+ CockroachDB
+ Firebird
+ Google Cloud Spanner
+ Microsoft SQL Server
+ Snowflake
+ TiDB
+ YugabyteDB

### PostgreSQL

> A szolgáltatásnév alapján való csatlakozáshoz a kapcsolódási szolgáltatásfájlban található szolgáltatásnevet, valamint a jelszót a jelszófájlból kell megadni. Ehhez meg kell adnod őket az adatbázis konfigurációjának OPTIONS részében a **DATABASES** beállításban:

```plaintext
Jelenlegi fájl:
    project
    └── project
        └── settings.py
```

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "OPTIONS": {
            "service": "my_service",
            "passfile": ".my_pgpass",
        },
    }
}
```

> **Szolgáltatásnév**:

```plaintext
Jelenlegi fájl:
    %APPDATA%\
    └── postgresql
        └── .pg_service.conf 
```

```conf
[my_service]
host=localhost
user=USER
dbname=NAME
port=5432
```

> **Jelszó**:

```plaintext
Jelenlegi fájl:
    %APPDATA%\
    └── postgresql
        └── pgpass.conf
```

```conf
localhost:5432:NAME:USER:PASSWORD
```

#### A PostgreSQL konfigurációjának optimalizálása

```plaintext
Jelenlegi fájl:
    %APPDATA%\
    └── postgresql
        └── postgresql.conf 
```

A Django számára az alábbi paraméterek szükségesek az adatbázis kapcsolatokhoz:

```conf
    client_encoding: 'UTF8',

    default_transaction_isolation: alapértelmezés szerint 'read committed', vagy az kapcsolat opciókban beállított érték (lásd alább),

    timezone:
        amikor a USE_TZ igaz, alapértelmezetten 'UTC', vagy a kapcsolathoz beállított TIME_ZONE érték,
        amikor a USE_TZ hamis, a globális TIME_ZONE beállítás értéke.
```

> Bővebben [itt!](https://docs.djangoproject.com/en/5.0/ref/databases/#postgresql-notes)

### MariaDB

> Bővebben [itt!](https://docs.djangoproject.com/en/5.0/ref/databases/#mariadb-notes)