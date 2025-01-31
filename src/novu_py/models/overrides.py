"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from novu_py.types import BaseModel
from typing_extensions import TypedDict


class OverridesChannel(str, Enum):
    r"""The channel type which is overridden"""

    IN_APP = "in_app"
    EMAIL = "email"
    SMS = "sms"
    CHAT = "chat"
    PUSH = "push"


class Source(str, Enum):
    r"""The source of overrides"""

    SUBSCRIBER = "subscriber"
    TEMPLATE = "template"
    WORKFLOW_OVERRIDE = "workflowOverride"


class OverridesTypedDict(TypedDict):
    channel: OverridesChannel
    r"""The channel type which is overridden"""
    source: Source
    r"""The source of overrides"""


class Overrides(BaseModel):
    channel: OverridesChannel
    r"""The channel type which is overridden"""

    source: Source
    r"""The source of overrides"""
