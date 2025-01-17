"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .activitynotificationresponsedto import (
    ActivityNotificationResponseDto,
    ActivityNotificationResponseDtoTypedDict,
)
from novu_py.types import BaseModel
from novu_py.utils import FieldMetadata, PathParamMetadata
import pydantic
from typing import Dict, List
from typing_extensions import Annotated, TypedDict


class NotificationsControllerGetNotificationRequestTypedDict(TypedDict):
    notification_id: str


class NotificationsControllerGetNotificationRequest(BaseModel):
    notification_id: Annotated[
        str,
        pydantic.Field(alias="notificationId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]


class NotificationsControllerGetNotificationResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: ActivityNotificationResponseDtoTypedDict


class NotificationsControllerGetNotificationResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: ActivityNotificationResponseDto
