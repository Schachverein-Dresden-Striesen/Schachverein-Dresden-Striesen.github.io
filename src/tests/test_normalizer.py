"""
Tests for the normalizer.
"""

from __future__ import annotations

from datetime import datetime

import pytest

from normalize.normalizer import Normalizer
from scraping.extractors import (
    HistoricalTournamentEntry,
    MatchResult,
    PlayerReference,
)


@pytest.fixture
def normalizer() -> Normalizer:
    """Create a normalizer instance."""
    return Normalizer()


@pytest.fixture
def sample_timestamp() -> datetime:
    """Sample timestamp for testing."""
    return datetime(2026, 9, 15, 12, 0, 0)


class TestNormalizePlayerName:
    """Tests for player name normalization."""

    def test_normalize_last_first_format(self, normalizer: Normalizer):
        """Test normalization of 'Last, First' format names."""
        result = normalizer._normalize_name("Pascual, Diego")
        assert result == "Pascual, Diego"

    def test_normalize_first_last_format(self, normalizer: Normalizer):
        """Test conversion of 'First Last' to 'Last, First'."""
        result = normalizer._normalize_name("Diego Pascual")
        assert result == "Pascual, Diego"

    def test_normalize_removes_extra_whitespace(self, normalizer: Normalizer):
        """Test that extra whitespace is removed."""
        result = normalizer._normalize_name("  Pascual  ,  Diego  ")
        assert result == "Pascual, Diego"

    def test_normalize_single_name(self, normalizer: Normalizer):
        """Test handling of single-word names."""
        result = normalizer._normalize_name("Kasparov")
        assert result == "Kasparov"

    def test_normalize_empty_string(self, normalizer: Normalizer):
        """Test handling of empty names."""
        result = normalizer._normalize_name("")
        assert result == ""


class TestParseFloat:
    """Tests for float parsing."""

    def test_parse_float_decimal_point(self, normalizer: Normalizer):
        """Test parsing floats with decimal point."""
        assert normalizer._parse_float("2.5") == 2.5
        assert normalizer._parse_float("0.5") == 0.5

    def test_parse_float_comma_decimal(self, normalizer: Normalizer):
        """Test parsing floats with German comma format."""
        assert normalizer._parse_float("2,5") == 2.5
        assert normalizer._parse_float("0,578") == 0.578

    def test_parse_float_with_whitespace(self, normalizer: Normalizer):
        """Test parsing floats with surrounding whitespace."""
        assert normalizer._parse_float("  2.5  ") == 2.5

    def test_parse_float_empty(self, normalizer: Normalizer):
        """Test that empty string returns None."""
        assert normalizer._parse_float("") is None
        assert normalizer._parse_float(None) is None

    def test_parse_float_invalid(self, normalizer: Normalizer):
        """Test that invalid strings return None."""
        assert normalizer._parse_float("abc") is None


class TestParseInt:
    """Tests for integer parsing."""

    def test_parse_int_valid(self, normalizer: Normalizer):
        """Test parsing valid integers."""
        assert normalizer._parse_int("1") == 1
        assert normalizer._parse_int("2009") == 2009

    def test_parse_int_with_whitespace(self, normalizer: Normalizer):
        """Test parsing integers with whitespace."""
        assert normalizer._parse_int("  1220  ") == 1220

    def test_parse_int_empty(self, normalizer: Normalizer):
        """Test that empty string returns None."""
        assert normalizer._parse_int("") is None
        assert normalizer._parse_int(None) is None

    def test_parse_int_invalid(self, normalizer: Normalizer):
        """Test that non-integer strings return None."""
        assert normalizer._parse_int("12.5") is None


class TestParseResult:
    """Tests for chess result parsing."""

    def test_parse_result_win(self, normalizer: Normalizer):
        """Test parsing win result."""
        assert normalizer._parse_result("1") == 1.0
        assert normalizer._parse_result("+") == 1.0

    def test_parse_result_draw(self, normalizer: Normalizer):
        """Test parsing draw result."""
        assert normalizer._parse_result("½") == 0.5
        assert normalizer._parse_result("0.5") == 0.5
        assert normalizer._parse_result("=") == 0.5

    def test_parse_result_loss(self, normalizer: Normalizer):
        """Test parsing loss result."""
        assert normalizer._parse_result("0") == 0.0
        assert normalizer._parse_result("-") == 0.0

    def test_parse_result_empty(self, normalizer: Normalizer):
        """Test that empty result returns None."""
        assert normalizer._parse_result("") is None
        assert normalizer._parse_result(None) is None


