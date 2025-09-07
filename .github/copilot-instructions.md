# GitHub Copilot Instructions für Vereins-Wiki

## Repository Kontext

Dies ist das Vereins-Wiki des Schachvereins Dresden-Striesen - ein Markdown- und Jekyll-basiertes Repository für statische Website-Inhalte. Es dient als primäres Repository zur Verwaltung einer Proof-of-Concept-Website für unseren kleinen Schachverein.

## Code-Standards

### Erforderlich vor jedem Commit
- Prüfen Sie, dass Website-Inhalte auf Deutsch verfasst sind, sofern nicht explizit anders angegeben
- Validieren Sie Markdown-Syntax und -Struktur
- Stellen Sie sicher, dass Jekyll-Build erfolgreich verläuft

### Entwicklungsworkflow
- Automatisierter Build mit GitHub Pages Jekyll
- Deutsche Sprache ist Standard für Inhalte, außer technische Dokumentation

## Wichtige Richtlinien

### 1. Markdown Best Practices
- Verwenden Sie konsistente Überschriftenhierarchie (# bis ####)
- Nutzen Sie semantisches Markdown für bessere Lesbarkeit
- Befolgen Sie deutsche Rechtschreibung und Grammatik
- Verwenden Sie relative Links für interne Verweise
- Optimieren Sie Bilder für Web-Performance

### 2. Code-Struktur und Organisation
- Behalten Sie die bestehende Verzeichnisstruktur bei
- Gruppieren Sie verwandte Inhalte logisch
- Verwenden Sie aussagekräftige Dateinamen auf Deutsch
- Dokumentieren Sie komplexe Logik und öffentliche APIs

### 3. Schachverein-spezifische Konventionen
- Historische Inhalte erfordern Quellenangaben
- Turnierergebnisse sollten strukturiert dargestellt werden
- Namen von Personen und Orten in korrekter deutscher Schreibweise
- Jahreszahlen und Daten im deutschen Format (TT.MM.JJJJ)

### 4. Jekyll und GitHub Pages
- Verwenden Sie Jekyll Front Matter für Metadaten
- Testen Sie Builds lokal vor dem Commit
- Nutzen Sie Jekyll-Features wie Collections für strukturierte Inhalte
- Beachten Sie GitHub Pages Limitierungen

## Dateiorganisation
- Hauptverzeichnis: Markdown-Inhalte für Website
- Bilder: Historische Dokumente und Fotos direkt im Repository

## Beitragsrichtlinien

1. **Sprache**: Deutsch für alle Inhalte, außer technische Code-Kommentare
2. **Historische Genauigkeit**: Überprüfen Sie historische Fakten vor dem Hinzufügen
3. **Bildoptimierung**: Komprimieren Sie Bilder angemessen für Web-Nutzung
4. **Markdown-Konsistenz**: Befolgen Sie etablierte Formatierungsstandards
5. **Commit-Nachrichten**: Auf Deutsch, klar und beschreibend

## Häufige Aufgaben

- **Neuen Artikel hinzufügen**: Markdown-Datei im Hauptverzeichnis erstellen
- **Turnierergebnis dokumentieren**: Strukturierte Tabellen verwenden
- **Historisches Dokument**: Mit Quellenangabe und Kontext hinzufügen

## Qualitätssicherung

- Rechtschreibprüfung für deutsche Inhalte
- Link-Validierung für interne und externe Verweise
- Jekyll-Build-Tests vor Deployment
- Responsive Design für mobile Geräte berücksichtigen