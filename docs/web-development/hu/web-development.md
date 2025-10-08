# Webfejlesztés Jegyzetek

Ez a jegyzetgyűjtemény a webfejlesztés főbb területeit és technológiáit foglalja össze, rövid leírásokkal és hivatkozásokkal a részletesebb jegyzetekhez.

---

## Frontend

A frontend a felhasználó által közvetlenül látható és használt része a webalkalmazásnak. A frontend fejlesztés a felhasználói felület és élmény megvalósításáról szól. Itt a cél, hogy a tervek interaktív, reszponzív és akadálymentes alkalmazásokká váljanak.

- **HTML** - A weboldalak szerkezetének alapja. **HTML** (HyperText Markup Language) adja a weboldalak szerkezetét, tartalmi elemeket (címek, bekezdések, űrlapok, képek, menük) határoz meg. Az újabb HTML5 szabvány szemantikus elemeket is tartalmaz, amelyek javítják az akadálymentességet és a keresőoptimalizálást.
- **CSS** - Stílusok, megjelenés, reszponzivitás. **CSS** (Cascading Style Sheets) felel a megjelenésért: tipográfia, színek, elrendezés, reszponzivitás (Flexbox, Grid, media query-k), animációk és változók. A modern CSS lehetővé teszi a mobilbarát, látványos felületek kialakítását.
- **[JavaScript](../../frontend/hu/javascript.md)** - Interaktivitás, dinamikus tartalom. **JavaScript** teszi dinamikussá a weboldalakat. Segítségével valósul meg az interaktivitás, az űrlapellenőrzés, az aszinkron kommunikáció (AJAX, Fetch API, WebSockets), valamint a frontendes keretrendszerek használata. A modern JavaScript (ES6+) új szintaxist, modulokat, osztályokat és fejlett funkciókat kínál.

### Keretrendszerek és könyvtárak

A fejlesztést jelentősen gyorsítják a keretrendszerek és könyvtárak, amelyek előre elkészített komponenseket, eszközöket és sablonokat kínálnak.

- **React:** Komponensalapú JavaScript könyvtár, amely hatékonyan kezeli a felhasználói felület változásait.
- **Angular:** TypeScript-alapú, komplex webalkalmazásokhoz tervezett keretrendszer.
- **Vue.js:** Egyszerű, reaktív JavaScript keretrendszer, amely gyors fejlesztést tesz lehetővé.
- **jQuery:** Egyszerűsíti a DOM-kezelést, eseménykezelést és AJAX-hívásokat.
- **Bootstrap:** Előre elkészített CSS és JavaScript komponensek, amelyekkel gyorsan készíthető reszponzív, mobilbarát felület.

---

## Backend

A backend a szerveroldali logikáért, adatkezelésért és üzleti folyamatokért felelős. A backend fejlesztés a szerveroldali programozásról, adatbázis-kezelésről és üzleti logikáról szól. A szerver oldali kód kezeli a kliens kéréseit, adatbázis-műveleteket végez, és dinamikus tartalmat generál.

- **Python:** Könnyen tanulható, sokoldalú nyelv.  
  - **Django:** Nagy, összetett projektekhez, beépített admin, biztonság és adatbázis-kezelés.
  - **Flask:** Egyszerűbb, rugalmasabb, kisebb alkalmazásokhoz vagy API-khoz.
- **Ruby:** Tiszta szintaxis, fejlesztőbarát.  
  - **Ruby on Rails:** Gyors prototípus-készítés, beépített megoldások.
- **PHP:** Kifejezetten webfejlesztésre tervezett szerveroldali nyelv.  
  - **Laravel:** Modern PHP keretrendszer, elegáns szintaxissal és sok beépített funkcióval.
- [Node.js](../../backend/hu/nodejs.md): JavaScript futtatókörnyezet szerveroldalon.  
  - **Express**: Minimalista, rugalmas keretrendszer API-khoz és webalkalmazásokhoz.
- **Java / C#:** Nagyvállalati alkalmazásokhoz, magas biztonság és teljesítmény.  
  - **Spring Boot (Java):** Előre konfigurált, könnyen bővíthető.
  - **.NET (C#):** Microsoft által fejlesztett, nagyvállalati környezetben elterjedt.

---

## Verziókezelés

A verziókezelő rendszerek (pl. Git) lehetővé teszik a forráskód változásainak nyomon követését, a csapatmunkát, a visszaállítást és a fejlesztési ágak kezelését. A GitHub, GitLab vagy Bitbucket platformokon könnyen megoszthatod projektjeidet, és együttműködhetsz más fejlesztőkkel.

---

## Adatbázis-kezelés

Az adatbázisok (SQL vagy NoSQL) tárolják és kezelik az alkalmazások adatait. Az SQL adatbázisok (pl. MySQL, PostgreSQL) relációs szerkezetűek, míg a NoSQL adatbázisok (pl. MongoDB, Firebase) rugalmasabb adattárolást kínálnak. Fontos a CRUD műveletek, indexelés és adatkapcsolatok ismerete.

---

## Reszponzív tervezés

A reszponzív design biztosítja, hogy a weboldalak minden eszközön (asztali, tablet, mobil) jól jelenjenek meg. Ehhez rugalmas elrendezések, fluid grid-ek, media query-k, valamint keretrendszerek (pl. Bootstrap, Tailwind CSS) használata szükséges. A mobilbarát, akadálymentes felületek ma már alapkövetelménynek számítanak.

---

## API-k és integráció

Az API-k lehetővé teszik külső szolgáltatások vagy adatok elérését, integrálását. A REST és GraphQL API-k segítségével dinamikusan jeleníthető meg adat, és interaktív, összetett alkalmazások építhetők. Fontos az autentikáció, a WebSocket-ek és a cache-elés ismerete.

---

> **Tipp:** A részletes jegyzetekhez kattints a fenti linkekre!
