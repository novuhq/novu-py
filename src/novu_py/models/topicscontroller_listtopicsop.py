"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .filtertopicsresponsedto import (
    FilterTopicsResponseDto,
    FilterTopicsResponseDtoTypedDict,
)
from novu_py.types import BaseModel
from novu_py.utils import FieldMetadata, QueryParamMetadata
import pydantic
from typing import Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class TopicsControllerListTopicsRequestTypedDict(TypedDict):
    page: NotRequired[int]
    r"""The page number to retrieve (starts from 0)"""
    page_size: NotRequired[int]
    r"""The number of items to return per page (default: 10)"""
    key: NotRequired[str]
    r"""A filter key to apply to the results"""


class TopicsControllerListTopicsRequest(BaseModel):
    page: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 0
    r"""The page number to retrieve (starts from 0)"""

    page_size: Annotated[
        Optional[int],
        pydantic.Field(alias="pageSize"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 10
    r"""The number of items to return per page (default: 10)"""

    key: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""A filter key to apply to the results"""


class TopicsControllerListTopicsResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: FilterTopicsResponseDtoTypedDict


class TopicsControllerListTopicsResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: FilterTopicsResponseDto
