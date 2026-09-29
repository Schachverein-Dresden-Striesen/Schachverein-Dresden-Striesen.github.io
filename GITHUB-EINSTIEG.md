# GitHub für Anfänger – Dein erster Beitrag zur Vereinswebseite

**Du möchtest einen Turnierbericht, eine Ankündigung oder andere Inhalte für unsere Website hinzufügen?** Dieser Leitfaden zeigt dir, wie es funktioniert – Schritt für Schritt und ohne Jargon.

**Hinweis:** Die GitHub-Oberfläche ist auf Englisch. Falls du dich unsicher fühlst, nutze die Browser-Übersetzung (rechts-Klick → Übersetzen) oder folge diesem Leitfaden als Anleitung.

---

## Schnellstart: Dein erster Beitrag

**Du möchtest schnell einen neuen Turnierbericht oder eine Ankündigung hinzufügen?** Hier ist der kürzeste Weg:

1. Öffne unser [GitHub-Repository](https://github.com/Schachverein-Dresden-Striesen/Schachverein-Dresden-Striesen.github.io) im Browser.
2. Melde dich mit deinem GitHub-Konto an.
3. Navigiere zu dem Ordner, in den dein Text gehört:
   - **Neue Seite?** → Ordner `pages`
   - **Turnierbericht?** → Ordner `pages/turnierberichte`
   - **Ankündigung?** → Ordner `pages`
4. Klicke auf **Add file** und wähle **Create new file**. Gib einen Namen ein, z. B. `2026-09-20-mein-turnierbericht.md`.
5. Schreibe deinen Text. (Formatierungsbeispiele findest du weiter unten.)
6. Klicke **Commit changes** und bestätige. GitHub speichert deine Änderung automatisch.
7. Nach ein paar Sekunden erscheint dein Text auf der Website!

> **Das funktioniert nur für kleine Änderungen über den Browser. Für größere Arbeiten (viele Dateien, Bilder hochladen) siehe die erweiterte Anleitung am Ende.**

---

## Grundlagen: Text schreiben und formatieren

### Markdown-Formatierung

**Markdown ist eine einfache Sprache zur Formatierung von Text.** Du musst nichts über HTML oder Code wissen – einfache Zeichen wie `#`, `*` und `-` machen dein Text formatiert und lesbar.

**Hier sind die wichtigsten Formatierungen:**

```markdown
# Das ist eine große Überschrift
## Das ist eine kleinere Überschrift
### Noch kleiner

**Das ist fettgedruckter Text** (wichtig!)
_Das ist kursiver Text_ (Betonung)

- Das ist eine Aufzählung
- Mit mehreren Punkten

1. Das ist eine nummerierte Liste
2. Mit Nummern

[Das ist ein Link](https://www.example.com)
```

**Praktische Beispiele für Vereinsinhalte:**

```markdown
# Turnier: Dresden Open 2026

## Ergebnisse

**Sieger:** Anna Müller (1950 DWZ)
**2. Platz:** Thomas Schmidt (1875 DWZ)
**3. Platz:** Lisa Weber (1820 DWZ)

## Teilnehmer nach Altersklasse

- U10: 8 Spieler
- U12: 12 Spieler
- U14: 15 Spieler

Mehr Infos: [Turnierausschreibung](turnierausschreibung.pdf)
```

### Wie funktioniert die Veröffentlichung?

Sobald du einen Text speicherst, passiert das **ganz automatisch**:

1. **Du speicherst** deinen Text auf GitHub (mit "Commit changes")
2. **GitHub erkennt** die Änderung sofort
3. **GitHub baut die Website** automatisch neu (mit Jekyll)
4. **Dein Text ist live** auf der Website – normalerweise in Sekunden oder wenigen Minuten

Du brauchst dich um nichts anderes zu kümmern. **Einfach schreiben, speichern, fertig!**

---

## Für erfahrenere Nutzer: Erweiterte Themen

### Was ist Versionskontrolle?

**Versionskontrolle ist ein System, das Änderungen an deinen Dateien über die Zeit verfolgt.**

Wenn du jemals Dateien wie `Turnierbericht_v1.md`, `Turnierbericht_final.md` und `Turnierbericht_WIRKLICH_final.md` gespeichert hast, kennst du das Problem. Git löst das, indem es jede Änderung aufzeichnet – wer sie gemacht hat, wann und warum. Falls nötig, kannst du zu einer früheren Version zurück.

> **Tipp:** Wenn jemand sagt "push deine Änderungen", meint er: lade deine Änderungen von deinem Computer auf GitHub hoch.

### GitHub-Sicherheit: Dein Konto schützen

**Dein GitHub-Konto ist wichtig – schütze es!**

- **Zwei-Faktor-Authentifizierung (2FA):** Aktiviere sie unter **Einstellungen → Passwort und Authentifizierung**. Das macht dein Konto viel sicherer.
- **Starkes Passwort:** Nutze ein eindeutiges Passwort, das du nirgendwo sonst verwendest.
- **Wiederherstellungscodes:** Wenn du 2FA aktivierst, speichere die Wiederherstellungscodes in einem Passwort-Manager. Sie sind dein Rettungsanker.

> **Wichtig:** Speichere niemals Passwörter oder geheime Schlüssel direkt in deinen Dateien!

### Git-Befehle (für fortgeschrittene Nutzer)

Wenn du lokal auf deinem Computer arbeiten möchtest, brauchst du Git-Befehle:

| Befehl                      | Was er tut                                             |
| --------------------------- | ------------------------------------------------------ |
| `git config --global ...`   | Legt deinen Namen für deine Commits fest               |
| `git clone <url>`           | Erstellt eine lokale Kopie unseres Repositorys         |
| `git add .`                 | Bereitet alle Änderungen vor                           |
| `git commit -m "Nachricht"` | Speichert einen Schnappschuss mit Beschreibung         |
| `git push`                  | Lädt deine Änderungen auf GitHub hoch                  |
| `git pull`                  | Lädt die neuesten Änderungen von GitHub herunter       |
| `git switch -c <branch>`    | Erstellt einen neuen Branch (Arbeitszweig)             |
| `git merge <branch>`        | Vereinigt einen Branch mit deinem aktuellen            |

### Dein eigenes Repository erstellen

Du brauchst kein eigenes Repo für unsere Website – das existiert schon. Falls du aber ein Projekt starten möchtest:

1. Gehe zu [github.com](https://github.com/) und klicke **New**
2. Gib einen Namen ein (z. B. `mein-turnier-projekt`)
3. Wähle "Public" oder "Private"
4. Setz ein Häkchen bei "README" und klick "Create"

Fertig! Dein Repository ist bereit.

### GitHub-Flow: Der komplette Arbeitsablauf

Der **GitHub-Flow** ist die Reihenfolge, in der du arbeitest, wenn du lokal auf deinem Computer arbeiten willst:

1. **Clone:** Lade das Repository auf deinen Computer

   ```bash
   git clone <url>
   ```

2. **Branch:** Erstelle einen Arbeits-Zweig

   ```bash
   git switch -c mein-turnierbericht
   ```

3. **Edit:** Bearbeite deine Dateien im Editor

4. **Commit:** Speichere deine Änderungen

   ```bash
   git commit -m "Turnierbericht hinzugefügt"
   ```

5. **Push:** Lade hoch auf GitHub

   ```bash
   git push
   ```

6. **Pull Request:** Öffne einen Änderungsvorschlag auf GitHub und lass ihn überprüfen

> **Tipp:** Gib deinen Branches beschreibende Namen wie `2026-09-turnier-leipzig` oder `fehler-bei-spielerliste-beheben`

### Pull Requests – Änderungen gemeinsam überprüfen

Ein **Pull Request** (PR) ist ein Vorschlag, deine Änderungen in das Hauptprojekt einzubauen. So funktioniert es:

1. Du pushst deinen Branch auf GitHub
2. GitHub zeigt einen Button "Open a pull request"
3. Du schreibst, was du geändert hast und warum
4. Andere können deine Änderungen kommentieren
5. Wenn alles passt, wird der PR "merged" (eingefügt)

**Tipp:** Kleine PRs sind besser – sie sind schneller überprüft und weniger fehleranfällig.

### Merge-Konflikte: Was tun wenn es Probleme gibt?

Ein **Merge-Konflikt** tritt auf, wenn zwei Personen die gleiche Stelle in einer Datei bearbeitet haben.

**Normalfall:** Die meisten Merges gehen automatisch. Klick auf den grünen **Merge pull request**-Button, bestätige – fertig!

**Mit Konflikt:** GitHub markiert die widersprüchlichen Stellen. Du schaust sie an, entscheidest, welche Version du behalten möchtest, und markierst es als gelöst.

### GitHub Issues und Projects

**Issues** sind wie Aufgabenlisten:

- Ein Issue ist eine Aufgabe, ein Fehler oder eine Idee
- Du kannst Issues zuweisen, kennzeichnen und diskutieren

**Projects** sind visuell:

- Sie zeigen Issues auf einem Kanban-Board (Spalten: Zu tun, In Arbeit, Fertig)
- Damit verliert niemand den Überblick

**Clever:** Wenn dein Pull Request ein Issue behebt, schreib in der PR-Beschreibung:

```
Closes #42
```

Sobald der PR merged wird, schließt GitHub das Issue automatisch.

### Sicherheit für Fortgeschrittene

GitHub hat eingebaute Sicherheitsfunktionen:

- **Geheime Schlüssel:** Falls du zufällig ein Passwort in einer Datei speicherst, warnt dich GitHub
- **Abhängigkeits-Überwachung:** GitHub prüft, ob deine Bibliotheken bekannte Sicherheitslücken haben

### Zu Open-Source beitragen

**Open Source** bedeutet: Der Code ist frei verfügbar, und jeder kann mitwirken.

Falls du zu anderen Projekten beitragen möchtest:

- Suche nach Projekten mit einer klaren `README` und einer `CONTRIBUTING.md`
- Suche Issues mit dem Label `good first issue`

**Wichtiger Unterschied:**

- **Branch:** Ein paralleler Arbeitsbereich in einem Repo, das dir gehört
- **Fork:** Eine komplette Kopie eines fremden Repos in dein Konto (für externe Projekte)

---

**Noch Fragen?** Frag einen Vereinsmitglied, das erfahren ist mit GitHub!
