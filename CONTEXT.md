# Vereins-Wiki Domain Model

This is the glossary for the club history and tournament data preservation project.

## Core Entities

### Club
A chess association or club recognized by the German chess federation (Deutscher Schachbund).

Example: SV Dresden-Striesen e.V. (F2810)

**Attributes:**
- name: official club name
- zps_id: ZPS club identifier (e.g., F2810)
- federation_url: URL of the club page on schachbund.de

---

### Player
A member of a club, identified uniquely by the combination of normalized name, profile URL, and ZPS number.

Example: Pascual, Diego (profile URL: dwz-spieler/NU4241593.html, ZPS: F2810-1220)

**Attributes:**
- name: canonical player name (Last, First)
- profile_url: stable URL to the player's DWZ profile page
- zps_number: club-specific player identifier
- club: the Club this player belongs to
- current_dwz: most recent German rating
- fide_elo: FIDE rating if available

---

### Tournament
A competitive event recognized by the federation, identified by tournament code and year.

Example: Bezirksliga 2026 (code: 019f75b9-af1b-77c0-9614-6aaa54318656)

**Attributes:**
- name: tournament name
- code: unique identifier (often a UUID from the source site)
- year: the year the tournament took place
- end_date: the date the tournament concluded
- tournament_url: URL to the tournament information page

---

### HistoricalTournamentEntry
A summary row from a player's profile page, representing that player's participation in a single tournament.

This is the aggregate view: one row = one tournament from one player's perspective.

**Attributes:**
- player: the Player
- tournament: the Tournament
- year: year of the tournament
- points: player's score in the tournament
- par: number of rounds played
- expected_value: expected score calculation (We)
- opponent_rating_avg: average DWZ of opponents
- performance_rating: calculated performance (Lstg.)
- rating_after_event: player's DWZ after the tournament

---

### MatchResult
An individual game or match result from a tournament detail page (Spielberichtsbogen).

This is the detailed view: one row = one game played.

**Attributes:**
- player: the Player
- tournament: the Tournament
- round: round number
- opponent_name: name of the opponent
- opponent_dwz: DWZ rating of the opponent
- result: game result (1, 0.5, or 0)
- expected_value: expected score for this game
- score_sheet_url: URL to the match scoresheet (if available)
- captured_at: timestamp when this record was extracted

---

### Snapshot
Raw HTML page stored for auditability and future reprocessing.

**Attributes:**
- source_url: the URL that was fetched
- raw_html: the full HTML content
- captured_at: timestamp of capture
- page_type: 'club_roster', 'player_profile', or 'tournament_detail'

---

### NormalizedRecord
A canonicalized data record ready for storage, derived from raw extracted data.

Normalization includes:
- Player name canonicalization (e.g., "Pascual, Diego" vs "diego pascual")
- Date parsing (various formats → ISO 8601)
- Rating normalization (numeric validation)
- Result standardization (mapping variants to 1, 0.5, 0)

**Attributes:**
- source_data: the original extracted dict
- normalized_fields: canonicalized versions of key fields
- is_ambiguous: flag indicating if human review is needed
- ambiguity_reason: if ambiguous, why (e.g., "missing opponent", "unparseable date")
- snapshot_reference: pointer to the Snapshot this was extracted from

---

## Relationships

- A **Club** contains many **Players**.
- A **Player** participates in many **Tournaments** (creates many **HistoricalTournamentEntry** rows).
- A **Tournament** contains many **MatchResults** (one per game played by any player).
- A **MatchResult** references a **Player** and a **Tournament**.
- Every extracted record has a **Snapshot** for auditability.
- A **NormalizedRecord** wraps extracted data for deduplication and validation.

---

## Key Distinctions

### HistoricalTournamentEntry vs. MatchResult

- **HistoricalTournamentEntry**: Comes from the player's profile page. One row per tournament from that player's view. Summary statistics only.
- **MatchResult**: Comes from the tournament detail page. One row per game played. Round-by-round detail.

A player in one tournament produces:
- 1 HistoricalTournamentEntry (the summary row on the player page)
- N MatchResults (one for each round/opponent faced)

Both are preserved; both are valuable.

---

## Canonical Terms

Use these terms throughout the codebase to avoid ambiguity:

- **player**: never "spieler", "member", or "athlete"
- **tournament**: never "event", "competition", or "turnier"
- **match_result**: never "game", "game_result", or "partie"
- **club_roster**: never "player_list" or "membership_list"
- **historical_entry**: never "history_row", "summary", or "table_row"
- **snapshot**: never "archive", "page_copy", or "backup"

---

## Domain Assumptions

1. Players are uniquely identified by the combination of (normalized_name, profile_url, zps_number). No single field is guaranteed stable across site updates.
2. Tournaments are uniquely identified by (code, year). If the code changes, (name, date) is a fallback.
3. A player cannot play against themselves in the same round.
4. Match results are immutable after the tournament concludes; they do not change on subsequent fetches.
5. Historical entries can be re-fetched and may differ slightly due to rating recalculations; differences are recorded for audit.
6. Snapshots are immutable; they are created once and never modified.
