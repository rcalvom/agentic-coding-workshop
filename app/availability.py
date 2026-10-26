"""Room selection logic for a requested time interval."""
from datetime import datetime

from .models import Reservation, Room


def intervals_overlap(
    request_start: datetime,
    request_end: datetime,
    booking_start: datetime,
    booking_end: datetime,
) -> bool:
    """Return whether a requested interval conflicts with an existing booking."""
    return request_start <= booking_end and request_end >= booking_start


def available_rooms(
    rooms: list[Room],
    reservations: list[Reservation],
    start: datetime,
    end: datetime,
    min_capacity: int,
) -> list[Room]:
    free = []
    for room in rooms:
        if room.capacity < min_capacity:
            continue
        busy = any(
            booking.room_id == room.id
            and intervals_overlap(start, end, booking.start, booking.end)
            for booking in reservations
        )
        if not busy:
            free.append(room)
    return sorted(free, key=lambda item: item.id)
