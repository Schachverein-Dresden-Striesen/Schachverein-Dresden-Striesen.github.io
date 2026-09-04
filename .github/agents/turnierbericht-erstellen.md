# Skill: Turnierbericht erstellen

Erstelle einen neuen Turnierbericht für den Schachverein Dresden-Striesen.

## Eingabe

Der Nutzer gibt Informationen zum Turnier an, zum Beispiel:
- Datum des Turniers
- Name des Turniers
- Ergebnisse, Teilnehmer, Platzierungen
- Optional: Bilder oder Dateinamen von Bildern

## Vorgehensweise

1. **Dateinamen bestimmen**: `pages/turnierberichte/JJJJMMTT-Titel-in-Kebab-Case.md`
   - Datum im Format JJJJMMTT (z.B. `20260425`)
   - Titel ohne Umlaute: ä→ae, ö→oe, ü→ue, ß→ss
   - Beispiel: `20260425-Maedchen-Schnellschach-Turnier-Leipzig.md`

2. **Front Matter einfügen**:
   ```yaml
   ---
   layout: single
   title: "TT.MM.JJJJ - Beschreibung des Turniers"
   sidebar:
     nav: "main"
   ---
   ```

3. **Bericht verfassen**:
   - Sprache: Deutsch
   - Stil: klar, vereinsnah, journalistisch
   - Ergebnisse in strukturierten Tabellen darstellen
   - Bilder referenzieren mit relativem Pfad zu `files/`

4. **Bilder einbinden** (falls vorhanden):
   - Dateien liegen in `files/`
   - HTML-Bild-Tags: `<!-- markdownlint-disable MD033 -->` davor setzen

5. **Link auf Übersichtsseite prüfen**: Prüfe, ob ein Link auf `pages/turnierberichte.md` ergänzt werden soll.

## Beispiel-Tabellenformat für Ergebnisse

```markdown
| Platz | Name | Verein | Punkte |
|-------|------|--------|--------|
| 1     | Max Mustermann | SV Dresden-Striesen | 5,0 |
| 2     | Erika Beispiel | SC Musterstadt | 4,5 |
```

## Qualitätsprüfung

- Kein abschließender Slash bei internen Links
- Datum im deutschen Format im Titel (TT.MM.JJJJ)
- Build prüfen: `bundle exec jekyll build`
