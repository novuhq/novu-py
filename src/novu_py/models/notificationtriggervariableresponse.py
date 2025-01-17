"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from novu_py.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class NotificationTriggerVariableResponseValueTypedDict(TypedDict):
    r"""The value of the variable"""


class NotificationTriggerVariableResponseValue(BaseModel):
    r"""The value of the variable"""


class NotificationTriggerVariableResponseType(str, Enum):
    r"""The type of the variable"""

    STRING = "String"
    ARRAY = "Array"
    BOOLEAN = "Boolean"


class NotificationTriggerVariableResponseTypedDict(TypedDict):
    name: str
    r"""The name of the variable"""
    value: NotRequired[NotificationTriggerVariableResponseValueTypedDict]
    r"""The value of the variable"""
    type: NotRequired[NotificationTriggerVariableResponseType]
    r"""The type of the variable"""


class NotificationTriggerVariableResponse(BaseModel):
    name: str
    r"""The name of the variable"""

    value: Optional[NotificationTriggerVariableResponseValue] = None
    r"""The value of the variable"""

    type: Optional[NotificationTriggerVariableResponseType] = None
    r"""The type of the variable"""
