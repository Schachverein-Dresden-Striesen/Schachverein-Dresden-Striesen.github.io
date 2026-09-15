# Retrospective: Piece Color Feature (2026-09-15)

**Session**: Implementation of piece color tracking for match results (spec: `.scratch/piece-color/spec.md`)  
**Outcome**: ✅ Success (61 tests passing, 18 new) + 2 code review findings  
**Duration**: Full implementation + test + review + fixes  

---

## Summary

The piece color tracking feature was fully implemented and committed successfully. However, **code review identified 2 spec compliance issues** that required fixing after implementation:

1. **Type annotation mismatch**: Used `str | None` instead of `Literal["white", "black"]`
2. **Error handling inverted**: Returned `None` for missing colors instead of raising `ValueError`

Both were caught in code review, not during implementation. This retrospective identifies automation opportunities to catch such issues earlier.

---

## Findings by Category

### 1. ⚠️ **Automated Checks** — Missing type checking (HIGH)

**Problem**: Code review found type annotation issues (`str | None` vs `Literal["white", "black"]`) that an automated type checker could have caught before commit.

**Impact**: 
- Type safety hole in dataclass definitions
- Error handling patterns not validated until review
- Spec compliance flags (like "raise on missing data") invisible to tooling

**Cause**: 
- No type checker (mypy, pylance) in pre-commit hooks or CI
- pyproject.toml has no `[tool.mypy]` config
- CODING_STANDARDS.md mentions types but doesn't specify checking tool

**Recommendation**: 
1. Add type checking to pre-commit hooks: `python -m mypy src/` 
2. Configure mypy in pyproject.toml (strict mode recommended for new code)
3. Update CODING_STANDARDS.md to document Literal usage and enum patterns

**Effort**: Low (add ~5 lines to `.lintstagedrc.json`, ~10 lines to pyproject.toml)

**Checklist**:
- [ ] Install mypy: add to dev dependencies in requirements.txt
- [ ] Configure mypy in pyproject.toml
- [ ] Add `python -m mypy src/` to .lintstagedrc.json
- [ ] Add mypy usage section to CODING_STANDARDS.md
- [ ] Test locally before committing

---

### 2. 📋 **Coding Standards** — Literal types and error handling patterns (MEDIUM)

**Problem**: 
- No documented guidance on when to use `Literal` vs `str | None` for constrained values
- No guidance on error handling pattern: when to `raise` vs return `None` for data quality issues

**Impact**:
- Agent made reasonable choices that violated spec requirements
- Review had to catch and fix both issues
- Future implementations of similar patterns will face the same ambiguity

**Recommendation**:
Add to CODING_STANDARDS.md in a new section **"Enums and Constrained Values"**:

```markdown
### Enums and Constrained Values

Use `Literal["value1", "value2"]` for small, fixed sets of string values (enum-like). Never use bare `str | None` for domain values with a known cardinality.

**Bad**:
```python
piece_color: str | None  # Could be anything
```

**Good**:
```python
from typing import Literal

piece_color: Literal["white", "black"] | None  # Type-safe, self-documenting
```

When a value has only 2-3 possible states, `Literal` is strongly preferred over `str` with documentation-only constraints.

### Data Quality & Error Handling

When normalizing data from external sources, distinguish between:

1. **Missing data that is truly optional**: Return `None` (e.g., optional ratings)
   ```python
   opponent_rating: int | None  # May not exist in source
   ```

2. **Missing data that flags ambiguous/malformed source**: Raise `ValueError` with context
   ```python
   if piece_color is None:
       raise ValueError(f"Match missing piece_color: {opponent}, round {round}")
   ```

Callers should handle the error (log it, skip the record, alert on data quality). Do not silently swallow required fields.
```

**Effort**: Low (add ~30 lines to CODING_STANDARDS.md)

**Checklist**:
- [ ] Add "Enums and Constrained Values" section with Literal guidance
- [ ] Add "Data Quality & Error Handling" section with error patterns
- [ ] Reference both sections from the relevant classes in docstrings

---

### 3. ✅ **Navigation** — Good (no issues)

The agent navigated efficiently:
- Spec was provided as an attachment (clear entry point)
- AGENTS.md pointed to CODING_STANDARDS.md for style guidance
- File locations were standard (`src/scraping/extractors.py`, `src/normalize/normalizer.py`)
- Test fixtures were in expected location (`docs/`)

**No action needed.** Current setup is navigable.

---

### 4. ✅ **Tool Economy** — Appropriate (no issues)

The agent:
- Used subagent for code review (expensive but necessary for spec validation)
- Avoided redundant file reads (batched parallel calls)
- Committed early after fixing review findings

No inefficiencies identified.

---

### 5. ✅ **Information Access** — Spec provided clearly

The spec was provided as an attachment and clearly described:
- Data model changes
- Extraction strategy
- Normalization rules  
- Implementation sequence

Agent had full context from the start.

---

## Action Items (Priority Order)

### High Priority
- [ ] **Add type checking to pre-commit**: Configure mypy + add to .lintstagedrc.json
  - *Why*: Catches type safety issues before review
  - *Effort*: ~20 minutes
  - *Owner*: Agent or human
  
### Medium Priority  
- [ ] **Update CODING_STANDARDS.md**: Add "Enums and Constrained Values" + "Data Quality & Error Handling" sections
  - *Why*: Prevents similar issues in future implementations
  - *Effort*: ~15 minutes
  - *Owner*: Human (knowledge encoding)

---

## Lessons Learned

1. **Specs are checked in review, not implementation**: Code review correctly identified spec violations. This is working as designed, but type checking could move the feedback earlier.

2. **Type safety is a guardrail, not a style preference**: Using `Literal` isn't optional when a value has known cardinality. It's a safety boundary.

3. **Error handling patterns need documented precedent**: When to raise vs return None for data quality was ambiguous. Future implementers need written guidance.

---

## Session Metrics

- **Tests written**: 18 new (61 total)
- **Files modified**: 5 (extractors, normalizer, tests × 2, CONTEXT.md)
- **Code review findings**: 2 (both fixed)
- **Commits**: 1 (after fixes)
- **Pre-commit checks**: Passed (black + ruff)
- **Type checking**: Not run (not in guardrails)

