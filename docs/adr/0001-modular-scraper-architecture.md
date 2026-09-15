# ADR-0001: Modular Scraper Architecture with Generous Timeouts

**Status:** Accepted  
**Date:** 2026-09-15  
**Deciders:** Club history project team

## Context

The project needs to reliably collect player and tournament data from the Schachbund website. The new website structure separates this data across three distinct pages:

1. Club roster page (lists players)
2. Player profile page (player's tournament history)
3. Tournament detail page (individual match results)

The old scraping code was monolithic and tightly coupled to browser automation. The new architecture must be:

- **Modular**: Each page type has its own scraper
- **Testable**: Scrapers can be tested with fixture HTML without a live website
- **Resilient**: One malformed row should not block the entire extraction
- **Auditable**: Raw HTML snapshots must be preserved

Additionally, the scraping job runs on a volunteer-maintained infrastructure with generous time budgets. We do not need to optimize for speed; we can afford to be patient with network latency and to retry failed requests.

## Decision

We will build three independent scraper classes (`ClubRosterScraper`, `PlayerHistoryScraper`, `TournamentDetailScraper`), each with the same contract:

```python
def extract(self, html: str) -> List[Dict]:
    """
    Extract structured records from raw HTML.
    
    Args:
        html: raw HTML page content
    
    Returns:
        list of dicts, one per record found
        
    Raises:
        ScraperError: if the page structure is unrecognizable
    """
```

### Extraction Implementation

- Use BeautifulSoup + CSS selectors, not XPath (simpler, more maintainable)
- Use the example HTML pages in `docs/` as source-of-truth selectors
- Parse with strict schema expectations: if a required field is missing, flag as ambiguous rather than skip

### Error Handling

- **Row-level errors are non-fatal**: If one tournament row fails to parse, log it, add to ambiguity queue, continue with the rest
- **Page-level errors are fatal**: If the page structure is unrecognizable (no player name found, no history table found), raise `ScraperError`
- **Never silently drop data**: Every extracted row is either valid or explicitly marked ambiguous

### Timeout and Retry Strategy

The project runs on a schedule we control. We have generous time budgets and prefer **reliability over speed**. Timeouts are configured as follows:

- **Page fetch timeout**: 60 seconds (vs. typical 10-30 seconds)
  - Rationale: Network latency on volunteer infrastructure is acceptable; we do not serve real-time users
- **Retry strategy**: Up to 3 automatic retries with exponential backoff (1s, 2s, 4s)
  - Rationale: Temporary network hiccups are common; most retries will succeed on the second attempt
- **Max wait per job**: 30 minutes (measured per complete club extraction run)
  - Rationale: Enough time to fetch ~200-400 pages (average club size) at 60s each with retries
- **No backoff between runs**: If a scheduled run fails entirely, the next scheduled run proceeds normally (no exponential backoff across job runs)
  - Rationale: Site outages or maintenance windows are rare and temporary; we do not want to compound delays across runs

**Configuration** (environment variables, with sensible defaults):

```
SCRAPER_FETCH_TIMEOUT_SECONDS=60
SCRAPER_MAX_RETRIES=3
SCRAPER_RETRY_BACKOFF_BASE=1
SCRAPER_JOB_MAX_DURATION_SECONDS=1800  # 30 minutes
SCRAPER_HEADLESS_BROWSER_TIMEOUT=60
```

### No Page Caching Between Runs

Each run fetches all pages fresh. We do not cache pages from previous runs in case the data changed. This is feasible because we run infrequently (e.g., weekly or on-demand) and the site's volume is low (one club, ~200 players).

### Snapshot Strategy

After successful fetch and before parsing, immediately save the raw HTML snapshot with timestamp and URL metadata. If parsing fails later, the snapshot is still available for manual inspection and future reprocessing.

### Orchestration (Single Seam)

The orchestration layer ties the scrapers together:

1. Fetch club page → ClubRosterScraper.extract() → list of PlayerReferences
2. For each player: Fetch player page → PlayerHistoryScraper.extract() → list of HistoricalTournamentEntries
3. For each tournament in the history: Fetch tournament page → TournamentDetailScraper.extract() → list of MatchResults
4. All records pass through Normalizer
5. Normalized records are compared against previous state → identify new/changed/unchanged
6. Only changed records are sent to review queue; unchanged records update metadata only
7. Approved records are persisted to Neo4j

No additional seams are introduced for unit testing; the test boundary is at the scraper's `extract()` method, using fixture HTML as input.

## Alternatives Considered

### Alternative 1: Single Monolithic Scraper
- **Rejected**: Harder to test, harder to reason about, harder to extend with additional data types later
- **Trade-off**: This alternative prioritizes code reuse over modularity

### Alternative 2: Aggressive Timeouts (10 seconds fetch, 1 retry, fail fast)
- **Rejected**: Volunteer infrastructure may have latency spikes; false failures would cause unnecessary re-runs and operator burden
- **Trade-off**: This alternative prioritizes speed over reliability

### Alternative 3: Selenium Throughout (for consistency with existing scripts)
- **Rejected**: Selenium introduces browser overhead, non-determinism, and difficult-to-debug failures; static HTML parsing is sufficient for this site
- **Trade-off**: This alternative maintains consistency with existing codebase at the cost of simplicity and testability

### Alternative 4: Page Caching Between Runs
- **Rejected**: Adds cache invalidation complexity; given low run frequency, the cost of re-fetching is negligible
- **Trade-of**: This alternative reduces network usage but complicates state management

## Consequences

### Positive

1. **Testable**: Each scraper is tested in isolation with fixture HTML; no browser or network required
2. **Resilient**: Row-level failures are isolated; partial extraction succeeds even if some records are ambiguous
3. **Modular**: Adding new data sources (e.g., federation-wide tournament data) requires only a new scraper class
4. **Auditable**: Raw snapshots preserve the exact page state at extraction time, enabling forensics and reprocessing
5. **Reliable**: Generous timeouts and retries tolerate infrastructure latency
6. **Understandable**: Three scrapers with identical contracts are easier to reason about than one complex one

### Negative

1. **More initial code**: Three scraper classes instead of one monolithic extractor (mitigated by identical contracts)
2. **Longer extraction time**: Three independent page fetches per player instead of single-pass extraction (acceptable given time budget)
3. **More network traffic**: Re-fetching known pages on each run instead of incremental updates (acceptable given low run frequency)

## Notes

- This ADR focuses on architectural principles, not implementation details (e.g., specific CSS selectors, exact Normalizer rules). Those belong in the scraper spec.
- Timeout values are recommendations; they can be tuned based on actual observed latency once the scraper is deployed.
- The "generous timeout" philosophy applies only to data collection; the review workflow (human approval before Neo4j write) is separate and has its own timelines.
- If the site implements aggressive bot detection (CAPTCHA, rate limiting), this ADR's assumptions may need to be revisited.
