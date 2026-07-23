# Implementierungs- und Content-Plan für SV Dresden-Striesen Webseite

**Stand:** 23. Juli 2026  
**Version:** 1.0

## Überblick

Dieser Plan dokumentiert alle identifizierten Tasks zur Verbesserung der Webseite des Schachvereins Dresden-Striesen e.V. basierend auf einer umfassenden Analyse der bestehenden Issues und Platzhalter-Inhalte.

## Zusammenfassung der Analyse

### Statistik

- **Offene Issues:** 16
- **Kategorien:** Technisch (4), Berichte (4), Aktualisierungen (5), Strukturverbesserungen (2), Externe Ressourcen (1)
- **Seiten mit Platzhaltern:** 6 (Schulschach, DWZ-Liste, Mannschaftskämpfe, Jugend, Ausschreibungen, Vereinsturniere)
- **Identifizierte Tasks:** 25

### Status Quo

**Stärken:**
- ✅ CI/CD-Prozess funktioniert (GitHub Pages + Jekyll)
- ✅ Theme-Migration auf Minimal Mistakes abgeschlossen
- ✅ Responsive Design vorhanden
- ✅ Vereins-Branding integriert
- ✅ Devcontainer-Setup für Entwicklung

**Verbesserungsbedarf:**
- ❌ Mehrere fehlerhafte Links
- ❌ Viele Platzhalter-Inhalte
- ❌ Fehlende Turnierberichte
- ❌ Veraltete Informationen
- ❌ Dokumentation unvollständig

## Task-Übersicht

### Priorität 1: Kritische technische Fehler (2 Tasks)

#### TASK-01: Fix broken links on homepage
- **Issue:** #48
- **Beschreibung:** Links von der Startseite reparieren - relative/root Links verwenden
- **Effort:** Low
- **Skill:** Technical/Frontend
- **Deadline:** Sofort
- **Abhängigkeiten:** Keine

#### TASK-02: Fix external links to open in new tab
- **Issue:** #7
- **Beschreibung:** jekyll-extlinks Plugin korrekt konfigurieren
- **Effort:** Low
- **Skill:** Technical/Jekyll Configuration
- **Deadline:** Woche 1
- **Abhängigkeiten:** Keine

---

### Priorität 2: Content - Fehlende Berichte (5 Tasks)

#### TASK-03: Turnierbericht 12. Vereinspokal
- **Issue:** #33
- **Beschreibung:** Ankündigung durch ausführlichen Bericht ersetzen (12.07.2026)
- **Effort:** Medium
- **Skill:** Content/Writing
- **Deadline:** Woche 3
- **Template:** `/templates/turnierbericht-template.md`
- **Abhängigkeiten:** Turnierergebnisse, Fotos

#### TASK-04: Bericht DEM 2026 Willingen
- **Issue:** #17
- **Beschreibung:** Turnierbericht zur Deutschen Einzelmeisterschaft
- **Effort:** Medium
- **Skill:** Content/Writing
- **Deadline:** Woche 3
- **Template:** `/templates/turnierbericht-template.md`
- **Abhängigkeiten:** Informationen von Teilnehmern

#### TASK-05: Bericht SMMs 2026
- **Issue:** #16
- **Beschreibung:** Bericht zu den Sächsischen Meisterschaften
- **Effort:** Medium
- **Skill:** Content/Writing
- **Deadline:** Woche 3
- **Template:** `/templates/turnierbericht-template.md`

#### TASK-06: Bericht Mädchen-Schnellschach-Turnier
- **Issue:** #15
- **Beschreibung:** Turnierbericht verfassen
- **Effort:** Medium
- **Skill:** Content/Writing
- **Deadline:** Woche 4
- **Template:** `/templates/turnierbericht-template.md`

#### TASK-07: Bericht DKJS 2026 integrieren
- **Issue:** #4
- **Beschreibung:** PDF-Bericht von Jörg als Markdown aufbereiten
- **Effort:** Low
- **Skill:** Content/Conversion
- **Deadline:** Woche 4
- **Abhängigkeiten:** PDF-Datei vorhanden

---

### Priorität 3: Content - Aktualisierungen (3 Tasks)

#### TASK-08: Jugendligen 2026/27 aktualisieren
- **Issue:** #43
- **Beschreibung:** Neue Jugendligen-Links auf Jugend-Seite integrieren
- **Effort:** Low
- **Skill:** Content/Update
- **Deadline:** Woche 5
- **Quelle:** https://svs-schach.liga.nu/cgi-bin/WebObjects/nuLigaSCHACHDE.woa/wa/leaguePage?championship=Dresden+Jugend+26%2F27

