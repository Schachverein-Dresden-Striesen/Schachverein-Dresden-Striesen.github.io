"""
Extractors for the three-stage scraping workflow.

Each extractor takes raw HTML and returns structured records:
- ClubRosterScraper: Extracts player list from club page
- PlayerHistoryScraper: Extracts tournament history from player profile
- TournamentDetailScraper: Extracts individual match results
"""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass
from typing import Any, Literal
from urllib.parse import urljoin

from bs4 import BeautifulSoup

LOGGER = logging.getLogger(__name__)


@dataclass(frozen=True)
class PlayerReference:
    """Stable player identity from club roster."""

    name: str
    zps_number: str
    profile_url: str


@dataclass(frozen=True)
class HistoricalTournamentEntry:
    """Tournament summary from player profile page."""

    year: str
    tournament_name: str
    tournament_url: str | None
    points: str | None
    par: str | None
    expected_value: str | None
    expected_rating: str | None
    opponent_rating_avg: str | None
    performance_rating: str | None
    rating_after_event: str | None
    row_type: str  # 'dewis', 'upgrade', etc.


@dataclass(frozen=True)
class MatchResult:
    """Individual match result from tournament detail page."""

    round: str
    opponent_name: str
    opponent_dwz: str | None
    result: str | None
    expected_value: str | None
    scoresheet_url: str | None
    piece_color: Literal["white", "black"] | None  # Extracted from CSS class


class ClubRosterScraper:
    """Extracts player list from club roster page (DWZ club page)."""

    BASE_URL = "https://www.schachbund.de/"

    def extract(self, html: str) -> list[PlayerReference]:
        """Extract player references from club roster page.

        Args:
            html: Raw HTML from the club roster page

        Returns:
            List of PlayerReference objects with stable identities
        """
        soup = BeautifulSoup(html, "html.parser")
        players: list[PlayerReference] = []

        # Find the main roster table
        table = soup.find("table", {"class": "body tablesorter"})
        if not table:
            LOGGER.warning("Could not find roster table in club page")
            return players

        tbody = table.find("tbody")
        if not tbody:
            LOGGER.warning("Could not find tbody in roster table")
            return players

        # Process each row
        for row in tbody.find_all("tr", {"class": re.compile(r"row_\d+")}, recursive=False):
            try:
                player = self._extract_player_row(row)
                if player:
                    players.append(player)
            except Exception as e:
                LOGGER.error(f"Error extracting player row: {e}", exc_info=True)
                continue

        LOGGER.info(f"Extracted {len(players)} players from club roster")
        return players

    def _extract_player_row(self, row: Any) -> PlayerReference | None:
        """Extract a single player from a table row.

        Expected columns:
        - col_1: ZPS number
        - col_3: Player name with link to profile
        """
        cols = row.find_all("td")
        if len(cols) < 4:
            return None

        # Extract ZPS number (col_1)
        zps_cell = cols[1]
        zps_number = zps_cell.get_text(strip=True)
        if not zps_number:
            return None

        # Extract player name and profile URL (col_3)
        player_cell = cols[3]
        player_link = player_cell.find("a")
        if not player_link:
            return None

        player_name = player_link.get_text(strip=True)
        profile_url = player_link.get("href", "")

        if not player_name or not profile_url:
            return None

        # Normalize profile URL to absolute
        if profile_url and not profile_url.startswith("http"):
            profile_url = urljoin(self.BASE_URL, profile_url)

        return PlayerReference(name=player_name, zps_number=zps_number, profile_url=profile_url)


class PlayerHistoryScraper:
    """Extracts tournament history from player profile page."""

    def extract(self, html: str) -> list[HistoricalTournamentEntry]:
        """Extract tournament history from player profile page.

        Args:
            html: Raw HTML from the player profile page

        Returns:
            List of HistoricalTournamentEntry objects
        """
        soup = BeautifulSoup(html, "html.parser")
        tournaments: list[HistoricalTournamentEntry] = []

        # Find the tournament history table
        table = soup.find("table", {"class": "body tablesorter"})
        if not table:
            LOGGER.warning("Could not find tournament history table in player page")
            return tournaments

        tbody = table.find("tbody")
        if not tbody:
            LOGGER.warning("Could not find tbody in tournament history table")
            return tournaments

        # Process each row
        for row in tbody.find_all("tr"):
            try:
                tournament = self._extract_tournament_row(row)
                if tournament:
                    tournaments.append(tournament)
            except Exception as e:
                LOGGER.error(f"Error extracting tournament row: {e}", exc_info=True)
                continue

        LOGGER.info(f"Extracted {len(tournaments)} tournament entries from player profile")
        return tournaments

    def _extract_tournament_row(self, row: Any) -> HistoricalTournamentEntry | None:
        """Extract a single tournament entry from a table row.

        Expected columns:
        - col_0: Row number or type indicator
        - col_1: Year
        - col_2: Tournament name (may have link)
        - col_3: Points
        - col_4: Par
        - col_5: Expected value (We)
        - col_6: Expected rating change (E)
        - col_7: Opponent rating avg
        - col_8: Performance rating
        - col_9: DWZ after event
        """
        cols = row.find_all("td")
        if len(cols) < 10:
            return None

        # Determine row type from classes
        row_type = ""
        for cls in row.get("class", []):
            if cls in ("dewis", "upgrade"):
                row_type = cls
                break

        # Extract year (col_1)
        year = cols[1].get_text(strip=True)
        if not year:
            return None

        # Extract tournament name and URL (col_2)
        tournament_cell = cols[2]
        tournament_link = tournament_cell.find("a")

        if tournament_link:
            tournament_name = tournament_link.get_text(strip=True)
            tournament_url = tournament_link.get("href", "")
        else:
            tournament_name = tournament_cell.get_text(strip=True)
            tournament_url = None

        if not tournament_name:
            return None

        # Extract numeric fields, handling empty cells
        points = self._extract_cell_value(cols[3])
        par = self._extract_cell_value(cols[4])
        expected_value = self._extract_cell_value(cols[5])
        expected_rating = self._extract_cell_value(cols[6])
        opponent_rating_avg = self._extract_cell_value(cols[7])
        performance_rating = self._extract_cell_value(cols[8])
        rating_after_event = self._extract_cell_value(cols[9])

        return HistoricalTournamentEntry(
            year=year,
            tournament_name=tournament_name,
            tournament_url=tournament_url,
            points=points,
            par=par,
            expected_value=expected_value,
            expected_rating=expected_rating,
            opponent_rating_avg=opponent_rating_avg,
            performance_rating=performance_rating,
            rating_after_event=rating_after_event,
            row_type=row_type,
        )

    def _extract_cell_value(self, cell: Any) -> str | None:
        """Extract text from a cell, returning None if empty or just whitespace."""
        text = cell.get_text(strip=True)
        return text if text else None


