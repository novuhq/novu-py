"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .messageactionresult import MessageActionResult, MessageActionResultTypedDict
from .messageactionstatusenum import MessageActionStatusEnum
from .messagebutton import MessageButton, MessageButtonTypedDict
from novu_py.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class MessageActionTypedDict(TypedDict):
    status: NotRequired[MessageActionStatusEnum]
    r"""Status of the message action"""
    buttons: NotRequired[List[MessageButtonTypedDict]]
    r"""List of buttons associated with the message action"""
    result: NotRequired[MessageActionResultTypedDict]
    r"""Result of the message action"""


class MessageAction(BaseModel):
    status: Optional[MessageActionStatusEnum] = None
    r"""Status of the message action"""

    buttons: Optional[List[MessageButton]] = None
    r"""List of buttons associated with the message action"""

    result: Optional[MessageActionResult] = None
    r"""Result of the message action"""