#### TASK-09: Frauenliga und MSK-Kongress aktualisieren
- **Issue:** #41
- **Beschreibung:** Informationen zur 3. Liga und MSK-Kongress hinzufügen
- **Effort:** Low
- **Skill:** Content/Update
- **Deadline:** Woche 5
- **Quellen:** 
  - https://ergebnisdienst.schachbund.de/bedt.php?liga=fro
  - https://www.deutsche-schachjugend.de/termine/2026/m-kongress/

#### TASK-10: Jugendergebnisse Herbst & Frühling integrieren
- **Issue:** #38
- **Beschreibung:** 15 Chess-results Links strukturiert auf Webseite darstellen
- **Effort:** Medium
- **Skill:** Content/Structuring
- **Deadline:** Woche 5
- **Abhängigkeiten:** Alle Turnier-Links vorhanden

---

### Priorität 4: Content - Seiten mit Platzhaltern (6 Tasks)

#### TASK-11: Schulschach-Seite vollständig ausarbeiten
- **Issue:** #44
- **Beschreibung:** Alle Unterabschnitte füllen
  - Schulkooperationen
  - Schach-AGs
  - Schulschachturniere
  - Lehrmaterialien
  - Fortbildungen
- **Effort:** High
- **Skill:** Content/Writing, Research
- **Deadline:** Woche 6
- **Abhängigkeiten:** Informationen von Schulschach-Verantwortlichen

#### TASK-12: DWZ-Liste komplett überarbeiten
- **Issue:** #34
- **Beschreibung:** 
  - Doppeleinträge entfernen
  - Aktuelle DWZ-Werte integrieren
  - Statistiken erstellen
  - Beste Vereinsspieler auflisten
- **Effort:** High
- **Skill:** Content/Data Processing
- **Deadline:** Woche 7
- **Quelle:** https://www.schachbund.de/verein/F2810.html
- **Abhängigkeiten:** Zugriff auf aktuelle DWZ-Daten

#### TASK-13: Jugend-Seite vervollständigen
- **Beschreibung:** Folgende Abschnitte ergänzen:
  - Jugendgruppen (nach Altersklassen)
  - Trainingszeiten (Wochentag, Uhrzeit, Ort)
  - Ansprechpartner (Name, Kontakt)
  - Erfolge unserer Jugend (Titel, Platzierungen)
  - Jugendturniere (kommende Termine)
- **Effort:** High
- **Skill:** Content/Writing
- **Deadline:** Woche 8
- **Abhängigkeiten:** Informationen von Jugendspielleiter

#### TASK-14: Mannschaftskämpfe - Spielpläne und Tabellen
- **Beschreibung:** 
  - Aktuelle Saison-Infos ergänzen
  - Spielpläne verlinken
  - Tabellen von nuLiga integrieren
  - Kommende Wettkampftermine
- **Effort:** Medium
- **Skill:** Content/Integration
- **Deadline:** Woche 8
- **Quelle:** https://svs-schach.liga.nu/

#### TASK-15: Ausschreibungen erweitern
- **Beschreibung:**
  - Vereinsinterne Turniere dokumentieren
  - Jugendturniere auflisten
  - Anmeldeverfahren erklären
  - Allgemeine Teilnahmebedingungen
- **Effort:** Medium
- **Skill:** Content/Writing
- **Deadline:** Woche 9
- **Template:** `/templates/ausschreibung-template.md`

#### TASK-16: Vereinsturniere - Archiv anlegen
- **Beschreibung:**
  - Vergangene Turniere strukturiert auflisten
  - Turnierkalender für kommende Events erstellen
  - Links zu Ergebnissen und Berichten
- **Effort:** Medium
- **Skill:** Content/Archiving
- **Deadline:** Woche 9

---

### Priorität 5: Strukturverbesserungen (2 Tasks)

#### TASK-17: Ausschreibungen und Vereinsturniere zusammenführen
- **Issue:** #31
- **Beschreibung:** Menüstruktur vereinfachen durch Zusammenführung
- **Neue Struktur:**
  - Offene Turniere (mit Ausschreibungen)
  - Vereinsturniere (VM, VMS, VMB)
  - Jugendturniere
  - Vergangene Turniere (Archiv)
- **Effort:** High
- **Skill:** Content/Restructuring, Technical
- **Deadline:** Woche 10
- **Abhängigkeiten:** TASK-15, TASK-16 abgeschlossen
- **Impact:** Navigation wird übersichtlicher

#### TASK-18: Tags-System überprüfen und optimieren
- **Issue:** #47
- **Beschreibung:** 
  - Aktuelles Tagging-System analysieren
  - Tags einkürzen/erweitern für bessere Übersicht
  - Konsistenz sicherstellen
