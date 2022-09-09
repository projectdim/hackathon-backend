import datetime
from typing import Literal
from pydantic import Field

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
    status_key: Literal[
            'intact',
            'stable',
            'accessible',
            'closed',
            'open'
        ] = Field(alias='statusKey')

    safety_level: float = Field(alias='safetyLevel', ge=0, le=0)
    distance: str
    modified_date: datetime.datetime = Field(alias='modifiedDate')
    description: str


class Marker(BaseModel):
    id: str
    lat: float
    lng: float
    address: "Address"
    photos: list["Photo"]
    statuses: list["Status"]