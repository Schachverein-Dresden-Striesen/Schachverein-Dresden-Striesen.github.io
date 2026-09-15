# 05: Add pyproject.toml with pytest configuration and metadata

**What to build:** Create a `pyproject.toml` file at the project root that declares the project metadata, pytest configuration, and tool settings. This centralizes Python tooling configuration and enables CI/CD and local automation to discover and run tests reliably.

**Blocked by:** 01: Create requirements.txt with all dependencies

**Status:** ready-for-agent

- [ ] Create `pyproject.toml` with:
  - `[build-system]` declaring build backend (setuptools recommended for simplicity)
  - `[project]` with name, version, description, dependencies (reference requirements.txt), and Python version requirement
  - `[tool.pytest.ini_options]` with testpaths pointing to `src/tests`, python_files pattern, and basic output settings
  - `[tool.black]` with line-length = 100
  - `[tool.ruff]` with line-length = 100 and sensible rules (E, W, F, I for now)
- [ ] Ensure pytest discovers tests correctly when run as `pytest` from the project root (may require adjusting `testpaths`)
- [ ] Verify `pip install -e .` works (developer install from pyproject.toml)
- [ ] Verify `pytest` can discover and run tests (working directory shouldn't matter once pyproject.toml is configured)
