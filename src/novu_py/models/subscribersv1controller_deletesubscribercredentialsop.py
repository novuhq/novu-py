"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from novu_py.types import BaseModel
from novu_py.utils import FieldMetadata, HeaderMetadata, PathParamMetadata
import pydantic
from typing import Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class SubscribersV1ControllerDeleteSubscriberCredentialsRequestTypedDict(TypedDict):
    subscriber_id: str
    provider_id: str
    idempotency_key: NotRequired[str]
    r"""A header for idempotency purposes"""


class SubscribersV1ControllerDeleteSubscriberCredentialsRequest(BaseModel):
    subscriber_id: Annotated[
        str,
        pydantic.Field(alias="subscriberId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]

    provider_id: Annotated[
        str,
        pydantic.Field(alias="providerId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]

    idempotency_key: Annotated[
        Optional[str],
        pydantic.Field(alias="idempotency-key"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""A header for idempotency purposes"""


class SubscribersV1ControllerDeleteSubscriberCredentialsResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]


class SubscribersV1ControllerDeleteSubscriberCredentialsResponse(BaseModel):
    headers: Dict[str, List[str]]
