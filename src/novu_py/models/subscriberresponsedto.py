"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .channelsettingsdto import ChannelSettingsDto, ChannelSettingsDtoTypedDict
from novu_py.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
import pydantic
from pydantic import model_serializer
from typing import Any, Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class SubscriberResponseDtoTypedDict(TypedDict):
    subscriber_id: str
    r"""The identifier used to create this subscriber, which typically corresponds to the user ID in your system."""
    organization_id: str
    r"""The unique identifier of the organization to which the subscriber belongs."""
    environment_id: str
    r"""The unique identifier of the environment associated with this subscriber."""
    deleted: bool
    r"""Indicates whether the subscriber has been deleted."""
    created_at: str
    r"""The timestamp indicating when the subscriber was created, in ISO 8601 format."""
    updated_at: str
    r"""The timestamp indicating when the subscriber was last updated, in ISO 8601 format."""
    id: NotRequired[str]
    r"""The internal ID generated by Novu for your subscriber. This ID does not match the `subscriberId` used in your queries. Refer to `subscriberId` for that identifier."""
    first_name: NotRequired[Nullable[str]]
    r"""The first name of the subscriber."""
    last_name: NotRequired[Nullable[str]]
    r"""The last name of the subscriber."""
    email: NotRequired[Nullable[str]]
    r"""The email address of the subscriber."""
    phone: NotRequired[Nullable[str]]
    r"""The phone number of the subscriber."""
    avatar: NotRequired[Nullable[str]]
    r"""The URL of the subscriber's avatar image."""
    locale: NotRequired[Nullable[str]]
    r"""The locale setting of the subscriber, indicating their preferred language or region."""
    channels: NotRequired[List[ChannelSettingsDtoTypedDict]]
    r"""An array of channel settings associated with the subscriber."""
    topics: NotRequired[List[str]]
    r"""An array of topics that the subscriber is subscribed to."""
    is_online: NotRequired[Nullable[bool]]
    r"""Indicates whether the subscriber is currently online."""
    last_online_at: NotRequired[Nullable[str]]
    r"""The timestamp indicating when the subscriber was last online, in ISO 8601 format."""
    v: NotRequired[float]
    r"""The version of the subscriber document."""
    data: NotRequired[Nullable[Dict[str, Any]]]
    r"""Additional custom data for the subscriber"""
    timezone: NotRequired[Nullable[str]]
    r"""Timezone of the subscriber"""


class SubscriberResponseDto(BaseModel):
    subscriber_id: Annotated[str, pydantic.Field(alias="subscriberId")]
    r"""The identifier used to create this subscriber, which typically corresponds to the user ID in your system."""

    organization_id: Annotated[str, pydantic.Field(alias="_organizationId")]
    r"""The unique identifier of the organization to which the subscriber belongs."""

    environment_id: Annotated[str, pydantic.Field(alias="_environmentId")]
    r"""The unique identifier of the environment associated with this subscriber."""

    deleted: bool
    r"""Indicates whether the subscriber has been deleted."""

    created_at: Annotated[str, pydantic.Field(alias="createdAt")]
    r"""The timestamp indicating when the subscriber was created, in ISO 8601 format."""

    updated_at: Annotated[str, pydantic.Field(alias="updatedAt")]
    r"""The timestamp indicating when the subscriber was last updated, in ISO 8601 format."""

    id: Annotated[Optional[str], pydantic.Field(alias="_id")] = None
    r"""The internal ID generated by Novu for your subscriber. This ID does not match the `subscriberId` used in your queries. Refer to `subscriberId` for that identifier."""

    first_name: Annotated[OptionalNullable[str], pydantic.Field(alias="firstName")] = (
        UNSET
    )
    r"""The first name of the subscriber."""

    last_name: Annotated[OptionalNullable[str], pydantic.Field(alias="lastName")] = (
        UNSET
    )
    r"""The last name of the subscriber."""

    email: OptionalNullable[str] = UNSET
    r"""The email address of the subscriber."""

    phone: OptionalNullable[str] = UNSET
    r"""The phone number of the subscriber."""

    avatar: OptionalNullable[str] = UNSET
    r"""The URL of the subscriber's avatar image."""

    locale: OptionalNullable[str] = UNSET
    r"""The locale setting of the subscriber, indicating their preferred language or region."""

    channels: Optional[List[ChannelSettingsDto]] = None
    r"""An array of channel settings associated with the subscriber."""

    topics: Annotated[
        Optional[List[str]],
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."
        ),
    ] = None
    r"""An array of topics that the subscriber is subscribed to."""

    is_online: Annotated[OptionalNullable[bool], pydantic.Field(alias="isOnline")] = (
        UNSET
    )
    r"""Indicates whether the subscriber is currently online."""

    last_online_at: Annotated[
        OptionalNullable[str], pydantic.Field(alias="lastOnlineAt")
    ] = UNSET
    r"""The timestamp indicating when the subscriber was last online, in ISO 8601 format."""

    v: Annotated[Optional[float], pydantic.Field(alias="__v")] = None
    r"""The version of the subscriber document."""

    data: OptionalNullable[Dict[str, Any]] = UNSET
    r"""Additional custom data for the subscriber"""

    timezone: OptionalNullable[str] = UNSET
    r"""Timezone of the subscriber"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "_id",
            "firstName",
            "lastName",
            "email",
            "phone",
            "avatar",
            "locale",
            "channels",
            "topics",
            "isOnline",
            "lastOnlineAt",
            "__v",
            "data",
            "timezone",
        ]
        nullable_fields = [
            "firstName",
            "lastName",
            "email",
            "phone",
            "avatar",
            "locale",
            "isOnline",
            "lastOnlineAt",
            "data",
            "timezone",
        ]
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