class TestCanonicalizePieceColor:
    """Tests for piece color canonicalization."""

    def test_canonicalize_white_lowercase(self, normalizer: Normalizer):
        """Test canonicalization of lowercase 'white'."""
        assert normalizer._canonicalize_piece_color("white") == "white"

    def test_canonicalize_white_uppercase(self, normalizer: Normalizer):
        """Test canonicalization of uppercase 'WHITE'."""
        assert normalizer._canonicalize_piece_color("WHITE") == "white"

    def test_canonicalize_white_mixed_case(self, normalizer: Normalizer):
        """Test canonicalization of mixed case 'White'."""
        assert normalizer._canonicalize_piece_color("White") == "white"

    def test_canonicalize_white_short_form(self, normalizer: Normalizer):
        """Test canonicalization of short form 'w'."""
        assert normalizer._canonicalize_piece_color("w") == "white"

    def test_canonicalize_white_german(self, normalizer: Normalizer):
        """Test canonicalization of German 'Weiß'."""
        assert normalizer._canonicalize_piece_color("Weiß") == "white"
        assert normalizer._canonicalize_piece_color("weiss") == "white"

    def test_canonicalize_black_lowercase(self, normalizer: Normalizer):
        """Test canonicalization of lowercase 'black'."""
        assert normalizer._canonicalize_piece_color("black") == "black"

    def test_canonicalize_black_uppercase(self, normalizer: Normalizer):
        """Test canonicalization of uppercase 'BLACK'."""
        assert normalizer._canonicalize_piece_color("BLACK") == "black"

    def test_canonicalize_black_short_form(self, normalizer: Normalizer):
        """Test canonicalization of short form 'b'."""
        assert normalizer._canonicalize_piece_color("b") == "black"

    def test_canonicalize_black_german(self, normalizer: Normalizer):
        """Test canonicalization of German 'Schwarz'."""
        assert normalizer._canonicalize_piece_color("Schwarz") == "black"
        assert normalizer._canonicalize_piece_color("schwarz") == "black"

    def test_canonicalize_with_whitespace(self, normalizer: Normalizer):
        """Test canonicalization with surrounding whitespace."""
        assert normalizer._canonicalize_piece_color("  white  ") == "white"
        assert normalizer._canonicalize_piece_color("\tblack\n") == "black"

    def test_canonicalize_empty(self, normalizer: Normalizer):
        """Test that empty/None values return None."""
        assert normalizer._canonicalize_piece_color("") is None
        assert normalizer._canonicalize_piece_color(None) is None

    def test_canonicalize_invalid_raises_error(self, normalizer: Normalizer):
        """Test that invalid values raise ValueError."""
        with pytest.raises(ValueError, match="Unrecognized piece color"):
            normalizer._canonicalize_piece_color("red")

        with pytest.raises(ValueError, match="Unrecognized piece color"):
            normalizer._canonicalize_piece_color("unknown")


class TestExtractTournamentCode:
    """Tests for tournament code extraction from URLs."""

    def test_extract_tournament_code_from_url(self, normalizer: Normalizer):
        """Test extracting tournament code from URL."""
        url = (
            "dwz-turniere/019f75b9-af1b-77c0-9614-6aaa54318656/"
            "019f75bb-27e6-7af4-9050-9065be61a5fc.html"
        )
        code = normalizer._extract_tournament_code(url)
        assert code == "019f75b9-af1b-77c0-9614-6aaa54318656"

    def test_extract_tournament_code_absolute_url(self, normalizer: Normalizer):
        """Test extracting tournament code from absolute URL."""
        url = "https://www.schachbund.de/dwz-turniere/019f75b9-af1b-77c0-9614-6aaa54318656/019f75bb-27e6-7af4-9050-9065be61a5fc.html"
        code = normalizer._extract_tournament_code(url)
        assert code == "019f75b9-af1b-77c0-9614-6aaa54318656"

    def test_extract_tournament_code_empty(self, normalizer: Normalizer):
        """Test that None URL returns None."""
        assert normalizer._extract_tournament_code(None) is None

    def test_extract_tournament_code_invalid_url(self, normalizer: Normalizer):
        """Test that URL without code pattern returns None."""
        assert normalizer._extract_tournament_code("https://example.com") is None


class TestNormalizePlayer:
    """Tests for player normalization."""

    def test_normalize_player_reference(
        self,
        normalizer: Normalizer,
        sample_timestamp: datetime,
    ):
        """Test normalization of player reference."""
        player_ref = PlayerReference(
            name="Diego Pascual",
            zps_number="1220",
            profile_url="https://www.schachbund.de/dwz-spieler/NU4241593.html",
        )

        normalized = normalizer.normalize_player(
            player_ref,
            source_page="https://www.schachbund.de/dwz-vereine/F2810.html",
            snapshot_timestamp=sample_timestamp,
        )

        assert normalized.name == "Pascual, Diego"
        assert normalized.zps_number == "1220"
        assert normalized.profile_url == "https://www.schachbund.de/dwz-spieler/NU4241593.html"
        assert normalized.snapshot_timestamp == sample_timestamp