- **Effort:** Medium
- **Skill:** Technical/Information Architecture
- **Deadline:** Woche 11
- **Seite:** https://www.sv-dresden-striesen.de/tags

---

### Priorität 6: Dokumentation (4 Tasks)

#### TASK-19: Codespaces-Dokumentation im README
- **Issue:** #29
- **Beschreibung:** README erweitern um:
  - GitHub Codespaces Kosten (Free Quota)
  - Konfigurationsdateien erklären
  - Wichtige Kommandos dokumentieren
- **Effort:** Low
- **Skill:** Documentation/Technical
- **Deadline:** Woche 1
- **Quelle:** https://docs.github.com/en/billing/concepts/product-billing/github-codespaces#free-quota

#### TASK-20: Beitragenden-Guide erstellen ✅
- **Beschreibung:** CONTRIBUTING.md mit:
  - Git-Workflow (Branch-Strategie)
  - Markdown-Standards
  - Bildoptimierung
  - Review-Prozess
  - Commit-Message-Konventionen
- **Effort:** Medium
- **Skill:** Documentation
- **Status:** ✅ Erledigt
- **Datei:** `CONTRIBUTING.md`

#### TASK-21: Content-Style-Guide entwickeln ✅
- **Beschreibung:** CONTENT_STYLE_GUIDE.md mit:
  - Deutsche Rechtschreibung und Grammatik
  - Einheitliche Terminologie
  - Datums-/Zeitformate
  - Namenskonventionen
  - Quellenangaben
  - Bildauswahl und -beschriftung
- **Effort:** Medium
- **Skill:** Documentation/Content Strategy
- **Status:** ✅ Erledigt
- **Datei:** `CONTENT_STYLE_GUIDE.md`

#### TASK-22: Link zu GitHub Blog integrieren
- **Issue:** #39
- **Beschreibung:** GitHub-Anfänger-Guide im README verlinken
- **Effort:** Very Low
- **Skill:** Documentation
- **Deadline:** Woche 12
- **Link:** https://github.blog/developer-skills/github/github-for-beginners-your-roadmap-to-mastering-the-github-essentials/

---

### Priorität 7: Zusätzliche Verbesserungen (3 Tasks)

#### TASK-23: Suchfunktion implementieren
- **Beschreibung:** Jekyll-Search-Plugin für bessere Content-Findability
- **Effort:** Medium
- **Skill:** Technical/Jekyll
- **Deadline:** Woche 12
- **Optionen:**
  - jekyll-algolia
  - Simple-Jekyll-Search
  - Lunr.js

#### TASK-24: Bildergalerie für historische Fotos
- **Beschreibung:** Strukturierte Galerie für:
  - Vereinsgeschichte
  - Turnierfotos
  - Mannschaftsfotos
- **Effort:** High
- **Skill:** Technical/Content
- **Deadline:** Woche 14+
- **Optionen:**
  - Jekyll Gallery Generator
  - Minimal Mistakes Gallery Feature

#### TASK-25: RSS-Feed für News und Turnierberichte
- **Beschreibung:** Jekyll-Feed-Plugin konfigurieren
- **Effort:** Low
- **Skill:** Technical/Jekyll
- **Deadline:** Woche 13
- **Plugin:** jekyll-feed

---

## Implementierungs-Roadmap

### Phase 1: Stabilisierung (Wochen 1-2)
**Ziel:** Technische Fehler beheben und Dokumentation verbessern

| Woche | Tasks | Verantwortlich | Status |
|-------|-------|----------------|--------|
| 1 | TASK-01, TASK-19, TASK-22 | Tech-Team | 🔴 Offen |
| 2 | TASK-02 | Tech-Team | 🔴 Offen |

**Deliverables:**
- [x] CONTRIBUTING.md
- [x] CONTENT_STYLE_GUIDE.md
- [x] Content-Templates
- [x] GitHub Issue Templates
- [ ] Erweiterte README
- [ ] Alle Links funktionieren
- [ ] Externe Links öffnen in neuem Tab

---

### Phase 2: Content Completion - Berichte (Wochen 3-4)
**Ziel:** Fehlende Turnierberichte nachreichen

| Woche | Tasks | Verantwortlich | Status |
|-------|-------|----------------|--------|
| 3 | TASK-03, TASK-04, TASK-05 | Content-Team | 🔴 Offen |
| 4 | TASK-06, TASK-07 | Content-Team | 🔴 Offen |

**Deliverables:**
- [ ] 5 neue Turnierberichte
- [ ] Bilder zu Turnieren
- [ ] Links zu Ergebnissen

