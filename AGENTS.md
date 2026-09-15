## Setup & Development Environment

**When**: setting up the Python environment, installing dependencies, running tests, or debugging import errors.

The [README.md](README.md) contains the authoritative setup guide:
- **Setup**: Python 3.10+, virtual environment, `pip install -r requirements.txt`
- **Running Tests**: `cd src && pytest tests/ -v` (note: `src/` is the Python package root)
- **Running Scraper**: `make run` or `cd src && python main.py`
- **Convenience commands**: `make install`, `make test`, `make verify`, `make run`

For development, see [CODING_STANDARDS.md](CODING_STANDARDS.md) for code style, docstring conventions, and pre-commit hooks.

---

## Agent skills

### Issue tracker
Issues are tracked as local markdown files under `.scratch/`. See `docs/agents/issue-tracker.md`.

### Triage labels
The default canonical triage roles are used: `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`. See `docs/agents/triage-labels.md`.

### Domain docs
Single-context repository: root `CONTEXT.md` and `docs/adr/` are the primary domain docs. See `docs/agents/domain.md`.
