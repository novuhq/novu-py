"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .credentialsdto import CredentialsDto, CredentialsDtoTypedDict
from .stepfilterdto import StepFilterDto, StepFilterDtoTypedDict
from enum import Enum
from novu_py.types import BaseModel
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class Channel(str, Enum):
    r"""The channel type for the integration, which defines how the integration communicates (e.g., email, SMS)."""

    IN_APP = "in_app"
    EMAIL = "email"
    SMS = "sms"
    CHAT = "chat"
    PUSH = "push"


class IntegrationResponseDtoTypedDict(TypedDict):
    environment_id: str
    r"""The unique identifier for the environment associated with this integration. This links to the Environment collection."""
    organization_id: str
    r"""The unique identifier for the organization that owns this integration. This links to the Organization collection."""
    name: str
    r"""The name of the integration, which is used to identify it in the user interface."""
    identifier: str
    r"""A unique string identifier for the integration, often used for API calls or internal references."""
    provider_id: str
    r"""The identifier for the provider of the integration (e.g., \"mailgun\", \"twilio\")."""
    channel: Channel
    r"""The channel type for the integration, which defines how the integration communicates (e.g., email, SMS)."""
    credentials: CredentialsDtoTypedDict
    r"""The credentials required for the integration to function, including API keys and other sensitive information."""
    active: bool
    r"""Indicates whether the integration is currently active. An active integration will process events and messages."""
    deleted: bool
    r"""Indicates whether the integration has been marked as deleted (soft delete)."""
    primary: bool
    r"""Indicates whether this integration is marked as primary. A primary integration is often the default choice for processing."""
    id: NotRequired[str]
    r"""The unique identifier of the integration record in the database. This is automatically generated."""
    deleted_at: NotRequired[str]
    r"""The timestamp indicating when the integration was deleted. This is set when the integration is soft deleted."""
    deleted_by: NotRequired[str]
    r"""The identifier of the user who performed the deletion of this integration. Useful for audit trails."""
    conditions: NotRequired[List[StepFilterDtoTypedDict]]
    r"""An array of conditions associated with the integration that may influence its behavior or processing logic."""


class IntegrationResponseDto(BaseModel):
    environment_id: Annotated[str, pydantic.Field(alias="_environmentId")]
    r"""The unique identifier for the environment associated with this integration. This links to the Environment collection."""

    organization_id: Annotated[str, pydantic.Field(alias="_organizationId")]
    r"""The unique identifier for the organization that owns this integration. This links to the Organization collection."""

    name: str
    r"""The name of the integration, which is used to identify it in the user interface."""

    identifier: str
    r"""A unique string identifier for the integration, often used for API calls or internal references."""

    provider_id: Annotated[str, pydantic.Field(alias="providerId")]
    r"""The identifier for the provider of the integration (e.g., \"mailgun\", \"twilio\")."""

    channel: Channel
    r"""The channel type for the integration, which defines how the integration communicates (e.g., email, SMS)."""

    credentials: CredentialsDto
    r"""The credentials required for the integration to function, including API keys and other sensitive information."""

    active: bool
    r"""Indicates whether the integration is currently active. An active integration will process events and messages."""

    deleted: bool
    r"""Indicates whether the integration has been marked as deleted (soft delete)."""

    primary: bool
    r"""Indicates whether this integration is marked as primary. A primary integration is often the default choice for processing."""

    id: Annotated[Optional[str], pydantic.Field(alias="_id")] = None
    r"""The unique identifier of the integration record in the database. This is automatically generated."""

    deleted_at: Annotated[Optional[str], pydantic.Field(alias="deletedAt")] = None
    r"""The timestamp indicating when the integration was deleted. This is set when the integration is soft deleted."""

    deleted_by: Annotated[Optional[str], pydantic.Field(alias="deletedBy")] = None
    r"""The identifier of the user who performed the deletion of this integration. Useful for audit trails."""

    conditions: Optional[List[StepFilterDto]] = None
    r"""An array of conditions associated with the integration that may influence its behavior or processing logic."""
