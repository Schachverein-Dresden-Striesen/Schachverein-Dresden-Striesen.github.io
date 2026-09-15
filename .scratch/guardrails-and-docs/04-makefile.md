# 04: Create Makefile with standard development commands

**What to build:** Add a Makefile at the project root with convenience commands for common development tasks: install dependencies, run tests, verify modules, and run the scraper. This gives agents and humans a discoverable interface to the project's standard operations.

**Blocked by:** 01: Create requirements.txt with all dependencies

**Status:** ready-for-agent

- [ ] Create Makefile with the following targets:
  - `make install` → `pip install -r requirements.txt`
  - `make test` → `cd src && pytest tests/ -v`
  - `make verify` → `cd src && python -c "from scraping.extractors import *; from normalize.normalizer import *; print('✓ All modules OK')"`
  - `make run` → `cd src && python main.py` (with a note about required environment variables)
- [ ] Add `.PHONY` declarations for all targets so they run unconditionally
- [ ] Include a help target (`.DEFAULT_GOAL := help`) that lists all commands with brief descriptions
- [ ] Verify all commands run successfully in a test environment
