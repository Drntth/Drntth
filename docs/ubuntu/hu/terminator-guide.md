# Terminator - Egy Linux terminálemulátor

---

> :uk: [English](../en/terminator-guide.md) | :hungary: Magyar

---

## Cél

A Terminator egy hatékony terminálemulátor, amely lehetővé teszi a felhasználók számára, hogy több terminál munkamenetet kezeljenek egyszerre. Olyan funkciókat kínál, mint a terminálok felosztása, egyedi elrendezések, szinkronizált gépelés és bővítmények támogatása, így ideális fejlesztők és rendszergazdák számára.

---

## Főbb fogalmak

- **Rácsos elrendezések**: A terminálok rácsszerű elrendezése a jobb szervezettség érdekében.
- **Egyedi profilok**: Egyedi beállítások meghatározása különböző munkafolyamatokhoz, például SSH vagy Git.
- **Szinkronizált gépelés**: Egyszerre több terminálban gépelhetsz, hogy parancsokat hajts végre több munkamenetben.
- **Bővítmények**: A funkcionalitás bővítése további funkciókkal, például terminálképernyőképekkel.

---

## Telepítés

A Terminator telepítése egyszerű, és egyetlen paranccsal elvégezhető:

- **Ubuntu esetén**:  

  ```bash
  sudo apt install terminator
  ```

---

## Hogyan használd a Terminator-t

Indítsd el a Terminator-t az alábbi parancs futtatásával a terminálban:

```bash
terminator
```

- **Terminál felosztása vízszintesen**: Használd a `Ctrl+Shift+O` billentyűkombinációt.
- **Terminál felosztása függőlegesen**: Használd a `Ctrl+Shift+E` billentyűkombinációt.
- **Aktív terminál törlése**: Használd a `Ctrl+Shift+X` billentyűkombinációt.
- **Terminálpanelek bezárása**: Kattints jobb gombbal a panelre, és válaszd a "Bezárás" lehetőséget.

---

## Gyorsbillentyűk

| Művelet                 | Gyorsbillentyű                               |
|-------------------------|----------------------------------------------|
| Vízszintes felosztás    | `Ctrl+Shift+O`                               |
| Függőleges felosztás    | `Ctrl+Shift+E`                               |
| Fül hozzáadása          | `Ctrl+Shift+T`                               |
| Panelek átméretezése    | `Ctrl+Shift+Arrow Keys`                      |
| Szinkronizált gépelés   | `Ctrl+Shift+I`                               |
| Aktív terminál törlése  | `Ctrl+Shift+X`                               |
| Munkamenet átnevezése   | `Alt+Shift+X`                                |
| Fül balra mozgatása     | `Alt+Shift+Left` vagy `Ctrl+Shift+PageUp`    |
| Fül jobbra mozgatása    | `Alt+Shift+Right` vagy `Ctrl+Shift+PageDown` |
| Következő fül           | `Ctrl+PageDown`                              |
| Előző fül               | `Ctrl+PageUp`                                |
| Panelek közötti fókusz  | `Alt+Arrow Keys`                             |

---

## Legjobb gyakorlatok

### Elrendezések mentése és betöltése

Használd a GUI beállítások szerkesztőjét az elrendezések mentéséhez és betöltéséhez különböző munkafolyamatokhoz. Ez lehetővé teszi, hogy gyorsan válts a különböző feladatokhoz igazított beállítások között.

- **Elrendezés mentése**: Az elrendezések automatikusan mentésre kerülnek a `~/.config/terminator/config` konfigurációs fájlba.
- **Elrendezés betöltése**

  - **Parancssoros módszer**: Használd az alábbi parancsot egy adott elrendezés betöltéséhez:

  ```bash
  terminator --layout=<layout_name>
  ```

  - **GUI/Gyorsbillentyűs módszer**:
    - Nyisd meg a Terminator ablakot.
    - Nyomd meg az `Alt + L` billentyűkombinációt az elrendezés kiválasztási menü megnyitásához, és töltsd be a saját konfigurációdat.
    - Alternatívaként kattints jobb gombbal a terminál ablakban, válaszd az **Elrendezések** lehetőséget, majd válaszd ki a saját konfigurációdat.

### Profilok használata

Hozz létre egyedi profilokat különböző feladatokhoz. A profilok lehetővé teszik, hogy egyedi beállításokat definiálj, például színeket, betűtípusokat és parancsokat különböző munkafolyamatokhoz.

Példa egy SSH profilra:

```ini
[[ssh]]
  background_darkness = 0.9
  background_type = transparent
  foreground_color = "#00ff00"
  title_hide_sizetext = True
```

### Bővítmények engedélyezése

Bővítsd a Terminator funkcionalitását bővítmények engedélyezésével. Például:

- **TerminalShot**: Képernyőképek készítése a terminálról.
- **LaunchpadCodeURLHandler**: URL-ek kezelése közvetlenül a terminálban.

A bővítmények engedélyezéséhez add hozzá őket a konfigurációs fájl `enabled_plugins` mezőjéhez:

```ini
[global_config]
  enabled_plugins = TerminalShot, LaunchpadCodeURLHandler
```

