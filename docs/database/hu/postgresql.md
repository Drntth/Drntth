# PostgreSQL

---

> [:uk: English](../en/) | :hungary: Magyar

**Cél**: A PostgreSQL egy erőteljes, nyílt forráskódú objektum-relációs adatbázis-kezelő rendszer. Széles körű terhelések kezelésére tervezték, egyetlen gépektől nagy webszolgáltatásokig, és ismert a megbízhatóságáról, funkciókészletéről és bővíthetőségéről. A PostgreSQL támogatja a fejlett adattípusokat, teljes ACID megfelelést, és jól testreszabható különböző felhasználási esetekhez.

---

## Kulcsfogalmak

### ACID megfelelés

A PostgreSQL teljes mértékben ACID-kompatibilis, ami azt jelenti, hogy garantálja az Atomiát (Atomicity), Következetességet (Consistency), Elkülönítést (Isolation) és Tartósságot (Durability) minden tranzakcióra. Ez biztosítja, hogy az adatbázis-műveletek megbízhatóak: vagy az összes változtatás végbemenet egy tranzakción belül, vagy egyik sem, és az adatbázis konzisztens állapotban marad hiba esetén is.

### Bővíthetőség

A PostgreSQL nagy mértékben bővíthető. Saját adattípusokat, operátorokat, függvényeket és akár eljárási nyelveket is definiálhatsz. Olyan kiterjesztések, mint a `hstore`, `uuid-ossp` és `pg_trgm` hozzáadhatók a funkcionalitás növeléséhez, így a PostgreSQL sokféle feladathoz alkalmazkodik.

### MVCC (Multi-Version Concurrency Control)

Az MVCC lehetővé teszi, hogy több tranzakció fusson egyszerre anélkül, hogy kölcsönösen zavarnák egymást. Ahelyett, hogy az egész adatbázist zárolná, a PostgreSQL több verziót tart az adatokból, ami magas párhuzamosságot és jó teljesítményt biztosít olvasási és írási műveleteknél.

### Sémák

A sémák logikai tárolók az adatbázis-objektumok (táblák, nézetek, függvények stb.) számára. Segítenek az adatok szervezésében, a jogosultságok kezelésében és az elnevezési ütközések elkerülésében, különösen nagy vagy többbérlős környezetekben.
Lásd a példakódot lent.

### Indexek

Az indexek speciális keresőtáblák, amelyeket az adatbázis-motor használhat az adatok gyorsabb lekérdezéséhez. A PostgreSQL több indextípust támogat (B-tree, Hash, GiST, GIN, BRIN), amelyek különböző lekérdezési mintákhoz és adattípusokhoz optimalizáltak, javítva a teljesítményt nagy adathalmazok esetén.
Lásd a példakódot lent.

### Replikáció

A PostgreSQL beépített támogatást nyújt mind a streaming, mind a logikai replikációhoz. A streaming replikáció egy tartalékszervert tart szinkronban a primerrel, míg a logikai replikáció lehetővé teszi az adatok szelektív replikálását az adatbázisok között, támogatva a magas elérhetőséget és a skálázást.

### Foreign Data Wrappers (FDW)

A FDW-k lehetővé teszik, hogy a PostgreSQL külső adatforrásokhoz (más adatbázisok, fájlok stb.) csatlakozzon, és úgy kérdezze le azokat, mintha helyi táblák lennének. Ez adatintegrációt és federációt tesz lehetővé különböző rendszerek között.

---

## Telepítés

- **Ubuntu esetén**:  

  ```bash
  sudo apt update
  sudo apt install postgresql postgresql-contrib
  ```

Ez telepíti a PostgreSQL szervert és néhány hasznos kiegészítőt.

---

## Alapvető használat

- **Szolgáltatás indítása/leállítása (Ubuntu)**:

  ```bash
  sudo systemctl start postgresql
  sudo systemctl stop postgresql
  sudo systemctl status postgresql
  ```

- **psql shell elérése**:

  ```bash
  sudo -u postgres psql
  ```

- **Adatbázis és felhasználó létrehozása**: Lásd a példakódot lent.

- **Kapcsolódás Pythonból (psycopg2) és alapvető műveletek végrehajtása**: Lásd a példakódot lent.

- **Alapvető SQL műveletek**: Lásd a példakódot lent.

---

## Gyors parancsok

- `\l` - Adatbázisok listázása a psql-ben
- `\dt` - Táblák listázása az aktuális adatbázisban
- `\c dbname` - Csatlakozás egy másik adatbázishoz
- `\q` - Kilépés a psql-ből
- Nyíl billentyűk, Tab kiegészítés és parancs előzmények használata a psql shellben

---

## Legjobb gyakorlatok

- Használj paraméterezett lekérdezéseket az SQL injection elkerülésére. Lásd a példakódot lent.
- Rendszeresen készíts mentést az adatbázisokról `pg_dump` vagy `pg_basebackup` használatával.
- Figyeld a teljesítményt `EXPLAIN` és `pg_stat_statements` segítségével.
- Alkalmazd a biztonsági frissítéseket és korlátozd a hálózati hozzáférést.
- Normalizáld az adatokat, de szükség esetén denormalizálj a jobb teljesítményért.
- Használj kapcsolat poolingot webalkalmazásoknál.
- Dokumentáld a sémaváltozásokat és használj migrációkat.

---

## Gyakori buktatók

- **Nem megfelelő hitelesítés beállítása**: Mindig konfiguráld a `pg_hba.conf` fájlt és használj erős jelszavakat.
- **Mentések figyelmen kívül hagyása**: Ütemezz rendszeres mentéseket az adatvesztés elkerülésére.
- **Indexek hiánya**: Az indexek nélküli lekérdezések lassú teljesítményhez vezethetnek.
- **Erőforrás-korlátozások**: Ne konfiguráld elégtelenül a memóriát és kapcsolatbeállításokat az adott terheléshez.
- **Hosszú ideig futó tranzakciók**: Asztaltömörödést (table bloat) és zárolási problémákat okozhatnak.

---

## Példa kód

- A sémák kezelésére szolgáló példa kód a [code könyvtárban található](../../../code/postgresql/schemas.sql).
- Az indexekhez kapcsolódó példa kód a [code könyvtárban található](../../../code/postgresql/indexes.sql).
- Adatbázis és felhasználó létrehozásához példa kód a [code könyvtárban található](../../../code/postgresql/create_database_and_user.sql).
- Pythonból történő kapcsolódásra és lekérdezések (SELECT, INSERT, UPDATE, DELETE, DDL) végrehajtására példa kód a [code könyvtárban található](../../../code/postgresql/connect_from_python.py).
- Alapvető SQL műveletek példa kódja a [code könyvtárban található](../../../code/postgresql/basic_sql_operations.sql).
- Paraméterezett lekérdezések használatára példa kód a [code könyvtárban található](../../../code/postgresql/parameterized_queries.py).

---

## Források

- [PostgreSQL Official Documentation](https://www.postgresql.org/docs/): Átfogó referencia és útmutatók.
- [Postgres Guide](https://postgresguide.com/): Gyakorlati tippek és magyarázatok a napi használathoz.
- [psycopg2 Documentation](https://www.psycopg.org/docs/): Python kliens könyvtár a PostgreSQL-hez.
- [DigitalOcean PostgreSQL Tutorials](https://www.digitalocean.com/community/tags/postgresql): Lépésről lépésre útmutatók a beállításhoz és kezeléshez.

---

*Last updated at: 2025.10.17.*
