# Vereins-Wiki

Tournament history preservation and analysis for **Schachverein Dresden-Striesen** e.V. (German chess club).

Historic data archive: [portal64neo4j/](portal64neo4j/) contains historical tournament results from youth divisions up to Saxony league level.

---

## Table of Contents

- [Quick Start](#quick-start)
- [Setup](#setup)
- [Running Tests](#running-tests)
- [Running the Scraper](#running-the-scraper)
- [Project Structure](#project-structure)
- [Development](#development)

---

## Quick Start

```bash
# Install dependencies
make install

# Verify modules load
make verify

# Run tests
make test

# Run the scraper workflow
make run
```

---

## Setup

### Requirements

- **Python**: 3.10 or later (tested on Python 3.11+)
- **Operating System**: Windows, macOS, or Linux
- **Neo4j**: (optional) required only if storing results to a graph database

### Step 1: Clone the Repository

```bash
git clone https://github.com/Schachverein-Dresden-Striesen/Vereins-Wiki.git
cd Vereins-Wiki
```

### Step 2: Create Virtual Environment (Recommended)

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- `selenium`: Web automation for fetching DWZ pages
- `pandas`: Data manipulation and analysis
- `beautifulsoup4`: HTML parsing
- `lxml`: XML/HTML processing
- `neo4j`: Graph database driver (for persisting results)
- `python-dotenv`: Environment variable management
- `pytest`: Testing framework

### Step 4: Configure Environment (if using Neo4j)

Create a `.env` file in the project root:

```bash
NEO4J_SERVERURL=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=your_password
DWZ_USERNAME=your_username
DWZ_PASSWORD=your_password
```

Environment variables are loaded by `src/config/settings.py`.

---

## Running Tests

The test suite includes 43 unit tests for scrapers, extractors, and normalizers. They use fixture HTML files stored in `docs/` to ensure reproducible, fast testing without hitting live websites.

### Run all tests:

```bash
make test
```

Or manually:

```bash
cd src && pytest tests/ -v
```

### Run a specific test file:

```bash
cd src && pytest tests/test_extractors.py -v
```

### Run a specific test:

```bash
cd src && pytest tests/test_extractors.py::TestClubRosterScraper::test_extract_players_returns_list -v
```

**Note:** Tests must be run from the `src/` directory because that is the Python package root. The Makefile handles this automatically.

---

## Running the Scraper

The scraper workflow fetches club roster and player tournament history from schachbund.de and stores it to Neo4j.

### Prerequisites

- Neo4j database running and accessible (local or remote)
- DWZ credentials set in `.env` (username and password)
- Firefox WebDriver (automatically downloaded by Selenium on first run, or install geckodriver manually)

### Run the workflow:

```bash
make run
```

Or manually:

```bash
cd src && python main.py
```

The workflow performs these steps:

1. **Fetch club roster** from schachbund.de/dwz-vereine/F2810.html
2. **Extract player list** using ClubRosterScraper
3. **For each player**:
   - Fetch player profile page
   - Extract tournament history using PlayerHistoryScraper
   - For each tournament with a detail URL:
     - Fetch tournament detail page
     - Extract match results using TournamentDetailScraper
4. **Normalize data** (player names, dates, ratings)
5. **Store to Neo4j** (players, tournaments, match results)
6. **Archive raw HTML** snapshots for audit trail and future reprocessing

All stages preserve raw HTML snapshots for reproducibility.

---

## Project Structure

```
Vereins-Wiki/
├── README.md                      # This file
├── CODING_STANDARDS.md            # Code style guide and conventions
├── requirements.txt               # Python dependencies (pinned versions)
├── pyproject.toml                 # Python project metadata and tool config
├── Makefile                       # Convenience commands (make test, make run)
│
├── src/                           # Main Python package (Python path root for imports)
│   ├── main.py                    # Entry point: Player tournament history workflow
│   ├── config/
│   │   └── settings.py            # Configuration: environment variables, paths
│   │
│   ├── scraping/                  # Web fetching and HTML parsing
│   │   ├── club_scraper.py        # Selenium-based page fetching
│   │   ├── extractors.py          # HTML parsers: ClubRosterScraper, PlayerHistoryScraper, TournamentDetailScraper
│   │   └── workflow.py            # Orchestration: three-stage extraction pipeline
│   │
│   ├── normalize/                 # Data cleaning and canonicalization
│   │   ├── normalizer.py          # Parsing and normalization functions
│   │   └── transform.py           # Data transformation helpers
│   │
│   ├── storage/                   # Persistence layer
│   │   ├── neo4j_client.py        # Neo4j graph database operations
│   │   └── snapshot_store.py      # Raw HTML snapshot archival
│   │
│   ├── data/                      # Runtime data directory
│   │   ├── raw_html/              # Intermediate HTML files
│   │   └── snapshots/             # Archived raw HTML snapshots
│   │
│   └── tests/                     # Unit tests (pytest)
│       ├── test_extractors.py     # 15 tests for parsers
│       └── test_normalizer.py     # 28 tests for normalization
│
├── docs/                          # Documentation and test fixtures
│   ├── dwz-spieler-NU4241593.html # Player profile fixture (test data)
│   ├── dwz-vereine-F2810.html     # Club roster fixture (test data)
│   └── adr/                       # Architecture Decision Records
│
├── CONTEXT.md                     # Domain model glossary (domain-driven design)
├── NOTES.md                       # Project notes and goals
│
└── portal64neo4j/                 # Historical tournament data (legacy schema)
    └── ...
```

**Key point**: `src/` is the Python package root. All imports are relative to `src/`, so the Makefile and tests run commands from `src/`.

---

## Development

### Code Style

All code follows the conventions in [CODING_STANDARDS.md](CODING_STANDARDS.md).

**Quick summary:**
- Format with `black` (100-char line length)
- Lint with `ruff` (catch undefined names, import order)
- Write docstrings for public functions
- Use type annotations on public APIs
- Write tests for new features and bug fixes

### Pre-Commit Hooks

Before committing, Husky runs automated checks (via `pre-commit`):
- `black` formats Python files
- `ruff` checks for linting violations

Fix violations and recommit. You can skip with `git commit --no-verify` if needed.

### Running Checks Locally

```bash
# Format code
black src/

# Lint code
ruff check src/

# Run tests
make test

# Verify module imports
make verify
```

### Adding New Tests

Place new tests in `src/tests/` alongside existing test files:

```python
import pytest
from pathlib import Path

@pytest.fixture
def sample_html():
    """Load sample HTML fixture."""
    fixture_path = Path(__file__).parent.parent.parent / "docs" / "sample.html"
    return fixture_path.read_text(encoding="utf-8")

def test_something(sample_html):
    """Test description."""
    assert True
```

Then run: `cd src && pytest tests/test_yourfile.py -v`

---

## Useful Links

- **Club website**: https://www.schachbund.de/dwz-vereine/F2810.html
- **DWZ (German Chess Federation)**: https://www.schachbund.de/
- **Neo4j**: https://neo4j.com/ (optional, for graph storage)
- **Selenium**: https://www.selenium.dev/ (browser automation)
- **pytest**: https://pytest.org/ (testing)

---

## License

[Add license information here, if applicable]

---

## Contributing

See [CODING_STANDARDS.md](CODING_STANDARDS.md) for contribution guidelines.
