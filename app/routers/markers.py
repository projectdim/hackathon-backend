from typing import Union, List
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/markers")


class Marker(BaseModel):
    id: str
    lat: float
    lng: float


@router.get("/", response_model=List[Marker])
def get_all_markers():
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
