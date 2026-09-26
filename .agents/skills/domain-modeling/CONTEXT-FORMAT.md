# CONTEXT.md-Format

## Struktur

```md
# {Kontextname}

{Ein oder zwei Sätze, die beschreiben, was dieser Kontext ist und warum er existiert.}

## Sprache

**Bestellung**:
{Eine Beschreibung des Begriffs in ein oder zwei Sätzen}
_Avoid_: Kauf, Transaktion

**Rechnung**:
Eine Zahlungsaufforderung, die nach der Lieferung an den Kunden gesendet wird.
_Avoid_: Zahlungsaufforderung

**Kunde**:
Eine Person oder Organisation, die Bestellungen aufgibt.
_Avoid_: Auftraggeber, Account
```

## Regeln

- **Sei deutlich.** Wenn es mehrere Wörter für dasselbe Konzept gibt, nimm das beste und liste die anderen unter `_Avoid_` auf.
- **Halte Definitionen knapp.** Maximal ein bis zwei Sätze. Definiere, was es *ist*, nicht, was es *tut*.
- **Nimm nur Begriffe auf, die spezifisch für den Kontext dieses Projekts sind.** Allgemeine Programmierkonzepte (Timeouts, Fehlertypen, Utility-Muster) gehören nicht hinein, auch wenn das Projekt sie häufig nutzt. Bevor du einen Begriff hinzufügst, frage dich: Ist das ein Konzept, das nur in diesem Kontext relevant ist, oder ein allgemeines Programmierkonzept? Nur Ersteres gehört hinein.
- **Gruppiere Begriffe unter Überschriften**, wenn natürliche Cluster entstehen. Wenn alle Begriffe zu einem zusammenhängenden Bereich passen, ist eine flache Liste auch okay.

## Einzelner vs. mehrere Kontexte

**Einzelner Kontext (die meisten Repositories):** Ein `CONTEXT.md` an der Root des Repositories.

**Mehrere Kontexte:** Eine `CONTEXT-MAP.md` an der Root listet die Kontexte, wo sie liegen und wie sie zueinander in Beziehung stehen:

```md
# Kontextkarte

## Kontexte

- [Bestellung](./src/ordering/CONTEXT.md): erhält und verfolgt Kundenbestellungen
- [Abrechnung](./src/billing/CONTEXT.md): erzeugt Rechnungen und verarbeitet Zahlungen
- [Auslieferung](./src/fulfillment/CONTEXT.md): organisiert Kommissionierung und Versand

## Beziehungen

- **Bestellung → Auslieferung**: Bestellung veröffentlicht `OrderPlaced`-Ereignisse; Auslieferung verarbeitet sie, um mit der Kommissionierung zu beginnen
- **Auslieferung → Abrechnung**: Auslieferung veröffentlicht `ShipmentDispatched`-Ereignisse; Abrechnung verarbeitet sie, um Rechnungen zu erzeugen
- **Bestellung ↔ Abrechnung**: gemeinsame Typen für `CustomerId` und `Money`
```

Die Skill erkennt automatisch, welche Struktur gilt:

- Wenn `CONTEXT-MAP.md` existiert, lese sie, um die Kontexte zu finden
- Wenn nur ein Root-`CONTEXT.md` existiert, handelt es sich um einen einzelnen Kontext
- Wenn keines existiert, erstelle lazily ein Root-`CONTEXT.md`, sobald der erste Begriff geklärt wurde

Wenn mehrere Kontexte existieren, schließe daraus, zu welchem aktuellen Thema der aktuelle Punkt gehört. Wenn das unklar ist, frage nach.
