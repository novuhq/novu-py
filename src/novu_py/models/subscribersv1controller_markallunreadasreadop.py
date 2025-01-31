"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .markallmessageasrequestdto import (
    MarkAllMessageAsRequestDto,
    MarkAllMessageAsRequestDtoTypedDict,
)
from novu_py.types import BaseModel
from novu_py.utils import (
    FieldMetadata,
    HeaderMetadata,
    PathParamMetadata,
    RequestMetadata,
)
import pydantic
from typing import Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class SubscribersV1ControllerMarkAllUnreadAsReadRequestTypedDict(TypedDict):
    subscriber_id: str
    mark_all_message_as_request_dto: MarkAllMessageAsRequestDtoTypedDict
    idempotency_key: NotRequired[str]
    r"""A header for idempotency purposes"""


class SubscribersV1ControllerMarkAllUnreadAsReadRequest(BaseModel):
    subscriber_id: Annotated[
        str,
        pydantic.Field(alias="subscriberId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]

    mark_all_message_as_request_dto: Annotated[
        MarkAllMessageAsRequestDto,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    idempotency_key: Annotated[
        Optional[str],
        pydantic.Field(alias="idempotency-key"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""A header for idempotency purposes"""


class SubscribersV1ControllerMarkAllUnreadAsReadResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: float


class SubscribersV1ControllerMarkAllUnreadAsReadResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: float
