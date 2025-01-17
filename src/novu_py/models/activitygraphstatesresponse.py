"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from novu_py.types import BaseModel
import pydantic
from typing import List
from typing_extensions import Annotated, TypedDict


class Channels(str, Enum):
    IN_APP = "in_app"
    EMAIL = "email"
    SMS = "sms"
    CHAT = "chat"
    PUSH = "push"


class ActivityGraphStatesResponseTypedDict(TypedDict):
    id: str
    count: float
    templates: List[str]
    channels: List[Channels]


class ActivityGraphStatesResponse(BaseModel):
    id: Annotated[str, pydantic.Field(alias="_id")]

    count: float

    templates: List[str]

    channels: List[Channels]
