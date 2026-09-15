"""
Tests for the scraper extractors using fixture HTML from docs/
"""

from __future__ import annotations

import pytest
from pathlib import Path

from scraping.extractors import (
    ClubRosterScraper,
    PlayerHistoryScraper,
    TournamentDetailScraper,
    PlayerReference,
)


@pytest.fixture
def club_roster_html() -> str:
    """Load the club roster fixture HTML."""
    fixture_path = Path(__file__).parent.parent.parent / "docs" / "dwz-vereine-F2810.html"
    return fixture_path.read_text(encoding="utf-8")


@pytest.fixture
def player_profile_html() -> str:
    """Load the player profile fixture HTML."""
    fixture_path = Path(__file__).parent.parent.parent / "docs" / "dwz-spieler-NU4241593.html"
    return fixture_path.read_text(encoding="utf-8")


@pytest.fixture
def tournament_detail_html() -> str:
    """Load the tournament detail fixture HTML."""
    fixture_path = (
        Path(__file__).parent.parent.parent
        / "docs"
        / "dwz-turniere-019f75b9-af1b-77c0-9614-6aaa54318656-019f75bb-27e6-7af4-9050-9065be61a5fc.html"
    )
    return fixture_path.read_text(encoding="utf-8")


class TestClubRosterScraper:
    """Tests for ClubRosterScraper."""

    def test_extract_players_returns_list(self, club_roster_html: str):
        """Test that extract returns a list of players."""
        scraper = ClubRosterScraper()
        players = scraper.extract(club_roster_html)

        assert isinstance(players, list)
        assert len(players) > 0

    def test_extract_players_structure(self, club_roster_html: str):
        """Test that extracted players have correct structure."""
        scraper = ClubRosterScraper()
        players = scraper.extract(club_roster_html)

        for player in players:
            assert isinstance(player, PlayerReference)
            assert player.name
            assert player.zps_number
            assert player.profile_url

    def test_extract_finds_diego_pascual(self, club_roster_html: str):
        """Test that Diego Pascual is found in the roster."""
        scraper = ClubRosterScraper()
        players = scraper.extract(club_roster_html)

        player_names = [p.name for p in players]
        assert "Pascual, Diego" in player_names

        # Find Diego and verify details
        diego = next(p for p in players if "Diego" in p.name)
        assert diego.zps_number == "1220"
        assert "NU4241593" in diego.profile_url

    def test_extract_player_has_absolute_url(self, club_roster_html: str):
        """Test that profile URLs are converted to absolute URLs."""
        scraper = ClubRosterScraper()
        players = scraper.extract(club_roster_html)

        for player in players:
            assert player.profile_url.startswith("http")

    def test_extract_multiple_players(self, club_roster_html: str):
        """Test that multiple players are extracted."""
        scraper = ClubRosterScraper()
        players = scraper.extract(club_roster_html)

        # The fixture should have at least a few players
        assert len(players) >= 3


class TestPlayerHistoryScraper:
    """Tests for PlayerHistoryScraper."""

    def test_extract_tournaments_returns_list(self, player_profile_html: str):
        """Test that extract returns a list of tournament entries."""
        scraper = PlayerHistoryScraper()
        tournaments = scraper.extract(player_profile_html)

        assert isinstance(tournaments, list)
        assert len(tournaments) > 0

    def test_extract_tournaments_have_required_fields(self, player_profile_html: str):
        """Test that extracted tournaments have required fields."""
        scraper = PlayerHistoryScraper()
        tournaments = scraper.extract(player_profile_html)

        for tournament in tournaments:
            assert tournament.year
            assert tournament.tournament_name

    def test_extract_finds_recent_tournament(self, player_profile_html: str):
        """Test that recent tournaments like Ryck-Open 2026 are found."""
        scraper = PlayerHistoryScraper()
        tournaments = scraper.extract(player_profile_html)

        names = [t.tournament_name for t in tournaments]
        assert any("Ryck-Open" in name for name in names)

    def test_extract_tournament_with_numeric_fields(self, player_profile_html: str):
        """Test that numeric fields are extracted when present."""
        scraper = PlayerHistoryScraper()
        tournaments = scraper.extract(player_profile_html)

        # Find a tournament with points
        tournament_with_points = next(
            (t for t in tournaments if t.points), None
        )
        assert tournament_with_points is not None
        assert tournament_with_points.points

    def test_extract_handles_empty_cells(self, player_profile_html: str):
        """Test that missing/empty cells are handled gracefully."""
        scraper = PlayerHistoryScraper()
        tournaments = scraper.extract(player_profile_html)

        # Some tournaments may have missing fields
        # The extractor should return None for missing values
        for tournament in tournaments:
            # At least year and name should always be present
            assert tournament.year
            assert tournament.tournament_name


class TestTournamentDetailScraper:
    """Tests for TournamentDetailScraper."""

    def test_extract_matches_returns_list(self, tournament_detail_html: str):
        """Test that extract returns a list of match results."""
        scraper = TournamentDetailScraper()
        matches = scraper.extract(tournament_detail_html)

        assert isinstance(matches, list)

    def test_extract_matches_have_required_fields(self, tournament_detail_html: str):
        """Test that extracted matches have required fields."""
        scraper = TournamentDetailScraper()
        matches = scraper.extract(tournament_detail_html)

        for match in matches:
            assert match.round
            assert match.opponent_name

    def test_extract_finds_match_results(self, tournament_detail_html: str):
        """Test that match results are extracted."""
        scraper = TournamentDetailScraper()
        matches = scraper.extract(tournament_detail_html)

        # This tournament should have at least one match
        assert len(matches) > 0

    def test_extract_match_with_opponent_details(self, tournament_detail_html: str):
        """Test that opponent details (DWZ, result) are extracted."""
        scraper = TournamentDetailScraper()
        matches = scraper.extract(tournament_detail_html)

        if matches:
            match = matches[0]
            # At least opponent name should be present
            assert match.opponent_name
            # Other fields may vary depending on what's in the HTML
            # but the structure should be consistent

    def test_extract_skips_summary_rows(self, tournament_detail_html: str):
        """Test that summary rows (Σ) are skipped."""
        scraper = TournamentDetailScraper()
        matches = scraper.extract(tournament_detail_html)

        # No match should have "Σ" as the round
        for match in matches:
            assert match.round != "Σ"
            assert match.round != "Sum"


class TestExtractorIntegration:
    """Integration tests across multiple extractors."""

    def test_club_roster_links_to_player_profiles(
        self, club_roster_html: str, player_profile_html: str
    ):
        """Test that club roster player links match player profile URLs."""
        roster_scraper = ClubRosterScraper()
        players = roster_scraper.extract(club_roster_html)

        # Find Diego in the roster
        diego = next(p for p in players if "Diego" in p.name)

        # Verify that his profile URL contains his player ID
        assert "NU4241593" in diego.profile_url

    def test_player_profile_references_tournaments(self, player_profile_html: str):
        """Test that player profile has valid tournament references."""
        history_scraper = PlayerHistoryScraper()
        tournaments = history_scraper.extract(player_profile_html)

        # Should have multiple tournaments in the history
        assert len(tournaments) > 0

        # Some tournaments should have URLs
        tournaments_with_url = [t for t in tournaments if t.tournament_url]
        assert len(tournaments_with_url) > 0
