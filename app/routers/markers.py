from typing import List

from fastapi import APIRouter
from pydantic import BaseModel

from app.routers.schemas import Marker, MarkerCreate

router = APIRouter(prefix="/markers")


class Pin(BaseModel):
    id: str
    lat: float
    lng: float


@router.get("/", response_model=List[Pin])
def get_all_markers():
    return [
        {"id": 2000, "lat": 50.19621, "lng": 23.88737},
        {"id": 2500, "lat": 49.91406, "lng": 27.30412},
    ]


@router.get(
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
            "id": "123",
            "type": "building",
            "statusKey": "intact",
            "safetyLevel": True,
            "distance": "",
            "modifiedDate": "2022-09-09T16:38:20.777994",
            "description":
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit interdum hendrerit ex "
                "vitae sodales.",
        },
            {
                "id": "314324",
                "type": "electricity",
                "statusKey": "stable",
                "safetyLevel": True,
                "distance": "",
                "modifiedDate": "2022-09-09T16:38:20.777994",
                "description": ""
            },
            {
                "id": "whatever",
                "type": "road",
                "statusKey": "stable",
                "safetyLevel": True,
                "distance": "",
                "modifiedDate": "2022-09-09T16:38:20.777994",
                "description":
                    "Lorem ipsum dolor sit amet, consectetur adipiscing elit interdum hendrerit "
                    "ex vitae sodales.",
            },
            {
                "id": "536534",
                "type": "water",
                "statusKey": "unstable",
                "safetyLevel": False,
                "distance": "",
                "modifiedDate": "2022-09-09T16:38:20.777994",
                "description":
                    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus interdum "
                    "hendrerit ex vitae sodales. Donec id leo ipsum. Phasellus volutpat aliquet "
                    "mauris, et blandit nulla laoreet vitae. Quisque ante dui, porta eu felis "
                    "nec, scelerisque pharetra turpis."
            },
            {
                "id": "5456524",
                "type": "petrol",
                "statusKey": "closed",
                "safetyLevel": False,
                "distance": "0.8km",
                "modifiedDate": "2022-09-09T16:38:20.777994",
                "description": ""
            },
            {
                "id": "5456524",
                "type": "medical",
                "statusKey": "open",
                "safetyLevel": True,
                "distance": "1.2km",
                "modifiedDate": "2022-09-09T16:38:20.777994",
                "description": ""
            }, ]
    }


@router.post("/", response_model=MarkerCreate)
def create_item(item: MarkerCreate):
    return item
