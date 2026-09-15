"""
Normalization layer for extracted records.

Converts raw extracted data into a canonical schema with:
- Standardized player names
- Parsed and validated dates
- Normalized result codes
- Deduplication markers
"""

from __future__ import annotations

import logging
import re
from dataclasses import asdict, dataclass
from datetime import datetime
from typing import Any

from scraping.extractors import (
    HistoricalTournamentEntry,
    MatchResult,
    PlayerReference,
)

LOGGER = logging.getLogger(__name__)


@dataclass(frozen=True)
class NormalizedPlayer:
    """Canonicalized player record."""

    name: str  # Last, First format
    zps_number: str
    profile_url: str
    source_page: str  # URL where player was found
    snapshot_timestamp: datetime


@dataclass(frozen=True)
class NormalizedTournament:
    """Canonicalized tournament record."""

    tournament_name: str
    year: str
    tournament_url: str | None
    tournament_code: str | None  # Extracted from URL if possible
    source_page: str
    snapshot_timestamp: datetime


@dataclass(frozen=True)
class NormalizedTournamentEntry:
    """Canonicalized tournament participation record."""

    player: NormalizedPlayer
    tournament: NormalizedTournament
    points: float | None
    par: int | None
    expected_value: float | None
    expected_rating: float | None
    opponent_rating_avg: float | None
    performance_rating: float | None
    rating_after_event: float | None
    entry_type: str  # 'tournament', 'upgrade', etc.
    source_page: str
    snapshot_timestamp: datetime


@dataclass(frozen=True)
class NormalizedMatch:
    """Canonicalized match result record."""

    player: NormalizedPlayer
    tournament: NormalizedTournament
    round: int | None
    opponent_name: str
    opponent_dwz: int | None
    result: float | None  # 1.0, 0.5, 0.0
    expected_value: float | None
    scoresheet_url: str | None
    source_page: str
    snapshot_timestamp: datetime


class Normalizer:
    """Normalizes extracted records into canonical schema."""

    def normalize_player(
        self,
        player_ref: PlayerReference,
        source_page: str,
        snapshot_timestamp: datetime,
    ) -> NormalizedPlayer:
        """Normalize a player reference."""
        return NormalizedPlayer(
            name=self._normalize_name(player_ref.name),
            zps_number=player_ref.zps_number,
            profile_url=player_ref.profile_url,
            source_page=source_page,
            snapshot_timestamp=snapshot_timestamp,
        )

    def normalize_tournament_entry(
        self,
        entry: HistoricalTournamentEntry,
        player: NormalizedPlayer,
        source_page: str,
        snapshot_timestamp: datetime,
    ) -> NormalizedTournamentEntry | None:
        """Normalize a tournament entry from player profile."""
        try:
            tournament_code = self._extract_tournament_code(entry.tournament_url)
            tournament = NormalizedTournament(
                tournament_name=entry.tournament_name,
                year=entry.year,
                tournament_url=entry.tournament_url,
                tournament_code=tournament_code,
                source_page=source_page,
                snapshot_timestamp=snapshot_timestamp,
            )

            return NormalizedTournamentEntry(
                player=player,
                tournament=tournament,
                points=self._parse_float(entry.points),
                par=self._parse_int(entry.par),
                expected_value=self._parse_float(entry.expected_value),
                expected_rating=self._parse_float(entry.expected_rating),
                opponent_rating_avg=self._parse_float(entry.opponent_rating_avg),
                performance_rating=self._parse_float(entry.performance_rating),
                rating_after_event=self._parse_float(entry.rating_after_event),
                entry_type=entry.row_type or "tournament",
                source_page=source_page,
                snapshot_timestamp=snapshot_timestamp,
            )
        except Exception as e:
            LOGGER.error(f"Error normalizing tournament entry: {e}", exc_info=True)
            return None

    def normalize_match(
        self,
        match: MatchResult,
        player: NormalizedPlayer,
        tournament: NormalizedTournament,
        source_page: str,
        snapshot_timestamp: datetime,
    ) -> NormalizedMatch | None:
        """Normalize a match result from tournament detail page."""
        try:
            return NormalizedMatch(
                player=player,
                tournament=tournament,
                round=self._parse_int(match.round),
                opponent_name=self._normalize_name(match.opponent_name),
                opponent_dwz=self._parse_int(match.opponent_dwz),
                result=self._parse_result(match.result),
                expected_value=self._parse_float(match.expected_value),
                scoresheet_url=match.scoresheet_url,
                source_page=source_page,
                snapshot_timestamp=snapshot_timestamp,
            )
        except Exception as e:
            LOGGER.error(f"Error normalizing match result: {e}", exc_info=True)
            return None

    # Normalization utility methods

    def _normalize_name(self, name: str) -> str:
        """Normalize player/opponent names: trim, standardize case."""
        if not name:
            return ""

        # Clean up extra whitespace
        name = " ".join(name.split())

        # Handle special case: "Last, First" format
        # Keep it as-is if already in that format
        if "," in name:
            parts = [p.strip() for p in name.split(",")]
            if len(parts) == 2:
                return f"{parts[0].strip()}, {parts[1].strip()}"

        # Otherwise assume First Last and convert to Last, First
        parts = name.rsplit(" ", 1)
        if len(parts) == 2:
            return f"{parts[1]}, {parts[0]}"

        return name

    def _extract_tournament_code(self, url: str | None) -> str | None:
        """Extract tournament code from URL pattern.

        Expected pattern: dwz-turniere/[CODE]/[PLAYER-ID].html
        """
        if not url:
            return None

        # Extract UUID-like code from URL
        match = re.search(r"dwz-turniere/([0-9a-f-]+)", url)
        if match:
            return match.group(1)

        return None

    def _parse_float(self, value: str | None) -> float | None:
        """Parse a float value, handling various formats."""
        if not value:
            return None

        # Clean up the value: remove non-numeric chars except decimal point and minus
        value = value.strip()
        if not value:
            return None

        # Handle German decimal format (comma)
        value = value.replace(",", ".")

        try:
            return float(value)
        except ValueError:
            LOGGER.debug(f"Could not parse float: {value}")
            return None

    def _parse_int(self, value: str | None) -> int | None:
        """Parse an integer value."""
        if not value:
            return None

        value = value.strip()
        if not value:
            return None

        try:
            return int(value)
        except ValueError:
            LOGGER.debug(f"Could not parse int: {value}")
            return None

    def _parse_result(self, result: str | None) -> float | None:
        """Parse chess result code (1, 0.5, 0 or ½, ½, etc.)."""
        if not result:
            return None

        result = result.strip()

        # Handle common representations
        result_map = {
            "1": 1.0,
            "½": 0.5,
            "0.5": 0.5,
            "0": 0.0,
            "+": 1.0,
            "-": 0.0,
            "=": 0.5,
        }

        if result in result_map:
            return result_map[result]

        # Try to parse as float
        return self._parse_float(result)

    def dedup_key(self, record: Any) -> str:
        """Generate a deduplication key for a record.

        For tournaments: (normalized_name, tournament_code, year)
        For matches: (player_name, tournament_code, round, opponent_name)
        """
        if isinstance(record, NormalizedTournamentEntry):
            return (
                f"tournament:{record.player.name}:"
                f"{record.tournament.tournament_code}:{record.tournament.year}"
            )
        elif isinstance(record, NormalizedMatch):
            return (
                f"match:{record.player.name}:"
                f"{record.tournament.tournament_code}:{record.round}:"
                f"{record.opponent_name}"
            )
        else:
            return hash(asdict(record)).__str__()
