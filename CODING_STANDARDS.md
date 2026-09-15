# Coding Standards

This document captures the coding conventions for the Schachverein-Wiki project. Most rules are enforced automatically via `black` and `ruff`; this file documents the judgment calls that require human review.

## Python Version

- **Minimum**: Python 3.10
- **Tested on**: Python 3.11+
- Use type annotations wherever possible; they improve readability and enable tooling support.

## Style & Formatting

- **Line length**: 100 characters (enforced by Black)
- **Indentation**: 4 spaces (PEP 8)
- **Import order**: Standard library → third-party → local (enforced by Ruff/isort)
- Format all code with `black` before committing (enforced by pre-commit hook)
- Lint with `ruff check` to catch undefined names and style violations
- On Windows or systems where tool executables are not in PATH, use Python module invocation: `python -m black`, `python -m ruff`

Run `make verify` to check that all modules import successfully, or manually:
```bash
cd src
python -m black --check .
python -m ruff check .
```

## Type Annotations

Use type annotations on all public functions and class methods:

```python
def extract_players(html: str) -> list[PlayerReference]:
    """Extract player references from club roster HTML."""
    ...
```

Type annotations on local variables are optional but encouraged for complex types. 

## Docstrings

Follow the existing project style: **one-line docstrings for simple functions, multi-line for complex ones.**

**One-liner** (public function with clear purpose):
```python
def extract_tournament_code(url: str) -> str:
    """Extract tournament UUID from tournament detail page URL."""
```

**Multi-line** (public function with complex logic or multiple steps):
```python
def extract_matches(html: str, tournament_url: str) -> list[MatchResult]:
    """
    Extract individual match results from tournament detail page.
    
    Each match row includes opponent name, rating, result (1/0.5/0),
    expected value, and captured timestamp.
    
    Args:
        html: Raw HTML of tournament detail page
        tournament_url: URL for cross-referencing
        
    Returns:
        List of MatchResult records
    """
```

**Model to follow**: See `src/scraping/extractors.py` and `src/normalize/normalizer.py` for examples.

No docstring needed for obvious properties, private methods (`_method`), or test helper functions—make the code self-documenting instead.

## Import Organization

```python
from __future__ import annotations  # Keep at top for Python 3.10 compatibility

import logging
from datetime import datetime
from pathlib import Path
from typing import Optional

from beautifulsoup4 import BeautifulSoup
from neo4j import GraphDatabase

from scraping.extractors import PlayerHistoryScraper
from storage.neo4j_client import Neo4jClient
```

Organize as: future imports → stdlib → third-party → local. Ruff will flag violations.

## Error Handling

- **Be specific**: Catch and raise specific exception types, not bare `Exception`
- **Log before re-raising**: Include context in logs so errors are debuggable
- **Avoid silent failures**: Do not use `except: pass` without a comment explaining why

```python
try:
    driver.verify_connectivity()
except neo4j.exceptions.ServiceUnavailable as e:
    LOGGER.error("Neo4j connection failed: %s", e)
    raise
```

## Testing

- Use pytest with fixtures (existing pattern)
- Test fixtures are stored in `src/tests/` alongside tests
- HTML fixtures for scrapers live in `docs/` and are loaded by fixtures in `src/tests/`
- One test file per module being tested (e.g., `test_extractors.py`, `test_normalizer.py`)
- Aim for 80%+ coverage of core logic (extractors, normalizer, storage)

## Classes and Modules

- **Single Responsibility**: Each class should have one reason to change
- **No God objects**: If a class exceeds ~300 lines, consider splitting it
- **Clear names**: Class names are nouns (Player, Tournament); method names are verbs (extract_players, add_result)

Example:
```python
class ClubRosterScraper:
    """Extracts player roster from club page HTML."""
    
    def extract_players(self, html: str) -> list[PlayerReference]:
        """Return list of players from roster."""
```

## Comments

- **Explain why, not what**: The code shows what it does; comments explain decisions
- **Avoid obvious comments**: 
  ```python
  # BAD: x = x + 1  # increment x
  
  # GOOD: delay_seconds = exponential_backoff(attempt)  # exponential backoff for retries
  ```
- Reserve comments for non-obvious algorithmic choices, workarounds, or external constraints

## Module Organization

**Scraping** (`src/scraping/`):
- `extractors.py`: Parser classes (ClubRosterScraper, PlayerHistoryScraper, TournamentDetailScraper)
- `club_scraper.py`: Web driver setup and page fetching
- `workflow.py`: Orchestration layer

**Normalization** (`src/normalize/`):
- `normalizer.py`: Parsing and canonicalization functions
- `transform.py`: Data transformation helpers

**Storage** (`src/storage/`):
- `neo4j_client.py`: Graph database operations
- `snapshot_store.py`: HTML snapshot persistence

**Configuration** (`src/config/`):
- `settings.py`: Environment-based configuration (dataclass with @dataclass decorator)

**Tests** (`src/tests/`):
- `test_extractors.py`: Parser unit tests
- `test_normalizer.py`: Normalization unit tests
- Fixtures load HTML from `docs/`

## Pre-Commit Hooks

Before committing, the following checks run automatically (via Husky + lint-staged):
- `black` for formatting (auto-fix)
- `ruff check --fix` for auto-fixable violations
- `ruff check` for reporting other violations (manual fix required)

If a check fails, the commit is blocked. Review the error, fix it, and try again. You can skip hooks with `git commit --no-verify` if needed, but don't make a habit of it.

## Review Checklist

When reviewing a PR, check:
- [ ] Code follows style above (black/ruff should catch most)
- [ ] Functions/classes have docstrings explaining purpose and arguments
- [ ] Error handling is specific (not bare except)
- [ ] Type annotations present on public APIs
- [ ] Tests updated for new code or bug fixes
- [ ] No console.log or print() left behind (use logging module instead)
- [ ] Constants are UPPERCASE; public functions are snake_case
- [ ] Imports organized correctly (stdlib → third-party → local)