class TestNormalizeTournamentEntry:
    """Tests for tournament entry normalization."""

    def test_normalize_tournament_entry(
        self,
        normalizer: Normalizer,
        sample_timestamp: datetime,
    ):
        """Test normalization of tournament entry."""
        player_ref = PlayerReference(
            name="Diego Pascual",
            zps_number="1220",
            profile_url="https://www.schachbund.de/dwz-spieler/NU4241593.html",
        )

        player = normalizer.normalize_player(
            player_ref,
            source_page="https://www.schachbund.de/dwz-spieler/NU4241593.html",
            snapshot_timestamp=sample_timestamp,
        )

        entry = HistoricalTournamentEntry(
            year="2026",
            tournament_name="Ryck-Open 2026",
            tournament_url="dwz-turniere/c20ee10e-fba0-4b31-9fc6-5539a037b5be/edb2919d-dcce-46c2-91fb-ea8ab6a06389.html",
            points="6",
            par="7",
            expected_value="4,344",
            expected_rating="25",
            opponent_rating_avg="1987",
            performance_rating="2315",
            rating_after_event="2121 - 17",
            row_type="dewis",
        )

        normalized = normalizer.normalize_tournament_entry(
            entry,
            player,
            source_page="https://www.schachbund.de/dwz-spieler/NU4241593.html",
            snapshot_timestamp=sample_timestamp,
        )

        assert normalized is not None
        assert normalized.player.name == "Pascual, Diego"
        assert normalized.tournament.year == "2026"
        assert normalized.points == 6.0
        assert normalized.par == 7
        assert normalized.expected_value == pytest.approx(4.344)

    def test_normalize_tournament_entry_handles_missing_fields(
        self,
        normalizer: Normalizer,
        sample_timestamp: datetime,
    ):
        """Test that tournament entries with missing fields are handled gracefully."""
        player_ref = PlayerReference(
            name="Diego Pascual",
            zps_number="1220",
            profile_url="https://www.schachbund.de/dwz-spieler/NU4241593.html",
        )

        player = normalizer.normalize_player(
            player_ref,
            source_page="https://www.schachbund.de/dwz-spieler/NU4241593.html",
            snapshot_timestamp=sample_timestamp,
        )

        # Upgrade entry with minimal fields
        entry = HistoricalTournamentEntry(
            year="2026",
            tournament_name="Umstufung 2026",
            tournament_url=None,
            points=None,
            par=None,
            expected_value=None,
            expected_rating=None,
            opponent_rating_avg=None,
            performance_rating=None,
            rating_after_event="2080 - 16",
            row_type="upgrade",
        )

        normalized = normalizer.normalize_tournament_entry(
            entry,
            player,
            source_page="https://www.schachbund.de/dwz-spieler/NU4241593.html",
            snapshot_timestamp=sample_timestamp,
        )

        assert normalized is not None
        assert normalized.points is None
        assert normalized.par is None
        assert normalized.entry_type == "upgrade"


