# 02: Optimize mypy wrapper script with documented flags

**What to build:** `run_mypy.py` is self-documenting with clear comments explaining why each command-line flag is needed, so developers understand the configuration and future tool integrations don't require debugging multiple flag combinations.

**Blocked by:** None (can start immediately)

**Status:** ready-for-agent

- [ ] Add comment above each mypy flag explaining its purpose (--ignore-missing-imports, --follow-imports=skip, --no-incremental)
- [ ] Document why --follow-imports=skip prevents numpy stub version conflicts
- [ ] Document why --no-incremental is required for lint-staged (pre-commit doesn't preserve .mypy_cache)
- [ ] Add module-level docstring referencing CODING_STANDARDS.md "mypy Known Issues" section
- [ ] Verify script execution time is sub-second for typical runs (lint-staged responsiveness)
- [ ] Confirm pre-commit hook integration still works with updated script
