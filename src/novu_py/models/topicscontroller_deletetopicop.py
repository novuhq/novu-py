"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .deletetopicresponsedto import (
    DeleteTopicResponseDto,
    DeleteTopicResponseDtoTypedDict,
)
from novu_py.types import BaseModel
from novu_py.utils import FieldMetadata, HeaderMetadata, PathParamMetadata
import pydantic
from typing import Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class TopicsControllerDeleteTopicRequestTypedDict(TypedDict):
    topic_key: str
    r"""The key identifier of the topic"""
    idempotency_key: NotRequired[str]
    r"""A header for idempotency purposes"""


class TopicsControllerDeleteTopicRequest(BaseModel):
    topic_key: Annotated[
        str,
        pydantic.Field(alias="topicKey"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""The key identifier of the topic"""

    idempotency_key: Annotated[
        Optional[str],
        pydantic.Field(alias="idempotency-key"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""A header for idempotency purposes"""


class TopicsControllerDeleteTopicResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: DeleteTopicResponseDtoTypedDict


class TopicsControllerDeleteTopicResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: DeleteTopicResponseDto
