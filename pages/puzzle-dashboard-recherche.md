---
layout: single
title: "Puzzle-Dashboard Recherche"
sidebar:
  nav: "main"
toc: true
toc_label: "Inhaltsverzeichnis"
toc_icon: "cog"
---

# Recherche: Optionen für Puzzle-Dashboard

Diese Dokumentation fasst die Recherche für das geplante Puzzle-Dashboard zusammen (siehe [Issue #30](https://github.com/Schachverein-Dresden-Striesen/Vereins-Wiki/issues/30)).

## Zielsetzung

Das Puzzle-Dashboard soll eine Übersicht der Puzzle-Aktivitäten der Vereinsmitglieder bieten:
- **Anzeige unter Klarnamen** (keine Benutzernamen der Plattformen)
- **Keine direkten Links** zu den Accounts (Datenschutz)
- **Datenquellen**: Öffentliche APIs von Lichess, chess.com, etc.
- **Beispiel-Account**: Lichess-Nutzer "Ahtemis"

## 1. API-Optionen für Datenquellen

### 1.1 Lichess API

**Vorteile:**
- Vollständig kostenlos und offen
- Umfassende REST API ohne Authentifizierung für öffentliche Daten
- Detaillierte Puzzle-Statistiken verfügbar
- JSON-Format, einfach zu verarbeiten
- Rate Limits sind großzügig (600 Requests/Minute)

**Verfügbare Puzzle-Daten:**
- Puzzle-Rating und Verlauf
- Gelöste Puzzles nach Kategorien
- Performance-Statistiken
- Aktuelle Aktivität

**API-Endpunkte:**
```
GET /api/user/{username}               # Basis-Profildaten
GET /api/user/{username}/rating-history # Rating-Verlauf inkl. Puzzles
```

**Beispiel-Datenstruktur:**
```json
{
  "id": "ahtemis",
  "username": "Ahtemis", 
  "perfs": {
    "puzzle": {
      "rating": 2100,
      "rd": 150,
      "prog": 25
    }
  }
}
```

### 1.2 Chess.com API

**Vorteile:**
- Kostenlos für nicht-kommerzielle Nutzung
- Gute Dokumentation
- Detaillierte Puzzle-Statistiken

**Nachteile:**
- Strengere Rate Limits
- Weniger umfangreiche Puzzle-API als Lichess
- Erfordert User-Agent Header

**API-Endpunkte:**
```
GET /pub/player/{username}             # Profildaten
GET /pub/player/{username}/stats       # Detaillierte Statistiken
```

### 1.3 Chess24, ChessKing (andere Plattformen)

**Status:** Begrenzte oder keine öffentlichen APIs verfügbar.

## 2. Visualisierungsoptionen

### 2.1 Web-basierte Charts (Empfohlen)

**Chart.js**
- **Pro:** Leichtgewichtig, responsive, große Community
- **Con:** Begrenzte Interaktivität bei komplexen Dashboards
- **Verwendung:** Basis-Charts (Linien, Balken, Radar)

**D3.js**
- **Pro:** Maximale Flexibilität, hochinteraktiv
- **Con:** Steile Lernkurve, aufwendiger zu implementieren
- **Verwendung:** Komplexe, maßgeschneiderte Visualisierungen

**Observable Plot**
- **Pro:** Moderne D3-Alternative, einfacher zu verwenden
- **Con:** Noch relativ neu
- **Verwendung:** Schnelle, elegante Visualisierungen

### 2.2 Dashboard-Frameworks

**Grafana**
- **Pro:** Professionelle Dashboard-Lösung, viele Datenquellen
- **Con:** Overkill für einfache Anwendung, erfordert Server

**Tableau Public**
- **Pro:** Mächtige Visualisierungen, keine Programmierung
- **Con:** Daten werden öffentlich, weniger Kontrolle

### 2.3 Empfohlene Visualisierungen für Puzzle-Daten

1. **Rating-Verlauf:** Liniendiagramm über Zeit
2. **Kategorie-Verteilung:** Radar-Chart für verschiedene Puzzle-Themen
3. **Aktivitäts-Heatmap:** Kalender-Ansicht der Puzzle-Aktivität
4. **Leistungsvergleich:** Balkendiagramm für Vereinsmitglieder
5. **Erfolgsquote:** Donut-Chart für gelöste/nicht gelöste Puzzles

## 3. Technische Framework-Optionen

### 3.1 Jekyll-Integration (Empfohlen für diese Website)

**Static Site mit JavaScript:**
```javascript
// Beispiel für Lichess API-Aufruf
async function fetchPuzzleStats(username) {
  const response = await fetch(`https://lichess.org/api/user/${username}`);
  const data = await response.json();
  return data.perfs.puzzle;
}
```

**Vorteile:**
- Passt in bestehende Jekyll-Infrastruktur
- Keine Server-Wartung erforderlich
- GitHub Pages kompatibel

**Nachteile:**
- Client-seitige API-Aufrufe sichtbar
- Rate Limits könnten problematisch werden

### 3.2 Node.js Backend

**Express.js + React/Vue Frontend:**
- **Pro:** Vollständige Kontrolle, Caching möglich, API-Keys verborgen
- **Con:** Hosting-Kosten, Server-Wartung erforderlich

### 3.3 Serverless Functions

**Netlify/Vercel Functions:**
- **Pro:** Automatische Skalierung, geringe Kosten
- **Con:** Cold starts, Komplexität für einfache Anwendung

## 4. Datenschutz und Anonymisierung

### 4.1 Datenschutz-Herausforderungen

**DSGVO-Relevante Aspekte:**
- Verarbeitung personenbezogener Daten (auch wenn öffentlich)
- Erforderlichkeit einer Rechtsgrundlage
- Informationspflicht gegenüber betroffenen Personen
- Recht auf Löschung

### 4.2 Anonymisierungs-Strategien

**Mapping-Tabelle (Empfohlen):**
```javascript
// Verschlüsselte Zuordnung (nicht im öffentlichen Code)
const memberMapping = {
  "ahtemis": "Max Mustermann",
  "user123": "Anna Schmidt",
  // ...
};
```

**Vorteile:**
- Vollständige Kontrolle über Anzeigenamen
- Keine Rückschlüsse auf tatsächliche Accounts möglich
- Einfache Aktualisierung bei Änderungen

**Implementierung:**
- Mapping-Daten in separater, nicht-öffentlicher Datei
- Server-seitige Verarbeitung oder Build-Zeit-Generierung
- Regelmäßige Rotation der Zuordnungen möglich

### 4.3 Rechtliche Empfehlungen

1. **Einverständniserklärung** der Vereinsmitglieder einholen
2. **Datenschutzerklärung** erweitern um Puzzle-Dashboard
3. **Opt-out-Möglichkeit** vorsehen
4. **Minimale Datenerhebung** - nur relevante Puzzle-Statistiken
5. **Regelmäßige Löschung** veralteter Daten

## 5. Implementierungsempfehlung

### 5.1 Empfohlene Architektur

**Phase 1: MVP (Minimal Viable Product)**
```
Jekyll Website
├── JavaScript für API-Aufrufe
├── Chart.js für Visualisierung  
├── Statische Mapping-Datei
└── Einfache Puzzle-Rating-Anzeige
```

**Phase 2: Erweiterte Features**
```
Serverless Functions (Netlify)
├── Sichere API-Aufrufe
├── Daten-Caching
├── Erweiterte Anonymisierung
└── Mehr Visualisierungen
```

### 5.2 Entwicklungsschritte

1. **Prototyp erstellen** (1-2 Wochen)
   - Lichess API-Integration
   - Basis-Chart mit Chart.js
   - Hardcodierte Beispieldaten

2. **Anonymisierung implementieren** (1 Woche)
   - Mapping-System entwickeln
   - Datenschutz-konforme Anzeige

3. **UI/UX verbessern** (1-2 Wochen)
   - Responsive Design
   - Erweiterte Visualisierungen
   - Benutzerfreundliche Navigation

4. **Produktionsreife** (1 Woche)
   - Fehlerbehandlung
   - Performance-Optimierung
   - Dokumentation

### 5.3 Geschätzte Kosten

**Entwicklung:** 20-30 Stunden (ehrenamtlich)
**Hosting:** Kostenlos (GitHub Pages + Netlify Functions Free Tier)
**Wartung:** 2-4 Stunden/Monat

## 6. Risiken und Mitigation

### 6.1 Technische Risiken

**API-Verfügbarkeit:**
- **Risiko:** Lichess/Chess.com API wird eingestellt
- **Mitigation:** Multi-Plattform-Unterstützung, Fallback-Mechanismen

**Rate Limits:**
- **Risiko:** Zu viele API-Aufrufe führen zu Sperrung
- **Mitigation:** Caching, intelligente Update-Zyklen

### 6.2 Datenschutz-Risiken

**Deanonymisierung:**
- **Risiko:** Rückschlüsse auf echte Accounts möglich
- **Mitigation:** Starke Anonymisierung, regelmäßige Rotation

**Ungewollte Datenpreisgabe:**
- **Risiko:** Sensible Spielinformationen werden sichtbar
- **Mitigation:** Strenge Datenminimierung, Opt-out-Optionen

## 7. Fazit und Empfehlung

### Empfohlene Lösung:

1. **Datenquelle:** Lichess API (primär) + Chess.com API (sekundär)
2. **Framework:** Jekyll + JavaScript für MVP
3. **Visualisierung:** Chart.js für einfache Implementation
4. **Hosting:** GitHub Pages (kostenlos)
5. **Anonymisierung:** Server-seitige Mapping-Tabelle

### Begründung:

- **Kosteneffizient:** Passt in bestehende Jekyll-Infrastruktur
- **Datenschutz-konform:** Starke Anonymisierung möglich
- **Wartungsarm:** Wenig zusätzliche Infrastruktur
- **Skalierbar:** Spätere Erweiterungen möglich

### Nächste Schritte:

1. Einverständniserklärung der Mitglieder einholen
2. Datenschutzerklärung aktualisieren
3. MVP-Prototyp entwickeln
4. Feedback der Vereinsmitglieder einholen
5. Iterative Verbesserungen basierend auf Nutzerfeedback

---

**Erstellt:** [Datum]  
**Autor:** Recherche für Issue #31  
**Status:** Entwurf zur Diskussion

[← Zurück zur Startseite]({{ site.baseurl }}/)