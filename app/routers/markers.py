from typing import Union, List
from fastapi import APIRouter
from pydantic import BaseModel
from ..entities.event_entity import EventEntity

router = APIRouter(prefix="/markers")


class Marker(BaseModel):
    id: str
    lat: float
    lng: float


@router.get("/", response_model=List[Marker])
def get_all_markers():
    data = EventEntity().find_by_id(10)
    data = EventEntity().create({
        'ts': "'2022-01-01 00:00:00'",
        'review_id': 1,
        'intact': 1,
        'stable_electricity': 1,
        'accessible': 1,
        'stable_water': 1,
        'gas_station': 1,
        'medical_facilities': 1,
        'comment': 1,
        'status': 1,
        'type': 1,
    })
    print(data)
    return [
        {
            "id": 2000,
            "lat": 3000,
            "lng": 221324
        }, {
            "id": 2500,
            "lat": 3400,
            "lng": 221324
        },
    ]

