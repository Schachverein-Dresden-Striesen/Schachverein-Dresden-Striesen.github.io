# 07: Create CODING_STANDARDS.md with project conventions

**What to build:** Document the project's coding conventions, style expectations, and review criteria. This serves as a reference for contributors and reviewers, encoding the judgment calls that automated tools cannot enforce (e.g., "write docstrings for public functions like the extractors do").

**Blocked by:** None (can start immediately)

**Status:** ready-for-agent

- [ ] Create `CODING_STANDARDS.md` with sections for:
  - Python version and general style (reference PEP 8, note that black/ruff enforce most of it)
  - Docstring expectations (point to existing examples in `scraping/extractors.py` and `normalize/normalizer.py` as models to follow)
  - Type annotations (use them; mypy optional for now, but annotate public APIs)
  - Import organization (isort/ruff style; no circular imports)
  - Module/class organization (single responsibility, no God objects)
  - Test structure (existing pytest + fixture pattern is the standard; keep it)
  - Error handling (be specific; avoid bare except clauses)
  - Comments and docstrings (only for non-obvious logic; self-documenting code preferred)
- [ ] Keep it concise (~200–300 lines) and point to external references (PEP 8, Black docs) for detail
- [ ] Update AGENTS.md with a pointer to this document for review-time reference
- [ ] Ensure it reflects the actual style of the existing codebase (extractors, normalizer, neo4j_client)
