"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .chatstepresponsedto import ChatStepResponseDto, ChatStepResponseDtoTypedDict
from .customstepresponsedto import CustomStepResponseDto, CustomStepResponseDtoTypedDict
from .delaystepresponsedto import DelayStepResponseDto, DelayStepResponseDtoTypedDict
from .digeststepresponsedto import DigestStepResponseDto, DigestStepResponseDtoTypedDict
from .emailstepresponsedto import EmailStepResponseDto, EmailStepResponseDtoTypedDict
from .inappstepresponsedto import InAppStepResponseDto, InAppStepResponseDtoTypedDict
from .pushstepresponsedto import PushStepResponseDto, PushStepResponseDtoTypedDict
from .runtimeissuedto import RuntimeIssueDto, RuntimeIssueDtoTypedDict
from .smsstepresponsedto import SmsStepResponseDto, SmsStepResponseDtoTypedDict
from .workfloworiginenum import WorkflowOriginEnum
from .workflowpreferencesresponsedto import (
    WorkflowPreferencesResponseDto,
    WorkflowPreferencesResponseDtoTypedDict,
)
from .workflowstatusenum import WorkflowStatusEnum
from novu_py.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from novu_py.utils import get_discriminator
import pydantic
from pydantic import Discriminator, Tag, model_serializer
from typing import Any, Dict, List, Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


class SlugTypedDict(TypedDict):
    r"""Slug of the workflow"""


class Slug(BaseModel):
    r"""Slug of the workflow"""


WorkflowResponseDtoStepsTypedDict = TypeAliasType(
    "WorkflowResponseDtoStepsTypedDict",
    Union[
        InAppStepResponseDtoTypedDict,
        EmailStepResponseDtoTypedDict,
        SmsStepResponseDtoTypedDict,
        PushStepResponseDtoTypedDict,
        ChatStepResponseDtoTypedDict,
        DelayStepResponseDtoTypedDict,
        DigestStepResponseDtoTypedDict,
        CustomStepResponseDtoTypedDict,
    ],
)


WorkflowResponseDtoSteps = Annotated[
    Union[
        Annotated[InAppStepResponseDto, Tag("in_app")],
        Annotated[EmailStepResponseDto, Tag("email")],
        Annotated[SmsStepResponseDto, Tag("sms")],
        Annotated[PushStepResponseDto, Tag("push")],
        Annotated[ChatStepResponseDto, Tag("chat")],
        Annotated[DelayStepResponseDto, Tag("delay")],
        Annotated[DigestStepResponseDto, Tag("digest")],
        Annotated[CustomStepResponseDto, Tag("custom")],
    ],
    Discriminator(lambda m: get_discriminator(m, "type", "type")),
]


class WorkflowResponseDtoTypedDict(TypedDict):
    name: str
    r"""Name of the workflow"""
    id: str
    r"""Unique identifier of the workflow"""
    workflow_id: str
    r"""Workflow identifier"""
    slug: SlugTypedDict
    r"""Slug of the workflow"""
    updated_at: str
    r"""Last updated timestamp"""
    created_at: str
    r"""Creation timestamp"""
    steps: List[WorkflowResponseDtoStepsTypedDict]
    r"""Steps of the workflow"""
    origin: WorkflowOriginEnum
    r"""Origin of the workflow"""
    preferences: WorkflowPreferencesResponseDtoTypedDict
    r"""Preferences for the workflow"""
    status: WorkflowStatusEnum
    r"""Status of the workflow"""
    description: NotRequired[str]
    r"""Description of the workflow"""
    tags: NotRequired[List[str]]
    r"""Tags associated with the workflow"""
    active: NotRequired[bool]
    r"""Whether the workflow is active"""
    issues: NotRequired[Dict[str, RuntimeIssueDtoTypedDict]]
    r"""Runtime issues for workflow creation and update"""
    last_triggered_at: NotRequired[Nullable[str]]
    r"""Timestamp of the last workflow trigger"""
    payload_schema: NotRequired[Nullable[Dict[str, Any]]]
    r"""The payload JSON Schema for the workflow"""
    payload_example: NotRequired[Nullable[Dict[str, Any]]]
    r"""Generated payload example based on the payload schema"""
    validate_payload: NotRequired[bool]
    r"""Whether payload schema validation is enabled"""


class WorkflowResponseDto(BaseModel):
    name: str
    r"""Name of the workflow"""

    id: Annotated[str, pydantic.Field(alias="_id")]
    r"""Unique identifier of the workflow"""

    workflow_id: Annotated[str, pydantic.Field(alias="workflowId")]
    r"""Workflow identifier"""

    slug: Slug
    r"""Slug of the workflow"""

    updated_at: Annotated[str, pydantic.Field(alias="updatedAt")]
    r"""Last updated timestamp"""

    created_at: Annotated[str, pydantic.Field(alias="createdAt")]
    r"""Creation timestamp"""

    steps: List[WorkflowResponseDtoSteps]
    r"""Steps of the workflow"""

    origin: WorkflowOriginEnum
    r"""Origin of the workflow"""

    preferences: WorkflowPreferencesResponseDto
    r"""Preferences for the workflow"""

    status: WorkflowStatusEnum
    r"""Status of the workflow"""

    description: Optional[str] = None
    r"""Description of the workflow"""

    tags: Optional[List[str]] = None
    r"""Tags associated with the workflow"""

    active: Optional[bool] = False
    r"""Whether the workflow is active"""

    issues: Optional[Dict[str, RuntimeIssueDto]] = None
    r"""Runtime issues for workflow creation and update"""

    last_triggered_at: Annotated[
        OptionalNullable[str], pydantic.Field(alias="lastTriggeredAt")
    ] = UNSET
    r"""Timestamp of the last workflow trigger"""

    payload_schema: Annotated[
        OptionalNullable[Dict[str, Any]], pydantic.Field(alias="payloadSchema")
    ] = UNSET
    r"""The payload JSON Schema for the workflow"""

    payload_example: Annotated[
        OptionalNullable[Dict[str, Any]], pydantic.Field(alias="payloadExample")
    ] = UNSET
    r"""Generated payload example based on the payload schema"""

    validate_payload: Annotated[
        Optional[bool], pydantic.Field(alias="validatePayload")
    ] = None
    r"""Whether payload schema validation is enabled"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "description",
            "tags",
            "active",
            "issues",
            "lastTriggeredAt",
            "payloadSchema",
            "payloadExample",
            "validatePayload",
        ]
        nullable_fields = ["lastTriggeredAt", "payloadSchema", "payloadExample"]
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
