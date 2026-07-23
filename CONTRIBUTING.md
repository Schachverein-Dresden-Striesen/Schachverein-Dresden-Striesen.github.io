# Beitragsrichtlinien für die SV Dresden-Striesen Webseite

Vielen Dank für Ihr Interesse, zur Webseite des Schachvereins Dresden-Striesen e.V. beizutragen! Diese Richtlinien helfen Ihnen dabei, effektiv mitzuwirken.

## Inhaltsverzeichnis

- [Wie kann ich beitragen?](#wie-kann-ich-beitragen)
- [Git-Workflow](#git-workflow)
- [Markdown-Standards](#markdown-standards)
- [Bildoptimierung](#bildoptimierung)
- [Review-Prozess](#review-prozess)
- [Commit-Message-Konventionen](#commit-message-konventionen)

## Wie kann ich beitragen?

Es gibt verschiedene Möglichkeiten, zur Webseite beizutragen:

1. **Content-Beiträge**: Turnierberichte, News, Vereinsinformationen
2. **Aktualisierungen**: Ligatabellen, Termine, Ergebnisse
3. **Fehlerbehebungen**: Tippfehler, fehlerhafte Links, veraltete Informationen
4. **Technische Verbesserungen**: Design, Performance, neue Features
5. **Dokumentation**: Verbesserung dieser Richtlinien und anderer Dokumente

## Git-Workflow

### Branch-Strategie

1. **Erstellen Sie einen Feature-Branch:**
   ```bash
   git checkout -b feature/ihr-feature-name
   # oder
   git checkout -b content/thema-des-beitrags
   # oder
   git checkout -b fix/beschreibung-des-fehlers
   ```

2. **Verwenden Sie aussagekräftige Branch-Namen:**
   - `feature/` - für neue Features
   - `content/` - für Content-Beiträge
   - `fix/` - für Fehlerbehebungen
   - `docs/` - für Dokumentationsänderungen

### Arbeiten mit dem Repository

1. **Repository klonen:**
   ```bash
   git clone https://github.com/Schachverein-Dresden-Striesen/Schachverein-Dresden-Striesen.github.io.git
   cd Schachverein-Dresden-Striesen.github.io
   ```

2. **Abhängigkeiten installieren:**
   ```bash
   bundle install
   ```

3. **Lokalen Server starten:**
   ```bash
   bundle exec jekyll serve
   ```
   Die Website ist dann unter `http://localhost:4000` erreichbar.

4. **Änderungen testen:**
   ```bash
   bundle exec jekyll build
   ```
   Stellen Sie sicher, dass der Build ohne Fehler durchläuft.

### Pull Request erstellen

1. **Pushen Sie Ihre Änderungen:**
   ```bash
   git push origin ihr-branch-name
   ```

2. **Erstellen Sie einen Pull Request auf GitHub**
   - Verwenden Sie eine aussagekräftige Beschreibung
   - Verlinken Sie relevante Issues mit `Fixes #123` oder `Closes #123`
   - Beschreiben Sie, was geändert wurde und warum

3. **Warten Sie auf Review**
   - Mindestens ein Vereinsmitglied sollte den PR reviewen
   - Reagieren Sie auf Feedback und nehmen Sie ggf. Anpassungen vor

## Markdown-Standards

### Allgemeine Regeln

- **Überschriften**: Verwenden Sie `#` bis `####` hierarchisch
- **Leerzeilen**: Eine Leerzeile vor und nach Überschriften, Listen, Codeblöcken
- **Listen**: Verwenden Sie `-` für ungeordnete Listen
- **Links**: Verwenden Sie sprechende Link-Texte, keine "hier klicken"

### Deutsche Rechtschreibung

- Verwenden Sie neue deutsche Rechtschreibung
- Achten Sie auf korrekte Groß- und Kleinschreibung
- Verwenden Sie deutsche Anführungszeichen: „..." oder »...«

### Datums- und Zeitformate

- Datum: `TT.MM.JJJJ` (z.B. 23.07.2026)
- Zeitraum: `TT.MM. - TT.MM.JJJJ` (z.B. 15.08. - 22.08.2026)
- Bei internationalen Kontexten: `JJJJ-MM-TT` (z.B. 2026-07-23)

### Front Matter

Jede Markdown-Seite sollte Front Matter enthalten:

```yaml
---
layout: single
title: "Seitentitel"
sidebar:
  nav: "main"
---
```

### Beispiel-Struktur

```markdown
---
layout: single
title: "Turnierbericht: Vereinspokal 2026"
sidebar:
  nav: "main"
---

Kurze Einleitung zum Turnier.

## Turnierverlauf

Beschreibung der Runden...

## Ergebnisse

| Platz | Name | Punkte |
|-------|------|--------|
| 1     | Max Mustermann | 7.0 |

## Fazit

Zusammenfassung und Ausblick...

---

[← Zurück zur Startseite]({{ site.baseurl }}/)
```

## Bildoptimierung

### Bildformate

- **Fotos**: JPEG (.jpg) mit 80-85% Qualität
- **Grafiken/Diagramme**: PNG (.png) für scharfe Kanten
- **Logos**: SVG (.svg) wenn möglich, sonst PNG

### Bildgrößen

- **Header-Bilder**: Max. 1920px Breite
- **Content-Bilder**: Max. 1200px Breite
- **Thumbnails**: Max. 400px Breite
- **Dateigröße**: Unter 500 KB pro Bild

### Bildoptimierung

Verwenden Sie Tools wie:
- [TinyPNG](https://tinypng.com/) für JPEG/PNG
- [ImageOptim](https://imageoptim.com/) (Mac)
- [Squoosh](https://squoosh.app/) (Browser-basiert)

### Dateinamen

- Kleinbuchstaben
- Keine Leerzeichen (verwenden Sie `-` oder `_`)
- Beschreibend: `vereinspokal-2026-siegerehrung.jpg`
- Datum voranstellen bei zeitbezogenen Bildern: `20260712-vereinspokal.jpg`

### Speicherort

```
/files/
  /images/
    /turniere/
      20260712-vereinspokal-siegerehrung.jpg
    /mannschaften/
      mannschaft-1-saison-2526.jpg
    /logos/
      sv-striesen-logo.svg
```

### Bilder einbinden

```markdown
![Beschreibender Alt-Text](/files/images/turniere/20260712-vereinspokal.jpg)

*Bildunterschrift: Siegerehrung beim 12. Vereinspokal*
```

## Review-Prozess

### Was wird geprüft?

1. **Inhaltliche Korrektheit**: Sind die Informationen richtig?
2. **Rechtschreibung und Grammatik**: Fehlerfreier deutscher Text?
3. **Markdown-Syntax**: Korrekt formatiert?
4. **Links**: Funktionieren alle internen und externen Links?
5. **Bilder**: Optimiert und korrekt eingebunden?
6. **Build**: Läuft `bundle exec jekyll build` ohne Fehler?

### Review-Checkliste

- [ ] Inhalt auf Richtigkeit geprüft
- [ ] Rechtschreibung und Grammatik korrekt
- [ ] Markdown-Syntax eingehalten
- [ ] Alle Links funktionieren
- [ ] Bilder optimiert (< 500 KB)
- [ ] Alt-Texte für Bilder vorhanden
- [ ] Jekyll Build erfolgreich
- [ ] Lokale Vorschau getestet
- [ ] Front Matter vollständig
- [ ] Datums- und Namensformate korrekt

## Commit-Message-Konventionen

### Format

```
Typ: Kurze Beschreibung (max. 50 Zeichen)

Ausführlichere Beschreibung, falls nötig.
Kann mehrere Absätze umfassen.

Fixes #123
```

### Typen

- `feat:` - Neues Feature oder neue Inhalte
- `fix:` - Fehlerbehebung
- `docs:` - Dokumentationsänderungen
- `style:` - Formatierung, Layout (kein Code/Content-Change)
- `refactor:` - Code-Umstrukturierung ohne Funktionsänderung
- `content:` - Inhaltliche Änderungen (Turnierberichte, News, etc.)
- `update:` - Aktualisierung bestehender Inhalte (Tabellen, Termine)
- `chore:` - Wartungsarbeiten, Dependency-Updates

### Beispiele

```bash
# Gute Commit-Messages
git commit -m "content: Turnierbericht 12. Vereinspokal hinzugefügt"
git commit -m "fix: Fehlerhafte Links auf Startseite korrigiert"
git commit -m "update: Mannschaftstabellen Saison 2026/27 aktualisiert"
git commit -m "feat: RSS-Feed für Turnierberichte implementiert"

# Schlechte Commit-Messages (vermeiden!)
git commit -m "Update"
git commit -m "Änderungen"
git commit -m "Fix"
```

### Mehrere Änderungen

Wenn möglich, committen Sie logisch zusammenhängende Änderungen einzeln:

```bash
# Statt eines großen Commits:
git add .
git commit -m "Verschiedene Änderungen"

# Besser: Mehrere kleine, fokussierte Commits
git add pages/jugend.md
git commit -m "content: Trainingszeiten für Jugendgruppen ergänzt"

git add pages/mannschaftskaempfe.md
git commit -m "update: Tabellenstände Bezirksliga aktualisiert"
```

## Fragen und Hilfe

Bei Fragen wenden Sie sich bitte an:

- **Technische Fragen**: [GitHub Issues](https://github.com/Schachverein-Dresden-Striesen/Schachverein-Dresden-Striesen.github.io/issues)
- **Content-Fragen**: Vorstand des Vereins
- **Dringende Probleme**: E-Mail an info@sv-dresden-striesen.de

## Code of Conduct

- Seien Sie respektvoll und konstruktiv
- Akzeptieren Sie unterschiedliche Perspektiven
- Fokussieren Sie auf das Wohl des Vereins und der Community
- Helfen Sie Neulingen und teilen Sie Ihr Wissen

Vielen Dank für Ihren Beitrag! 🎉♟️
