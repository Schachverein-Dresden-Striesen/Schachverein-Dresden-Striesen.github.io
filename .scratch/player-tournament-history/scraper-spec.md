## Problem Statement

The repository has legacy scraping scripts for collecting player and tournament data from the German chess federation website, but these scripts are not aligned with the new Schachbund website structure. The new website separates concerns across three distinct pages: the club roster page, individual player profile pages, and tournament detail pages. The current architecture does not reflect this three-stage extraction workflow, making it difficult to maintain, extend, and test the data collection pipeline. As a result, the project cannot reliably capture and normalize player tournament history from the current source.

## Solution

Build a modular, testable scraper architecture that reflects the three-stage extraction flow of the website:

1. **Club roster discovery**: Extract the list of players from the club page.
2. **Player history extraction**: For each player, extract the tournament history and match statistics from their profile page.
3. **Tournament detail extraction**: For each tournament, fetch and normalize individual match results.

Each stage will have its own scraper class with a clear contract: raw HTML in, structured records out. All raw HTML will be preserved as snapshots, all records will be normalized into a canonical schema, and only ambiguous or changed records will require human review.

## User Stories

1. As a club historian, I want to extract the current player roster from the club page, so that I can identify all active club members.
2. As a club historian, I want to extract each player's tournament history from their profile page, so that I have a comprehensive record of their competitive activity.
3. As a club historian, I want to extract individual match results and opponent information from tournament detail pages, so that I can reconstruct the full competitive narrative.
4. As a data engineer, I want the scraper to preserve raw HTML snapshots of every fetched page, so that I can audit what the source data looked like at the time of extraction.
5. As a data engineer, I want each scraper to be independently testable with fixture HTML, so that I can validate extraction logic without a live website or browser.
6. As a data engineer, I want the scraper to extract stable player identities (name, profile URL, ZPS number), so that I can deduplicate and track players across multiple runs.
7. As a data engineer, I want the scraper to extract all tournament metadata (name, date, code, DWZ values), so that tournaments can be uniquely identified and queried.
8. As a data engineer, I want the scraper to extract match-level details (round, opponent, result, expected value), so that individual games are preserved alongside summary statistics.
9. As a data engineer, I want the normalization layer to canonicalize player names and dates, so that minor formatting variations do not create duplicate records.
10. As a data engineer, I want the normalization layer to detect and flag ambiguous or incomplete rows, so that they can be triaged separately from clean data.
11. As a data engineer, I want the scraper to continue extracting valid rows even when individual rows are malformed, so that one bad record does not block the entire run.
12. As a data engineer, I want the system to compare new data against previously stored records, so that only changed or new records are flagged for review.
13. As a repository maintainer, I want the scraper to be fully integrated with the existing Python project structure, so that it uses the same dependencies and patterns already in place.
14. As a repository maintainer, I want the scraper to support both login and public-page access modes, so that it can adapt if the source site's visibility changes.
15. As a repository maintainer, I want all scrapers to log their progress and errors clearly, so that I can diagnose issues without running the code interactively.
16. As a data maintainer, I want the extracted data to flow directly into Neo4j using the existing graph schema, so that the workflow integrates with the current persistence layer.
17. As a data maintainer, I want snapshot metadata (URL, timestamp, source page) to be attached to every record, so that the audit trail is complete.
18. As a data maintainer, I want the system to support incremental and full backfill modes, so that I can run both scheduled updates and one-time historical imports.
19. As a club archivist, I want the review queue to be a small, annotated subset of data only when needed, so that the review process remains lightweight.
20. As a club archivist, I want the system to detect when a player's profile URL or identity has changed, so that historical records can be re-linked correctly.
21. As a club archivist, I want tournament names to be stored alongside normalized versions, so that I can query by both exact and approximate match.
22. As a club archivist, I want to see which tournaments a player has competed in, in chronological order, so that their career progression is clear.
23. As a club archivist, I want to store the opponent's average rating and expected value for each tournament, so that performance metrics can be analyzed.
24. As a club archivist, I want to preserve both the tournament summary row (from the player page) and the detailed match rows (from the tournament page), so that both views of the data are available.
25. As a user of the project, I want the scraper to work with the example pages already in the docs directory, so that I can validate the extraction logic immediately.
26. As a user of the project, I want a clear error message if the website structure changes and selectors no longer match, so that I know what part of the pipeline broke.
27. As a repository maintainer, I want the scraper to be modular enough that I can swap out individual extractors without rewriting the orchestration, so that the system remains flexible.
28. As a repository maintainer, I want the scraper to support rate limiting and polite fetching practices, so that the project does not overload the source website.
29. As a data engineer, I want to be able to run the scraper against a single player page for testing, so that I can develop and validate extraction logic incrementally.
30. As a data engineer, I want the scraper to produce output in both JSON and Neo4j-ready formats, so that it can be used for reporting and archival.

