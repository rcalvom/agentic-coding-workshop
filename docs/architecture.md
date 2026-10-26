# Architecture

The application is a small FastAPI service that serves read-only queries from version-controlled JSON files. It has no database server, login mechanism, or third-party service dependencies.

## Components

- `app/main.py`: defines the HTTP endpoints and validates query parameters.
- `app/models.py`: defines the `Room` and `Reservation` domain models.
- `app/store.py`: loads `data/rooms.json` and `data/reservations.json`.
- `app/availability.py`: filters rooms by capacity and determines reservation conflicts.
- `tests/`: exercises the HTTP endpoints, request validation, and availability logic.

## Request flow

For `GET /rooms/available`:

1. FastAPI parses `start`, `end`, and `min_capacity`.
2. `app/main.py` validates the timestamps and interval length.
3. `app/store.py` loads the room inventory and existing reservations.
4. `app/availability.py` selects rooms meeting the capacity requirement without a conflicting booking.
5. The endpoint serializes the selected rooms as `available_rooms`.

## Data model

**Room:** `id`, `building`, `capacity`.

**Reservation:** `room_id`, `start`, `end`.

Reservation timestamps are stored as ISO 8601 strings and parsed as timezone-aware datetimes. Room IDs connect reservations to the room inventory.

## Development

Run the API with `python -m uvicorn app.main:app --reload` and tests with `python -m pytest -q`. Changes to reservation semantics should be checked against [the API contract](api-spec.md) and corresponding boundary tests.

## Scope

Data is file-backed and reloaded on requests. The application does not create or update reservations, guarantee concurrent booking safety, or persist mutations.