class TestNormalizeMatch:
    """Tests for match result normalization."""

    def test_normalize_match_result(
        self,
        normalizer: Normalizer,
        sample_timestamp: datetime,
    ):
        """Test normalization of match result."""
        player_ref = PlayerReference(
            name="Diego Pascual",
            zps_number="1220",
            profile_url="https://www.schachbund.de/dwz-spieler/NU4241593.html",
        )

        player = normalizer.normalize_player(
            player_ref,
            source_page="https://www.schachbund.de/dwz-spieler/NU4241593.html",
            snapshot_timestamp=sample_timestamp,
        )

        # Create a minimal tournament for the match
        tournament_entry = HistoricalTournamentEntry(
            year="2026",
            tournament_name="Bezirksliga",
            tournament_url="dwz-turniere/019f75b9-af1b-77c0-9614-6aaa54318656/019f75bb-27e6-7af4-9050-9065be61a5fc.html",
            points=None,
            par=None,
            expected_value=None,
            expected_rating=None,
            opponent_rating_avg=None,
            performance_rating=None,
            rating_after_event=None,
            row_type="dewis",
        )

        tournament = normalizer.normalize_tournament_entry(
            tournament_entry,
            player,
            source_page="https://www.schachbund.de/dwz-spieler/NU4241593.html",
            snapshot_timestamp=sample_timestamp,
        ).tournament

        match = MatchResult(
            round="3",
            opponent_name="Fiedler, Harald",
            opponent_dwz="2009",
            result="½",
            expected_value="0.580",
            scoresheet_url="dwz-turniere/019f75b9-af1b-77c0-9614-6aaa54318656/019f75bb-27e6-7bf4-a012-c366ce47eb7a.html",
            piece_color="white",
        )

        normalized = normalizer.normalize_match(
            match,
            player,
            tournament,
            source_page="https://www.schachbund.de/dwz-turniere/019f75b9-af1b-77c0-9614-6aaa54318656/019f75bb-27e6-7af4-9050-9065be61a5fc.html",
            snapshot_timestamp=sample_timestamp,
        )

        assert normalized is not None
        assert normalized.round == 3
        assert normalized.opponent_name == "Fiedler, Harald"
        assert normalized.opponent_dwz == 2009
        assert normalized.result == 0.5
        assert normalized.expected_value == pytest.approx(0.580)
        assert normalized.piece_color == "white"

    def test_normalize_match_with_black_pieces(
        self,
        normalizer: Normalizer,
        sample_timestamp: datetime,
    ):
        """Test normalization of match with black pieces."""
        player_ref = PlayerReference(
            name="Diego Pascual",
            zps_number="1220",
            profile_url="https://www.schachbund.de/dwz-spieler/NU4241593.html",
        )

        player = normalizer.normalize_player(
            player_ref,
            source_page="https://www.schachbund.de/dwz-spieler/NU4241593.html",
            snapshot_timestamp=sample_timestamp,
        )

        # Create a minimal tournament for the match
        tournament_entry = HistoricalTournamentEntry(
            year="2026",
            tournament_name="Bezirksliga",
            tournament_url="dwz-turniere/c20ee10e-fba0-4b31-9fc6-5539a037b5be/edb2919d-dcce-46c2-91fb-ea8ab6a06389.html",
            points=None,
            par=None,
            expected_value=None,
            expected_rating=None,
            opponent_rating_avg=None,
            performance_rating=None,
            rating_after_event=None,
            row_type="dewis",
        )

        tournament = normalizer.normalize_tournament_entry(
            tournament_entry,
            player,
            source_page="https://www.schachbund.de/dwz-spieler/NU4241593.html",
            snapshot_timestamp=sample_timestamp,
        ).tournament

        match = MatchResult(
            round="2",
            opponent_name="Müller, Hans",
            opponent_dwz="1850",
            result="1",
            expected_value="0.650",
            scoresheet_url="dwz-turniere/c20ee10e-fba0-4b31-9fc6-5539a037b5be/another-game.html",
            piece_color="black",
        )

        normalized = normalizer.normalize_match(
            match,
            player,
            tournament,
            source_page="https://www.schachbund.de/dwz-turniere/c20ee10e-fba0-4b31-9fc6-5539a037b5be/edb2919d-dcce-46c2-91fb-ea8ab6a06389.html",
            snapshot_timestamp=sample_timestamp,
        )

        assert normalized is not None
        assert normalized.round == 2
        assert normalized.opponent_name == "Müller, Hans"
        assert normalized.piece_color == "black"

    def test_normalize_match_with_missing_piece_color(
        self,
        normalizer: Normalizer,
        sample_timestamp: datetime,
    ):
        """Test that matches with missing piece_color are flagged as ambiguous."""
        player_ref = PlayerReference(
            name="Diego Pascual",
            zps_number="1220",
            profile_url="https://www.schachbund.de/dwz-spieler/NU4241593.html",
        )

        player = normalizer.normalize_player(
            player_ref,
            source_page="https://www.schachbund.de/dwz-spieler/NU4241593.html",
            snapshot_timestamp=sample_timestamp,
        )

        tournament_entry = HistoricalTournamentEntry(
            year="2026",
            tournament_name="Bezirksliga",
            tournament_url="dwz-turniere/019f75b9-af1b-77c0-9614-6aaa54318656/019f75bb-27e6-7af4-9050-9065be61a5fc.html",
            points=None,
            par=None,
            expected_value=None,
            expected_rating=None,
            opponent_rating_avg=None,
            performance_rating=None,
            rating_after_event=None,
            row_type="dewis",
        )

        tournament = normalizer.normalize_tournament_entry(
            tournament_entry,
            player,
            source_page="https://www.schachbund.de/dwz-spieler/NU4241593.html",
            snapshot_timestamp=sample_timestamp,
        ).tournament

        # Match with missing piece_color (ambiguous data)
        match = MatchResult(
            round="4",
            opponent_name="Schmidt, Klaus",
            opponent_dwz="2100",
            result="0",
            expected_value="0.400",
            scoresheet_url="dwz-turniere/019f75b9-af1b-77c0-9614-6aaa54318656/another-game.html",
            piece_color=None,  # Missing piece color = ambiguous data
        )

        # normalize_match should catch the error and return None (data quality issue)
        normalized = normalizer.normalize_match(
            match,
            player,
            tournament,
            source_page="https://www.schachbund.de/dwz-turniere/019f75b9-af1b-77c0-9614-6aaa54318656/019f75bb-27e6-7af4-9050-9065be61a5fc.html",
            snapshot_timestamp=sample_timestamp,
        )

        # Should return None due to missing piece_color (flagged as ambiguous)
        assert normalized is None
