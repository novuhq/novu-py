"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from novu_py.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class MarkMessageActionAsSeenDtoStatus(str, Enum):
    r"""Message action status"""

    PENDING = "pending"
    DONE = "done"


class MarkMessageActionAsSeenDtoPayloadTypedDict(TypedDict):
    r"""Message action payload"""


class MarkMessageActionAsSeenDtoPayload(BaseModel):
    r"""Message action payload"""


class MarkMessageActionAsSeenDtoTypedDict(TypedDict):
    status: MarkMessageActionAsSeenDtoStatus
    r"""Message action status"""
    payload: NotRequired[MarkMessageActionAsSeenDtoPayloadTypedDict]
    r"""Message action payload"""


class MarkMessageActionAsSeenDto(BaseModel):
    status: MarkMessageActionAsSeenDtoStatus
    r"""Message action status"""

    payload: Optional[MarkMessageActionAsSeenDtoPayload] = None
    r"""Message action payload"""
