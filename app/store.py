"""Deterministic local fixtures; no network or database required."""
import json
from datetime import datetime
from pathlib import Path

from .models import Reservation, Room

_DATA = Path(__file__).resolve().parent.parent / "data"


def load_rooms() -> list[Room]:
    items = json.loads((_DATA / "rooms.json").read_text(encoding="utf-8"))
    return [Room(**item) for item in items]


def load_reservations() -> list[Reservation]:
    items = json.loads((_DATA / "reservations.json").read_text(encoding="utf-8"))
    return [
        Reservation(
            room_id=item["room_id"],
            start=datetime.fromisoformat(item["start"].replace("Z", "+00:00")),
            end=datetime.fromisoformat(item["end"].replace("Z", "+00:00")),
        )
        for item in items
    ]
