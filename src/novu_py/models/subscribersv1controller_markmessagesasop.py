"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .messagemarkasrequestdto import (
    MessageMarkAsRequestDto,
    MessageMarkAsRequestDtoTypedDict,
)
from .messageresponsedto import MessageResponseDto, MessageResponseDtoTypedDict
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


class SubscribersV1ControllerMarkMessagesAsRequestTypedDict(TypedDict):
    subscriber_id: str
    message_mark_as_request_dto: MessageMarkAsRequestDtoTypedDict
    idempotency_key: NotRequired[str]
    r"""A header for idempotency purposes"""


class SubscribersV1ControllerMarkMessagesAsRequest(BaseModel):
    subscriber_id: Annotated[
        str,
        pydantic.Field(alias="subscriberId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]

    message_mark_as_request_dto: Annotated[
        MessageMarkAsRequestDto,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    idempotency_key: Annotated[
        Optional[str],
        pydantic.Field(alias="idempotency-key"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""A header for idempotency purposes"""


class SubscribersV1ControllerMarkMessagesAsResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: List[MessageResponseDtoTypedDict]


class SubscribersV1ControllerMarkMessagesAsResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: List[MessageResponseDto]
