"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .notificationtriggervariable import (
    NotificationTriggerVariable,
    NotificationTriggerVariableTypedDict,
)
from enum import Enum
from novu_py.types import BaseModel
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class Type(str, Enum):
    r"""Type of the trigger"""

    EVENT = "event"


class NotificationTriggerDtoTypedDict(TypedDict):
    type: Type
    r"""Type of the trigger"""
    identifier: str
    r"""Identifier of the trigger"""
    variables: List[NotificationTriggerVariableTypedDict]
    r"""Variables of the trigger"""
    subscriber_variables: NotRequired[List[NotificationTriggerVariableTypedDict]]
    r"""Subscriber variables of the trigger"""


class NotificationTriggerDto(BaseModel):
    type: Type
    r"""Type of the trigger"""

    identifier: str
    r"""Identifier of the trigger"""

    variables: List[NotificationTriggerVariable]
    r"""Variables of the trigger"""

    subscriber_variables: Annotated[
        Optional[List[NotificationTriggerVariable]],
        pydantic.Field(alias="subscriberVariables"),
    ] = None
    r"""Subscriber variables of the trigger"""
