"""Small domain models used in the workshop."""
from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class Room:
    id: str
    building: str
    capacity: int


@dataclass(frozen=True)
class Reservation:
    room_id: str
    start: datetime
    end: datetime
