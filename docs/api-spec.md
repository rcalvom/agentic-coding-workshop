# API contract and acceptance criteria

This educational API uses only deterministic local fixtures. Fix the implementation, not tests or specifications.

## Endpoints

- `GET /health` returns `{"status":"ok"}`.
- `GET /rooms` returns `{"rooms":[...]}` with `id`, `building`, `capacity`.
- `GET /rooms/available?start=<ISO8601>&end=<ISO8601>&min_capacity=<integer>` returns `{"available_rooms":[...]}` sorted by room ID.

## Availability rules

1. Intervals are half-open `[start, end)`: adjacent intervals do not conflict.
2. Positive-duration overlaps make a room unavailable.
3. Capacity must be >= `min_capacity`, which defaults to 1.
4. All timestamps must include timezone offsets. Compare instants.
5. `start >= end`, intervals longer than 24 hours, and `min_capacity < 1` return HTTP 422.
6. Rooms not blocked by reservations are available. No network or database is required.

## Example

```http
GET /rooms/available?start=2026-10-27T11:00:00Z&end=2026-10-27T11:30:00Z&min_capacity=4
```

Expected: `ENG-303` and `LIB-202`, in that order. LIB-202's booking ends at 11:00, while ENG-303's next booking begins at 11:30.

## Change policy

Do not weaken validation, alter fixture expectations or change the tests just to make a bug appear fixed.
