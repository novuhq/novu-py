"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .subscriberresponsedto import SubscriberResponseDto, SubscriberResponseDtoTypedDict
from .updatesubscriberchannelrequestdto import (
    UpdateSubscriberChannelRequestDto,
    UpdateSubscriberChannelRequestDtoTypedDict,
)
from novu_py.types import BaseModel
from novu_py.utils import FieldMetadata, PathParamMetadata, RequestMetadata
import pydantic
from typing import Dict, List
from typing_extensions import Annotated, TypedDict


class SubscribersControllerModifySubscriberChannelRequestTypedDict(TypedDict):
    subscriber_id: str
    update_subscriber_channel_request_dto: UpdateSubscriberChannelRequestDtoTypedDict


class SubscribersControllerModifySubscriberChannelRequest(BaseModel):
    subscriber_id: Annotated[
        str,
        pydantic.Field(alias="subscriberId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]

    update_subscriber_channel_request_dto: Annotated[
        UpdateSubscriberChannelRequestDto,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]


class SubscribersControllerModifySubscriberChannelResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: SubscriberResponseDtoTypedDict


class SubscribersControllerModifySubscriberChannelResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: SubscriberResponseDto
