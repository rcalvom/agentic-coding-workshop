"""FastAPI server for the workshop."""
from datetime import datetime, timedelta

from fastapi import FastAPI, HTTPException, Query

from .availability import available_rooms
from .store import load_reservations, load_rooms

app = FastAPI(title="Campus Study Room API", version="0.1.0")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/rooms")
def rooms() -> dict:
    return {"rooms": [room.__dict__ for room in load_rooms()]}


@app.get("/rooms/available")
def rooms_available(
    start: datetime,
    end: datetime,
    min_capacity: int = Query(default=1, ge=1),
) -> dict:
    if start.tzinfo is None or end.tzinfo is None:
        raise HTTPException(status_code=422, detail="start and end must include a UTC offset")
    if start >= end:
        raise HTTPException(status_code=422, detail="start must be before end")
    if end - start > timedelta(hours=24):
        raise HTTPException(status_code=422, detail="interval may not exceed 24 hours")
    result = available_rooms(
        load_rooms(), load_reservations(), start, end, min_capacity
    )
    return {"available_rooms": [room.__dict__ for room in result]}
