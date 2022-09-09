import datetime
from typing import List
from jinja2 import Template

from fastapi import APIRouter
from pydantic import BaseModel

from app.support.database.db import Query
from app.support.database.transformation import transform_data

from app.routers.schemas import Marker, MarkerCreate

router = APIRouter(prefix="/markers")


class Pin(BaseModel):
    id: str
    lat: float
    lng: float


@router.get("/", response_model=List[Pin])
def get_all_markers():
    data = {'data': {'statuses': "('active')"}}
    template = open(f"app/sql_templates/select_markers.sql", 'r').read()
    query = Template(template).render(data)
    markers_data = Query().select(query)
    return transform_data(markers_data)


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
            "id": "whatever",
            "type": "building",
            "statusKey": "stable",
            "safetyLevel": 3,
            "distance": "whatever",
            "modifiedDate": datetime.datetime.utcnow(),
            "description": "b"
        }]
    }


@router.post("/", response_model=MarkerCreate)
def create_item(item: MarkerCreate):
    return item
