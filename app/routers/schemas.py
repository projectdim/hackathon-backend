import datetime
from typing import Literal
from pydantic import Field

from pydantic import BaseModel


class Pin(BaseModel):
    id: str
    lat: float
    lng: float


class Data(BaseModel):
    markers: list["Pin"]


class Address(BaseModel):
    city: str
    zipcode: str
    street: str


class Photo(BaseModel):
    url: str


class Status(BaseModel):
    type: Literal[
        'building',
        'electricity',
        'water',
        'roads',
        'fuel'
    ]
    status_key: Literal[
        'intact',
        'stable',
        'accessible',
        'closed',
        'open'
    ] = Field(alias='statusKey')

    safety_level: bool = Field(alias='safetyLevel')
    modified_date: datetime.datetime = Field(alias='modifiedDate')
    description: str


class Contact(BaseModel):
    label: str
    telephone_number: float = Field(alias='telephoneNumber')
    email: str


class MarkerCreate(BaseModel):
    address: "Address"
    photos: list["Photo"]
    statuses: list["Status"]


class Marker(MarkerCreate):
    id: str
