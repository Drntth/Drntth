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

```plaintext
Jelenlegi fájl:
    App
    └── AFP1_Nagy_Project
        └── main
            └── uj_oldal_neve
                └── views.py 
```