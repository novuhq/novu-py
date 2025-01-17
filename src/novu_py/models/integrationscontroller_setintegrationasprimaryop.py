"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .integrationresponsedto import (
    IntegrationResponseDto,
    IntegrationResponseDtoTypedDict,
)
from novu_py.types import BaseModel
from novu_py.utils import FieldMetadata, PathParamMetadata
import pydantic
from typing import Dict, List
from typing_extensions import Annotated, TypedDict


class IntegrationsControllerSetIntegrationAsPrimaryRequestTypedDict(TypedDict):
    integration_id: str


class IntegrationsControllerSetIntegrationAsPrimaryRequest(BaseModel):
    integration_id: Annotated[
        str,
        pydantic.Field(alias="integrationId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]


class IntegrationsControllerSetIntegrationAsPrimaryResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: IntegrationResponseDtoTypedDict


class IntegrationsControllerSetIntegrationAsPrimaryResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: IntegrationResponseDto
