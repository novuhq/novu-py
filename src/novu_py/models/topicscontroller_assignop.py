"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .addsubscribersrequestdto import (
    AddSubscribersRequestDto,
    AddSubscribersRequestDtoTypedDict,
)
from .assignsubscribertotopicdto import (
    AssignSubscriberToTopicDto,
    AssignSubscriberToTopicDtoTypedDict,
)
from novu_py.types import BaseModel
from novu_py.utils import FieldMetadata, PathParamMetadata, RequestMetadata
import pydantic
from typing import Dict, List
from typing_extensions import Annotated, TypedDict


class TopicsControllerAssignRequestTypedDict(TypedDict):
    topic_key: str
    r"""The topic key"""
    add_subscribers_request_dto: AddSubscribersRequestDtoTypedDict


class TopicsControllerAssignRequest(BaseModel):
    topic_key: Annotated[
        str,
        pydantic.Field(alias="topicKey"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""The topic key"""

    add_subscribers_request_dto: Annotated[
        AddSubscribersRequestDto,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]


class TopicsControllerAssignResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: AssignSubscriberToTopicDtoTypedDict


class TopicsControllerAssignResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: AssignSubscriberToTopicDto
