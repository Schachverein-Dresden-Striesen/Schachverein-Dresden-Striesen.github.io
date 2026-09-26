# ADR 0001: Single Context Glossary für Domänensprache

**Status:** Accepted  
**Date:** 2026-09-26  
**Deciders:** Agent Team

## Problem

Das Repository arbeitet mit Fachbegriffen aus der Schachvereins-Domäne (Mitglied, Turnier, DWZ, etc.) und der Repository-Verwaltung (Skill, Agentic Work, etc.). Ohne zentrale Quelle für die genaue Bedeutung entstehen Missverständnisse:

- Ein Begriff wird im Gespräch anders interpretiert als gemeint.
- Neue Mitwirkende müssen die Fachsprache "erraten".
- Implementierungsentscheidungen vermischen sich mit Domänen-Definitionen.

## Decision

Das Repository führt ein zentrales **`CONTEXT.md`-Glossar**, das **nur Domänenbegriffe** enthält:

- Schachvereins-Konzepte: Mitglied, Turnier, DWZ, Schulschach, etc.
- **Keine** Repository-Operationen (Skill, Agentic Work, etc.) — diese sind Tooling, nicht Domäne.
- **Keine** Implementierungsdetails (Datenbankschema, APIs, etc.).

Das Glossar ist die Primary Source für die Sprache aller Diskussionen. Wenn ein Begriff mehrdeutig oder umstritten ist, wird er hier geklärt, bevor andere Arbeit fortgeht.

## Rationale

- **Klarheit:** Ein gemeinsames Glossar verhindert 3am-Debugging von Missverständnissen.
- **Separation of Concerns:** Domäne (was der Verein tut) ist getrennt von Tooling (wie wir die Website bauen).
- **Langlebigkeit:** Domänenbegriffe sind stabil; Tooling wechselt. Das Glossar bleibt lesbar.
- **Agent-freundlich:** Eine klare Domänensprache macht es Agents leichter, Anfragen zu verstehen und Fehler zu vermeiden.

## Consequences

- **Pro:** Neue Mitwirkende haben eine klare Referenz.
- **Pro:** Ambiguität wird schnell erkannt und geklärt.
- **Gegen:** Das Glossar muss gepflegt werden — wenn sich ein Begriff ändert, muss es aktualisiert werden.
- **Gegen:** Grenzen zwischen "Domäne" und "Implementierung" erfordern Urteilskraft (aber das ist ein Feature, nicht ein Bug).

## Follow-up

Siehe `.agents/skills/domain-modeling/CONTEXT-FORMAT.md` für das Template und die Regeln.
