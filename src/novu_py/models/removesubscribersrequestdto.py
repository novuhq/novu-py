"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from novu_py.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class RemoveSubscribersRequestDtoTypedDict(TypedDict):
    subscribers: List[str]
    r"""List of subscriber identifiers that will be removed to the topic"""


class RemoveSubscribersRequestDto(BaseModel):
    subscribers: List[str]
    r"""List of subscriber identifiers that will be removed to the topic"""
