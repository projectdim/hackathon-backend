from fastapi import APIRouter
from pydantic import BaseModel
from app.entities.event_entity import EventEntity

events_router = APIRouter(prefix="/events")


class Event(BaseModel):
    id: str


@events_router.get("/")
# @events_router.get("/", response_model=List[Event])
def get_all():
    return EventEntity().find_all()