---

### Phase 3: Content Updates (Woche 5)
**Ziel:** Aktuelle Informationen einpflegen

| Woche | Tasks | Verantwortlich | Status |
|-------|-------|----------------|--------|
| 5 | TASK-08, TASK-09, TASK-10 | Content-Team | 🔴 Offen |

**Deliverables:**
- [ ] Aktuelle Jugendligen verlinkt
- [ ] Frauenliga-Infos aktualisiert
- [ ] Jugendergebnisse strukturiert dargestellt

---

### Phase 4: Major Content Work (Wochen 6-9)
**Ziel:** Alle Platzhalter-Seiten füllen

| Woche | Tasks | Verantwortlich | Status |
|-------|-------|----------------|--------|
| 6 | TASK-11 (Schulschach) | Content-Team | 🔴 Offen |
| 7 | TASK-12 (DWZ-Liste) | Content-Team | 🔴 Offen |
| 8 | TASK-13, TASK-14 | Content-Team | 🔴 Offen |
| 9 | TASK-15, TASK-16 | Content-Team | 🔴 Offen |

**Deliverables:**
- [ ] Schulschach-Seite vollständig
- [ ] DWZ-Liste überarbeitet
- [ ] Jugend-Seite komplett
- [ ] Mannschaftskämpfe aktualisiert
- [ ] Ausschreibungen erweitert
- [ ] Turnier-Archiv angelegt

---

### Phase 5: Strukturelle Verbesserungen (Wochen 10-11)
**Ziel:** Navigation und Struktur optimieren

| Woche | Tasks | Verantwortlich | Status |
|-------|-------|----------------|--------|
| 10 | TASK-17 (Zusammenführung) | Tech+Content | 🔴 Offen |
| 11 | TASK-18 (Tags) | Tech-Team | 🔴 Offen |

**Deliverables:**
- [ ] Vereinfachte Navigation
- [ ] Optimiertes Tag-System
- [ ] Bessere Informationsarchitektur

---

### Phase 6: Dokumentation & Enhancement (Wochen 12-13)
**Ziel:** Zusätzliche Features implementieren

| Woche | Tasks | Verantwortlich | Status |
|-------|-------|----------------|--------|
| 12 | TASK-23 (Suche) | Tech-Team | 🔴 Offen |
| 13 | TASK-25 (RSS) | Tech-Team | 🔴 Offen |

**Deliverables:**
- [ ] Suchfunktion aktiv
- [ ] RSS-Feed verfügbar

---

### Phase 7: Erweiterungen (Woche 14+)
**Ziel:** Nice-to-have Features

| Woche | Tasks | Verantwortlich | Status |
|-------|-------|----------------|--------|
| 14+ | TASK-24 (Galerie) | Tech+Content | 🔴 Offen |

**Deliverables:**
- [ ] Bildergalerie implementiert

---

## Content-Plan: Inhaltliche Prioritäten

### Sofort benötigt (Aktualität)
1. **Turnierberichte 2026** - TASKS 03-07
   - Vereinspokal
   - DEM Willingen
   - SMMs
   - Mädchen-Schnellschach
   - DKJS

2. **Ligaaktualisierungen** - TASKS 08-10
   - Jugendligen 2026/27
   - Frauenliga
   - Jugendergebnisse

3. **Fehlerkorrektur** - TASKS 01-02
   - Links reparieren
   - Externe Links konfigurieren

### Wichtig für Besucher (Informationswert)
1. **Jugend-Informationen** - TASK 13
   - Trainingszeiten
   - Ansprechpartner
   - Altersgruppen

2. **Schulschach-Details** - TASK 11
   - Für interessierte Schulen
   - Für Eltern

3. **Turnierinfos** - TASKS 15-16
   - Ausschreibungen
   - Anmeldeverfahren

### Langfristig wertvoll (Archiv/Historie)
1. **Turnier-Archiv** - TASK 16
   - Strukturierte Historie
   - Ergebnisse vergangener Jahre

2. **Vereinsgeschichte** - TASK 24
   - Bildergalerie
   - Historische Dokumente

3. **Mitgliederprofile** - Future
   - Erfolgsgeschichten
   - Interviews

---

## Erfolgskriterien und Metriken

### Technische Metriken
- [ ] 0 broken links auf der Website
- [ ] 100% externe Links öffnen in neuem Tab
- [ ] Jekyll Build-Zeit < 30 Sekunden
- [ ] Lighthouse Score > 90
- [ ] Mobile-friendly Test bestanden

