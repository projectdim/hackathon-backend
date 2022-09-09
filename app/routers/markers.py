import datetime
from typing import List

from fastapi import APIRouter
from pydantic import BaseModel
from app.entities.review_entity import ReviewEntity

from app.routers.schemas import Marker, MarkerCreate

markers_router = APIRouter(prefix="/markers")


class Pin(BaseModel):
    id: str
    lat: float
    lng: float


@markers_router.get("/", response_model=List[Pin])
def get_all_markers():
    # return ReviewEntity.find_all()
    return [
        { "id": 2000, "lat": 50.19621, "lng": 23.88737 },
        { "id": 2500, "lat": 49.91406, "lng": 27.30412 },
    ]


@markers_router.get(
    "/{marker_id}",
    response_model=Marker
)
def marker_detail(marker_id: str):
    return {
        "id": "tnehosu",
        "lat": 54.55,
        "lng": 22.15,
        "address": {
            "city": "Krakow",
            "zipcode": "00-001",
            "street": "Krupnicza"
        },
        "photos": [{
            "id": "a",
            "label": "a person",
            "url": "http://localhost:8000/static/test_1.jpg"
        }, {
            "id": "b",
            "label": "an other person",
            "url": "http://localhost:8000/static/test_2.jpg"
        }],
        "statuses": [{
            "id": "whatever",
            "type": "building",
            "statusKey": "stable",
            "safetyLevel": 3,
            "distance": "whatever",
            "modifiedDate": datetime.datetime.utcnow(),
            "description": "b"
        }]
    }


@markers_router.post("/", response_model=MarkerCreate)
def create_item(item: MarkerCreate):
    return item
