"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .delayregularmetadata import DelayRegularMetadata, DelayRegularMetadataTypedDict
from .delayscheduledmetadata import (
    DelayScheduledMetadata,
    DelayScheduledMetadataTypedDict,
)
from .digestregularmetadata import DigestRegularMetadata, DigestRegularMetadataTypedDict
from .digesttimedmetadata import DigestTimedMetadata, DigestTimedMetadataTypedDict
from .messagetemplate import MessageTemplate, MessageTemplateTypedDict
from .replycallback import ReplyCallback, ReplyCallbackTypedDict
from .stepfilterdto import StepFilterDto, StepFilterDtoTypedDict
from novu_py.types import BaseModel
import pydantic
from typing import List, Optional, Union
from typing_extensions import Annotated, NotRequired, TypedDict


NotificationStepDataMetadataTypedDict = Union[
    DelayScheduledMetadataTypedDict,
    DelayRegularMetadataTypedDict,
    DigestTimedMetadataTypedDict,
    DigestRegularMetadataTypedDict,
]
r"""Metadata associated with the workflow step. Can vary based on the type of step."""


NotificationStepDataMetadata = Union[
    DelayScheduledMetadata,
    DelayRegularMetadata,
    DigestTimedMetadata,
    DigestRegularMetadata,
]
r"""Metadata associated with the workflow step. Can vary based on the type of step."""


class NotificationStepDataTypedDict(TypedDict):
    id: NotRequired[str]
    r"""Unique identifier for the notification step."""
    uuid: NotRequired[str]
    r"""Universally unique identifier for the notification step."""
    name: NotRequired[str]
    r"""Name of the notification step."""
    template_id: NotRequired[str]
    r"""ID of the template associated with this notification step."""
    active: NotRequired[bool]
    r"""Indicates whether the notification step is active."""
    should_stop_on_fail: NotRequired[bool]
    r"""Determines if the process should stop on failure."""
    template: NotRequired[MessageTemplateTypedDict]
    r"""Message template used in this notification step."""
    filters: NotRequired[List[StepFilterDtoTypedDict]]
    r"""Filters applied to this notification step."""
    parent_id: NotRequired[str]
    r"""ID of the parent notification step, if applicable."""
    metadata: NotRequired[NotificationStepDataMetadataTypedDict]
    r"""Metadata associated with the workflow step. Can vary based on the type of step."""
    reply_callback: NotRequired[ReplyCallbackTypedDict]
    r"""Callback information for replies, including whether it is active and the callback URL."""


class NotificationStepData(BaseModel):
    id: Annotated[Optional[str], pydantic.Field(alias="_id")] = None
    r"""Unique identifier for the notification step."""

    uuid: Optional[str] = None
    r"""Universally unique identifier for the notification step."""

    name: Optional[str] = None
    r"""Name of the notification step."""

    template_id: Annotated[Optional[str], pydantic.Field(alias="_templateId")] = None
    r"""ID of the template associated with this notification step."""

    active: Optional[bool] = None
    r"""Indicates whether the notification step is active."""

    should_stop_on_fail: Annotated[
        Optional[bool], pydantic.Field(alias="shouldStopOnFail")
    ] = None
    r"""Determines if the process should stop on failure."""

    template: Optional[MessageTemplate] = None
    r"""Message template used in this notification step."""

    filters: Optional[List[StepFilterDto]] = None
    r"""Filters applied to this notification step."""

    parent_id: Annotated[Optional[str], pydantic.Field(alias="_parentId")] = None
    r"""ID of the parent notification step, if applicable."""

    metadata: Optional[NotificationStepDataMetadata] = None
    r"""Metadata associated with the workflow step. Can vary based on the type of step."""

    reply_callback: Annotated[
        Optional[ReplyCallback], pydantic.Field(alias="replyCallback")
    ] = None
    r"""Callback information for replies, including whether it is active and the callback URL."""
