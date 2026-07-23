# Content-Style-Guide für die SV Dresden-Striesen Webseite

Dieser Leitfaden definiert Standards für Inhalte auf der Webseite des Schachvereins Dresden-Striesen e.V.

## Inhaltsverzeichnis

- [Sprache und Ton](#sprache-und-ton)
- [Terminologie](#terminologie)
- [Formatierung](#formatierung)
- [Quellenangaben](#quellenangaben)
- [Bildauswahl und Beschriftung](#bildauswahl-und-beschriftung)
- [Verschiedene Content-Typen](#verschiedene-content-typen)

## Sprache und Ton

### Grundprinzipien

- **Sprache**: Deutsch (neue deutsche Rechtschreibung)
- **Ton**: Freundlich, professionell, zugänglich
- **Zielgruppe**: Vereinsmitglieder, interessierte Spieler, Eltern, Öffentlichkeit
- **Perspektive**: Wir-Form ("Unser Verein...", "Wir freuen uns...")

### Anrede

- **Allgemein**: Förmlich mit "Sie" (Ausnahme: direkte Jugendansprache)
- **Jugend-Content**: Informell mit "Du" ist erlaubt
- **Intern**: Bei internen Vereinsangelegenheiten "Du" oder "Sie" je nach Kontext

### Beispiele

✅ **Gut:**
> Wir freuen uns, Sie zu unserem 12. Vereinspokal einzuladen. Das Turnier findet am 12. Juli 2026 in unseren Vereinsräumen statt.

❌ **Vermeiden:**
> Ihr seid eingeladen zum Vereinspokal. Kommt am 12.7. vorbei!

## Terminologie

### Vereinsbezogene Begriffe

| Richtig | Falsch/Vermeiden |
|---------|------------------|
| SV Dresden-Striesen e.V. | SV Striesen, Striesen |
| Schachverein Dresden-Striesen | Verein Striesen |
| Vereinsräume | Clubräume, Schachclub |
| Vereinsmitglied | Mitglied (wenn Kontext unklar) |
| Jugendspielleiter | Jugendtrainer (informell ok) |

### Schachbegriffe

| Richtig | Falsch/Vermeiden |
|---------|------------------|
| Deutsche Wertungszahl (DWZ) | DWZ-Zahl (redundant) |
| Elo-Zahl | ELO, Elo-Rating |
| Bezirksliga | Bezirks-Liga |
| Vereinsmeisterschaft (VM) | VM-Turnier |
| Schnellschach | Speed Chess, Rapidschach |
| Blitzschach | Blitz, Blitz-Turnier |

### Personenbezeichnungen

- Verwenden Sie geschlechtsneutrale oder inklusive Formulierungen
- **Gut**: Spielerinnen und Spieler, Teilnehmende, Mitglieder
- **Akzeptabel**: Spieler (generisches Maskulinum, wenn klar inklusiv gemeint)

## Formatierung

### Datums- und Zeitangaben

| Format | Verwendung | Beispiel |
|--------|------------|----------|
| TT.MM.JJJJ | Standard-Datumsformat | 23.07.2026 |
| TT. Monat JJJJ | Ausgeschriebenes Datum | 23. Juli 2026 |
| TT.MM. | Jahr implizit | 23.07. |
| HH:MM Uhr | Zeitangabe | 14:30 Uhr |
| JJJJ-MM-TT | ISO-Format (Dateinamen) | 2026-07-23 |

### Zahlen und Einheiten

- **Zahlen 0-12**: Ausschreiben (eins, zwei, drei...)
- **Zahlen ab 13**: Ziffern (13, 42, 100)
- **Große Zahlen**: Tausendertrennzeichen mit Punkt (1.000, 10.000)
- **Punkte**: Dezimalformat mit Komma (7,5 Punkte)

### Abkürzungen

| Abkürzung | Ausgeschrieben | Verwendung |
|-----------|----------------|------------|
| DWZ | Deutsche Wertungszahl | Nach erstmaliger Nennung |
| VM | Vereinsmeisterschaft | Nach erstmaliger Nennung |
| DEM | Deutsche Einzelmeisterschaft | Nach erstmaliger Nennung |
| DSJ | Deutsche Schachjugend | Nach erstmaliger Nennung |
| SV | Schachverein | Nur im Vereinsnamen |

### Überschriften

- **H1** (`#`): Seitentitel (wird durch Front Matter definiert)
- **H2** (`##`): Hauptabschnitte
- **H3** (`###`): Unterabschnitte
- **H4** (`####`): Feinere Untergliederung

### Listen

- **Ungeordnete Listen**: `-` für Aufzählungen
- **Geordnete Listen**: `1.` für Rangfolgen, Schrittanleitungen
- **Verschachtelte Listen**: Zwei Leerzeichen Einrückung

### Hervorhebungen

- **Fett** (`**Text**`): Wichtige Begriffe, Betonung
- *Kursiv* (`*Text*`): Fremdsprachen, Publikationstitel
- `Code` (`` `Text` ``): Technische Begriffe, Dateinamen

## Quellenangaben

### Historische Inhalte

Bei historischen Informationen immer Quellen angeben:

```markdown
## 100 Jahre Vereinsgeschichte

Der Schachverein Dresden-Striesen wurde 1923 gegründet.[^1]

[^1]: Quelle: Vereinschronik, Peter Hofmann, 2023
```

### Externe Daten

Bei Tabellen, Statistiken, Ergebnissen:

```markdown
## Turnierergebnisse

Quelle: [Chess-Results](https://chess-results.com/tnr123456.aspx?lan=0)
```

### Bilder

```markdown
![Vereinsfoto 2025](/files/images/vereinsfoto-2025.jpg)

*Foto: Max Mustermann, 2025*
```

## Bildauswahl und Beschriftung

### Bildauswahl

**Verwenden Sie Bilder, die:**
- ✅ Relevant für den Content sind
- ✅ Vereinsaktivitäten zeigen
- ✅ Gute technische Qualität haben
- ✅ Personen nur mit deren Einverständnis zeigen
- ✅ Die Vereinswerte repräsentieren

**Vermeiden Sie:**
- ❌ Stock-Fotos ohne Bezug zum Verein
- ❌ Unscharfe oder schlecht belichtete Bilder
- ❌ Bilder mit Personen ohne Einverständnis
- ❌ Urheberrechtlich geschützte Bilder ohne Lizenz

### Alt-Texte

Jedes Bild braucht einen beschreibenden Alt-Text:

```markdown
![Siegerehrung beim 12. Vereinspokal mit drei Gewinnern](/files/images/vereinspokal-2026.jpg)
```

### Bildunterschriften

Verwenden Sie kursive Bildunterschriften:

```markdown
*Bildunterschrift: Die Gewinner des 12. Vereinspokals bei der Siegerehrung*
```

## Verschiedene Content-Typen

### Turnierberichte

**Struktur:**
1. Einleitung (Datum, Ort, Teilnehmerzahl)
2. Turnierverlauf (Highlights, besondere Partien)
3. Ergebnisse (Tabelle oder Top 3)
4. Fazit (Danksagungen, Ausblick)

**Beispiel:**
```markdown
---
layout: single
title: "Turnierbericht: 12. Vereinspokal"
sidebar:
  nav: "main"
---

Am 12. Juli 2026 fand der 12. Striesener Vereinspokal statt. 
24 Spielerinnen und Spieler kämpften in sieben Runden um den Titel.

## Turnierverlauf

Die erste Runde begann pünktlich um 10:00 Uhr...

## Ergebnisse

| Platz | Name | Punkte |
|-------|------|--------|
| 1 | Max Mustermann | 6,5 |
| 2 | Erika Musterfrau | 6,0 |
| 3 | Hans Schmidt | 5,5 |

[Vollständige Ergebnisse auf Chess-Results](https://chess-results.com/...)

## Fazit

Ein spannender Turniertag mit vielen interessanten Partien. 
Wir danken allen Teilnehmenden und freuen uns auf den 
13. Vereinspokal im kommenden Jahr!

---

[← Zurück zur Startseite]({{ site.baseurl }}/)
```

### Ausschreibungen

**Struktur:**
1. Turnierbezeichnung
2. Datum und Uhrzeit
3. Ort
4. Teilnahmebedingungen
5. Zeitkontrolle
6. Anmeldung
7. Kontakt

**Beispiel:**
```markdown
## 13. Striesener Vereinspokal

**Datum:** Sonntag, 13. Juli 2027  
**Uhrzeit:** 10:00 Uhr  
**Ort:** Vereinsräume, Haydnstraße 49, 01309 Dresden

### Teilnahmebedingungen

Offen für alle Spielerinnen und Spieler ab 16 Jahren.

### Modus

7 Runden Schweizer System  
Bedenkzeit: 40 Minuten + 30 Sekunden Inkrement

### Anmeldung

Bis 10.07.2027 per E-Mail an: turnier@sv-dresden-striesen.de

[Ausschreibung als PDF](/files/ausschreibungen/2027-vereinspokal.pdf)
```

### News und Ankündigungen

**Struktur:**
1. Einprägsame Überschrift
2. Zusammenfassung (Was, Wann, Wo)
3. Details
4. Call-to-Action

**Beispiel:**
```markdown
### Wichtiger Hinweis: Raumänderung im August

**In den kommenden vier Wochen** findet unser Spielbetrieb 
vorübergehend in der Fechterhalle statt.

**Neuer Ort:**  
Fechterhalle, Weißeritzstraße 2, 01067 Dresden

**Zeitraum:**  
01.08. - 31.08.2026

Weitere Informationen zur [Anfahrt](#).
```

### Mannschaftsberichte

**Struktur:**
1. Mannschaft und Liga
2. Gegner und Datum
3. Spielverlauf (Brett für Brett)
4. Endergebnis
5. Tabellensituation

**Beispiel:**
```markdown
## 1. Mannschaft: Sieg gegen SK König Dresden

**Liga:** Bezirksliga Dresden  
**Datum:** 15.10.2026  
**Ergebnis:** 5:3

### Spielverlauf

**Brett 1:** Max Mustermann - Gegner: 1:0  
**Brett 2:** Erika Musterfrau - Gegner: 0,5:0,5  
...

### Tabellenstand

Nach diesem Sieg steht unsere 1. Mannschaft auf Platz 3 
der Bezirksliga.

[Aktuelle Tabelle auf nuLiga](https://svs-schach.liga.nu/...)
```

## Checkliste für neuen Content

Vor Veröffentlichung prüfen:

- [ ] Deutsche Rechtschreibung korrekt
- [ ] Terminologie konsistent verwendet
- [ ] Datumsformat TT.MM.JJJJ
- [ ] Alle Links funktionieren
- [ ] Bilder optimiert und mit Alt-Text
- [ ] Quellenangaben vorhanden (wenn nötig)
- [ ] Front Matter vollständig
- [ ] Rücklink zur Startseite
- [ ] Markdown-Syntax korrekt
- [ ] Lokale Vorschau getestet

## Weiterführende Ressourcen

- [CONTRIBUTING.md](CONTRIBUTING.md) - Technische Beitragsrichtlinien
- [README.md](README.md) - Repository-Dokumentation
- [Duden Online](https://www.duden.de/) - Rechtschreibung
- [Jekyll Dokumentation](https://jekyllrb.com/docs/) - Technische Details

---

**Letzte Aktualisierung:** Juli 2026
