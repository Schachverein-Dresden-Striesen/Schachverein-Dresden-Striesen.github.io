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

Beiträge sind willkommen! Bitte lesen Sie zunächst unsere [Beitragsrichtlinien](CONTRIBUTING.md) und den [Content-Style-Guide](CONTENT_STYLE_GUIDE.md).

- **Issue erstellen:** [GitHub Issues](https://github.com/Schachverein-Dresden-Striesen/Schachverein-Dresden-Striesen.github.io/issues)
- **Implementierungsplan:** [IMPLEMENTATION_PLAN.md](IMPLEMENTATION_PLAN.md)
- **Milestones:** [GitHub Milestones](https://github.com/Schachverein-Dresden-Striesen/Schachverein-Dresden-Striesen.github.io/milestones)

### Hilfreiche Ressourcen

- [GitHub für Anfänger: Roadmap zu den GitHub-Grundlagen](https://github.blog/developer-skills/github/github-for-beginners-your-roadmap-to-mastering-the-github-essentials/)
- [Content-Templates](templates/) - Vorlagen für Turnierberichte, Ausschreibungen, etc.

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

## GitHub Codespaces

GitHub Codespaces bietet eine vollständige Entwicklungsumgebung direkt im Browser - perfekt für schnelle Änderungen ohne lokales Setup.

### Codespace starten

1. **In GitHub:** Klicken Sie auf `Code` → `Codespaces` → `Create codespace on website`
2. **Warten Sie** ~2-3 Minuten, bis die Umgebung bereit ist
3. **Fertig!** Jekyll ist bereits installiert und konfiguriert

### Kosten

GitHub Codespaces bietet ein **kostenloses Kontingent**:
- **120 Core-Stunden pro Monat** (kostenlos)
- **15 GB Speicher** (kostenlos)

**Beispielrechnung:**
- 2-Core-Maschine (Standard): 60 Stunden/Monat kostenlos
- 4-Core-Maschine: 30 Stunden/Monat kostenlos

Für typische Content-Arbeiten (1-2 Stunden/Woche) ist das kostenlose Kontingent **mehr als ausreichend**.

[Mehr zu Codespaces-Kosten →](https://docs.github.com/en/billing/concepts/product-billing/github-codespaces#free-quota)

### Wichtige Kommandos in Codespaces

```bash
# Jekyll-Server starten (Vorschau der Website)
bundle exec jekyll serve

# Build testen (ohne Server)
bundle exec jekyll build

# Neuen Branch erstellen
git checkout -b content/mein-beitrag

# Änderungen committen
git add .
git commit -m "content: Mein Beitrag hinzugefügt"

# Push und Pull Request erstellen
git push origin content/mein-beitrag
```

### Konfigurationsdateien

Folgende Dateien konfigurieren Codespaces:

- **`.devcontainer/devcontainer.json`**: Container-Konfiguration
- **`.github/workflows/copilot-setup-steps.yml`**: Automatisches Setup für GitHub Copilot-Agenten
- **`Gemfile`**: Ruby-Abhängigkeiten

### GitHub Copilot Support

Das Repository enthält eine Copilot-Setup-Workflow (`.github/workflows/copilot-setup-steps.yml`), der die Jekyll-Entwicklungsumgebung für GitHub Copilot-Agenten vorbereitet. 
Dies ermöglicht es Copilot, Ruby-Dependencies automatisch zu installieren und die Jekyll-Build-Umgebung einzurichten.

