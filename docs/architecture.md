# Architecture

- `app/main.py`: FastAPI routes and request validation.
- `app/models.py`: dataclass types for rooms and reservations.
- `app/store.py`: local JSON fixture loader.
- `app/availability.py`: availability filtering and booking-overlap logic.
- `data/`: test fixtures, deliberately not a live scheduling backend.
- `tests/`: HTTP-level functional and boundary tests.

The API is intentionally small so agents can inspect all relevant source and see verification output within ten minutes.
