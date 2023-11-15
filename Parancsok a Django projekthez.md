# DJANGO ALAPOK

---
> **==App/AFP1_Nagy_Projekt/main/db.sqlite3== --> ezt az adatbázist nem tölti fel Git-re ez mindenkinél egyedi, a lejjebb írt kóddal lehet feltölteni, ha nem generálja le a környezet létre kell hozni**
**VS Code Extensions/==SQLite Viewer== --> az oldal által kezelt adatbázis(db.sqlite3) megjelenítése a VS Code-ban**
**==Command Prompt== terminál megnyitása a VS Code-ban**

---

## BELÉPÉS A FEJLESZTŐI KÖRNYEZETBE

### Mappastruktúra

```plaintext
App / AFP1_Nagy_Project --> Python virtuális környezet mappa
├── main --> Django projekt mappa
| ├── main
| | ├── settings.py --> függőségek hozzáadása
| | └── urls.py --> elérési út függőségek
| ├── users --> users oldal, új oldal létrehozása
| | ├── templates --> html oldalak
| | | └── all_users.html 
| | ├── models.py --> adatbázisműveletek (új tábla inicializálása)
| | ├── urls.py --> elérési út meghatározása
| | └── views.py --> megjelenítendő html oldal kezelése
| ├── db.sqlite3 --> adatbázis
| └── manage.py --> kezeli a webszervert
├── Scripts
| └── activate --> belép a Python virtuális környezetbe
├── .gitignore
└── requirements.txt
```

```plaintext
Jelenlegi mappa:
    App
    └── AFP1_Nagy_Project
```

- `Scripts\activate` _// belép a python virtuális környezetébe_

```plaintext
Jelenlegi mappa:
    App
    └── AFP1_Nagy_Project
        └── main
```

