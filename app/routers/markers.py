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
        { "id": 2000, "lat": 50.19621, "lng": 23.88737 }, 
        { "id": 2500, "lat": 49.91406, "lng": 27.30412 },
    ]
