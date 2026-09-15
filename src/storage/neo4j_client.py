from __future__ import annotations

import logging
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
