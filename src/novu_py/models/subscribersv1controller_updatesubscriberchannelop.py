"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .subscriberresponsedto import SubscriberResponseDto, SubscriberResponseDtoTypedDict
from .updatesubscriberchannelrequestdto import (
    UpdateSubscriberChannelRequestDto,
    UpdateSubscriberChannelRequestDtoTypedDict,
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


class SubscribersV1ControllerUpdateSubscriberChannelRequestTypedDict(TypedDict):
    subscriber_id: str
    update_subscriber_channel_request_dto: UpdateSubscriberChannelRequestDtoTypedDict
    idempotency_key: NotRequired[str]
    r"""A header for idempotency purposes"""


class SubscribersV1ControllerUpdateSubscriberChannelRequest(BaseModel):
    subscriber_id: Annotated[
        str,
        pydantic.Field(alias="subscriberId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]

    update_subscriber_channel_request_dto: Annotated[
        UpdateSubscriberChannelRequestDto,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    idempotency_key: Annotated[
        Optional[str],
        pydantic.Field(alias="idempotency-key"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""A header for idempotency purposes"""


class SubscribersV1ControllerUpdateSubscriberChannelResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: SubscriberResponseDtoTypedDict


class SubscribersV1ControllerUpdateSubscriberChannelResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: SubscriberResponseDto
