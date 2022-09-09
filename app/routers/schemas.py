from pydantic import BaseModel


class Address(BaseModel):
    city: str
    zipcode: str
    street: str

class Photo(BaseModel):
    id: str
    label: str
    url: str


class Marker(BaseModel):
    id: str
    lat: float
    lng: float
    address: "Address"
    photos: list["Photo"]