# Schachverein Dresden-Striesen e.V

Diese Website wird mit GitHub Pages und Jekyll erstellt und automatisch bereitgestellt. Sie enthält alle notwendigen Dateien und Konfigurationen für die automatische Veröffentlichung bei Änderungen.

**Live-Website:** [www.sv-dresden-striesen.de](https://www.sv-dresden-striesen.de)

## Projektstruktur

- **_config.yml**: Jekyll-Konfiguration für GitHub Pages
- **index.md**: Hauptseite der Website
- **pages/**: Inhaltsseiten des Vereins
- **files/**: Dateien, Bilder und Dokumente
- **data/navigation.yml**: Menü der Webseite
- **CNAME**: Konfiguration des Domainnamen der Webseite. Achtung, muss auch im DNS entsprechend konfiguriert sein.
- **.devcontainer/**: Vorlage für Entwicklungsumgebung (z.B. in [VS Code](https://code.visualstudio.com/docs/devcontainers/faq))

### Deployment

Änderungen werden automatisch über GitHub Actions veröffentlicht, wenn sie in den `website`-Branch gepusht werden.

### GitHub Copilot Support

Das Repository enthält eine Copilot-Setup-Workflow (`.github/workflows/copilot-setup-steps.yml`), der die Jekyll-Entwicklungsumgebung für GitHub Copilot-Agenten vorbereitet.
Dies ermöglicht es Copilot, Ruby-Dependencies automatisch zu installieren und die Jekyll-Build-Umgebung einzurichten.

Siehe auch [`docs/agents/`](docs/agents/) für Ressourcen zu Agentic Work und der Skills Library.

## Mitwirkung

Beiträge sind willkommen! Bitte erstellen Sie einen Pull Request oder öffnen Sie ein [Issue](https://github.com/Schachverein-Dresden-Striesen/Schachverein-Dresden-Striesen.github.io/issues) für Vorschläge oder Verbesserungen.
Aktueller Webseite-Meilenstein: [Milestones](https://github.com/Schachverein-Dresden-Striesen/Schachverein-Dresden-Striesen.github.io/milestone/1).

Bei Fragen schaue auch durch die

- [Historie an Pull-Requests](https://github.com/Schachverein-Dresden-Striesen/Schachverein-Dresden-Striesen.github.io/pulls?q=is%3Apr)
- [einzelnen Änderungen](https://github.com/Schachverein-Dresden-Striesen/Schachverein-Dresden-Striesen.github.io/commits/website/)

beziehungsweise wende dich gerne an [unser Team](https://github.com/Schachverein-Dresden-Striesen/Schachverein-Dresden-Striesen.github.io/people) 😊.

> **Neu bei GitHub?** Lies zuerst unseren [GitHub-Einstiegsleitfaden](GITHUB-EINSTIEG.md), um die Grundlagen zu verstehen.

## Lokale Entwicklung

### Voraussetzungen

- [Git](https://git-scm.com/)
- Für die lokale Installation zusätzlich: Ruby 3.x oder kompatibel

### Schnellstart

1. Repository klonen:

      ```bash
      git clone https://github.com/Schachverein-Dresden-Striesen/Schachverein-Dresden-Striesen.github.io.git
      cd Schachverein-Dresden-Striesen.github.io
      ```

1. Entwicklungsumgebung wählen:

   **Devcontainer (empfohlen):**

      `code .`

      - In VS Code: `F1` → `Dev Containers: Reopen in Container`
   
      Die Abhängigkeiten werden dort automatisch installiert

   **Lokale Installation:**

      ```bash
      gem install bundler
      bundle install
      ```

1. Website starten:

   ```bash
   bundle exec jekyll serve
   ```

   Die Seite läuft dann unter `http://localhost:4000`.

### Inhalte bearbeiten

- Bearbeiten Sie Markdown-Dateien (`.md`) in VSCode oder Ihrem bevorzugten Editor
- **Oder direkt in GitHub über die Weboberfläche**
- Änderungen werden automatisch beim Speichern übernommen (Live-Reload)
- Neue Seiten können im `pages/` Verzeichnis erstellt werden
