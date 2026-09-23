---
name: domain-modeling
description: Das Domänenmodell eines Projekts aktiv schärfen und pflegen. Nützlich bei der Diskussion von Begriffen, beim Bearbeiten von CONTEXT.md oder beim Erfassen von ADRs.
---

# Modellierung der Domäne

Baue und schärfe das Domänenmodell des Projekts aktiv mit, während du entwirfst. Das ist die *aktive* Disziplin: Begriffe hinterfragen, Randfälle erfinden und das Glossar sowie die Entscheidungen sofort dokumentieren, sobald sie klar werden. (Bloßes *Lesen* von `CONTEXT.md` als Vokabular ist nicht diese Skill: Das ist eine Einzeiler-Gewohnheit, die jede Skill übernehmen kann. Diese Skill dient dazu, das Modell zu verändern, nicht nur zu konsumieren.)

## Dateistruktur

Die meisten Repositories haben einen einzigen Kontext:

```
/
├── CONTEXT.md
├── docs/
│   └── adr/
│       ├── 0001-event-sourced-orders.md
│       └── 0002-postgres-for-write-model.md
└── src/
```

Wenn an der Wurzel eine `CONTEXT-MAP.md` existiert, hat das Repository mehrere Kontexte. Die Karte zeigt, wo jeder von ihnen liegt:

```
/
├── CONTEXT-MAP.md
├── docs/
│   └── adr/                          ← Entscheidungen auf Systemebene
├── src/
│   ├── ordering/
│   │   ├── CONTEXT.md
│   │   └── docs/adr/                 ← kontextbezogene Entscheidungen
│   └── billing/
│       ├── CONTEXT.md
│       └── docs/adr/
```

Erstelle Dateien nur dann, wenn du auch etwas Relevantes dokumentieren willst. Wenn kein `CONTEXT.md` existiert, erstelle eines, sobald der erste Begriff geklärt ist. Wenn kein `docs/adr/` existiert, erstelle es, sobald die erste ADR benötigt wird.

## Während der Sitzung

### Begriffe gegen das Glossar prüfen

Wenn ein Nutzer einen Begriff verwendet, der mit der bestehenden Sprache in `CONTEXT.md` nicht übereinstimmt, nenne das sofort. "Dein Glossar definiert 'Stornierung' als X, aber du scheinst Y zu meinen. Welche Bedeutung ist gemeint?"

### Unscharfe Sprache präzisieren

Wenn der Nutzer vage oder überladene Begriffe verwendet, schlage einen präzisen kanonischen Begriff vor. "Du sagst 'Konto': meinst du den Kunden oder den Benutzer? Das sind unterschiedliche Dinge."

### Konkrete Szenarien diskutieren

Wenn Domänenbeziehungen besprochen werden, prüfe sie mit konkreten Szenarien. Erfinde Szenarien, die Grenzfälle aufdecken und den Nutzer zwingen, die Grenzen zwischen Begriffen präzise zu bestimmen.

### Mit dem Code abgleichen

Wenn der Nutzer beschreibt, wie etwas funktioniert, prüfe, ob der Code das ebenfalls bestätigt. Wenn du einen Widerspruch findest, stelle ihn offen: "Dein Code storniert komplette Bestellungen, aber du hast gerade gesagt, eine Teilstornierung sei möglich. Was ist richtig?"

### CONTEXT.md direkt aktualisieren

Wenn ein Begriff geklärt ist, aktualisiere `CONTEXT.md` sofort an Ort und Stelle. Staple diese Änderungen nicht: Erfasse sie direkt. Verwende das Format aus [CONTEXT-FORMAT.md](./CONTEXT-FORMAT.md).

`CONTEXT.md` sollte völlig frei von Implementierungsdetails sein. Behandle es nicht als Spezifikation, Notizblock oder Sammelstelle für Implementierungsentscheidungen. Es ist nur ein Glossar.

### ADRs sparsam anbieten

Biete nur dann an, eine ADR zu erstellen, wenn alle drei Bedingungen erfüllt sind:

1. **Schwer rückgängig zu machen**: Die Kosten, später die Meinung zu ändern, sind erheblich.
2. **Ohne Kontext überraschend**: Ein späterer Leser wird sich fragen: "Warum haben sie es so gemacht?"
3. **Das Ergebnis eines echten Trade-offs**: Es gab echte Alternativen, und man hat sich bewusst für eine entschieden.

Wenn eine der drei Bedingungen fehlt, überspringe die ADR. Verwende das Format in [ADR-FORMAT.md](./ADR-FORMAT.md).
