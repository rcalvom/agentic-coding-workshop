# Campus Study Room API — API contract

The service provides read-only room and availability queries backed by local JSON data.

## `GET /health`

**Response (200)**

```json
{"status": "ok"}
```

## `GET /rooms`

Returns the room inventory.

**Response (200)**

```json
{
  "rooms": [
    {"id": "LIB-101", "building": "Library", "capacity": 2},
    {"id": "LIB-202", "building": "Library", "capacity": 4},
    {"id": "ENG-303", "building": "Engineering", "capacity": 6}
  ]
}
```

The list reflects the current contents of `data/rooms.json`.

## `GET /rooms/available`

Returns rooms that meet the capacity requirement and are not reserved for any overlapping portion of the requested interval. Results are sorted by room ID.

### Query parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| `start` | ISO 8601 timestamp | Yes | Requested start, with timezone offset |
| `end` | ISO 8601 timestamp | Yes | Requested end, with timezone offset |
| `min_capacity` | Integer | No | Minimum number of seats; defaults to 1 |

### Validation and availability rules

1. `start` must be strictly earlier than `end`.
2. Both timestamps must include timezone offsets. Equivalent timestamps with different offsets represent the same instant.
3. Requested intervals cannot exceed 24 hours.
4. `min_capacity` must be at least 1.
5. Reservations and requests use half-open intervals `[start, end)`: intervals that touch at a boundary are not overlapping.
6. Rooms with capacity below `min_capacity`, or with any positive-duration reservation overlap, are excluded.
7. Responses list available rooms in ascending room-ID order.

Invalid requests return HTTP 422.

### Example

```http
GET /rooms/available?start=2026-10-27T13:00:00Z&end=2026-10-27T13:30:00Z&min_capacity=4
```

**Response (200)**

```json
{
  "available_rooms": [
    {"id": "ENG-303", "building": "Engineering", "capacity": 6},
    {"id": "LIB-202", "building": "Library", "capacity": 4}
  ]
}
```

See `/docs` and `/openapi.json` for the generated HTTP schema.
