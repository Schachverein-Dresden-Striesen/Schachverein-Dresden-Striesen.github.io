# Vereins-Wiki - Schachverein Dresden-Striesen e.V.

Diese Website wird mit GitHub Pages und Jekyll erstellt und automatisch bereitgestellt. Sie enthält alle notwendigen Dateien und Konfigurationen für die automatische Veröffentlichung bei Änderungen.

## Projektstruktur

- **index.md**: Hauptseite der Website
- **pages/**: Inhaltsseiten des Vereins
- **files/**: Dateien, Bilder und Dokumente
- **_config.yml**: Jekyll-Konfiguration für GitHub Pages
- **.devcontainer/**: Entwicklungsumgebung für VSCode

## Lokale Entwicklung

### Voraussetzungen

- [Git](https://git-scm.com/)
- [VSCode](https://code.visualstudio.com/) (empfohlen)
- [Docker](https://www.docker.com/) (für Devcontainer)

### Option 1: VSCode mit Devcontainer (empfohlen)

Diese Methode funktioniert plattformübergreifend auf Windows, macOS und Linux:

1. **Repository klonen**:
   ```bash
   git clone https://github.com/Schachverein-Dresden-Striesen/Vereins-Wiki.git
   cd Vereins-Wiki
   ```

2. **In VSCode öffnen**:
   ```bash
   code .
   ```

3. **Devcontainer starten**:
   - VSCode wird automatisch vorschlagen, den Container zu öffnen
   - Oder: Drücken Sie `F1`, tippen Sie "Dev Containers: Reopen in Container"
   - Der Container wird automatisch mit allen benötigten Abhängigkeiten erstellt

4. **Abhängigkeiten installieren** (im Container-Terminal):
   ```bash
   bundle install
   ```

5. **Entwicklungskonfiguration erstellen** (optional, für bessere lokale Entwicklung):
   ```bash
   echo "github: false" > _config_dev.yml
   echo "repository: \"\"" >> _config_dev.yml
   ```

6. **Website lokal starten**:
   ```bash
   # Mit Entwicklungskonfiguration (empfohlen):
   bundle exec jekyll serve --host 0.0.0.0 --config _config.yml,_config_dev.yml
   
   # Oder ohne Entwicklungskonfiguration:
   bundle exec jekyll serve --host 0.0.0.0
   ```

Die Website ist dann unter `http://localhost:4000` erreichbar.

### Option 2: Lokale Installation

Falls Sie keinen Docker verwenden möchten:

1. **Ruby installieren** (Version 2.7 oder höher)
   - Windows: [RubyInstaller](https://rubyinstaller.org/)
   - macOS: `brew install ruby` (mit [Homebrew](https://brew.sh/))
   - Linux: Paketmanager Ihrer Distribution verwenden

2. **Repository klonen**:
   ```bash
   git clone https://github.com/Schachverein-Dresden-Striesen/Vereins-Wiki.git
   cd Vereins-Wiki
   ```

3. **Bundler installieren**:
   ```bash
   gem install bundler
   ```

4. **Abhängigkeiten installieren**:
   ```bash
   bundle install
   ```

5. **Entwicklungskonfiguration erstellen** (optional):
   ```bash
   echo "github: false" > _config_dev.yml
   echo "repository: \"\"" >> _config_dev.yml
   ```

6. **Website lokal starten**:
   ```bash
   # Mit Entwicklungskonfiguration (empfohlen):
   bundle exec jekyll serve --config _config.yml,_config_dev.yml
   
   # Oder ohne Entwicklungskonfiguration:
   bundle exec jekyll serve
   ```

Die Website ist dann unter `http://localhost:4000` erreichbar.

### Inhalte bearbeiten

- Bearbeiten Sie Markdown-Dateien (`.md`) in VSCode oder Ihrem bevorzugten Editor
- Änderungen werden automatisch beim Speichern übernommen (Live-Reload)
- Neue Seiten können im `pages/` Verzeichnis erstellt werden

### Deployment

Änderungen werden automatisch über GitHub Actions veröffentlicht, wenn sie in den `main`-Branch gepusht werden.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