- `python manage.py runserver` _// a webszerver elindítása_
  - [http://127.0.0.1:8000/](http://127.0.0.1:8000/) _// webszerver elérése a böngészőben_
  - [http://127.0.0.1:8000/users/](http://127.0.0.1:8000/uj_oldal_neve/) _//users oldal elérése_
  - [http://127.0.0.1:8000/uj_oldal_neve/](http://127.0.0.1:8000/uj_oldal_neve/) _// létrehozott új oldal felületének elérése_
- `Ctrl + C`_// webszerver leállítása_
- `python manage.py migrate` _// a keletkezett változtatások elmentése, amikor a main mappa valamelyik python fájljában (settings.py) változás keletkezik_

---

## ÚJ OLDALAK HOZZÁADÁSA

```plaintext
Jelenlegi mappa:
    App
    └── AFP1_Nagy_Project
        └── main
```

- `python manage.py startapp uj_oldal_neve` _// új oldal létrehozása, előtte mindig le kell állítani a szervert, majd a tesztelés előtt újra el kell indítani_

```plaintext
Jelenlegi fájl:
    App
    └── AFP1_Nagy_Project
        └── main
            └── uj_oldal_neve
                └── views.py  --> a html oldal megjelenítése
```

```python
from django.shortcuts import render
from django.http import HttpResponse
def uj_oldal_neve(request):
    return HttpResponse("Új oldal szövege") # az oldal lekérésekor megjelenő szöveg
```

```plaintext
Jelenlegi fájl:
    App
    └── AFP1_Nagy_Project
        └── main
            └── uj_oldal_neve
                └── urls.py  --> elérési út, manuálisan kell létrehozni a fájlt
```

```python
from django.urls import path
from . import views
urlpatterns = [
    path('uj_oldal_neve/', views.uj_oldal_neve, name='uj_oldal_neve'), # az elérési útvonal megadása
]
```

> ha új oldalt hozunk létre hozzá kell adni az elérési útját az admin felülethez, hogy a böngésző keresősávjába [http://127.0.0.1:8000/uj_oldal_neve/](http://127.0.0.1:8000/uj_oldal_neve/) ilyen alapban rá lehessen keresni és megjelenítse az oldal tartalmát

```plaintext
Jelenlegi fájl:
    App
    └── AFP1_Nagy_Project
        └── main
            └── main
                └── urls.py  --> az előbb létrehozott elérési utak hozzáadása a főprogramhoz
```

```python
from django.contrib import admin
from django.urls import include, path
urlpatterns = [
    path('', include('uj_oldal_neve.urls')), # új elérési út hozzáadása
    path('admin/', admin.site.urls),
]

```

---

## HTML OLDALAK KEZELÉSE I

> ha az egyes oldalaknak külön html fájlokat akarunk csinálni, akkor az adott oldal mappájába létre kell hozni egy templates mappát ahol elhelyezhetőek a html fájlokat

```plaintext
Jelenlegi fájl:
    App
    └── AFP1_Nagy_Project
        └── main
            └── uj_oldal_neve
                └── templates  --> ezt a mappát létre kell hozni
                    └── uj_html.html  --> ide kell létrehozni a html oldalakat
```

```html
<!DOCTYPE html>
<html>
<body>
<h1>Létrehoztál egy új oldalt</h1>
<p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Tempore quisquam maiores vel, in illo laborum cumque quae voluptate qui dignissimos ut rerum illum, veritatis nobis voluptatum est eligendi, sequi excepturi?</p>
</body>
</html>
```

> ebben az esetben meg kell változtatni az adott oldal views.py fájljának tartalmát

```plaintext
Jelenlegi fájl:
    App
    └── AFP1_Nagy_Project
        └── main
            └── uj_oldal_neve
                └── views.py 
```

```python
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
def uj_oldal_neve(request):
    template = loader.get_template('uj_oldal_neve.html') # ide kell a templates mappába létrehozott html fájl neve
    return HttpResponse(template.render())
```

> ezután a main beállításait módosítani kell úgy, hogy érzékelje az uj_oldal_neve mappát úgy mint egy oldalt

```plaintext
Jelenlegi fájl:
    App
    └── AFP1_Nagy_Project
        └── main
            └── main
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
        'uj_oldal_neve', # itt kell hozzáadni az új oldalakat
    ]
```

- `python manage.py migrate`

## ADATBÁZIS KEZELÉS

### az adott oldal adatbázisműveletei

```plaintext
Jelenlegi fájl:
    App
    └── AFP1_Nagy_Project
        └── main
            └── uj_oldal_neve
                └── models.py 
```

```python
from django.db import models
class tabla_neve(models.Model): # új tábla inicializálása
    szoveg = models.CharField(max_length=255) # attribútumok hozzáadása
    szam = models.IntegerField()
    datum = models.DateField()
    idegen_kulcs = models.ForeignKey(masik_tabla_neve, on_delete=models.CASCADE)
    elsodleges_kulcs = models.CharField(max_length=100, primary_key=True) # ha nem adunk meg a rendszer generál egyet automatikusan
    valasztas = models.TextChoices("valaszthato1", "valaszthato2")
```

- `python manage.py makemigrations uj_oldal_neve` _// tábla létrehozása az adatbázisban_
- `python manage.py migrate` _// módosítások mentése_
- `python manage.py sqlmigrate uj_oldal_neve 0001` _// SQL parancsok megtekintése (a 0001 az adott változatás, ha másik módosítás SQL parancsait szeretnénk megnézni, akkor az uj_oldal_neve/migrations mappában vannak az adott számú változtatások között)_

#### adatbázis feltöltése elemekkel, ezek módosítása / törlése

- `python manage.py shell` _// a python virtuális környezetében a Python Shell_

> Kilépés: Ctrl + Z gomb lenyomására beír egy ^Z-t erre nyomni kell egy Enter-t

##### új elemek hozzáadása a táblához

```shell
>>> from uj_oldal_neve.models import tabla_neve # a tabla_neve tábla importálása
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
    App
    └── AFP1_Nagy_Project
        └── main
            └── uj_oldal_neve
                └── models.py 
```

```python
from django.db import models
class tabla_neve(models.Model):
    szoveg = models.CharField(max_length=255)
    szam = models.IntegerField()
    datum = models.DateField()
    idegen_kulcs = models.ForeignKey(masik_tabla_neve, on_delete=models.CASCADE)
    elsodleges_kulcs = models.CharField(max_length=100, primary_key=True) // ha nem adunk meg a rendszer generál egyet automatikusan
    valasztas = models.TextChoices("valaszthato1", "valaszthato2")
    uj_szam = models.IntegerField() # új attribútumok hozzáadása
    uj_datum = models.DateField() # új attribútumok hozzáadása
```

- `py manage.py makemigrations uj_oldal_neve` _// új attribútumok hozzáadása esetén elmenti a változtatásokat (ebben az esetbe meg kell adni egy default értéket, de erre fog figyelmeztetni a program, egy választási lehetőséggel ahol a 2 beírása és Enter lenyomása után kell megadni az alapértéket, ha ezt korábban nem tettük meg)_
- `2` _// 2. lehetőség kiválasztása, majd Enter_
- `py manage.py makemigrations uj_oldal_neve`

```plaintext
Jelenlegi fájl:
    App
    └── AFP1_Nagy_Project
        └── main
            └── uj_oldal_neve
                └── models.py 
```

```python
from django.db import models
class tabla_neve(models.Model):
    szoveg = models.CharField(max_length=255)
    szam = models.IntegerField()
    datum = models.DateField()
    idegen_kulcs = models.ForeignKey(masik_tabla_neve, on_delete=models.CASCADE)
    elsodleges_kulcs = models.CharField(max_length=100, primary_key=True) // ha nem adunk meg a rendszer generál egyet automatikusan
    valasztas = models.TextChoices("valaszthato1", "valaszthato2")
    uj_szam = models.IntegerField(null=True) # az előbb beírt parancsok itt adják hozzá a 'null=True' kiegészítést
    uj_datum = models.DateField(null=True)
```

- `python manage.py makemigrations uj_oldal_neve`
- `python manage.py migrate`
// ezután a meglévő mezőket az előzőekben leírtak szerint lehet az adott attribútumokra vonatkozóan feltölteni *1

## HTML OLDALAK KEZELÉSE II

```plaintext
Jelenlegi fájl:
    App
    └── AFP1_Nagy_Project
        └── main
            └── uj_oldal_neve
                └── templates 
                    └── adatbazis_elemek_kilistazasa  --> ez a html fogja kilistázni az összes elemét az adatbázisnak
```

```html
<!DOCTYPE html>
<html>
<body>
<h1>Adatbázis elemek kilistázása</h1>
<ul>
    {% for elem in lista %} <!-- % elemek közé helyezet kód a Django nyelv logikája --> 
        <li>{{ elem.attributum1 }} {{ elem.attributum2 }}</li>
    {% endfor %}
</ul>
</body>
</html>
```

```plaintext
Jelenlegi fájl:
    App
    └── AFP1_Nagy_Project
        └── main
            └── uj_oldal_neve
                └── views.py 
```

> ezután meg kell változatni a `views.py` fájlban az oldal elérését / importálni kell a táblát

```python
from django.http import HttpResponse
from django.template import loader
from .models import tabla_neve
def tabla_neve_listazas(request):
    lista = tabla_neve.objects.all().values()
    template = loader.get_template('adatbazis_elemek_kilistazasa.html')
    context = {
        'lista': lista,
    }
    return HttpResponse(template.render(context, request))
```