### Content-Metriken
- [ ] 0 Seiten mit Platzhalter-Inhalten
- [ ] Alle aktuellen Ligen 2026/27 verlinkt
- [ ] Mindestens 10 Turnierberichte pro Jahr
- [ ] DWZ-Liste monatlich aktualisiert
- [ ] Alle Mannschaftsergebnisse aktuell

### Dokumentations-Metriken
- [x] README vollständig (alle Setup-Optionen dokumentiert)
- [x] CONTRIBUTING.md vorhanden
- [x] Content-Style-Guide etabliert
- [x] Mindestens 4 Content-Templates verfügbar
- [x] GitHub Issue Templates erstellt

### Benutzer-Metriken (nach Launch)
- Website-Besuche pro Monat
- Verweildauer auf Seiten
- Bounce Rate
- Mobile vs. Desktop Traffic
- Meistbesuchte Seiten

---

## Risiken und Abhängigkeiten

### Risiken

| Risiko | Wahrscheinlichkeit | Impact | Mitigation |
|--------|-------------------|--------|------------|
| Content-Informationen nicht verfügbar | Hoch | Hoch | Frühzeitig bei Verantwortlichen anfragen |
| Zeitliche Überschneidungen | Mittel | Mittel | Flexible Deadlines, Priorisierung |
| Technische Kompatibität | Niedrig | Hoch | Frühzeitiges Testen |
| Fehlende Bilder | Mittel | Niedrig | Stockfotos als Fallback |

### Abhängigkeiten

**Externe:**
- nuLiga für Mannschaftsergebnisse
- Chess-Results für Turnierergebnisse
- DWZ-Datenbank des Schachbunds

**Interne:**
- Jugendspielleiter (Informationen Jugend)
- Schulschach-Verantwortliche (Schulschach-Content)
- Turnierorganisatoren (Turnierberichte)
- Vorstand (Freigaben, strategische Entscheidungen)

---

## Ressourcen

### Dokumentation
- [CONTRIBUTING.md](CONTRIBUTING.md) - Beitragsrichtlinien
- [CONTENT_STYLE_GUIDE.md](CONTENT_STYLE_GUIDE.md) - Content-Standards
- [README.md](README.md) - Repository-Dokumentation

### Templates
- `/templates/turnierbericht-template.md` - Turnierberichte
- `/templates/ausschreibung-template.md` - Turnierausschreibungen
- `/templates/news-template.md` - News und Ankündigungen
- `/templates/mannschaftsbericht-template.md` - Mannschaftsberichte

### GitHub Issue Templates
- `.github/ISSUE_TEMPLATE/content-beitrag.yml` - Content-Beiträge
- `.github/ISSUE_TEMPLATE/bug-report.yml` - Fehlerberichte
- `.github/ISSUE_TEMPLATE/content-update.yml` - Content-Updates
- `.github/ISSUE_TEMPLATE/feature-request.yml` - Feature-Vorschläge

### Externe Ressourcen
- [Jekyll Dokumentation](https://jekyllrb.com/docs/)
- [Minimal Mistakes Theme](https://mmistakes.github.io/minimal-mistakes/)
- [Markdown Guide](https://www.markdownguide.org/)
- [GitHub Pages](https://pages.github.com/)

---

## Nächste Schritte

### Sofort (diese Woche)
1. ✅ Dokumentation erstellt (CONTRIBUTING.md, CONTENT_STYLE_GUIDE.md)
2. ✅ Templates bereitgestellt
3. ✅ Issue Templates eingerichtet
4. [ ] Team-Meeting: Priorisierung und Verantwortlichkeiten
5. [ ] TASK-01: Fehlerhafte Links reparieren
6. [ ] TASK-19: README erweitern (Codespaces)
7. [ ] TASK-22: GitHub Blog Link hinzufügen

### Kurzfristig (nächste 2 Wochen)
1. [ ] TASK-02: Externe Links konfigurieren
2. [ ] Informationen für Turnierberichte sammeln
3. [ ] Content-Team briefen zu Templates
4. [ ] Erste Turnierberichte erstellen (TASK-03)

### Mittelfristig (nächste 4 Wochen)
1. [ ] Alle ausstehenden Turnierberichte (TASKS 04-07)
2. [ ] Content-Updates durchführen (TASKS 08-10)
3. [ ] Planung für Platzhalter-Seiten (TASKS 11-16)

---

## Change Log

| Datum | Version | Änderungen | Autor |
|-------|---------|-----------|-------|
| 2026-07-23 | 1.0 | Initiale Erstellung des Plans | Copilot Agent |

---

**Kontakt für Fragen zu diesem Plan:**  
GitHub Issues: https://github.com/Schachverein-Dresden-Striesen/Schachverein-Dresden-Striesen.github.io/issues
