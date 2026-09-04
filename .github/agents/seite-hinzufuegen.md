# Skill: Neue Inhaltsseite hinzufügen

Legt eine neue Inhaltsseite im Repository des Schachvereins Dresden-Striesen an.

## Eingabe

Der Nutzer gibt an:
- Thema / Titel der Seite
- Inhalt oder Stichpunkte
- Ob die Seite im Navigationsmenü erscheinen soll

## Vorgehensweise

1. **Dateinamen bestimmen**: `pages/seitenname.md`
   - Kurzname, Kleinbuchstaben, Bindestriche statt Leerzeichen
   - Kein Datum im Dateinamen (das ist nur für Turnierberichte)
   - Beispiele: `jugend.md`, `schulschach.md`, `vereinsturniere.md`

2. **Front Matter einfügen**:
   ```yaml
   ---
   layout: single
   title: "Seitentitel"
   sidebar:
     nav: "main"
   ---
   ```
   - Der Permalink wird automatisch aus `_config.yml` gesetzt: `/seitenname` (kein Slash am Ende)

3. **Inhalt verfassen**:
   - Sprache: Deutsch
   - Überschriften-Hierarchie: `##` für Hauptabschnitte, `###` für Unterabschnitte
   - Emojis in Fließtext sind im Vereinsstil akzeptiert
   - `<!-- markdownlint-disable MD033 -->` vor HTML-Blöcken setzen

4. **Navigation ergänzen** (falls gewünscht):
   - Datei `_data/navigation.yml` öffnen
   - Unter `main:` neuen Eintrag hinzufügen:
     ```yaml
     - title: "Seitentitel"
       url: /seitenname
     ```
   - URL ohne abschließenden Slash!

## Qualitätsprüfung

- Interne Links immer ohne Slash am Ende: `/vorstand` ✓, `/vorstand/` ✗
- Front Matter vollständig und korrekt
- Build prüfen: `bundle exec jekyll build`
