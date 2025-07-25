"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .environmentresponsedto import (
    EnvironmentResponseDto,
    EnvironmentResponseDtoTypedDict,
)
from .updateenvironmentrequestdto import (
    UpdateEnvironmentRequestDto,
    UpdateEnvironmentRequestDtoTypedDict,
)
from novu_py.types import BaseModel
from novu_py.utils import (
    FieldMetadata,
    HeaderMetadata,
    PathParamMetadata,
    RequestMetadata,
)
import pydantic
from typing import Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class EnvironmentsControllerV1UpdateMyEnvironmentRequestTypedDict(TypedDict):
    environment_id: str
    r"""The unique identifier of the environment"""
    update_environment_request_dto: UpdateEnvironmentRequestDtoTypedDict
    idempotency_key: NotRequired[str]
    r"""A header for idempotency purposes"""


class EnvironmentsControllerV1UpdateMyEnvironmentRequest(BaseModel):
    environment_id: Annotated[
        str,
        pydantic.Field(alias="environmentId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""The unique identifier of the environment"""

    update_environment_request_dto: Annotated[
        UpdateEnvironmentRequestDto,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    idempotency_key: Annotated[
        Optional[str],
        pydantic.Field(alias="idempotency-key"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""A header for idempotency purposes"""


class EnvironmentsControllerV1UpdateMyEnvironmentResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: EnvironmentResponseDtoTypedDict


class EnvironmentsControllerV1UpdateMyEnvironmentResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: EnvironmentResponseDto
