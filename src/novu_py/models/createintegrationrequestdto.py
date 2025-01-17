"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .credentialsdto import CredentialsDto, CredentialsDtoTypedDict
from .stepfilterdto import StepFilterDto, StepFilterDtoTypedDict
from enum import Enum
from novu_py.types import BaseModel
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CreateIntegrationRequestDtoChannel(str, Enum):
    r"""The channel type for the integration"""

    IN_APP = "in_app"
    EMAIL = "email"
    SMS = "sms"
    CHAT = "chat"
    PUSH = "push"


class CreateIntegrationRequestDtoTypedDict(TypedDict):
    provider_id: str
    r"""The provider ID for the integration"""
    channel: CreateIntegrationRequestDtoChannel
    r"""The channel type for the integration"""
    name: NotRequired[str]
    r"""The name of the integration"""
    identifier: NotRequired[str]
    r"""The unique identifier for the integration"""
    environment_id: NotRequired[str]
    r"""The ID of the associated environment"""
    credentials: NotRequired[CredentialsDtoTypedDict]
    r"""The credentials for the integration"""
    active: NotRequired[bool]
    r"""If the integration is active, the validation on the credentials field will run"""
    check: NotRequired[bool]
    r"""Flag to check the integration status"""
    conditions: NotRequired[List[StepFilterDtoTypedDict]]
    r"""Conditions for the integration"""


class CreateIntegrationRequestDto(BaseModel):
    provider_id: Annotated[str, pydantic.Field(alias="providerId")]
    r"""The provider ID for the integration"""

    channel: CreateIntegrationRequestDtoChannel
    r"""The channel type for the integration"""

    name: Optional[str] = None
    r"""The name of the integration"""

    identifier: Optional[str] = None
    r"""The unique identifier for the integration"""

    environment_id: Annotated[Optional[str], pydantic.Field(alias="_environmentId")] = (
        None
    )
    r"""The ID of the associated environment"""

    credentials: Optional[CredentialsDto] = None
    r"""The credentials for the integration"""

    active: Optional[bool] = None
    r"""If the integration is active, the validation on the credentials field will run"""

    check: Optional[bool] = None
    r"""Flag to check the integration status"""

    conditions: Optional[List[StepFilterDto]] = None
    r"""Conditions for the integration"""
