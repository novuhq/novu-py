"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .stepsoverrides import StepsOverrides, StepsOverridesTypedDict
from .subscriberpayloaddto import SubscriberPayloadDto, SubscriberPayloadDtoTypedDict
from .tenantpayloaddto import TenantPayloadDto, TenantPayloadDtoTypedDict
from .topicpayloaddto import TopicPayloadDto, TopicPayloadDtoTypedDict
from novu_py.types import BaseModel
import pydantic
from typing import Any, Dict, List, Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


class OverridesTypedDict(TypedDict):
    r"""This could be used to override provider specific configurations"""

    steps: NotRequired[Dict[str, StepsOverridesTypedDict]]
    r"""This could be used to override provider specific configurations"""
    providers: NotRequired[Dict[str, Dict[str, Any]]]
    r"""Overrides the provider configuration for the entire workflow and all steps"""
    email: NotRequired[Dict[str, Any]]
    r"""Override the email provider specific configurations for the entire workflow"""
    push: NotRequired[Dict[str, Any]]
    r"""Override the push provider specific configurations for the entire workflow"""
    sms: NotRequired[Dict[str, Any]]
    r"""Override the sms provider specific configurations for the entire workflow"""
    chat: NotRequired[Dict[str, Any]]
    r"""Override the chat provider specific configurations for the entire workflow"""
    layout_identifier: NotRequired[str]
    r"""Override the layout identifier for the entire workflow"""


class Overrides(BaseModel):
    r"""This could be used to override provider specific configurations"""

    steps: Optional[Dict[str, StepsOverrides]] = None
    r"""This could be used to override provider specific configurations"""

    providers: Optional[Dict[str, Dict[str, Any]]] = None
    r"""Overrides the provider configuration for the entire workflow and all steps"""

    email: Annotated[
        Optional[Dict[str, Any]],
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."
        ),
    ] = None
    r"""Override the email provider specific configurations for the entire workflow"""

    push: Annotated[
        Optional[Dict[str, Any]],
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."
        ),
    ] = None
    r"""Override the push provider specific configurations for the entire workflow"""

    sms: Annotated[
        Optional[Dict[str, Any]],
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."
        ),
    ] = None
    r"""Override the sms provider specific configurations for the entire workflow"""

    chat: Annotated[
        Optional[Dict[str, Any]],
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."
        ),
    ] = None
    r"""Override the chat provider specific configurations for the entire workflow"""

    layout_identifier: Annotated[
        Optional[str],
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible.",
            alias="layoutIdentifier",
        ),
    ] = None
    r"""Override the layout identifier for the entire workflow"""


OneTypedDict = TypeAliasType(
    "OneTypedDict", Union[TopicPayloadDtoTypedDict, SubscriberPayloadDtoTypedDict, str]
)


One = TypeAliasType("One", Union[TopicPayloadDto, SubscriberPayloadDto, str])


ToTypedDict = TypeAliasType(
    "ToTypedDict",
    Union[
        TopicPayloadDtoTypedDict, SubscriberPayloadDtoTypedDict, List[OneTypedDict], str
    ],
)
r"""The recipients list of people who will receive the notification."""


To = TypeAliasType("To", Union[TopicPayloadDto, SubscriberPayloadDto, List[One], str])
r"""The recipients list of people who will receive the notification."""


ActorTypedDict = TypeAliasType(
    "ActorTypedDict", Union[SubscriberPayloadDtoTypedDict, str]
)
r"""It is used to display the Avatar of the provided actor's subscriber id or actor object.

If a new actor object is provided, we will create a new subscriber in our system
"""


Actor = TypeAliasType("Actor", Union[SubscriberPayloadDto, str])
r"""It is used to display the Avatar of the provided actor's subscriber id or actor object.

If a new actor object is provided, we will create a new subscriber in our system
"""


TenantTypedDict = TypeAliasType(
    "TenantTypedDict", Union[TenantPayloadDtoTypedDict, str]
)
r"""It is used to specify a tenant context during trigger event.
Existing tenants will be updated with the provided details.
"""


Tenant = TypeAliasType("Tenant", Union[TenantPayloadDto, str])
r"""It is used to specify a tenant context during trigger event.
Existing tenants will be updated with the provided details.
"""


class TriggerEventRequestDtoTypedDict(TypedDict):
    workflow_id: str
    r"""The trigger identifier of the workflow you wish to send. This identifier can be found on the workflow page."""
    to: ToTypedDict
    r"""The recipients list of people who will receive the notification."""
    payload: NotRequired[Dict[str, Any]]
    r"""The payload object is used to pass additional custom information that could be
    used to render the workflow, or perform routing rules based on it.
    This data will also be available when fetching the notifications feed from the API to display certain parts of the UI.
    """
    overrides: NotRequired[OverridesTypedDict]
    r"""This could be used to override provider specific configurations"""
    transaction_id: NotRequired[str]
    r"""A unique identifier for this transaction, we will generate a UUID if not provided."""
    actor: NotRequired[ActorTypedDict]
    r"""It is used to display the Avatar of the provided actor's subscriber id or actor object.

    If a new actor object is provided, we will create a new subscriber in our system
    """
    tenant: NotRequired[TenantTypedDict]
    r"""It is used to specify a tenant context during trigger event.
    Existing tenants will be updated with the provided details.
    """


class TriggerEventRequestDto(BaseModel):
    workflow_id: Annotated[str, pydantic.Field(alias="name")]
    r"""The trigger identifier of the workflow you wish to send. This identifier can be found on the workflow page."""

    to: To
    r"""The recipients list of people who will receive the notification."""

    payload: Optional[Dict[str, Any]] = None
    r"""The payload object is used to pass additional custom information that could be
    used to render the workflow, or perform routing rules based on it.
    This data will also be available when fetching the notifications feed from the API to display certain parts of the UI.
    """

    overrides: Optional[Overrides] = None
    r"""This could be used to override provider specific configurations"""

    transaction_id: Annotated[Optional[str], pydantic.Field(alias="transactionId")] = (
        None
    )
    r"""A unique identifier for this transaction, we will generate a UUID if not provided."""

    actor: Optional[Actor] = None
    r"""It is used to display the Avatar of the provided actor's subscriber id or actor object.

    If a new actor object is provided, we will create a new subscriber in our system
    """

    tenant: Optional[Tenant] = None
    r"""It is used to specify a tenant context during trigger event.
    Existing tenants will be updated with the provided details.
    """
