"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .unseencountresponse import UnseenCountResponse, UnseenCountResponseTypedDict
from novu_py.types import BaseModel
from novu_py.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata
import pydantic
from typing import Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class SubscribersControllerGetUnseenCountRequestTypedDict(TypedDict):
    subscriber_id: str
    seen: NotRequired[bool]
    r"""Indicates whether to count seen notifications."""
    limit: NotRequired[float]
    r"""The maximum number of notifications to return."""


class SubscribersControllerGetUnseenCountRequest(BaseModel):
    subscriber_id: Annotated[
        str,
        pydantic.Field(alias="subscriberId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]

    seen: Annotated[
        Optional[bool],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = False
    r"""Indicates whether to count seen notifications."""

    limit: Annotated[
        Optional[float],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 100
    r"""The maximum number of notifications to return."""


class SubscribersControllerGetUnseenCountResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: UnseenCountResponseTypedDict


class SubscribersControllerGetUnseenCountResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: UnseenCountResponse
