# 03: Add inline documentation to pyproject.toml

**What to build:** The `[tool.mypy]` section in pyproject.toml includes comments explaining configuration choices and cross-references to CODING_STANDARDS.md, so developers can understand mypy setup without context-switching.

**Blocked by:** None (can start immediately)

**Status:** ready-for-agent

- [ ] Add comment block above [tool.mypy] section explaining purpose ("Type checking configuration") and how to run it manually
- [ ] Add brief rationale comment for each mypy setting:
  - python_version = "3.10" (project minimum)
  - disallow_untyped_defs = true (enforces annotations on public APIs)
  - ignore_missing_imports = true (third-party stubs missing)
  - follow_imports = "skip" (prevents numpy stub version issues)
- [ ] Add comment referencing CODING_STANDARDS.md section on type annotations
- [ ] Include example command: `python run_mypy.py` or `python -m mypy src/ --ignore-missing-imports`
- [ ] Verify pyproject.toml is still valid TOML after adding comments
