"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .channeltypeenum import ChannelTypeEnum
from .emailblock import EmailBlock, EmailBlockTypedDict
from .messagecta import MessageCTA, MessageCTATypedDict
from .messagestatusenum import MessageStatusEnum
from .subscriberresponsedto import SubscriberResponseDto, SubscriberResponseDtoTypedDict
from .workflowresponse import WorkflowResponse, WorkflowResponseTypedDict
from novu_py.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
import pydantic
from pydantic import model_serializer
from typing import List, Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


ContentTypedDict = TypeAliasType(
    "ContentTypedDict", Union[List[EmailBlockTypedDict], str]
)
r"""Content of the message, can be an email block or a string"""


Content = TypeAliasType("Content", Union[List[EmailBlock], str])
r"""Content of the message, can be an email block or a string"""


class MessageResponseDtoPayloadTypedDict(TypedDict):
    r"""The payload that was used to send the notification trigger"""


class MessageResponseDtoPayload(BaseModel):
    r"""The payload that was used to send the notification trigger"""


class MessageResponseDtoOverridesTypedDict(TypedDict):
    r"""Provider specific overrides used when triggering the notification"""


class MessageResponseDtoOverrides(BaseModel):
    r"""Provider specific overrides used when triggering the notification"""


class MessageResponseDtoTypedDict(TypedDict):
    template_id: str
    r"""Template ID associated with the message"""
    environment_id: str
    r"""Environment ID where the message is sent"""
    message_template_id: str
    r"""Message template ID"""
    organization_id: str
    r"""Organization ID associated with the message"""
    notification_id: str
    r"""Notification ID associated with the message"""
    subscriber_id: str
    r"""Subscriber ID associated with the message"""
    created_at: str
    r"""Creation date of the message"""
    content: ContentTypedDict
    r"""Content of the message, can be an email block or a string"""
    transaction_id: str
    r"""Transaction ID associated with the message"""
    channel: ChannelTypeEnum
    r"""Channel type through which the message is sent"""
    read: bool
    r"""Indicates if the message has been read"""
    seen: bool
    r"""Indicates if the message has been seen"""
    cta: MessageCTATypedDict
    r"""Call to action associated with the message"""
    status: MessageStatusEnum
    r"""Status of the message"""
    id: NotRequired[str]
    r"""Unique identifier for the message"""
    subscriber: NotRequired[SubscriberResponseDtoTypedDict]
    r"""Subscriber details, if available"""
    template: NotRequired[WorkflowResponseTypedDict]
    r"""Workflow template associated with the message"""
    template_identifier: NotRequired[str]
    r"""Identifier for the message template"""
    delivered_at: NotRequired[List[str]]
    r"""Array of delivery dates for the message, if the message has multiple delivery dates, for example after being snoozed"""
    last_seen_date: NotRequired[str]
    r"""Last seen date of the message, if available"""
    last_read_date: NotRequired[str]
    r"""Last read date of the message, if available"""
    subject: NotRequired[str]
    r"""Subject of the message, if applicable"""
    snoozed_until: NotRequired[str]
    r"""Date when the message will be unsnoozed"""
    email: NotRequired[str]
    r"""Email address associated with the message, if applicable"""
    phone: NotRequired[str]
    r"""Phone number associated with the message, if applicable"""
    direct_webhook_url: NotRequired[str]
    r"""Direct webhook URL for the message, if applicable"""
    provider_id: NotRequired[str]
    r"""Provider ID associated with the message, if applicable"""
    device_tokens: NotRequired[List[str]]
    r"""Device tokens associated with the message, if applicable"""
    title: NotRequired[str]
    r"""Title of the message, if applicable"""
    feed_id: NotRequired[Nullable[str]]
    r"""Feed ID associated with the message, if applicable"""
    error_id: NotRequired[str]
    r"""Error ID if the message has an error"""
    error_text: NotRequired[str]
    r"""Error text if the message has an error"""
    payload: NotRequired[MessageResponseDtoPayloadTypedDict]
    r"""The payload that was used to send the notification trigger"""
    overrides: NotRequired[MessageResponseDtoOverridesTypedDict]
    r"""Provider specific overrides used when triggering the notification"""


