"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .channelcredentials import ChannelCredentials, ChannelCredentialsTypedDict
from enum import Enum
from novu_py.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ChannelSettingsDtoProviderID(str, Enum):
    r"""The provider identifier for the credentials"""

    SLACK = "slack"
    DISCORD = "discord"
    MSTEAMS = "msteams"
    MATTERMOST = "mattermost"
    RYVER = "ryver"
    ZULIP = "zulip"
    GRAFANA_ON_CALL = "grafana-on-call"
    GETSTREAM = "getstream"
    ROCKET_CHAT = "rocket-chat"
    WHATSAPP_BUSINESS = "whatsapp-business"
    FCM = "fcm"
    APNS = "apns"
    EXPO = "expo"
    ONE_SIGNAL = "one-signal"
    PUSHPAD = "pushpad"
    PUSH_WEBHOOK = "push-webhook"
    PUSHER_BEAMS = "pusher-beams"


class ChannelSettingsDtoTypedDict(TypedDict):
    provider_id: ChannelSettingsDtoProviderID
    r"""The provider identifier for the credentials"""
    credentials: ChannelCredentialsTypedDict
    r"""Credentials payload for the specified provider"""
    integration_id: str
    r"""The unique identifier of the integration associated with this channel."""
    integration_identifier: NotRequired[str]
    r"""The integration identifier"""


class ChannelSettingsDto(BaseModel):
    provider_id: Annotated[
        ChannelSettingsDtoProviderID, pydantic.Field(alias="providerId")
    ]
    r"""The provider identifier for the credentials"""

    credentials: ChannelCredentials
    r"""Credentials payload for the specified provider"""

    integration_id: Annotated[str, pydantic.Field(alias="_integrationId")]
    r"""The unique identifier of the integration associated with this channel."""

    integration_identifier: Annotated[
        Optional[str], pydantic.Field(alias="integrationIdentifier")
    ] = None
    r"""The integration identifier"""
