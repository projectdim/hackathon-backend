import datetime
from typing import Literal

from pydantic import BaseModel


class Address(BaseModel):
    city: str
    zipcode: str
    street: str


class Photo(BaseModel):
    id: str
    label: str
    url: str


class Status(BaseModel):
    id: str
    type: Literal[
            'building',
            'electricity',
            'water',
            'roads',
            'fuel'
        ]
    statusKey: Literal[
            'intact',
            'stable',
            'accessible',
            'closed',
            'open'
        ]

    safetyLevel: float
    distance: str
    modifiedDate: datetime.datetime
    description: str


class Marker(BaseModel):
    id: str
    lat: float
    lng: float
    address: "Address"
    photos: list["Photo"]
    statuses: list["Status"]