class TournamentDetailScraper:
    """Extracts individual match results from tournament detail page."""

    BASE_URL = "https://www.schachbund.de/"

    def extract(self, html: str) -> list[MatchResult]:
        """Extract match results from tournament detail page.

        Args:
            html: Raw HTML from the tournament detail/scoresheet page

        Returns:
            List of MatchResult objects
        """
        soup = BeautifulSoup(html, "html.parser")
        matches: list[MatchResult] = []

        # Find the tournament detail table (Spielberichtsbogen)
        # Look for table with thead containing "Runde", "Gegner" headers
        tables = soup.find_all("table", {"class": "body"})

        if not tables:
            LOGGER.warning("Could not find tournament detail table")
            return matches

        # Use the second table (first is usually header info)
        table = tables[-1] if len(tables) > 1 else tables[0]

        tbody = table.find("tbody")
        if not tbody:
            LOGGER.warning("Could not find tbody in tournament detail table")
            return matches

        # Process each row (skip summary row with "Σ" or "Sum")
        for row in tbody.find_all("tr", recursive=False):
            try:
                match = self._extract_match_row(row)
                if match:
                    matches.append(match)
            except Exception as e:
                LOGGER.error(f"Error extracting match row: {e}", exc_info=True)
                continue

        LOGGER.info(f"Extracted {len(matches)} match results from tournament detail page")
        return matches

    def _extract_match_row(self, row: Any) -> MatchResult | None:
        """Extract a single match result from a table row.

        Expected columns:
        - Runde (Round)
        - Gegner (Opponent name/link)
        - Scoresheet (link)
        - DWZ (Opponent rating)
        - Ergebnis (Result)
        - We (Expected value)
        """
        cols = row.find_all("td")

        # Skip summary rows (Σ or Sum)
        if len(cols) > 0:
            first_cell = cols[0].get_text(strip=True)
            if first_cell in ("Σ", "Sum", "∑"):
                return None

        if len(cols) < 6:
            return None

        # Extract round (Runde)
        round_text = cols[0].get_text(strip=True)
        if not round_text:
            return None

        # Extract opponent (Gegner) - may have link
        opponent_cell = cols[1]
        opponent_link = opponent_cell.find("a")
        opponent_name = opponent_link.get_text(strip=True) if opponent_link else ""
        opponent_name = opponent_name or opponent_cell.get_text(strip=True)

        if not opponent_name:
            return None

        # Extract scoresheet URL (third column)
        scoresheet_cell = cols[2]
        scoresheet_link = scoresheet_cell.find("a")
        scoresheet_url = scoresheet_link.get("href", "") if scoresheet_link else None
        if scoresheet_url and not scoresheet_url.startswith("http"):
            scoresheet_url = urljoin(self.BASE_URL, scoresheet_url)

        # Extract opponent DWZ (fourth column)
        opponent_dwz = cols[3].get_text(strip=True) if len(cols) > 3 else None
        opponent_dwz = opponent_dwz if opponent_dwz else None

        # Extract result (fifth column)
        result = cols[4].get_text(strip=True) if len(cols) > 4 else None
        result = result if result else None

        # Extract piece color from result cell CSS classes (fifth column)
        piece_color: Literal["white", "black"] | None = None
        if len(cols) > 4:
            result_classes = cols[4].get("class", [])
            if "white" in result_classes:
                piece_color = "white"
            elif "black" in result_classes:
                piece_color = "black"

        # Extract expected value (sixth column)
        expected_value = cols[5].get_text(strip=True) if len(cols) > 5 else None
        expected_value = expected_value if expected_value else None

        return MatchResult(
            round=round_text,
            opponent_name=opponent_name,
            opponent_dwz=opponent_dwz,
            result=result,
            expected_value=expected_value,
            scoresheet_url=scoresheet_url,
            piece_color=piece_color,
        )
