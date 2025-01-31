"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .subscriberpayloaddto import SubscriberPayloadDto, SubscriberPayloadDtoTypedDict
from .tenantpayloaddto import TenantPayloadDto, TenantPayloadDtoTypedDict
from novu_py.types import BaseModel
import pydantic
from typing import Any, Dict, Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


class TriggerEventToAllRequestDtoOverridesTypedDict(TypedDict):
    r"""This could be used to override provider specific configurations"""


class TriggerEventToAllRequestDtoOverrides(BaseModel):
    r"""This could be used to override provider specific configurations"""


TriggerEventToAllRequestDtoActorTypedDict = TypeAliasType(
    "TriggerEventToAllRequestDtoActorTypedDict",
    Union[SubscriberPayloadDtoTypedDict, str],
)
r"""It is used to display the Avatar of the provided actor's subscriber id or actor object.
If a new actor object is provided, we will create a new subscriber in our system

"""


TriggerEventToAllRequestDtoActor = TypeAliasType(
    "TriggerEventToAllRequestDtoActor", Union[SubscriberPayloadDto, str]
)
r"""It is used to display the Avatar of the provided actor's subscriber id or actor object.
If a new actor object is provided, we will create a new subscriber in our system

"""


TriggerEventToAllRequestDtoTenantTypedDict = TypeAliasType(
    "TriggerEventToAllRequestDtoTenantTypedDict", Union[TenantPayloadDtoTypedDict, str]
)
r"""It is used to specify a tenant context during trigger event.
If a new tenant object is provided, we will create a new tenant.

"""


TriggerEventToAllRequestDtoTenant = TypeAliasType(
    "TriggerEventToAllRequestDtoTenant", Union[TenantPayloadDto, str]
)
r"""It is used to specify a tenant context during trigger event.
If a new tenant object is provided, we will create a new tenant.

"""


class TriggerEventToAllRequestDtoTypedDict(TypedDict):
    name: str
    r"""The trigger identifier associated for the template you wish to send. This identifier can be found on the template page."""
    payload: Dict[str, Any]
    r"""The payload object is used to pass additional information that
    could be used to render the template, or perform routing rules based on it.
    For In-App channel, payload data are also available in <Inbox />
    """
    overrides: NotRequired[TriggerEventToAllRequestDtoOverridesTypedDict]
    r"""This could be used to override provider specific configurations"""
    transaction_id: NotRequired[str]
    r"""A unique identifier for this transaction, we will generated a UUID if not provided."""
    actor: NotRequired[TriggerEventToAllRequestDtoActorTypedDict]
    r"""It is used to display the Avatar of the provided actor's subscriber id or actor object.
    If a new actor object is provided, we will create a new subscriber in our system

    """
    tenant: NotRequired[TriggerEventToAllRequestDtoTenantTypedDict]
    r"""It is used to specify a tenant context during trigger event.
    If a new tenant object is provided, we will create a new tenant.

    """


class TriggerEventToAllRequestDto(BaseModel):
    name: str
    r"""The trigger identifier associated for the template you wish to send. This identifier can be found on the template page."""

    payload: Dict[str, Any]
    r"""The payload object is used to pass additional information that
    could be used to render the template, or perform routing rules based on it.
    For In-App channel, payload data are also available in <Inbox />
    """

    overrides: Optional[TriggerEventToAllRequestDtoOverrides] = None
    r"""This could be used to override provider specific configurations"""

    transaction_id: Annotated[Optional[str], pydantic.Field(alias="transactionId")] = (
        None
    )
    r"""A unique identifier for this transaction, we will generated a UUID if not provided."""

    actor: Optional[TriggerEventToAllRequestDtoActor] = None
    r"""It is used to display the Avatar of the provided actor's subscriber id or actor object.
    If a new actor object is provided, we will create a new subscriber in our system

    """

    tenant: Optional[TriggerEventToAllRequestDtoTenant] = None
    r"""It is used to specify a tenant context during trigger event.
    If a new tenant object is provided, we will create a new tenant.

    """
