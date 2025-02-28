"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .notificationtriggervariableresponse import (
    NotificationTriggerVariableResponse,
    NotificationTriggerVariableResponseTypedDict,
)
from .triggerreservedvariableresponse import (
    TriggerReservedVariableResponse,
    TriggerReservedVariableResponseTypedDict,
)
from .triggertypeenum import TriggerTypeEnum
from novu_py.types import BaseModel
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class NotificationTriggerResponseTypedDict(TypedDict):
    type: TriggerTypeEnum
    r"""The type of the trigger"""
    identifier: str
    r"""The identifier of the trigger"""
    variables: List[NotificationTriggerVariableResponseTypedDict]
    r"""The variables of the trigger"""
    subscriber_variables: NotRequired[
        List[NotificationTriggerVariableResponseTypedDict]
    ]
    r"""The subscriber variables of the trigger"""
    reserved_variables: NotRequired[List[TriggerReservedVariableResponseTypedDict]]
    r"""The reserved variables of the trigger"""


class NotificationTriggerResponse(BaseModel):
    type: TriggerTypeEnum
    r"""The type of the trigger"""

    identifier: str
    r"""The identifier of the trigger"""

    variables: List[NotificationTriggerVariableResponse]
    r"""The variables of the trigger"""

    subscriber_variables: Annotated[
        Optional[List[NotificationTriggerVariableResponse]],
        pydantic.Field(alias="subscriberVariables"),
    ] = None
    r"""The subscriber variables of the trigger"""

    reserved_variables: Annotated[
        Optional[List[TriggerReservedVariableResponse]],
        pydantic.Field(alias="reservedVariables"),
    ] = None
    r"""The reserved variables of the trigger"""
