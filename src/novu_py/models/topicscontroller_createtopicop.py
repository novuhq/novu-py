"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .createtopicresponsedto import (
    CreateTopicResponseDto,
    CreateTopicResponseDtoTypedDict,
)
from novu_py.types import BaseModel
from typing import Dict, List
from typing_extensions import TypedDict


class TopicsControllerCreateTopicResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: CreateTopicResponseDtoTypedDict


class TopicsControllerCreateTopicResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: CreateTopicResponseDto
