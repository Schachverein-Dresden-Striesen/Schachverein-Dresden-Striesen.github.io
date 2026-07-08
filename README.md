<!-- markdownlint-disable-next-line MD026 -->
# Schachverein Dresden-Striesen e.V.  

Diese Website wird mit GitHub Pages und Jekyll erstellt und automatisch bereitgestellt. Sie enthält alle notwendigen Dateien und Konfigurationen für die automatische Veröffentlichung bei Änderungen.

**Live-Website:** [www.sv-dresden-striesen.de](https://www.sv-dresden-striesen.de)

## Projektstruktur

- **CNAME**: Konfiguration des Domainnamen der Webseite. Achtung, muss auch im DNS entsprechend konfiguriert sein.
- **index.md**: Hauptseite der Website
- **data/navigation.yml**: Menü der Webseite
- **pages/**: Inhaltsseiten des Vereins
- **files/**: Dateien, Bilder und Dokumente
- **_config.yml**: Jekyll-Konfiguration für GitHub Pages
- **.devcontainer/**: Entwicklungsumgebung für VSCode

## Mitwirkung

Beiträge sind willkommen! Bitte erstellen Sie einen Pull Request oder öffnen Sie ein [Issue](https://github.com/Schachverein-Dresden-Striesen/Schachverein-Dresden-Striesen.github.io/issues) für Vorschläge oder Verbesserungen.
Aktueller Meilenstein: [Milestones](https://github.com/Schachverein-Dresden-Striesen/Schachverein-Dresden-Striesen.github.io/milestones).

## Lokale Entwicklung

### Voraussetzungen

**Für beide Optionen:**

- [Git](https://git-scm.com/)

**Option 1 (empfohlen):**

- [VSCode](https://code.visualstudio.com/)
- [Docker](https://www.docker.com/)

**Option 2:**

- Ruby (Version 2.7 oder höher)
  - Windows: [RubyInstaller](https://rubyinstaller.org/)
  - macOS: `brew install ruby` (mit [Homebrew](https://brew.sh/))
  - Linux: Paketmanager Ihrer Distribution verwenden

### Setup

1. **Repository klonen**:

   ```bash
   git clone https://github.com/Schachverein-Dresden-Striesen/Schachverein-Dresden-Striesen.github.io.git
   ```

2. **Entwicklungsumgebung wählen:**

   **Option A: VSCode mit Devcontainer (empfohlen)**

   ```bash
   code .
   ```

   - VSCode wird automatisch vorschlagen, den Container zu öffnen
   - Oder: `F1` → "Dev Containers: Reopen in Container"
   - Abhängigkeiten werden automatisch installiert

   **Option B: Lokale Installation**

   ```bash
   gem install bundler
   bundle install
   ```

3. **Website starten**:

   ```bash
   # Mit Standard-Konfiguration:
   bundle exec jekyll serve
   ```

Die Website ist dann unter `http://localhost:4000` erreichbar.

### Inhalte bearbeiten

- Bearbeiten Sie Markdown-Dateien (`.md`) in VSCode oder Ihrem bevorzugten Editor
- **Oder direkt in GitHub über die Weboberfläche**
- Änderungen werden automatisch beim Speichern übernommen (Live-Reload)
- Neue Seiten können im `pages/` Verzeichnis erstellt werden

### Deployment

Änderungen werden automatisch über GitHub Actions veröffentlicht, wenn sie in den `website`-Branch gepusht werden.

### GitHub Copilot Support

Das Repository enthält eine Copilot-Setup-Workflow (`.github/workflows/copilot-setup-steps.yml`), der die Jekyll-Entwicklungsumgebung für GitHub Copilot-Agenten vorbereitet. 
Dies ermöglicht es Copilot, Ruby-Dependencies automatisch zu installieren und die Jekyll-Build-Umgebung einzurichten.

