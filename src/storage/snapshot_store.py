from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path


class SnapshotStore:
    def __init__(self, base_dir: Path):
        self.base_dir = Path(base_dir)
        self.base_dir.mkdir(parents=True, exist_ok=True)

    def save_raw_html(self, filename: str, html: str) -> Path:
        path = self.base_dir / filename
        path.write_text(html, encoding="utf-8")
        return path

    def save_json(self, filename: str, payload: dict) -> Path:
        path = self.base_dir / filename
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
        return path

    def timestamped_name(self, prefix: str, suffix: str = "json") -> str:
        now = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
        return f"{prefix}_{now}.{suffix}"