## Implementation Decisions

- The scraper will be structured as three independent extractor classes: `ClubRosterScraper`, `PlayerHistoryScraper`, and `TournamentDetailScraper`. Each will have the same interface: `extract(html: str) -> List[dict]`.
- The extraction logic will be based on BeautifulSoup and CSS selectors derived from the example HTML pages in the docs directory. XPath is avoided in favor of simpler CSS selectors.
- The `ClubRosterScraper` will extract player name, profile URL, and ZPS number from the club roster page. It will identify player links by navigating the page structure and return a canonical PlayerReference object.
- The `PlayerHistoryScraper` will extract the tournament history table from the player profile page. Each row will produce a HistoricalTournamentEntry object with fields: year, tournament_name, tournament_url, points, expected_value, opponent_rating_avg, rating_after_event, and others.
- The `TournamentDetailScraper` will extract individual match rows from the tournament detail page (the Spielberichtsbogen). Each row will produce a MatchResult object with fields: round, opponent_name, opponent_dwz, result, expected_value, and score_sheet_link.
- Player identity will be built from: normalized name + profile URL + ZPS number. This tuple will serve as the stable key for deduplication.
- Tournament identity will be built from: tournament code (UUID in the current site) + year. If the code is not stable, the name + date combination will be used as a fallback.
- The `Normalizer` will canonicalize: player names (trim, standardize case), dates (parse multiple formats), ratings (numeric), results (map to standard result codes: 1, 0.5, 0).
- All raw HTML will be saved with a timestamped filename and stored alongside the extracted records so that the snapshot is always retrievable.
- The orchestration layer will call all three scrapers in sequence and feed their output through the normalizer before persisting to Neo4j.
- The Neo4j schema will use existing patterns from the codebase: nodes for Player, Tournament, Club; relationships for PLAYED, COMPETED_IN, BELONGS_TO.
- The system will maintain a local cache of previously extracted records (as JSON or SQLite) so that new vs. changed records can be identified without hitting Neo4j every time.
- Error handling will be non-fatal: if a single row fails to parse, it will be logged and added to an ambiguity queue, not block the entire extraction.
- The scraper will support both authenticated (login required) and unauthenticated modes via environment variables.
- Logging will be configured per module and sent to files in a logs directory within the project.
- The scraper will not attempt to parse pages beyond the three defined stages; if additional data layers are needed, they will be added as separate scrapers.

## Testing Decisions

A good test for the scrapers will:
- Use the example HTML fixtures already in the docs directory (or similar realistic HTML).
- Call the scraper's extract method with raw HTML as input.
- Assert that the returned list of records matches expected field values and counts.
- Not mock or spy on internal BeautifulSoup calls; test only the external contract (HTML in, records out).
- Not test the orchestration flow in detail; that belongs to an integration test with a real or mock database.

The following modules will be tested:

- **ClubRosterScraper**: Test extraction of player name, profile URL, and ZPS number from the club page fixture.
- **PlayerHistoryScraper**: Test extraction of tournament history rows, including handling of empty cells and multiple tournaments per year.
- **TournamentDetailScraper**: Test extraction of individual match results, including round, opponent, result, and DWZ values.
- **Normalizer**: Test canonicalization of names, dates, and results; test handling of missing fields; test deduplication logic.
- **SnapshotStore**: Test that raw HTML is saved and retrieved correctly; test timestamped filenames.
- **Neo4jClient**: Integration test with a fixture database or test container; test node creation and relationship establishment.

Prior art: The repository already contains Selenium-based extraction scripts in `speichere_dwz_daten.py` and `speichere_turnier_daten.py`. The new test pattern will follow the same logging and error-handling conventions but will isolate the HTML parsing logic so it can be tested deterministically without a browser.

## Out of Scope

- Building a UI or dashboard for browsing historical data.
- Supporting other chess federations or rating systems beyond DWZ.
- Real-time or live match tracking.
- Predictive analytics or ELO calculations.
- Export to formats other than Neo4j and JSON.
- Handling of arbitration reports, tournament complaints, or other non-standard federation data.
- Integration with external federation APIs (if they exist and are not documented).

## Further Notes

- The example HTML pages provided in the docs directory are authentic samples from the current Schachbund website and should be used as the source of truth for selector validation.
- The scraper will be developed incrementally: first the club roster, then player history, then tournament details. Each stage can be tested independently.
- If the website implements anti-scraping measures (CAPTCHA, rate limiting), the project should document workarounds and respect the site's terms of service.
- The project's existing infrastructure (logging, configuration, Neo4j access) is already in place and should be reused by the scraper.
- Future enhancements (such as parsing match notation or fetching FIDE ELO data) can be added as separate extractor modules without affecting the core scraper architecture.
