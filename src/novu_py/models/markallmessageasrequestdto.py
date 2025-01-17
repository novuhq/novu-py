"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from novu_py.types import BaseModel
import pydantic
from typing import List, Optional, Union
from typing_extensions import Annotated, NotRequired, TypedDict


FeedIdentifierTypedDict = Union[str, List[str]]
r"""Optional feed identifier or array of feed identifiers"""


FeedIdentifier = Union[str, List[str]]
r"""Optional feed identifier or array of feed identifiers"""


class MarkAllMessageAsRequestDtoMarkAs(str, Enum):
    r"""Mark all subscriber messages as read, unread, seen or unseen"""

    READ = "read"
    SEEN = "seen"
    UNREAD = "unread"
    UNSEEN = "unseen"


class MarkAllMessageAsRequestDtoTypedDict(TypedDict):
    mark_as: MarkAllMessageAsRequestDtoMarkAs
    r"""Mark all subscriber messages as read, unread, seen or unseen"""
    feed_identifier: NotRequired[FeedIdentifierTypedDict]
    r"""Optional feed identifier or array of feed identifiers"""


class MarkAllMessageAsRequestDto(BaseModel):
    mark_as: Annotated[MarkAllMessageAsRequestDtoMarkAs, pydantic.Field(alias="markAs")]
    r"""Mark all subscriber messages as read, unread, seen or unseen"""

    feed_identifier: Annotated[
        Optional[FeedIdentifier], pydantic.Field(alias="feedIdentifier")
    ] = None
    r"""Optional feed identifier or array of feed identifiers"""
