from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_rooms_response():
    response = client.get("/rooms")
    assert response.status_code == 200
    rooms = response.json()["rooms"]
    assert [room["id"] for room in rooms] == ["LIB-101", "LIB-202", "ENG-303"]
    assert rooms[2]["capacity"] == 6
