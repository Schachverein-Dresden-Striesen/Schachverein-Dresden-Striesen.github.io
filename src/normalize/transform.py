from __future__ import annotations

from typing import Any


def normalize_player_record(raw: dict[str, Any]) -> dict[str, Any]:
    return {
        "player_name": raw.get("player_name") or raw.get("name"),
        "tournament_name": raw.get("tournament_name"),
        "tournament_date": raw.get("tournament_date"),
        "result": raw.get("result"),
        "opponent": raw.get("opponent"),
        "source_url": raw.get("source_url"),
    }


def normalize_players(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [normalize_player_record(row) for row in rows]
