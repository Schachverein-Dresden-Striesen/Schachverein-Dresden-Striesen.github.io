# Schachverein Dresden-Striesen e.V

Diese Website wird mit GitHub Pages und Jekyll erstellt und automatisch bereitgestellt.

**Live-Website:** [www.sv-dresden-striesen.de](https://www.sv-dresden-striesen.de)

---

## Schnellstart für deine Rolle

### Ich möchte einen Turnierbericht oder eine Ankündigung hinzufügen

→ Siehe [Content Creator Guide](CONTENT-GUIDE.md)  
(Keine technischen Kenntnisse nötig; alles läuft im Browser.)

### Ich bin ein Entwickler und möchte lokal arbeiten

→ Siehe [Developer Setup](#developer-setup) unten.

### Ich bin Agent-Operator und nutze GitHub Copilot

→ Siehe [`docs/agents/`](docs/agents/) für Setup und Bedienungsanleitung.

---

## Developer Setup

### Voraussetzungen

- [Git](https://git-scm.com/)
- Für die lokale Installation: Ruby 3.x (oder Devcontainer nutzen)

### Schnellstart

1. Repository klonen:

   ```bash
   git clone https://github.com/Schachverein-Dresden-Striesen/Schachverein-Dresden-Striesen.github.io.git
   cd Schachverein-Dresden-Striesen.github.io
   ```

2. Entwicklungsumgebung aufsetzen:

   **Devcontainer (empfohlen):**

   ```bash
   code .
   # In VS Code: F1 → Dev Containers: Reopen in Container
   ```

   **Oder lokal:**

   ```bash
   gem install bundler && bundle install
   ```

3. Website starten:

   ```bash
   bundle exec jekyll serve
   ```

   → Läuft unter `http://localhost:4000`

### Weitere Developer-Docs

- [GitHub Anfänger-Guide](GITHUB-EINSTIEG.md) — wenn du mit GitHub nicht vertraut bist
- [Developer Guide](DEVELOPER.md) — Workflow, Features bauen, Testing, Deployment

---

## Projektstruktur

- **_config.yml**: Jekyll-Konfiguration
- **index.md**: Hauptseite
- **pages/**: Inhaltsseiten (Turnierberichte, Ankündigungen, etc.)
- **files/**: Dokumente, Bilder, Assets
- **data/navigation.yml**: Menü-Struktur
- **.devcontainer/**: Vorlagen für Entwicklungsumgebung
- **docs/adr/**: Architektur-Entscheidungen
- **docs/agents/**: Agent-Setup und Skills

### Deployment

Änderungen werden automatisch über GitHub Actions veröffentlicht, wenn sie in den `website`-Branch gepusht werden.

---

## Mitwirkung

Alle Beiträge sind willkommen!

- **Turnierberichte oder Ankündigungen?** → [Content Creator Guide](CONTENT-GUIDE.md)
- **Code-Änderungen oder Features?** → [Developer Guide](DEVELOPER.md)
- **Bugs gefunden?** → Öffne ein [Issue](https://github.com/Schachverein-Dresden-Striesen/Schachverein-Dresden-Striesen.github.io/issues)
- **Fragen oder Diskussionen?** → Wende dich an [unser Team](https://github.com/Schachverein-Dresden-Striesen/Schachverein-Dresden-Striesen.github.io/people)

Aktueller Meilenstein: [Milestones](https://github.com/Schachverein-Dresden-Striesen/Schachverein-Dresden-Striesen.github.io/milestone/1)

---

## Dokumentation

- **[CONTEXT.md](CONTEXT.md)** — Glossar der Domänenbegriffe
- **[docs/adr/](docs/adr/)** — Architektur-Entscheidungen
- **[docs/agents/](docs/agents/)** — Agent-Operator-Guides
