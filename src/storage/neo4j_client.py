from __future__ import annotations

import logging
from datetime import datetime
from typing import Any, Iterable

from neo4j import GraphDatabase

LOGGER = logging.getLogger(__name__)


class Neo4jClient:
    def __init__(self, uri: str, user: str, password: str):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
        self.driver.verify_connectivity()
        LOGGER.info("Connected to Neo4j at %s", uri)

    def close(self) -> None:
        self.driver.close()

    def create_player(self, player_name: str, club_id: str | None = None) -> None:
        with self.driver.session(database="neo4j") as session:
            session.run(
                "MERGE (p:Player {name: $name}) "
                "SET p.club_id = coalesce($club_id, p.club_id)",
                name=player_name,
                club_id=club_id,
            )

    def add_tournament_result(
        self,
        player_name: str,
        tournament_name: str,
        tournament_date: str,
        result: str,
        opponent: str | None = None,
    ) -> None:
        with self.driver.session(database="neo4j") as session:
            session.run(
                "MATCH (p:Player {name: $player_name}) "
                "MERGE (t:Tournament {name: $tournament_name, date: $tournament_date}) "
                "CREATE (p)-[:PLAYED]->(t) "
                "SET t.result = $result, t.opponent = $opponent",
                player_name=player_name,
                tournament_name=tournament_name,
                tournament_date=tournament_date,
                result=result,
                opponent=opponent,
            )

    def list_players(self) -> Iterable[Any]:
        with self.driver.session(database="neo4j") as session:
            result = session.run("MATCH (p:Player) RETURN p.name AS name ORDER BY name")
            return [record["name"] for record in result]

    # New methods for normalized records (player-tournament-history scraper)

    def store_player(
        self,
        name: str,
        zps_number: str | None = None,
        profile_url: str | None = None,
        club_id: str = "F2810",
    ) -> None:
        """Create or update a player node."""
        with self.driver.session(database="neo4j") as session:
            session.run(
                "MERGE (p:Player {name: $name}) "
                "SET p.zps_number = coalesce($zps_number, p.zps_number), "
                "    p.profile_url = coalesce($profile_url, p.profile_url), "
                "    p.club_id = coalesce($club_id, p.club_id), "
                "    p.updated_at = datetime()",
                name=name,
                zps_number=zps_number,
                profile_url=profile_url,
                club_id=club_id,
            )

    def store_tournament(
        self,
        name: str,
        year: str,
        code: str | None = None,
        url: str | None = None,
    ) -> None:
        """Create or update a tournament node."""
        with self.driver.session(database="neo4j") as session:
            session.run(
                "MERGE (t:Tournament {name: $name, year: $year}) "
                "SET t.code = coalesce($code, t.code), "
                "    t.url = coalesce($url, t.url), "
                "    t.updated_at = datetime()",
                name=name,
                year=year,
                code=code,
                url=url,
            )

    def store_tournament_entry(
        self,
        player_name: str,
        tournament_name: str,
        year: str,
        points: float | None = None,
        par: int | None = None,
        expected_value: float | None = None,
        opponent_rating_avg: int | None = None,
        performance_rating: float | None = None,
        rating_after_event: int | None = None,
    ) -> None:
        """Create or update a PARTICIPATED_IN relationship with tournament metadata."""
        with self.driver.session(database="neo4j") as session:
            session.run(
                "MATCH (p:Player {name: $player_name}) "
                "MATCH (t:Tournament {name: $tournament_name, year: $year}) "
                "MERGE (p)-[rel:PARTICIPATED_IN]->(t) "
                "SET rel.points = coalesce($points, rel.points), "
                "    rel.par = coalesce($par, rel.par), "
                "    rel.expected_value = coalesce($expected_value, rel.expected_value), "
                "    rel.opponent_rating_avg = coalesce($opponent_rating_avg, rel.opponent_rating_avg), "
                "    rel.performance_rating = coalesce($performance_rating, rel.performance_rating), "
                "    rel.rating_after_event = coalesce($rating_after_event, rel.rating_after_event), "
                "    rel.updated_at = datetime()",
                player_name=player_name,
                tournament_name=tournament_name,
                year=year,
                points=points,
                par=par,
                expected_value=expected_value,
                opponent_rating_avg=opponent_rating_avg,
                performance_rating=performance_rating,
                rating_after_event=rating_after_event,
            )

    def store_match_result(
        self,
        player_name: str,
        tournament_name: str,
        year: str,
        round_num: int | None,
        opponent_name: str,
        opponent_dwz: int | None = None,
        result: float | None = None,
        expected_value: float | None = None,
    ) -> None:
        """Create or update a match result node and PLAYED_IN relationship."""
        with self.driver.session(database="neo4j") as session:
            # Create opponent player if not exists
            session.run(
                "MERGE (opponent:Player {name: $opponent_name})",
                opponent_name=opponent_name,
            )

            # Create match result node
            session.run(
                "MATCH (p:Player {name: $player_name}) "
                "MATCH (t:Tournament {name: $tournament_name, year: $year}) "
                "MATCH (opponent:Player {name: $opponent_name}) "
                "MERGE (m:MatchResult {player_name: $player_name, "
                "                      tournament_name: $tournament_name, "
                "                      year: $year, "
                "                      round: $round_num, "
                "                      opponent_name: $opponent_name}) "
                "SET m.opponent_dwz = coalesce($opponent_dwz, m.opponent_dwz), "
                "    m.result = coalesce($result, m.result), "
                "    m.expected_value = coalesce($expected_value, m.expected_value), "
                "    m.updated_at = datetime() "
                "MERGE (p)-[:PLAYED_AGAINST {round: $round_num}]->(opponent) "
                "MERGE (m)-[:IN_TOURNAMENT]->(t)",
                player_name=player_name,
                tournament_name=tournament_name,
                year=year,
                round_num=round_num,
                opponent_name=opponent_name,
                opponent_dwz=opponent_dwz,
                result=result,
                expected_value=expected_value,
            )

    def get_player_history(self, player_name: str) -> list[dict[str, Any]]:
        """Get all tournament participations for a player."""
        with self.driver.session(database="neo4j") as session:
            result = session.run(
                "MATCH (p:Player {name: $name})-[rel:PARTICIPATED_IN]->(t:Tournament) "
                "RETURN t.name AS tournament, t.year AS year, "
                "       rel.points AS points, rel.par AS par, "
                "       rel.expected_value AS expected_value, "
                "       rel.opponent_rating_avg AS opponent_rating_avg, "
                "       rel.performance_rating AS performance_rating, "
                "       rel.rating_after_event AS rating_after_event "
                "ORDER BY t.year DESC, t.name",
                name=player_name,
            )
            return [dict(record) for record in result]
