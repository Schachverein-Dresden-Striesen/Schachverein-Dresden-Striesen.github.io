# Skill: Markdown-Review

Führt ein redaktionelles und technisches Review einer oder mehrerer Markdown-Dateien durch.

## Eingabe

Der Nutzer gibt eine oder mehrere Dateien an, die geprüft werden sollen (z.B. einen neuen Turnierbericht oder eine Inhaltsseite).

## Vorgehensweise

### 1. Technische Prüfung

- **Front Matter**: Sind `layout`, `title` und `sidebar.nav` vorhanden?
- **Titel-Format**: Für Turnierberichte: `"TT.MM.JJJJ - Beschreibung"`?
- **Überschriften-Hierarchie**: Beginnt der Inhalt mit `##` (nicht `#`, da der Titel aus Front Matter kommt)?
- **HTML-Blöcke**: Ist `<!-- markdownlint-disable MD033 -->` vor inline-HTML gesetzt?
- **Interne Links**: Kein abschließender Slash (`/seite` ✓, `/seite/` ✗)?
- **Externe Links**: HTTPS statt HTTP?

### 2. Sprachliche Prüfung (Deutsch)

- Rechtschreibung und Grammatik
- Korrekte Schreibweise von Namen (Personen, Orte, Vereine)
- Datumsformat: TT.MM.JJJJ (z.B. `25.04.2026`)
- Vereinsname: „Schachverein Dresden-Striesen e.V." (mit Bindestrich und „e.V.")

### 3. Redaktionelle Prüfung

- Ist der Text klar und verständlich für Vereinsmitglieder und Interessierte?
- Sind Ergebnisse strukturiert (Tabellen für Platzierungen)?
- Sind Quellenangaben für historische Inhalte vorhanden?
- Ist der Ton vereinsgemäß (freundlich, informativ, ohne Werbejargon)?

## Ausgabe

Gliedere das Feedback in:
- 🔴 **Muss behoben werden** (technische Fehler, falsche Fakten)
- 🟡 **Sollte verbessert werden** (Stil, Klarheit)
- 🟢 **Gut gelöst** (Lob für gelungene Stellen)

Schlage konkrete Korrekturen vor und erkläre, warum die Änderung den Text verbessert.
