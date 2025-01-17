"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .actorfeeditemdto import ActorFeedItemDto, ActorFeedItemDtoTypedDict
from .channeltypeenum import ChannelTypeEnum
from .messagecta import MessageCTA, MessageCTATypedDict
from .subscriberfeedresponsedto import (
    SubscriberFeedResponseDto,
    SubscriberFeedResponseDtoTypedDict,
)
from datetime import datetime
from enum import Enum
from novu_py.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
import pydantic
from pydantic import model_serializer
from typing import Any, Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class NotificationFeedItemDtoStatus(str, Enum):
    r"""Current status of the notification."""

    SENT = "sent"
    ERROR = "error"
    WARNING = "warning"


class NotificationFeedItemDtoTypedDict(TypedDict):
    id: str
    r"""Unique identifier for the notification."""
    template_id: str
    r"""Identifier for the template used to generate the notification."""
    environment_id: str
    r"""Identifier for the environment where the notification is sent."""
    message_template_id: str
    r"""Identifier for the message template used."""
    organization_id: str
    r"""Identifier for the organization sending the notification."""
    notification_id: str
    r"""Unique identifier for the notification instance."""
    subscriber_id: str
    r"""Unique identifier for the subscriber receiving the notification."""
    feed_id: str
    r"""Identifier for the feed associated with the notification."""
    job_id: str
    r"""Identifier for the job that triggered the notification."""
    transaction_id: str
    r"""Unique identifier for the transaction associated with the notification."""
    content: str
    r"""The main content of the notification."""
    channel: ChannelTypeEnum
    r"""Channel type through which the message is sent"""
    read: bool
    r"""Indicates whether the notification has been read by the subscriber."""
    seen: bool
    r"""Indicates whether the notification has been seen by the subscriber."""
    deleted: bool
    r"""Indicates whether the notification has been deleted."""
    cta: MessageCTATypedDict
    r"""Call-to-action information associated with the notification."""
    status: NotificationFeedItemDtoStatus
    r"""Current status of the notification."""
    created_at: NotRequired[Nullable[datetime]]
    r"""Timestamp indicating when the notification was created."""
    updated_at: NotRequired[Nullable[datetime]]
    r"""Timestamp indicating when the notification was last updated."""
    actor: NotRequired[ActorFeedItemDtoTypedDict]
    r"""Actor details related to the notification, if applicable."""
    subscriber: NotRequired[SubscriberFeedResponseDtoTypedDict]
    r"""Subscriber details associated with this notification."""
    template_identifier: NotRequired[Nullable[str]]
    r"""Identifier for the template used, if applicable."""
    provider_id: NotRequired[Nullable[str]]
    r"""Identifier for the provider that sends the notification."""
    subject: NotRequired[Nullable[str]]
    r"""The subject line for email notifications, if applicable."""
    device_tokens: NotRequired[Nullable[List[str]]]
    r"""Device tokens for push notifications, if applicable."""
    payload: NotRequired[Dict[str, Any]]
    r"""The payload that was used to send the notification trigger."""
    overrides: NotRequired[Dict[str, Any]]
    r"""Provider-specific overrides used when triggering the notification."""


class NotificationFeedItemDto(BaseModel):
    id: Annotated[str, pydantic.Field(alias="_id")]
    r"""Unique identifier for the notification."""

    template_id: Annotated[str, pydantic.Field(alias="_templateId")]
    r"""Identifier for the template used to generate the notification."""

    environment_id: Annotated[str, pydantic.Field(alias="_environmentId")]
    r"""Identifier for the environment where the notification is sent."""

    message_template_id: Annotated[str, pydantic.Field(alias="_messageTemplateId")]
    r"""Identifier for the message template used."""

    organization_id: Annotated[str, pydantic.Field(alias="_organizationId")]
    r"""Identifier for the organization sending the notification."""

    notification_id: Annotated[str, pydantic.Field(alias="_notificationId")]
    r"""Unique identifier for the notification instance."""

    subscriber_id: Annotated[str, pydantic.Field(alias="_subscriberId")]
    r"""Unique identifier for the subscriber receiving the notification."""

    feed_id: Annotated[str, pydantic.Field(alias="_feedId")]
    r"""Identifier for the feed associated with the notification."""

    job_id: Annotated[str, pydantic.Field(alias="_jobId")]
    r"""Identifier for the job that triggered the notification."""

    transaction_id: Annotated[str, pydantic.Field(alias="transactionId")]
    r"""Unique identifier for the transaction associated with the notification."""

    content: str
    r"""The main content of the notification."""

    channel: ChannelTypeEnum
    r"""Channel type through which the message is sent"""

    read: bool
    r"""Indicates whether the notification has been read by the subscriber."""

    seen: bool
    r"""Indicates whether the notification has been seen by the subscriber."""

    deleted: bool
    r"""Indicates whether the notification has been deleted."""

    cta: MessageCTA
    r"""Call-to-action information associated with the notification."""

    status: NotificationFeedItemDtoStatus
    r"""Current status of the notification."""

    created_at: Annotated[
        OptionalNullable[datetime], pydantic.Field(alias="createdAt")
    ] = UNSET
    r"""Timestamp indicating when the notification was created."""

    updated_at: Annotated[
        OptionalNullable[datetime], pydantic.Field(alias="updatedAt")
    ] = UNSET
    r"""Timestamp indicating when the notification was last updated."""

    actor: Optional[ActorFeedItemDto] = None
    r"""Actor details related to the notification, if applicable."""

    subscriber: Optional[SubscriberFeedResponseDto] = None
    r"""Subscriber details associated with this notification."""

    template_identifier: Annotated[
        OptionalNullable[str], pydantic.Field(alias="templateIdentifier")
    ] = UNSET
    r"""Identifier for the template used, if applicable."""

    provider_id: Annotated[
        OptionalNullable[str], pydantic.Field(alias="providerId")
    ] = UNSET
    r"""Identifier for the provider that sends the notification."""

    subject: OptionalNullable[str] = UNSET
    r"""The subject line for email notifications, if applicable."""

    device_tokens: Annotated[
        OptionalNullable[List[str]], pydantic.Field(alias="deviceTokens")
    ] = UNSET
    r"""Device tokens for push notifications, if applicable."""

    payload: Optional[Dict[str, Any]] = None
    r"""The payload that was used to send the notification trigger."""

    overrides: Optional[Dict[str, Any]] = None
    r"""Provider-specific overrides used when triggering the notification."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "createdAt",
            "updatedAt",
            "actor",
            "subscriber",
            "templateIdentifier",
            "providerId",
            "subject",
            "deviceTokens",
            "payload",
            "overrides",
        ]
        nullable_fields = [
            "createdAt",
            "updatedAt",
            "templateIdentifier",
            "providerId",
            "subject",
            "deviceTokens",
        ]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
