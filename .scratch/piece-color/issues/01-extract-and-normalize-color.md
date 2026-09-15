Status: ready-for-agent

# Implement piece color extraction

## Goal

Extract and normalize piece color (white/black) from DWZ tournament detail pages, add it to MatchResult, and preserve it through the storage pipeline.

## Acceptance criteria

- [ ] `Enum` class for `PieceColor` defined (white, black)
- [ ] `MatchResult.piece_color` added as `PieceColor | None`
- [ ] `TournamentDetailScraper._extract_match_row()` extracts color from CSS class
- [ ] `Normalizer` validates and canonicalizes color (raises error if missing)
- [ ] Existing tests still pass
- [ ] New tests cover: color extraction, canonicalization, missing-color error
- [ ] CONTEXT.md MatchResult definition points to implementation as done

## Implementation notes

**CSS class patterns** (from sample HTML):
- Result cell has class list: `right-line bottom-line result white` → extract "white"
- Result cell has class list: `right-line bottom-line result black` → extract "black"

**Canonicalization rules**:
- Strip whitespace, lowercase
- Map variant spellings: "Weiß"→"white", "Schwarz"→"black"
- Map single-letter: "w"/"W"→"white", "b"/"B"→"black"
- Raise `ValueError` if no match (flag as ambiguous)

**Storage**:
- Optional field in MatchResult (`piece_color: PieceColor | None`)
- Error handling: if CSS class is missing, leave as None and log warning (don't crash)
- Normalizer: if encountering a MatchResult with None piece_color, raise error for human review

## Files to change

- `src/scraping/extractors.py` — MatchResult dataclass, TournamentDetailScraper
- `src/config/settings.py` or `src/scraping/colors.py` — PieceColor enum
- `src/normalize/normalizer.py` — color validation/canonicalization
- `src/tests/test_extractors.py` — test color extraction
- `src/tests/test_normalizer.py` — test color normalization

## Related

- Spec: `.scratch/piece-color/spec.md`
- Domain: CONTEXT.md MatchResult
- Grilling notes: 2026-09-15 session (user decision tree resolved above)
