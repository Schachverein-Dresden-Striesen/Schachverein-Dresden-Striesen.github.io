# Preserve player tournament history

## Purpose

Keep a durable, queryable record of each player’s tournament history from the current Schachbund club page, even after the source site changes or pages are restructured.

## Trigger

- Primary trigger: an event-driven refresh when the club roster page or a player profile page changes.
- Fallback trigger: a scheduled weekly refresh to catch missed updates.
- Event-triggering is preferred because the source is a public site and the workflow is driven by discovered changes, not by fixed calendar churn.

## Loop

Each run of the workflow is one pass over the current club roster and the known player set.

1. Load the club roster page for the Dresden-Striesen association page.
2. Enumerate all current players and their profile URLs.
3. For each player, fetch the player details page.
4. Extract tournament-history rows and normalize them into canonical fields.
5. Compare against the stored history.
6. Save new/updated records and keep a source snapshot.
7. Send a single brief to the human only when there are ambiguous or changed records.

## Canonical fields

Each tournament-history record should include:

- player_id or player_name
- source_url
- tournament_name
- tournament_date
- event_type or category if present
- round or board if present
- opponent_name
- result
- source_snapshot_path
- captured_at

## Extraction rules

- Prefer the newest official club page as the source of truth.
- Store both normalized structured data and raw HTML/page snapshots for auditability.
- Treat identity links as stable anchors: player profile URL, player name, and the club roster position are used to match records.
- Keep a per-player history log so the same tournament can be seen over time as page changes occur.

## Checkpoint

- No checkpoint for silent, fully parsed, no-change runs.
- One human checkpoint only when a run finds new records, changed data, or extraction ambiguity.
- The checkpoint should be a brief summarizing: what changed, which players were affected, and any rows that need manual confirmation.

## Push right

Do the following before human review:

- fetch the page
- parse the rows
- normalize fields
- deduplicate against current history
- identify only the truly ambiguous entries
- assemble the review brief

This keeps human involvement to one late decision point.

## Brief

The brief is a short summary, not raw data.

Example:

> 3 players had tournament-history updates. 11 new entries were captured, 2 rows were ambiguous due to formatting changes, and one historical record was re-linked to the correct player profile. Review the ambiguous rows here: [link to review view or file].

## Output

The workflow produces:

- a normalized history dataset for players and tournaments
- a raw source snapshot for each fetched page
- a change log showing additions and edits
- an optional Neo4j or JSON store compatible with the existing project structure

## Definition of done

This workflow is done when an implementer could build it without asking another question about scope, trigger, output format, or checkpoint behavior.

## Recommended implementation note

The current repo already contains the right building blocks: Python scrapers, a Neo4j data layer, and a storage pattern for historical pages. The new workflow should extend that pattern rather than replace it.
