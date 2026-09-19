# Skill: Link-Validierung

Prüft alle internen und externen Links im Repository des Schachvereins Dresden-Striesen auf häufige Fehler.

## Vorgehensweise

### 1. Interne Links mit abschließendem Slash finden

Durchsuche alle Markdown-Dateien in `pages/` und `index.md` nach Links, die mit `/` enden:

```bash
grep -rn '](/[^)]*/)' pages/ index.md
```

Solche Links funktionieren in der Vorschau, schlagen aber auf GitHub Pages fehl.

**Korrekt**: `[Vorstand](/vorstand)`  
**Falsch**: `[Vorstand](/vorstand/)`

### 2. Links zu nicht existierenden internen Seiten

Extrahiere alle internen Links (beginnend mit `/`) und prüfe, ob die entsprechende Seite existiert:
- Seiten in `pages/` werden unter `/:basename` erreichbar (z.B. `/vorstand`)
- Turnierberichte unter `/turnierberichte/:basename`
- Sonderfall: `/` verweist auf `index.md`

### 3. HTTP statt HTTPS bei externen Links

```bash
grep -rn '](http://' pages/ index.md
```

Externe Links sollten auf HTTPS verweisen, um Mixed-Content-Warnungen zu vermeiden.

### 4. Navigation prüfen

Prüfe, ob alle URLs in `_data/navigation.yml` auf existierende Seiten verweisen und keinen abschließenden Slash haben.

## Ausgabe

Liste alle gefundenen Probleme gruppiert nach Typ:
- 🔴 Links mit abschließendem Slash
- 🟡 Links auf nicht existierende Seiten
- 🟡 HTTP-Links (statt HTTPS)

Für jedes Problem: Dateiname, Zeilennummer und Korrekturvorschlag.
