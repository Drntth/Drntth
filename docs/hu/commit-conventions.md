# Commit Konvenciók

> :uk: [English](docs/commit-conventions.md) | :hungary: Magyar

**Cél**: A commit üzenetek egységesítése az átláthatóság és a projekt történetének jobb követhetősége érdekében.

---

## Formátumok & Példák

### Egyszerű Formátum

```plaintext
<típus>(<terület>): <rövid összefoglaló>
```

```bash
docs: CHANGELOG helyesírás javítása
```

### Konvencionális Commit Formátum

```plaintext
<típus>[opcionális terület]: <leírás>

[opcionális törzs]

[opcionális lábléc(ek)]
```

```bash
feat(auth): felhasználói bejelentkezési végpont hozzáadása

- POST /login végpont implementálása
- JWT token generálás hozzáadása
- Felhasználó modell validáció frissítése

Closes #45
```

### Példa Bash parancs

```bash
git commit -m "feat(auth): felhasználói bejelentkezési végpont hozzáadása" \
  -m "- POST /login végpont implementálása\n" \
  -m "- JWT token generálás hozzáadása\n" \
  -m "- Felhasználó modell validáció frissítése\n\n" \
  -m "Closes #45"
```

---

## Commit Típusok & Terület

- **feat**: Új funkció
- **fix**: Hibajavítás
- **docs**: Dokumentáció módosítás
- **style**: Kódstílus változás (formázás, szóközök)
- **refactor**: Kód refaktorálás
- **test**: Tesztek hozzáadása vagy frissítése
- **chore**: Karbantartási feladatok (pl. függőségek frissítése)

> **Terület**: Az érintett modul, komponens vagy terület (pl. `auth`, `ui`, `api`)

---

## Commit üzenet felépítése

### Leírás

- Rövid, tömör összefoglaló a változásról (legfeljebb 50 karakter)

### Törzs (Opcionális)

- Részletes magyarázat a változásról
- Használj felsorolást az átláthatóságért
- Írd le, mit és miért változtattál

### Lábléc (Opcionális)

- Hivatkozás hibajegyekre vagy pull requestekre (pl. `Closes #123`)

---

## Commitok visszavonása

- A commitok visszavonásához használd a `revert:` típust.

  Példa:

  ```plaintext
  revert: soha többé ne beszéljünk a tészta incidensről

  Hivatkozások: 676104e, a215868
  ```

  Example Bash Command:

  ```bash
  git revert <commit-hash>
  # Példa: git revert 676104e
  ```

  > Tipp: Ha rossz commit típust használsz, `git rebase -i`-vel javíthatod merge vagy release előtt.

---

## Tippek, kis- és nagybetűk, legjobb gyakorlatok

- A commit típusok nem érzékenyek a kis- és nagybetűkre, de használj egységes írásmódot.
- Írj világos, tömör üzeneteket
- Használj jelen időt (pl. „funkció hozzáadása”, ne „hozzáadott funkció”)
- Tartsd a sorhosszt 72 karakter alatt
- Válaszd el a tárgyat a törzstől egy üres sorral
- Ha nem szabványos commit típust használsz, a tooling figyelmen kívül hagyhatja, de nem kritikus.
- Nem minden közreműködőnek kell követnie a szabványt; a maintainer-ek squash merge során javíthatják az üzeneteket.
- Ha egy commit több típusba is illik, bontsd szét több commitra az átláthatóságért.

---

## Git Hook Szkript

A konvencionális commit üzenetformátum automatikus ellenőrzéséhez használhatsz szerver oldali git hookot:

Hozd létre az alábbi fájlt a repository mappában `.git/hooks/pre-receive` néven:

```bash
#!/usr/bin/env bash

# Pre-receive hook that will block commits with messages that do not follow regex rule
commit_msg_type_regex='feat|fix|refactor|style|test|docs|build'
commit_msg_scope_regex='.{1,20}'
commit_msg_description_regex='.{1,100}'
commit_msg_regex="^(${commit_msg_type_regex})(\(${commit_msg_scope_regex}\))?: (${commit_msg_description_regex})$"
merge_msg_regex="^Merge branch '.+'$"

zero_commit="0000000000000000000000000000000000000000"
excludeExisting="--not --all"
error=""

while read oldrev newrev refname; do
    if [ "$newrev" = "$zero_commit" ]; then
      continue
    fi
    if [ "$oldrev" = "$zero_commit" ]; then
      rev_span=`git rev-list $newrev $excludeExisting`
    else
      rev_span=`git rev-list $oldrev..$newrev $excludeExisting`
    fi
    for commit in $rev_span; do
      commit_msg_header=$(git show -s --format=%s $commit)
      if ! [[ "$commit_msg_header" =~ (${commit_msg_regex})|(${merge_msg_regex}) ]]; then
        echo "$commit" >&2
        echo "ERROR: Invalid commit message format" >&2
        echo "$commit_msg_header" >&2
        error="true"
      fi
    done
done

if [ -n "$error" ]; then
    exit 1
fi
```

A hook futtathatóvá tétele:

```bash
chmod +x .git/hooks/pre-receive
```

---

## Források

- [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
- [Git Commit Guidelines](https://github.com/angular/angular/blob/main/CONTRIBUTING.md#commit)
- [Conventional Commit Messages](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13)

---

*Utoljára frissítve: 2025.08.02.*
