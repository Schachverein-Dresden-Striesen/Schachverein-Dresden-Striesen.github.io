<!-- markdownlint-disable-next-line MD026 -->
# Schachverein Dresden-Striesen e.V.  

Diese Website wird mit GitHub Pages und Jekyll erstellt und automatisch bereitgestellt. Sie enthält alle notwendigen Dateien und Konfigurationen für die automatische Veröffentlichung bei Änderungen.

**Live-Website:** [www.sv-dresden-striesen.de](https://www.sv-dresden-striesen.de)

## Projektstruktur

- **index.md**: Hauptseite der Website
- **pages/**: Inhaltsseiten des Vereins
- **files/**: Dateien, Bilder und Dokumente
- **_config.yml**: Jekyll-Konfiguration für GitHub Pages
- **.devcontainer/**: Entwicklungsumgebung für GitHub Codespaces und VSCode

## Mitwirkung

Beiträge sind willkommen! Bitte erstellen Sie einen Pull Request oder öffnen Sie ein [Issue](https://github.com/Schachverein-Dresden-Striesen/Schachverein-Dresden-Striesen.github.io/issues) für Vorschläge oder Verbesserungen.
Aktueller Meilenstein: [Milestones](https://github.com/Schachverein-Dresden-Striesen/Schachverein-Dresden-Striesen.github.io/milestones).

## Lokale Entwicklung

### Voraussetzungen

**Option A – GitHub Codespaces:** kein lokales Setup erforderlich, nur ein GitHub-Account

**Gemeinsame Voraussetzungen für Option B und C:**

- [Git](https://git-scm.com/)

**Option B – VSCode mit Devcontainer (zusätzlich):**

- [VSCode](https://code.visualstudio.com/)
- [Docker](https://www.docker.com/)

**Option C – Lokale Installation (zusätzlich):**

- Ruby (Version 2.7 oder höher)
  - Windows: [RubyInstaller](https://rubyinstaller.org/)
  - macOS: `brew install ruby` (mit [Homebrew](https://brew.sh/))
  - Linux: Paketmanager Ihrer Distribution verwenden

### Setup

1. **Repository klonen** *(nur für Option B und C nötig)*:

   ```bash
   git clone https://github.com/Schachverein-Dresden-Striesen/Schachverein-Dresden-Striesen.github.io.git
   ```

2. **Entwicklungsumgebung wählen:**

   **Option A: GitHub Codespaces (kein lokales Setup nötig)**

   [GitHub Codespaces](https://docs.github.com/de/codespaces/overview) startet eine vollständige Entwicklungsumgebung direkt im Browser – keine lokale Installation erforderlich.

   - Auf der Repository-Seite: **Code → Codespaces → Codespace erstellen auf ...**
   - Oder per [GitHub CLI](https://cli.github.com/): `gh codespace create`
   - Die Umgebung basiert auf `.devcontainer/devcontainer.json` und startet fertig konfiguriert mit allen Abhängigkeiten

   > **Kosten:** Jeder GitHub-Account bietet ein monatliches [kostenloses Kontingent](https://docs.github.com/de/billing/concepts/product-billing/github-codespaces#free-quota) (Kernstunden + Speicher). Nach Überschreitung des Kontingents können Kosten entstehen. Weitere Informationen unter [Codespaces-Abrechnung](https://docs.github.com/de/billing/concepts/product-billing/github-codespaces).

   **Option B: VSCode mit Devcontainer**

   ```bash
   code .
   ```

   - VSCode wird automatisch vorschlagen, den Container zu öffnen
   - Oder: `F1` → "Dev Containers: Reopen in Container"
   - Abhängigkeiten werden automatisch installiert

   **Option C: Lokale Installation**

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

