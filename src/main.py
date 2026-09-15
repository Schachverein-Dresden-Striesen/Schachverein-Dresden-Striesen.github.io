from __future__ import annotations

import logging
from pathlib import Path

from config.settings import SETTINGS
from normalize.transform import normalize_players
from scraping.club_scraper import ClubScraper
from storage.neo4j_client import Neo4jClient
from storage.snapshot_store import SnapshotStore

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s:%(name)s %(message)s")
LOGGER = logging.getLogger(__name__)


def main() -> None:
    LOGGER.info("Starting player tournament history refresh")

    scraper = ClubScraper(
        club_url=SETTINGS.club_url,
        login_url=SETTINGS.login_url,
        username=SETTINGS.dwz_username,
        password=SETTINGS.dwz_password,
    )
    raw_page = scraper.fetch_club_page()

    snapshot_store = SnapshotStore(SETTINGS.snapshot_dir)
    snapshot_path = snapshot_store.save_raw_html(
        snapshot_store.timestamped_name("club_page"), raw_page
    )
    LOGGER.info("Saved raw HTML snapshot to %s", snapshot_path)

    client = Neo4jClient(
        uri=SETTINGS.neo4j_uri,
        user=SETTINGS.neo4j_user,
        password=SETTINGS.neo4j_password,
    )

    try:
        records = normalize_players([])
        for record in records:
            if record.get("player_name"):
                client.create_player(record["player_name"])
    finally:
        client.close()


if __name__ == "__main__":
    main()
