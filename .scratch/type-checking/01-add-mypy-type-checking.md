# 01: Add mypy type checking to pre-commit guardrails

**What to build:** Enable automated type checking that catches type safety issues (like incorrect use of `str | None` vs `Literal["white", "black"]`) before code review. mypy runs in pre-commit hook, blocks commits with type errors, and prevents pattern mistakes that would otherwise only surface in review.

**Blocked by:** None (can start immediately)

**Status:** ready-for-agent

- [ ] Install mypy as dev dependency in requirements.txt (latest stable)
- [ ] Configure mypy in pyproject.toml with strict mode for `src/`
- [ ] Add `python -m mypy src/` to .lintstagedrc.json as a pre-commit task
- [ ] Run mypy on current codebase; identify and fix any type violations
- [ ] Test pre-commit hook locally: verify it blocks commits with type errors
- [ ] Add "Type Checking with mypy" section to CODING_STANDARDS.md explaining usage and patterns
- [ ] Commit all changes (requirements.txt, pyproject.toml, .lintstagedrc.json, fixes, CODING_STANDARDS.md)

---

## Notes

**mypy Configuration**: Use strict mode for `src/` to catch all type issues early. `tests/` can use basic checks (type coverage still matters but lower stakes).

**CODING_STANDARDS.md Addition**: Include:
- When to use `Literal["a", "b"]` for constrained values (not bare `str | None`)
- When to `raise ValueError` vs return `None` for data quality / required fields
- Code examples (good/bad)
- Reference to related sections in docstrings of dataclasses

**Verification**: After setup, verify mypy catches at least one intentional type error (e.g., temporarily assign a string to an `int` field, run mypy, confirm it reports the error, then revert).
