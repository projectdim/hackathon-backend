from pydantic import BaseModel
from app.routers.create_schemas import MarkerCreate, PhotoCreate, StatusCreate


class Address(BaseModel):
    city: str
    zipcode: str
    street: str


class Photo(PhotoCreate):
    id: str


class Status(StatusCreate):
    id: str


class Marker(MarkerCreate):
    id: str
