# 01: Expand CODING_STANDARDS.md with pre-commit integration patterns

**What to build:** CODING_STANDARDS.md documents reusable patterns for integrating tools into pre-commit hooks, so future developers (and agents) can:
- Understand why wrapper scripts are needed for certain tools (lint-staged argument incompatibility)
- Recognize when to use direct tool invocation vs wrapper scripts
- Solve known issues like mypy + numpy stub incompatibility
- Understand data quality error handling patterns (Literal types, ValueError validation)

**Blocked by:** None (can start immediately)

**Status:** ready-for-agent

- [ ] Add section "Pre-commit Tool Integration Patterns" with lint-staged wrapper script guidance and rationale
- [ ] Add section "mypy Known Issues" documenting numpy stub compatibility and workaround (`--follow-imports=skip`)
- [ ] Add section "Data Quality and Type Validation" explaining Literal type usage, when to raise ValueError, and patterns for flagging ambiguous data
- [ ] All sections include code examples from the current codebase (extractors.py piece_color, workflow.py type fixes)
- [ ] Sections cross-reference each other and point to relevant config files (pyproject.toml, .lintstagedrc.json, run_mypy.py)
- [ ] CODING_STANDARDS.md remains under 2,000 lines; if it exceeds that, create a new docs/ reference file and link to it
