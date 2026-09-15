# Source package

This directory contains the Python-first project skeleton for the Dresden-Striesen club history workflow.

## Structure

- `scraping/`: browser-based collection of club roster and player pages
- `normalize/`: normalization and cleaning of extracted records
- `storage/`: Neo4j and snapshot persistence
- `config/`: runtime settings and environment-driven configuration
- `data/`: raw and normalized data artifacts

## Run

```bash
python -m src.main
```

This is intentionally a small initial skeleton aligned with the repository’s existing Selenium + Neo4j approach.
