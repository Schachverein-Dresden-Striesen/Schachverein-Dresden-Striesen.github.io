from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Settings:
    club_url: str = "https://www.schachbund.de/dwz-vereine/F2810.html"
    login_url: str = "https://www.schachbund.de/anmelden.html"
    data_dir: Path = Path(__file__).resolve().parents[1] / "data"
    raw_html_dir: Path = Path(__file__).resolve().parents[1] / "data" / "raw_html"
    snapshot_dir: Path = Path(__file__).resolve().parents[1] / "data" / "snapshots"
    neo4j_uri: str = os.getenv("NEO4J_SERVERURL", "bolt://localhost:7687")
    neo4j_user: str = os.getenv("NEO4J_USER", "neo4j")
    neo4j_password: str = os.getenv("NEO4J_PASSWORD", "password")
    dwz_username: str = os.getenv("DWZ_USERNAME", "")
    dwz_password: str = os.getenv("DWZ_PASSWORD", "")
    dwz_path: str = os.getenv("DWZ_PATH", str(Path.home()))


SETTINGS = Settings()
