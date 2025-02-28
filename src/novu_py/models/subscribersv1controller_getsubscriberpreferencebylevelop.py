"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .getsubscriberpreferencesresponsedto import (
    GetSubscriberPreferencesResponseDto,
    GetSubscriberPreferencesResponseDtoTypedDict,
)
from enum import Enum
from novu_py.types import BaseModel
from novu_py.utils import (
    FieldMetadata,
    HeaderMetadata,
    PathParamMetadata,
    QueryParamMetadata,
)
import pydantic
from typing import Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class Parameter(str, Enum):
    r"""the preferences level to be retrieved (template / global)"""

    GLOBAL = "global"
    TEMPLATE = "template"


class SubscribersV1ControllerGetSubscriberPreferenceByLevelRequestTypedDict(TypedDict):
    preference_level: Parameter
    r"""the preferences level to be retrieved (template / global)"""
    subscriber_id: str
    include_inactive_channels: NotRequired[bool]
    r"""A flag which specifies if the inactive workflow channels should be included in the retrieved preferences. Default is true"""
    idempotency_key: NotRequired[str]
    r"""A header for idempotency purposes"""


class SubscribersV1ControllerGetSubscriberPreferenceByLevelRequest(BaseModel):
    preference_level: Annotated[
        Parameter,
        pydantic.Field(alias="parameter"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""the preferences level to be retrieved (template / global)"""

    subscriber_id: Annotated[
        str,
        pydantic.Field(alias="subscriberId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]

    include_inactive_channels: Annotated[
        Optional[bool],
        pydantic.Field(alias="includeInactiveChannels"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""A flag which specifies if the inactive workflow channels should be included in the retrieved preferences. Default is true"""

    idempotency_key: Annotated[
        Optional[str],
        pydantic.Field(alias="idempotency-key"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""A header for idempotency purposes"""


class SubscribersV1ControllerGetSubscriberPreferenceByLevelResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: List[GetSubscriberPreferencesResponseDtoTypedDict]


class SubscribersV1ControllerGetSubscriberPreferenceByLevelResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: List[GetSubscriberPreferencesResponseDto]
