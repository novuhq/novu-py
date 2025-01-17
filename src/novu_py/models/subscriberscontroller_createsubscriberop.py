"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .subscriberresponsedto import SubscriberResponseDto, SubscriberResponseDtoTypedDict
from novu_py.types import BaseModel
from typing import Dict, List
from typing_extensions import TypedDict


class SubscribersControllerCreateSubscriberResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: SubscriberResponseDtoTypedDict


class SubscribersControllerCreateSubscriberResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: SubscriberResponseDto
