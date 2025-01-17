"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from novu_py.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class NotificationGroupTypedDict(TypedDict):
    name: str
    environment_id: str
    organization_id: str
    id: NotRequired[str]
    parent_id: NotRequired[str]


class NotificationGroup(BaseModel):
    name: str

    environment_id: Annotated[str, pydantic.Field(alias="_environmentId")]

    organization_id: Annotated[str, pydantic.Field(alias="_organizationId")]

    id: Annotated[Optional[str], pydantic.Field(alias="_id")] = None

    parent_id: Annotated[Optional[str], pydantic.Field(alias="_parentId")] = None
