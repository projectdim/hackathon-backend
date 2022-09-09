from typing import Union, List

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/markers")

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: List[str] = []


@router.get("/items/", response_model=Item)
async def create_item():
    return {
        "name": "dsfjsdf",
        "price": 4263173,
    }


@router.get("/")
def get_all_markers():
    return [
        {
            "longitude": 2000,
            "latitude": 3000
        }, {
            "longitude": 2500,
            "latitude": 3400
        },
    ]
