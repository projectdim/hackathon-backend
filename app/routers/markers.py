from fastapi import APIRouter

from app.routers.schemas import Marker

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
        }]
    }