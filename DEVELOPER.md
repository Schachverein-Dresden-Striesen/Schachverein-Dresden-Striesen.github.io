# Developer Guide

Du willst Features bauen, die Navigation ändern oder den Code verbessern?
Hier ist alles, was du brauchst.

## Setup

Siehe [README.md](README.md) → Developer Setup

Kurz zusammengefasst:

```bash
# Option 1: Devcontainer (empfohlen)
code .
# In VS Code: F1 → Dev Containers: Reopen in Container

# Option 2: Lokal
gem install bundler && bundle install
bundle exec jekyll serve
```

Website läuft dann unter `http://localhost:4000`.

## Workflow

### 1. Feature planen

Bevor du Code schreibst, prüfe:

- Gibt es schon ein Issue dafür? → Schau in [Issues](https://github.com/Schachverein-Dresden-Striesen/Schachverein-Dresden-Striesen.github.io/issues)
- Passt die Feature zum Projekt? → Lass dich inspirieren von [Milestones](https://github.com/Schachverein-Dresden-Striesen/Schachverein-Dresden-Striesen.github.io/milestone/1)
- Fragen zum Design? → Öffne ein [Issue](https://github.com/Schachverein-Dresden-Striesen/Schachverein-Dresden-Striesen.github.io/issues) und diskutiere

### 2. Branch erstellen

```bash
git checkout -b feature/kurze-beschreibung
# Beispiel: git checkout -b feature/navigation-mobile-optimieren
```

### 3. Code schreiben und testen

Schreib deinen Code in VSCode oder deinem Editor.

**Lokal testen:**

```bash
bundle exec jekyll serve
```

Öffne `http://localhost:4000` im Browser und prüfe deine Änderungen. Die Seite updated automatisch beim Speichern (Live-Reload).

### 4. Änderungen committen

```bash
git add .
git commit -m "Beschreibung der Änderung"
```

**Commit-Nachricht-Stil:**

- Deutsch, Präsens
- Kurz (max. 50 Zeichen)
- Beispiele:
  - `Navigationsmenü für mobile Geräte optimieren`
  - `DWZ-Liste laden und formatieren`
  - `Fehler beim Laden von Turnierberichten beheben`

### 5. Push und Pull Request

```bash
git push origin feature/kurze-beschreibung
```

Dann öffnest du auf GitHub einen **Pull Request**:

1. Gehe zu [Pull Requests](https://github.com/Schachverein-Dresden-Striesen/Schachverein-Dresden-Striesen.github.io/pulls)
2. Klicke **New Pull Request**
3. Wähle deinen Branch
4. Schreib eine aussagekräftige Beschreibung, was die PR ändert
5. Klick **Create Pull Request**

### 6. Review und Feedback

Das Team bespricht die PR und gibt Feedback. Du kannst direkt weitere Commits pushen — die PR update automatisch.

### 7. Merge

Wenn alles ok ist, wird die PR gemerged. Congratulations! 🎉

## Projektstruktur

```
.
├── _config.yml          # Jekyll-Konfiguration
├── index.md             # Startseite
├── pages/               # Website-Seiten (Turnierberichte, etc.)
├── files/               # Dokumente, Assets
├── _data/
│   ├── navigation.yml   # Menü-Struktur
│   └── ...
├── _includes/           # HTML-Templates
├── docs/
│   ├── adr/             # Architektur-Entscheidungen
│   └── agents/          # Agent-Operator-Guides
└── .devcontainer/       # Dev-Environment-Setup
```

### Wichtigste Dateien

- **_config.yml**: Jekyll allgemein konfigurieren (Titel, URL, etc.)
- **data/navigation.yml**: Menü-Einträge hinzufügen/ändern
- **pages/*.md**: Neue Seiten hinzufügen (Turnierberichte, Ankündigungen, etc.)
- **docs/adr/*.md**: Warum habt ihr so designed? (Architektur-Entscheidungen)

## Qualitätsstandards

Alle Beiträge müssen folgende Standards erfüllen:

### Quality Rules

- **Inhalt auf Deutsch:** Website-Content bleibt auf Deutsch (außer explizit anders angegeben)
- **Markdown validieren:** Syntax und Struktur prüfen
- **Jekyll Build erfolgreich:** Stelle sicher, `bundle exec jekyll build` führt fehlerfrei durch
- **Jekyll Front Matter:** Meta-Daten verwenden, relative Links für interne Verweise
- **Historische Genauigkeit:** Fakten mit Quellen belegen

### Style Rules

- **Verzeichnis-Struktur erhalten:** Keine Umstrukturierung ohne Diskussion
- **Dateinamen Deutsch:** Aussagekräftige deutsche Namen für Dateien und Ordner
- **Bilder optimieren:** Für Web geeignete Größe und Format (JPG/WebP/PNG, nicht zu groß)
- **Deutsche Orthografie:** Korrekte Rechtschreibung und Grammatik
- **GitHub Pages Limitations:** Keine trailing slashes in Links (z.B. `/seite/` statt `/seite`)

Fragen zu den Standards? → [GitHub Issues](https://github.com/Schachverein-Dresden-Striesen/Schachverein-Dresden-Striesen.github.io/issues)

## Architektur-Entscheidungen

Warum wurde etwas so designed? Siehe [`docs/adr/`](docs/adr/) für **Architektur Decision Records (ADRs)**.

**Wenn du eine major change machst:** Erwäge, eine ADR zu schreiben.

Lese [`docs/adr/0001-single-context-glossary.md`](docs/adr/0001-single-context-glossary.md) für ein Beispiel.

## Glossar

Was bedeutet "Turnier", "Mitglied", "DWZ"? Siehe [`CONTEXT.md`](CONTEXT.md) — die Domänen-Sprache des Projekts.

## Probleme oder Fragen?

- **Issue öffnen:** [GitHub Issues](https://github.com/Schachverein-Dresden-Striesen/Schachverein-Dresden-Striesen.github.io/issues)
- **Diskussionen:** [GitHub Discussions](https://github.com/Schachverein-Dresden-Striesen/Schachverein-Dresden-Striesen.github.io/discussions)
- **Direkt vom Team hören:** [Team Seite](https://github.com/Schachverein-Dresden-Striesen/Schachverein-Dresden-Striesen.github.io/people)

## Neu bei GitHub?

Kein Problem. Siehe [GitHub Anfänger-Guide](GITHUB-EINSTIEG.md) für die Grundlagen (Repositories, Branches, Pull Requests, etc.).
