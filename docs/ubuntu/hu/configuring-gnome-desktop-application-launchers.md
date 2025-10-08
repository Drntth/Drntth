# Gnome Asztali Alkalmazásindítók Konfigurálása

---

> [:uk: English](../en/configuring-gnome-desktop-application-launchers.md) | :hungary: Magyar

---

## Cél

Ez az útmutató bemutatja, hogyan lehet konfigurálni az Ubuntu Gnome asztal bal oldalán megjelenő alkalmazásikonok indítási paramétereit. Ez magában foglalja a `~/.local/share/applications` könyvtárban található `.desktop` fájlok szerkesztését.

---

## Kulcsfogalmak

- **Desktop fájlok**: A `.desktop` fájlok határozzák meg, hogyan indul egy alkalmazás, beleértve annak nevét, ikonját és végrehajtási paramétereit.
- **Egyéni indítók**: Felhasználó által létrehozott `.desktop` fájlok olyan alkalmazásokhoz, amelyek nincsenek rendszer szinten telepítve.
- **Fájl helye**: A felhasználóspecifikus `.desktop` fájlok a `~/.local/share/applications` könyvtárban találhatók.

---

## Telepítés

Nincs szükség további telepítésre, mivel a `.desktop` fájlok kezelése beépített funkció a Gnome asztali környezetben.

---

## Alapvető Használat

1. **Keresse meg a `.desktop` fájlt**: Navigáljon a `~/.local/share/applications` könyvtárba, hogy megtalálja vagy létrehozza az alkalmazás `.desktop` fájlját.

2. **Szerkessze a `.desktop` fájlt**: Nyissa meg a fájlt egy szövegszerkesztővel:

  ```bash
  nano ~/.local/share/applications/example.desktop
  ```

3. **Módosítsa az Exec sort a kívánt paraméterekkel**: `Exec=/path/to/application --parameter1 --parameter2`

4. **Mentés és frissítés**: Mentse a fájlt, majd frissítse az asztali menüt:

  ```bash
  update-desktop-database ~/.local/share/applications/
  ```

5. **Tesztelje a konfigurációt**: Kattintson az ikonra az asztalon vagy az alkalmazás áttekintőben, hogy ellenőrizze a változtatásokat.

---

## Gyorsbillentyűk

- `Super + A`: Az alkalmazás áttekintő megnyitása.
- `Alt + F2`: Parancs futtatása.

---

## Legjobb Gyakorlatok

- Mindig készítsen biztonsági másolatot a `.desktop` fájlokról a módosítások előtt.
- Használjon abszolút elérési utakat az Exec mezőben, hogy elkerülje a problémákat.
- Azonnal tesztelje a változtatásokat, hogy megbizonyosodjon azok helyességéről.

---

## Gyakori Hibák

- **Helytelen elérési utak**: Ellenőrizze kétszer az elérési utakat és a paramétereket az Exec mezőben.
- **Gyorsítótár problémák**: Ha a változtatások nem jelennek meg, próbálja újraindítani a Gnome Shell-t: ```Alt + F2, majd írja be az `r` betűt és nyomja meg az Entert.```

---

## Példa Kód

### Általános Példa Indító

Az alábbi egy általános példa egy `.desktop` fájlra, amelynek neve [`example.desktop`](../../../code/gnome-desktop/example.desktop), és amely egy egyéni alkalmazásindító létrehozására használható.

A fájl használatához másolja azt a `~/.local/share/applications` könyvtárba, és nevezze át a kívánt alkalmazás nevére:

```bash
cp /code/example.desktop ~/.local/share/applications/application_name.desktop
```

Ezután nyissa meg a másolt fájlt, és módosítsa a paramétereket az alkalmazásának megfelelően:

- `Name`: Az alkalmazás neve (pl. "Egyéni Alkalmazás").
- `Comment`: Rövid leírás arról, hogy mit csinál az alkalmazás.
- `Exec`: A végrehajtandó parancs, beleértve a szükséges paramétereket (pl. `/path/to/application --parameter1 --parameter2`).
- `Icon`: Az alkalmazás ikonjának elérési útja.
- `Terminal`: Állítsa `false` értékre, ha az alkalmazás nem igényel terminált.
- `Type`: Mindig `Application` értékre állítsa.
- `Categories`: Adja meg a kategóriát (pl. `Utility`).

### Terminator Indító Példa

Az alábbi egy [`terminator.desktop`](../../../code/gnome-desktop/terminator.desktop) fájl példa, amely a Terminator terminál emulátort indítja egy adott elrendezéssel.

A fájl használatához másolja azt a saját könyvtárába, és módosítsa a `--layout` paramétert a saját konfigurációs elrendezésének nevére:

```bash
cp /code/terminator.desktop ~/.local/share/applications/terminator.desktop
```

Ezután mentse a fájlt, és frissítse az asztali menüt:

```bash
update-desktop-database ~/.local/share/applications/
```

---

## Források

- [Gnome Dokumentáció](https://help.gnome.org/users/gnome-help/stable/index.html): Hivatalos Gnome súgódokumentáció.
- [Ubuntu Közösségi Súgó Wiki](https://help.ubuntu.com/community): Közösség által készített súgóforrások Ubuntu felhasználók számára.
