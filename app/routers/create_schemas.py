import datetime
from typing import Literal

from pydantic import BaseModel, Field


class Address(BaseModel):
    city: str
    zipcode: str
    street: str


class PhotoCreate(BaseModel):
    label: str
    url: str


class StatusCreate(BaseModel):
    type: str
    # type: Literal[
    #         'building',
    #         'electricity',
    #         'water',
    #         'roads',
    #         'fuel'
    #     ]
    status_key: str = Field(alias="statusKey")
    # status_key: Literal[
    #         'intact',
    #         'stable',
    #         'accessible',
    #         'closed',
    #         'open'
    #     ] = Field(alias='statusKey')

    safety_level: float = Field(alias='safetyLevel', ge=0, le=10)
    distance: str
    modified_date: datetime.datetime = Field(alias='modifiedDate')
    description: str


class MarkerCreate(BaseModel):
    lat: float
    lng: float
    address: "Address"
    photos: list["PhotoCreate"]
    statuses: list["StatusCreate"]
