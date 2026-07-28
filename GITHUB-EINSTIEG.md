<!-- Auszug aus https://github.blog/developer-skills/github/github-for-beginners-your-roadmap-to-mastering-the-github-essentials/
Polly Davidson @pollyday

Formatiert, adaptiert und übersetzt von Martin Röbke
Ergänzt um Inhalte aus https://pappater.github.io/docs/GitHub%20Pages%20and%20Jekyll/
-->

# GitHub für Einsteiger: Dein Wegweiser zu den Grundlagen

**Bist du neu bei GitHub?** Dieser Leitfaden erklärt dir die Versionskontrolle, Repositories, Pull-Requests und alles andere, was du für den Start mit GitHub brauchst.

**Autorin:** Polly Davidson (@pollyday)  
**Datum:** 15. Juli 2026  
[Lies den vollständigen Original-Artikel (Englisch)](https://github.blog/developer-skills/github/github-for-beginners-your-roadmap-to-mastering-the-github-essentials/)

---

Jeder fängt mal an. Egal, ob du deine allererste Zeile Code schreibst oder schon seit Jahren entwickelst und die Werkzeuge dahinter nie ganz gelernt hast – dieser Leitfaden ist dein Einstieg.

Dies ist die komplette „GitHub für Einsteiger“-Serie in einer zusammenhängenden Geschichte – ein detaillierter Pfad, der dich von „Was ist überhaupt ein Repository?“ bis zur Zusammenarbeit an echten Projekten und dem Mitwirken an Open Source führt.

Lies ihn von oben bis unten, und du wirst ein vollständiges Verständnis dafür haben, wie moderne Software auf GitHub entwickelt wird. Spring zu einem beliebigen Abschnitt, und du findest eine eigenständige Antwort. Lass uns loslegen!

---

## Schnellstart: Dein erster Beitrag

**Du möchtest schnell einen neuen Turnierbericht oder eine Ankündigung hinzufügen?** Hier ist der kürzeste Weg:

1. Öffne unser GitHub-Repository im Browser.
1. Melde dich mit deinem GitHub-Konto an!
1. Navigiere zum Ordner, in den dein neuer Text gehört (z. B. `pages` für neue Seiten oder [turnierberichte](https://github.com/Schachverein-Dresden-Striesen/Schachverein-Dresden-Striesen.github.io/tree/website/pages/turnierberichte) für Berichte).
1. Klicke auf **Add file** (Auswahl `Create new file`="Leere Datei" oder `Upload files`="Datei hochladen") und benenne die Datei (z. B. `mein-artikel.md`).
1. Schreibe deinen Text in Markdown (siehe Abschnitt 5 für Formatierungsbeispiele).
1. Klicke **Commit changes** zum Speichern, und fülle das "Commit-Fenster" aus. Die Voreinstellung ist für den Anfang ausreichend", kann aber in `message` (Überschrift) und `description` erweitert werden.
1. Klicke "Propose changes" - es erfolgt automatisch die Erstellung (oder Ergänzung) auf dem Zweig/Branch und die Weiterleitung zu "Open a pull request", um die Änderung auf dem haupt-Zweig vorzuschlagen.
1. Fertig! Wenige Sekunden später ist deine Änderung in GitHub für andere sichtbar und kann diskutiert werden, bevor es Live geschaltet wird.

> **Hinweis:** Das funktioniert nur für kleine Änderungen. Für umfangreichere Arbeiten lies weiter – der vollständige Leitfaden unten zeigt dir alle Möglichkeiten.

---

## Teil 1: Finde dich zurecht

### 1. Was ist Versionskontrolle (und warum ist sie wichtig)?

**Versionskontrolle ist ein System, das Änderungen an deinen Dateien über die Zeit verfolgt. Git ist das weltweit am weitesten verbreitete System dafür.**

Wenn du jemals Dateien wie `Marken-Guide_v2`, `Marken-Guide_final` und `Marken-Guide_WIRKLICH_final` gespeichert hast, kennst du das Problem, das die Versionskontrolle löst. Git zeichnet jede Änderung auf, die du machst, sodass du sehen kannst, was sich wann und warum geändert hat. Wenn du zu einer früheren Version zurückkehren musst, ist das auch kein Problem. Du brauchst nie wieder einen Ordner voller „finaler“ Dateien.

Git arbeitet mit drei Bereichen: deinem **Arbeitsverzeichnis** (wo du arbeitest), dem **Staging-Bereich** (wo du prüfst, was hochgeladen werden soll) und dem **lokalen Speicher** (wo deine gespeicherte Historie liegt). Drei Befehle bewegen die Arbeit zwischen diesen Bereichen (`git status`, `git add` und `git commit`), und du wirst sie so oft benutzen, dass sie dir zur Routine werden.

> **Tipp:** Wenn jemand sagt „push deine Änderungen", meint er, du sollst deine Änderungen von deinem Computer auf GitHub hochladen.

### 2. Wie richte ich mein GitHub-Konto ein und sichere es ab?

**Dein GitHub-Konto ist deine digitale Identität als Schreiber. Du solltest sicherstellen, dass es gut geschützt ist.**

Die Aktivierung der Zwei-Faktor-Authentifizierung (2FA) fügt eine zweite Schutzebene hinzu, die dein Konto sicher hält, selbst wenn dein Passwort gestohlen wird. Passwörter allein sind anfällig. Aktiviere 2FA unter **Einstellungen → Passwort und Authentifizierung**.

Wenn du schon dabei bist, erstelle dir eine **Profil-Beschreibung**. Das ist eine Art lebendiges Portfolio deiner Fähigkeiten, Projekte und Interessen. Erstelle ein öffentliches Repository mit demselben Namen wie dein Benutzername, füge eine `README.md`-Datei hinzu, und alle deine Informationen werden auf deiner Profilseite für andere sichtbar.

> **&#128161; Tipp:** Lade deine Wiederherstellungscodes herunter und speichere sie in einem Passwort-Manager. Sie sind dein einziger Weg zurück, falls du dein Gerät verlierst.

### 3. Welche Git-Befehle brauche ich wirklich?

**Eine kleine Auswahl an Git-Befehlen deckt den täglichen Arbeitsablauf fast jedes Entwicklers ab.**

Die Befehle, mit denen du vertraut werden solltest, sind `config`, `init`, `clone`, `add`, `commit`, `push`, `pull`, `branch` und `switch`.

Du musst nicht ganz Git auswendig lernen. Hier sind die wichtigsten für den Anfang:

| Befehl                      | Was er tut                                             |
| --------------------------- | ------------------------------------------------------ |
| `git config --global ...`   | Legt deinen Namen für deine Commits fest               |
| `git init`                  | Macht den aktuellen Ordner zu einem Git-Repository     |
| `git clone <url>`           | Erstellt eine lokale Kopie eines Online-Repositorys    |
| `git status`                | Zeigt, was sich geändert hat und was bereit ist        |
| `git add .`                 | Bereitet alle Änderungen für den nächsten Commit vor   |
| `git commit -m "Nachricht"` | Speichert einen Schnappschuss deiner Änderungen        |
| `git switch -c <branch>`    | Erstellt einen neuen Arbeitszweig und wechselt dorthin |
| `git push`                  | Lädt deine lokalen Commits auf GitHub hoch             |
| `git pull`                  | Lädt die neuesten Änderungen von GitHub herunter       |
| `git merge <branch>`        | Fügt einen anderen Branch in deinen aktuellen ein      |

## Teil 2: Erstelle dein erstes Projekt

### 4. Wie erstelle ich mein erstes Repository?

**Ein Repository (kurz „Repo“) ist ein Projektordner, der Änderungen verfolgt, die Historie speichert und es mehreren Personen ermöglicht, nahtlos zusammenzuarbeiten.**

Dies ist die Heimatbasis deines Projekts. Starte von deinem **Dashboard**, der Seite, auf der du nach der Anmeldung bei [github.com](https://github.com/) landest.

- Klicke auf den grünen **New**-Button.
- Gib deinem Repo einen Namen.
- Wähle, ob es öffentlich oder privat sein soll.
- Setze ein Häkchen, um eine **README**-Datei hinzuzufügen. Dies ist das Erste, was Besucher sehen, und sollte als Eingangstür zu deinem Projekt dienen.

Das war's! Du hast ein Repository. Optional kannst du eine `.gitignore`-Datei hinzufügen, um Datenmüll aus der Versionskontrolle fernzuhalten, und eine Lizenz, um anderen mitzuteilen, was sie mit deinem Code tun dürfen.

Wofür ist eine `.gitignore` gut? Während du arbeitest, füllt sich dein Projektordner mit Dateien, die du nie selbst geschrieben hast (z. B. Systemdateien, heruntergeladene Abhängigkeiten). Diese willst du nicht verfolgen oder teilen. Eine `.gitignore`-Datei listet sie auf und sagt Git, sie zu ignorieren.

### 5. Was ist Markdown und wie benutze ich es?

**Markdown ist eine einfache Sprache zur Formatierung von Text. So schreibst du READMEs, Issues, Pull-Requests und Kommentare auf GitHub.**

Markdown verwandelt einfache Symbole in saubere Formatierungen. Mit ein paar Tastenanschlägen erstellst du Texte, die angenehm zu lesen sind. Hier sind die wichtigsten Beispiele:

```markdown
# Das ist eine grosse Überschrift

## Das ist eine Zwischenüberschrift

### Das ist eine kleinere Überschrift

**Das ist fettgedruckter Text** (wichtig!)
_Das ist kursiver Text_ (betonung)

- Das ist
- eine Aufzählung

1. Das ist
2. eine Nummerierte Liste

[Das ist ein Link](https://www.example.com)

`Das ist eingefuegter Code oder ein Befehl`
```

**Praktischer Tipp:** Wenn du einen Turnierbericht schreibst, nutze:

- Überschriften für Abschnitte
- Fettdruck für wichtige Ergebnisse
- Listen für Spieler oder Ergebnisse
- Links zu weiteren Informationen

### 6. Was ist der GitHub-Flow?

**Der GitHub-Flow ist der wiederholbare Kreislauf, um sicher Arbeit zu einem gemeinsamen Projekt hinzuzufügen: Branch erstellen, Änderungen committen, pushen, einen Pull-Request öffnen, mergen.**

Hier ist der Rhythmus, den du immer wieder wiederholen wirst:

1.  Klone das Repo auf deinen Computer _(falls noch nicht da)_
2.  Erstelle einen Branch für deine Arbeit.
3.  Mache Änderungen.
4.  Commite sie (speichere sie).
5.  Pushe sie auf GitHub (lade sie hoch).
6.  Öffne einen Pull-Request (einen Änderungsvorschlag).

> **&#128161; Tipp:** Gib Branches beschreibende Namen wie `fehler-im-login-beheben` oder `dunkelmodus-hinzufuegen`, damit jeder auf einen Blick weiß, worum es geht.

## Teil 3: Arbeite mit anderen zusammen

### 7. Was ist ein Pull-Request?

**Ein Pull-Request ist ein Vorschlag, eine Reihe von Änderungen von einem Branch in einen anderen zu übernehmen, mit einem eingebauten Bereich für Teamkollegen zur Überprüfung und Diskussion.**

Ein Pull-Request ist der Ort, an dem Zusammenarbeit stattfindet. Er zeigt visuell, was genau du geändert hast, und gibt den Prüfern einen Ort zum Kommentieren. Schreibe einen klaren Titel und eine Beschreibung und überprüfe deinen eigenen Pull-Request zuerst, um offensichtliche Fehler zu finden.

> **&#128161; Tipp:** Kleinere Pull-Requests sind einfacher und schneller zu überprüfen und zu mergen, bieten weniger Raum für Fehler und schaffen eine klarere Änderungshistorie.

### 8. Wie merge ich einen Pull-Request und löse einen Merge-Konflikt?

Das "Mergen" integriert überprüfte Änderungen in deinen Ziel-Branch. Ein **Merge-Konflikt** entsteht, wenn Git deine Hilfe braucht, weil zwei **Änderungen dieselben Codezeilen berühren**.

Die meisten Merges sind ein grüner Knopf: Klicke auf **Merge pull request**, bestätige, fertig. 🎉 Manchmal bearbeiten zwei Personen/Branches dieselben Zeilen einer Datei, und Git kann nicht entscheiden, welche Version richtig ist. In diesem Fall markiert GitHub die widersprüchlichen Abschnitte. Du wählst aus, was du behalten möchtest, markierst das Problem als gelöst und führst die Zusammenführung durch.

### 9. Was sind GitHub Issues und Projects?

**Issues verfolgen einzelne Aufgaben, Fehler und Ideen, während Projects diese Issues auf einem visuellen Board organisieren, damit nichts durchrutscht.**

Issues sind wie teilbare, nachverfolgbare Notizen. Jedes ist eine Aufgabe, ein Fehler oder eine Idee, die du zuweisen, kennzeichnen und diskutieren kannst. Projects ziehen diese Issues auf ein Kanban-Board, sodass du den Status aller Aufgaben auf einen Blick siehst.

Ein kleiner Trick: Wenn du einen Pull-Request öffnest, um ein Issue zu beheben, kannst du in der Beschreibung des Pull-Requests ein Schlüsselwort wie `Closes #42` schreiben (wobei #42 die Nummer der Aufgabe ist). Sobald die Änderung zusammengeführt wird, schließt GitHub die Aufgabe automatisch für dich.

## Teil 4: Bringe deine Projekte auf das nächste Level

### 10. Was ist GitHub Actions?

**GitHub Actions ist eine Automatisierungsplattform, die Aufgaben automatisch ausführt, wenn in deinem Repo etwas passiert.**

Bei unserer Vereinswebseite passiert das automatisch: Sobald du einen neuen Artikel speicherst, führt GitHub Actions automatisch die folgenden Schritte aus:

1. Es erkennt, wenn der [website branch](https://github.com/Schachverein-Dresden-Striesen/Schachverein-Dresden-Striesen.github.io/branches) aktualisiert wurde.
2. Es startet Jekyll (unser Website-Bauwerkzeug).
3. Jekyll wandelt all deine Markdown-Dateien und Konfiguration in die fertige Webseite um.
4. Die Website wird mit dem Inhalt live aktualisiert.

Du brauchst dich um nichts mehr zu kümmern – GitHub erledigt alles im Hintergrund.

### 11. Wie veröffentliche ich eine Webseite kostenlos mit GitHub Pages & Jekyll?

**GitHub Pages** ist ein kostenloser Dienst von GitHub, der statische Webseiten direkt aus einem Repository heraus veröffentlicht. **Jekyll** ist ein Werkzeug, das einfache Textdateien (wie unsere Markdown-Artikel) in eine fertige Webseite umwandelt. Wir nutzen beides in Kombination.

**Und so funktioniert es bei uns:**

1.  **Du schreibst:** Du erstellst oder bearbeitest eine Markdown-Datei in unserem Repository – zum Beispiel einen neuen Turnierbericht im Ordner `turnierberichte`.
2.  **Du speicherst:** Sobald deine Änderungen im `website`-Branch gespeichert sind, übernimmt GitHub automatisch.
3.  **Jekyll baut:** GitHub Pages nutzt Jekyll, um alle unsere Markdown-Dateien, Vorlagen und Bilder zu einer kompletten, klickbaren Webseite zusammenzubauen.
4.  **Die Seite ist live:** Wenige Augenblicke später sind deine Änderungen unter [www.schachverein-dresden-striesen.de](https://www.schachverein-dresden-striesen.de) für alle sichtbar.

Du musst dich also nicht um Server oder komplizierte Technik kümmern. Schreib einfach deinen Text, und GitHub erledigt den Rest.

> **&#128161; Tipp für Fortgeschrittene:** Wenn du Änderungen vor der Veröffentlichung auf deinem eigenen Computer (oder in Codespaces im Web-Browser) testen möchtest, kannst du Jekyll lokal installieren. Mit dem Befehl `bundle exec jekyll serve` startest du eine Vorschau-Webseite auf deinem PC.

### 12. Wie sichere ich meinen Code auf GitHub ab?

Sicherheit ist kein letzter Schritt, sondern eine Gewohnheit. GitHub hat eine eingebaute Sicherheitssuite, die automatisch Probleme findet und dir hilft, sie zu beheben.

**Das schützt dein Konto:**

- **Zwei-Faktor-Authentifizierung (2FA):** Aktiviere sie in den Einstellungen. Sie verhindert, dass andere dein Konto übernehmen, selbst wenn sie dein Passwort haben.
- **Starkes Passwort:** Benutze ein eindeutiges Passwort, das du sonst nirgendwo verwendest.
- **Wiederherstellungscodes:** Speichere diese sicher auf – sie sind dein Rettungsanker, falls du dein Gerät verlierst.

**Das schützt dein Repository:**

- **Geheime Schlüssel:** Wenn du API-Schlüssel oder Passwörter zufällig hochlädst, erkennt GitHub dies automatisch und warnt dich.
- **Abhängigkeits-Überwachung:** GitHub prüft automatisch, ob die verwendeten Bibliotheken bekannte Sicherheitslücken haben, und schlägt Aktualisierungen vor.

> **Tipp:** Speichere niemals Passwörter oder geheime Schlüssel direkt in deinen Dateien!

### 13. Wie kann ich zu Open Source beitragen?

**Open-Source-Software hat frei verfügbaren Code, den jeder studieren und verbessern kann, und GitHub ist ihr Zuhause.**

Wie findest du das perfekte Projekt zum Mitwirken? Suche nach Projekten mit einer klaren `README`, einer `CONTRIBUTING.md` (Anleitung zum Mitwirken) und Issues, die als `good first issue` (guter erster Beitrag) markiert sind.

Ein **Fork** ist deine persönliche Kopie des Repositorys eines anderen, in der du frei experimentieren und dann deine Änderungen mit einem Pull-Request vorschlagen kannst.

Was ist der Unterschied zwischen einem Fork und einem Branch? Ein **Branch** ist ein paralleler Arbeitsbereich _innerhalb_ eines Repositorys, für das du bereits die Erlaubnis zum Ändern hast. Ein **Fork** kopiert ein ganzes Repository in _dein_ Konto, was du brauchst, wenn du keine Berechtigung hast, das Original zu bearbeiten (wie bei den meisten Open-Source-Projekten).

---

**Hast du noch Fragen?** Schau dir die [häufig gestellten Fragen](https://github.blog/developer-skills/github/github-for-beginners-answers-to-some-common-questions/) an oder sieh dir die [komplette YouTube-Serie „GitHub für Einsteiger“](https://www.youtube.com/playlist?list=PL0lo9MOBetEFcp4SCWinBdpml9B2U25-f) an.
