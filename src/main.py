from __future__ import annotations

import logging

from config.settings import SETTINGS
from scraping.workflow import PlayerTournamentHistoryWorkflow

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s:%(name)s %(message)s",
)
LOGGER = logging.getLogger(__name__)


def main() -> None:
    """Main entry point for the player tournament history scraper."""
    LOGGER.info("Starting player tournament history scraper workflow")

    workflow = PlayerTournamentHistoryWorkflow(
        club_url=SETTINGS.club_url,
        login_url=SETTINGS.login_url,
        username=SETTINGS.dwz_username,
        password=SETTINGS.dwz_password,
        snapshot_dir=SETTINGS.snapshot_dir,
        neo4j_uri=SETTINGS.neo4j_uri,
        neo4j_user=SETTINGS.neo4j_user,
        neo4j_password=SETTINGS.neo4j_password,
    )

    result = workflow.run()
    LOGGER.info(result)


if __name__ == "__main__":
    main()
