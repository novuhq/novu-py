"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .markmessageactionasseendto import (
    MarkMessageActionAsSeenDto,
    MarkMessageActionAsSeenDtoTypedDict,
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
from typing import Any, Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class SubscribersV1ControllerMarkActionAsSeenRequestTypedDict(TypedDict):
    message_id: str
    type: Any
    subscriber_id: str
    mark_message_action_as_seen_dto: MarkMessageActionAsSeenDtoTypedDict
    idempotency_key: NotRequired[str]
    r"""A header for idempotency purposes"""


class SubscribersV1ControllerMarkActionAsSeenRequest(BaseModel):
    message_id: Annotated[
        str,
        pydantic.Field(alias="messageId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]

    type: Annotated[
        Any, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    subscriber_id: Annotated[
        str,
        pydantic.Field(alias="subscriberId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]

    mark_message_action_as_seen_dto: Annotated[
        MarkMessageActionAsSeenDto,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    idempotency_key: Annotated[
        Optional[str],
        pydantic.Field(alias="idempotency-key"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""A header for idempotency purposes"""


class SubscribersV1ControllerMarkActionAsSeenResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: MessageResponseDtoTypedDict


class SubscribersV1ControllerMarkActionAsSeenResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: MessageResponseDto
