"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from novu_py.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CreateTopicResponseDtoTypedDict(TypedDict):
    key: str
    r"""User defined custom key and provided by the user that will be an unique identifier for the Topic created."""
    id: NotRequired[str]
    r"""The unique identifier for the Topic created."""


class CreateTopicResponseDto(BaseModel):
    key: str
    r"""User defined custom key and provided by the user that will be an unique identifier for the Topic created."""

    id: Annotated[Optional[str], pydantic.Field(alias="_id")] = None
    r"""The unique identifier for the Topic created."""
