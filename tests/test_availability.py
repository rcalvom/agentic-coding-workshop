from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
BASE = "/rooms/available"


def get_ids(start: str, end: str, min_capacity: int = 1) -> list[str]:
    response = client.get(BASE, params={"start": start, "end": end, "min_capacity": min_capacity})
    assert response.status_code == 200, response.text
    return [room["id"] for room in response.json()["available_rooms"]]


def test_regular_overlap_excludes_reserved_rooms():
    assert get_ids("2026-10-27T11:45:00Z", "2026-10-27T11:55:00Z") == ["LIB-202"]


def test_capacity_filter():
    assert get_ids("2026-10-27T13:00:00Z", "2026-10-27T13:30:00Z", 4) == ["ENG-303", "LIB-202"]


def test_adjacent_to_booking_end_is_available():
    assert "LIB-202" in get_ids("2026-10-27T11:00:00Z", "2026-10-27T11:15:00Z", 4)


def test_adjacent_to_booking_start_is_available():
    assert "ENG-303" in get_ids("2026-10-27T11:00:00Z", "2026-10-27T11:30:00Z", 4)


def test_timezone_offsets_represent_same_instant():
    assert get_ids("2026-10-27T07:00:00-04:00", "2026-10-27T07:30:00-04:00", 4) == ["ENG-303", "LIB-202"]


def test_invalid_interval_is_rejected():
    response = client.get(BASE, params={"start": "2026-10-27T12:00:00Z", "end": "2026-10-27T11:00:00Z"})
    assert response.status_code == 422


def test_naive_datetime_is_rejected():
    response = client.get(BASE, params={"start": "2026-10-27T11:00:00", "end": "2026-10-27T12:00:00"})
    assert response.status_code == 422


def test_invalid_capacity_is_rejected():
    response = client.get(BASE, params={"start": "2026-10-27T11:00:00Z", "end": "2026-10-27T12:00:00Z", "min_capacity": 0})
    assert response.status_code == 422