### Dinamikus beállítások

#### Dinamikus elrendezések

A Terminator lehetővé teszi az elrendezések dinamikus módosítását futásidőben:

- **Panelek átméretezése**:

  - Használd a `Ctrl+Shift+Arrow Keys` billentyűkombinációt a panelek dinamikus átméretezéséhez.

- **Panelek átrendezése**:

  - Húzd és ejtsd a paneleket az átrendezéshez.

#### Egyedi címek hozzárendelése

Hozzárendelhetsz egyedi címeket az egyes terminálpanelekhez, hogy jobban rendszerezhesd a munkaterületedet.

- **GUI használatával**: Kattints jobb gombbal a terminál panelre, és válaszd a "Cím beállítása" lehetőséget.
- **Parancssor használatával**: Indítsd el a Terminator-t egy egyedi címmel:

  ```bash
  terminator --title="<custom_title>"
  ```

#### Szinkronizált gépelés

A szinkronizált gépelés lehetővé teszi, hogy egyszerre több terminálban gépelj. Ez különösen hasznos, ha ugyanazokat a parancsokat kell végrehajtanod több szerveren.

- **Hogyan engedélyezd**:

  - Nyomd meg a `Ctrl+Shift+I` billentyűkombinációt a szinkronizált gépelés engedélyezéséhez.

- **Leírás**:

  - Az összes kiválasztott terminál egyszerre fogadja az inputot.

---

## Gyakori problémák

- **A Terminator nem indul el**: Győződj meg arról, hogy a Python telepítve van, és a megfelelő verziót használod, mivel a Terminator Python-alapú. Ha a probléma továbbra is fennáll, próbáld meg debug módban futtatni a Terminator-t, hogy részletesebb hibaüzeneteket kapj:

```bash
terminator --debug
```

- **Konfigurációs fájl sérülése**: Ha a konfigurációs fájl megsérül, töröld vagy nevezd át a `~/.config/terminator/config` fájlt, majd indítsd újra a Terminator-t az alapértelmezett konfiguráció újragenerálásához. Alternatív megoldásként telepítsd újra a Terminator-t:

  ```bash
  sudo apt install --reinstall terminator
  ```

- **Nem működő gyorsbillentyűk**: Győződj meg arról, hogy a gyorsbillentyűket nem írják felül más alkalmazások.

- **Elrendezések nem mentődnek megfelelően**: Az elrendezések nem mentődnek a Terminator bezárása után. Győződj meg arról, hogy a konfigurációs fájl írható, és hogy az elrendezést kifejezetten mented a GUI használatával vagy a konfigurációs fájl manuális szerkesztésével.

---

## Példa konfiguráció

Az alábbiakban egy Terminator konfigurációs fájl példát láthatsz, amely bemutatja, hogyan állíthatsz be profilokat, elrendezéseket és parancsokat. Ez a konfiguráció tartalmazza:

- **Profilok**: Egyedi profilok SSH és Git munkafolyamatokhoz.
- **Elrendezések**: Egy elrendezés több panellel, beleértve az SSH és Git parancsokat.
- **Parancsok**: Előre definiált parancsok specifikus munkafolyamatokhoz.

A teljes példakonfigurációs fájlt itt találod: [own-config-1](../../../code/terminator/own-config-1).

Íme egy példa arra, hogyan néz ki a Terminator egy egyedi elrendezéssel:

![Terminator Példa Elrendezés](../../../assets/ubuntu/own-config-1.png)

### Hogyan használd a példakonfigurációt

1. Másold a példakonfigurációs fájlt a Terminator konfigurációs könyvtárába:

```bash
cp /path/to/example/own-config-1 ~/.config/terminator/config
```

2. Nyisd meg a konfigurációs fájlt, és frissítsd a `#` megjegyzéseket, hogy tükrözzék a saját beállításaidat. Például:

- Cseréld le a `# own ssh connection` részt a saját SSH parancsodra, például:

```bash
command = ssh user@your-server.com
```

- Cseréld le a `# own path to git repository` részt a Git repód elérési útjára, például:

```bash
command = cd /home/your-user/git-repo && git pull && bash
```

3. Indítsd újra a Terminator-t:

```bash
terminator
```

3. Töltsd be az elrendezést:

  - **Parancssoros módszer**:
    Használd az alábbi parancsot egy adott elrendezés betöltéséhez:

    ```bash
    terminator --layout=own-config
    ```

  - **GUI/Gyorsbillentyűs módszer**:
    - Nyisd meg a Terminator ablakot.
    - Nyomd meg az `Alt + L` billentyűkombinációt az elrendezés kiválasztási menü megnyitásához, és töltsd be a saját konfigurációdat.
    - Alternatívaként kattints jobb gombbal a terminál ablakban, válaszd az **Elrendezések** lehetőséget, majd válaszd ki a saját konfigurációdat.

---

## Források

- [Terminator Dokumentáció](https://gnome-terminator.readthedocs.io/en/latest/index.html)
- [GitHub Repository](https://github.com/gnome-terminator/terminator)
- [Terminator Bővítmények](https://gnome-terminator.readthedocs.io/en/latest/plugins.html)
