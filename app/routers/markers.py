import datetime
from typing import List

from fastapi import APIRouter
from app.routers.schemas import Marker, MarkerCreate, Pin

router = APIRouter(prefix="/markers")


@router.get("/", response_model=List[Pin])
def get_all_markers():
    return [
        { "id": 2000, "lat": 50.19621, "lng": 23.88737 },
        { "id": 2500, "lat": 49.91406, "lng": 27.30412 },
    ]


@router.get(
    "/{marker_id}",
    response_model=Marker
)
def marker_detail(marker_id: str):
    return {
        "id": "tnehosu",
        "address": {
            "city": "Krakow",
            "zipcode": "00-001",
            "street": "Krupnicza"
        },
        "photos": [{
            "url": "http://localhost:8000/static/test_1.jpg"
        }, {
            "url": "http://localhost:8000/static/test_2.jpg"
        }],
        "statuses": [{
            "type": "building",
            "statusKey": "stable",
            "safetyLevel": 3,
            "modifiedDate": datetime.datetime.utcnow(),
            "description": "b"
        }]
    }


@router.post("/", response_model=MarkerCreate)
def create_item(item: MarkerCreate):
    return item
