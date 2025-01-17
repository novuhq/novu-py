"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from novu_py.types import BaseModel
from typing_extensions import TypedDict


class CreateTopicRequestDtoTypedDict(TypedDict):
    key: str
    r"""User defined custom key and provided by the user that will be an unique identifier for the Topic created."""
    name: str
    r"""User defined custom name and provided by the user that will name the Topic created."""


class CreateTopicRequestDto(BaseModel):
    key: str
    r"""User defined custom key and provided by the user that will be an unique identifier for the Topic created."""

    name: str
    r"""User defined custom name and provided by the user that will name the Topic created."""
