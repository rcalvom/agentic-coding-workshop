# Campus Study Room Availability API

A lightweight REST API for finding available study rooms across campus buildings. The service exposes room information and answers availability queries using locally stored reservation data.

## Features

- List rooms and their building and seating capacity.
- Find rooms available during a requested time interval.
- Filter results by minimum capacity.
- Validate date/time ranges and timezone information.
- Explore the API using FastAPI's automatically generated OpenAPI documentation.

The service is read-only. Room and reservation records are stored in `data/*.json`; no external database or credentials are required.

## Requirements

- Python 3.10+
- Git (to clone the repository)

## Getting started

Clone the repository and install its dependencies in a virtual environment:

```bash
git clone https://github.com/rcalvom/agentic-coding-workshop.git
cd agentic-coding-workshop
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

On Windows PowerShell, use `py -m venv .venv` and run `.\.venv\Scripts\python.exe -m pip install -r requirements.txt`.

Start the API:

```bash
python -m uvicorn app.main:app --reload
```

The service runs at `http://127.0.0.1:8000`. Interactive API documentation is available at [`/docs`](http://127.0.0.1:8000/docs), and the OpenAPI schema at `/openapi.json`.

## API endpoints

| Method | Path | Description |
|---|---|---|
| GET | `/health` | Service health status |
| GET | `/rooms` | List rooms and capacities |
| GET | `/rooms/available` | List rooms available for a time interval and minimum capacity |

Example:

```bash
curl 'http://127.0.0.1:8000/rooms/available?start=2026-10-27T13:00:00Z&end=2026-10-27T13:30:00Z&min_capacity=4'
```

Example response:

```json
{
  "available_rooms": [
    {"id": "ENG-303", "building": "Engineering", "capacity": 6},
    {"id": "LIB-202", "building": "Library", "capacity": 4}
  ]
}
```

Timestamps must include a timezone offset. The API uses half-open intervals, `[start, end)`, so a reservation ending at the requested start time does not block the room. See [API specification](docs/api-spec.md) for validation rules.

## Project structure

```text
app/
  main.py            HTTP endpoints and request validation
  models.py          Room and reservation models
  store.py           JSON data loading
  availability.py    Room availability calculation
data/
  rooms.json         Room inventory
  reservations.json  Existing room reservations
docs/
  api-spec.md        API contract
  architecture.md    Components and request flow
tests/
  test_rooms.py
  test_availability.py
```

## Running tests

```bash
python -m pytest -q
```

Tests cover endpoint responses, filtering, input validation, and reservation boundaries. For a failing test, inspect its assertion, compare behavior against the API contract, and check the [issue tracker](https://github.com/rcalvom/agentic-coding-workshop/issues).

## Contributing

Bug reports and feature requests are welcome through GitHub Issues. For code changes, follow [CONTRIBUTING.md](CONTRIBUTING.md), add appropriate tests, and describe how behavior was verified.

## License

[MIT](LICENSE).
