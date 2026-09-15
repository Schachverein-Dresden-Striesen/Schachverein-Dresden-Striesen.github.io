# Player Tournament History Scraper

This package implements a modular, testable scraper architecture for capturing and preserving player tournament history from the Schachbund website.

## Architecture

The system is organized into three stages:

1. **Club Roster Discovery** (`scraping/extractors.py::ClubRosterScraper`)
   - Extracts player list from club page
   - Returns: `PlayerReference[]` (name, ZPS#, profile URL)

2. **Player History Extraction** (`scraping/extractors.py::PlayerHistoryScraper`)
   - Extracts tournament history from player profile
   - Returns: `HistoricalTournamentEntry[]` per player

3. **Tournament Detail Extraction** (`scraping/extractors.py::TournamentDetailScraper`)
   - Extracts individual match results
   - Returns: `MatchResult[]` per tournament

## Directory Structure

- `scraping/`: Extractors for the three-stage pipeline
  - `extractors.py`: `ClubRosterScraper`, `PlayerHistoryScraper`, `TournamentDetailScraper`
  - `club_scraper.py`: Selenium-based page fetching (existing)
  - `workflow.py`: Orchestration of the complete pipeline

- `normalize/`: Normalization and canonicalization
  - `normalizer.py`: `Normalizer` class for converting extracted data to canonical schema
  - `transform.py`: Legacy transformation code (existing)

- `storage/`: Persistence layer
  - `neo4j_client.py`: Neo4j operations (enhanced with new methods)
  - `snapshot_store.py`: Raw HTML snapshot preservation

- `config/`: Configuration
  - `settings.py`: Runtime settings (club URL, Neo4j connection, etc.)

- `tests/`: Test suite
  - `test_extractors.py`: Unit tests for each extractor with fixture HTML
  - `test_normalizer.py`: Tests for normalization logic

- `data/`: Data artifacts directory (raw and normalized)

## Key Features

### Resilience
- **Snapshots**: All raw HTML preserved for auditability and reprocessing
- **Non-fatal errors**: Individual row failures don't block extraction
- **Graceful handling**: Missing fields treated as None, not errors

### Testability
- **Fixture-based**: Tests use real HTML from `docs/` directory
- **Deterministic**: No browser or external dependencies in unit tests
- **Modular**: Each extractor testable in isolation

### Maintainability
- **Clear contracts**: `HTML → List[Record]` interface for each extractor
- **Separation of concerns**: Extraction, normalization, storage in separate layers
- **Deduplication**: Stable keys prevent duplicate records
- **Logging**: Detailed logging at each stage for troubleshooting

## Running the Workflow

From the project root:

```bash
python3 src/main.py
```

This will:
1. Fetch the club roster page
2. Extract player list
3. Process each player's tournament history
4. Extract tournament details for each tournament
5. Normalize and store all records to Neo4j
6. Report summary of extracted and stored records

## Configuration

Environment variables (set via `.env` or shell):

- `DWZ_USERNAME`: Username for Schachbund login
- `DWZ_PASSWORD`: Password for Schachbund login
- `NEO4J_SERVERURL`: Neo4j server URL (default: `bolt://localhost:7687`)
- `NEO4J_USER`: Neo4j username (default: `neo4j`)
- `NEO4J_PASSWORD`: Neo4j password (default: `password`)

## Implementation Details

### Extractors

All extractors follow the same pattern:
1. Parse HTML with BeautifulSoup using CSS selectors
2. Find the main data table
3. Iterate through rows, extracting known columns
4. Return strongly-typed records (dataclasses)
5. Log errors for individual rows, but don't raise exceptions

### Normalizer

Converts raw extracted data into canonical form:
- Player names: Convert "First Last" to "Last, First"
- Results: Map chess result codes (1, ½, 0) to floats (1.0, 0.5, 0.0)
- Numbers: Parse German format (comma decimal) and English format
- URLs: Extract stable tournament codes from URL patterns
- Deduplication: Generate stable keys for detecting duplicates

### Storage

Neo4j schema:
- `Player` nodes with `zps_number`, `profile_url`, `club_id`
- `Tournament` nodes with `name`, `year`, `code`, `url`
- `PARTICIPATED_IN` relationships with tournament statistics
- `MatchResult` nodes for individual games
- `PLAYED_AGAINST` relationships for player matchups

## Testing

Run tests with pytest (requires: `pip install pytest beautifulsoup4`):

```bash
python3 -m pytest src/tests/test_extractors.py -v
python3 -m pytest src/tests/test_normalizer.py -v
```

Tests use fixture HTML files from `docs/`:
- `dwz-vereine-F2810.html`: Club roster
- `dwz-spieler-NU4241593.html`: Player profile
- `dwz-turniere-...html`: Tournament detail page

## Future Extensions

The modular architecture supports adding:
- Match notation extraction (PGN parsing)
- FIDE ELO scraper
- Historical data backfill
- Event-driven or scheduled updates
- Additional federation sites

See `Architecture Documentation` in the root directory for detailed design.

