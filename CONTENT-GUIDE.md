# Content Creator Guide

Du willst einen Turnierbericht, eine Ankündigung oder andere Inhalte hinzufügen?
Du brauchst **keine technischen Kenntnisse** — alles funktioniert im Browser.

## Schnellstart

1. Öffne [unser GitHub Repository](https://github.com/Schachverein-Dresden-Striesen/Schachverein-Dresden-Striesen.github.io)
2. Melde dich an
3. Navigiere zu `pages/turnierberichte/` (für Berichte) oder `pages/` (für neue Seiten)
4. Klicke **Add file** → **Create new file**
5. Benenne die Datei (z.B. `2026-10-turnier-seiffen.md`)
6. Schreib deinen Inhalt in Markdown (siehe unten)
7. **Commit** und **Propose changes**
8. Fertig! Dein Bericht wird überprüft und live geschaltet.

## Markdown Template für Turnierberichte

```markdown
---
layout: page
title: "Name des Turniers"
date: 2026-10-15
categories: turnierberichte
---

# Name des Turniers

Kurzer Teaser oder Zusammenfassung.

## Ergebnisse

- 1. Platz: Name
- 2. Platz: Name

## Bericht

Dein Turnierbericht hier...
```

### Vordefinierte Felder

- **layout**: `page` (lassen wie es ist)
- **title**: Titel deines Berichts
- **date**: Datum des Turniers (Format: JJJJ-MM-TT)
- **categories**: `turnierberichte` für Turnierberichte, `ankündigungen` für Ankündigungen

## Benennungskonvention

Dateinamen folgen dem Muster: `JJJJ-MM-TT-ereignis-name.md`

**Beispiele:**
- `2026-10-15-turnier-seiffen.md`
- `2026-09-20-verbandstag-ankündigung.md`
- `2026-12-01-weihnachtsfeier.md`

**Regeln:**
- Nur Kleinbuchstaben
- Zahlen und Bindestriche
- Keine Umlaute oder Sonderzeichen (außer Bindestrich)
- Deutsche Datumsangabe: Tag-Monat-Jahr

## Markdown Basics

Du brauchst kein Markdown-Experte zu sein. Hier die wichtigsten Formatierungen:

### Überschriften

```markdown
# Hauptüberschrift (die wird automatisch vom Titel übernommen)
## Zweite Ebene
### Dritte Ebene
```

### Fettdruck und Kursiv

```markdown
**Fettgedruckt** (wichtige Worte)
*Kursiv* (Hervorhebungen)
```

### Listen

```markdown
- Punkt 1
- Punkt 2
- Punkt 3

1. Erster Punkt
2. Zweiter Punkt
3. Dritter Punkt
```

### Links

```markdown
[Linktext](https://beispiel.de)
```

## Hilfreiche Tipps

- **Bilder hochladen:** Bitte zunächst ein Issue öffnen oder das Team kontaktieren — Bilder sollten optimiert werden
- **Längere Berichte:** Nutze Unterabschnitte mit `##` und `###` für bessere Lesbarkeit
- **Quellen zitieren:** Wenn du Informationen aus anderen Quellen verwendest, füge einen Link hinzu
- **Vorschau:** Auf GitHub kannst du den "Preview"-Tab nutzen, um zu sehen, wie dein Bericht aussieht

## Weitere Infos

- **Neu bei GitHub?** → [GitHub Anfänger-Guide](GITHUB-EINSTIEG.md)
- **Fragen oder Probleme?** → Wende dich an [unser Team](https://github.com/Schachverein-Dresden-Striesen/Schachverein-Dresden-Striesen.github.io/people)
- **Schnellere Rückmeldung?** → Öffne ein [Issue](https://github.com/Schachverein-Dresden-Striesen/Schachverein-Dresden-Striesen.github.io/issues) und erkläre, was du ändern möchtest
