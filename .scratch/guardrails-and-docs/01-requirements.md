# 01: Create requirements.txt with all dependencies

**What to build:** A `requirements.txt` file at the project root that lists all direct Python dependencies (selenium, pandas, beautifulsoup4, lxml, neo4j, python-dotenv, pytest) with pinned versions. This becomes the single source of truth for what agents and humans should install.

**Blocked by:** None (can start immediately)

**Status:** ready-for-agent

- [ ] Create `requirements.txt` at project root with all direct dependencies (selenium, pandas, beautifulsoup4, lxml, neo4j, python-dotenv, pytest)
- [ ] Pin versions to currently installed versions for reproducibility
- [ ] Verify `pip install -r requirements.txt` in a fresh environment installs all packages successfully