class MessageResponseDto(BaseModel):
    template_id: Annotated[str, pydantic.Field(alias="_templateId")]
    r"""Template ID associated with the message"""

    environment_id: Annotated[str, pydantic.Field(alias="_environmentId")]
    r"""Environment ID where the message is sent"""

    message_template_id: Annotated[str, pydantic.Field(alias="_messageTemplateId")]
    r"""Message template ID"""

    organization_id: Annotated[str, pydantic.Field(alias="_organizationId")]
    r"""Organization ID associated with the message"""

    notification_id: Annotated[str, pydantic.Field(alias="_notificationId")]
    r"""Notification ID associated with the message"""

    subscriber_id: Annotated[str, pydantic.Field(alias="_subscriberId")]
    r"""Subscriber ID associated with the message"""

    created_at: Annotated[str, pydantic.Field(alias="createdAt")]
    r"""Creation date of the message"""

    content: Content
    r"""Content of the message, can be an email block or a string"""

    transaction_id: Annotated[str, pydantic.Field(alias="transactionId")]
    r"""Transaction ID associated with the message"""

    channel: ChannelTypeEnum
    r"""Channel type through which the message is sent"""

    read: bool
    r"""Indicates if the message has been read"""

    seen: bool
    r"""Indicates if the message has been seen"""

    cta: MessageCTA
    r"""Call to action associated with the message"""

    status: MessageStatusEnum
    r"""Status of the message"""

    id: Annotated[Optional[str], pydantic.Field(alias="_id")] = None
    r"""Unique identifier for the message"""

    subscriber: Optional[SubscriberResponseDto] = None
    r"""Subscriber details, if available"""

    template: Optional[WorkflowResponse] = None
    r"""Workflow template associated with the message"""

    template_identifier: Annotated[
        Optional[str], pydantic.Field(alias="templateIdentifier")
    ] = None
    r"""Identifier for the message template"""

    delivered_at: Annotated[
        Optional[List[str]], pydantic.Field(alias="deliveredAt")
    ] = None
    r"""Array of delivery dates for the message, if the message has multiple delivery dates, for example after being snoozed"""

    last_seen_date: Annotated[Optional[str], pydantic.Field(alias="lastSeenDate")] = (
        None
    )
    r"""Last seen date of the message, if available"""

    last_read_date: Annotated[Optional[str], pydantic.Field(alias="lastReadDate")] = (
        None
    )
    r"""Last read date of the message, if available"""

    subject: Optional[str] = None
    r"""Subject of the message, if applicable"""

    snoozed_until: Annotated[Optional[str], pydantic.Field(alias="snoozedUntil")] = None
    r"""Date when the message will be unsnoozed"""

    email: Optional[str] = None
    r"""Email address associated with the message, if applicable"""

    phone: Optional[str] = None
    r"""Phone number associated with the message, if applicable"""

    direct_webhook_url: Annotated[
        Optional[str], pydantic.Field(alias="directWebhookUrl")
    ] = None
    r"""Direct webhook URL for the message, if applicable"""

    provider_id: Annotated[Optional[str], pydantic.Field(alias="providerId")] = None
    r"""Provider ID associated with the message, if applicable"""

    device_tokens: Annotated[
        Optional[List[str]], pydantic.Field(alias="deviceTokens")
    ] = None
    r"""Device tokens associated with the message, if applicable"""

    title: Optional[str] = None
    r"""Title of the message, if applicable"""

    feed_id: Annotated[OptionalNullable[str], pydantic.Field(alias="_feedId")] = UNSET
    r"""Feed ID associated with the message, if applicable"""

    error_id: Annotated[Optional[str], pydantic.Field(alias="errorId")] = None
    r"""Error ID if the message has an error"""

    error_text: Annotated[Optional[str], pydantic.Field(alias="errorText")] = None
    r"""Error text if the message has an error"""

    payload: Optional[MessageResponseDtoPayload] = None
    r"""The payload that was used to send the notification trigger"""

    overrides: Optional[MessageResponseDtoOverrides] = None
    r"""Provider specific overrides used when triggering the notification"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "_id",
            "subscriber",
            "template",
            "templateIdentifier",
            "deliveredAt",
            "lastSeenDate",
            "lastReadDate",
            "subject",
            "snoozedUntil",
            "email",
            "phone",
            "directWebhookUrl",
            "providerId",
            "deviceTokens",
            "title",
            "_feedId",
            "errorId",
            "errorText",
            "payload",
            "overrides",
        ]
        nullable_fields = ["_feedId"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in type(self).model_fields.items():
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
