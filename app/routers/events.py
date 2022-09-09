from fastapi import APIRouter
from typing import List
from pydantic import BaseModel
from app.entities.event_entity import EventEntity

events_router = APIRouter(prefix="/events")


class EventModel(BaseModel):
    id: str
    ts: str
    review_id: str
    intact: str
    stable_electricity: str
    accessible: str
    stable_water: str
    gas_station: str
    medical_facilities: str
    comment: str
    status: str
    type: str


@events_router.get("/", response_model=List[EventModel])
def get_all():
    return EventEntity().find_all()@events_router.get("/", response_model=List[EventModel])


@events_router.post("/", response_model=EventModel)
def create():
    return EventEntity().create()
