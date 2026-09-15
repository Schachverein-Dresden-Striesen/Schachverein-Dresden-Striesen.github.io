# Piece Color Tracking

## Overview

Capture and preserve the piece color (white or black) that each player used in tournament matches. This enables future analysis by color, opening preparation, and player statistics by side.

## Why now?

Chess analysis often depends on knowing which color a player had. Historical data shows DWZ website already encodes this in the Spielberichtsbogen (tournament detail pages) via CSS classes on result cells.

## Source

DWZ Spielberichtsbogen pages contain result cells marked with CSS classes:
- `result white` — player played white and result is shown
- `result black` — player played black and result is shown

Examples:
- `docs/dwz-turniere-019f75b9-af1b-77c0-9614-6aaa54318656-019f75bb-27e6-7af4-9050-9065be61a5fc.html` (round 3, Diego Pascual vs Fiedler: `<td class="right-line bottom-line result white">½</td>`)
- `docs/dwz-turniere-c20ee10e-fba0-4b31-9fc6-5539a037b5be-edb2919d-dcce-46c2-91fb-ea8ab6a06389.html` (multiple matches showing similar pattern)

## Data model changes

**MatchResult** gains:
- `piece_color: Literal["white", "black"]` — enum-like string representing the piece color

**Normalizer** gains logic to:
- Extract color from CSS class name in source HTML
- Canonicalize variants (e.g., "White" → "white", "Weiß" → "white", "w" → "white")
- Raise error if color is missing (flag as ambiguous data)

## Implementation strategy (for next sprint)

1. Add `Enum` class to `src/config/settings.py` or new `src/scraping/colors.py`
2. Update `MatchResult` dataclass in `src/scraping/extractors.py`
3. Extend `TournamentDetailScraper._extract_match_row()` to read color from CSS class
4. Add normalization logic in `Normalizer` to validate/canonicalize
5. Add tests in `src/tests/test_extractors.py` and `src/tests/test_normalizer.py`
6. Update workflow to track and store color

---

## Context

- **Requested**: 2026-09-15
- **Priority**: Nice-to-have (not blocking current sprints)
- **Domain**: MatchResult.piece_color
- **Related docs**: CONTEXT.md (MatchResult definition)
