"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .bulkcreatesubscriberresponsedto import (
    BulkCreateSubscriberResponseDto,
    BulkCreateSubscriberResponseDtoTypedDict,
)
from .bulksubscribercreatedto import (
    BulkSubscriberCreateDto,
    BulkSubscriberCreateDtoTypedDict,
)
from novu_py.types import BaseModel
from novu_py.utils import FieldMetadata, HeaderMetadata, RequestMetadata
import pydantic
from typing import Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class SubscribersControllerBulkCreateSubscribersRequestTypedDict(TypedDict):
    bulk_subscriber_create_dto: BulkSubscriberCreateDtoTypedDict
    idempotency_key: NotRequired[str]
    r"""A header for idempotency purposes"""


class SubscribersControllerBulkCreateSubscribersRequest(BaseModel):
    bulk_subscriber_create_dto: Annotated[
        BulkSubscriberCreateDto,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    idempotency_key: Annotated[
        Optional[str],
        pydantic.Field(alias="idempotency-key"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""A header for idempotency purposes"""


class SubscribersControllerBulkCreateSubscribersResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: BulkCreateSubscriberResponseDtoTypedDict


class SubscribersControllerBulkCreateSubscribersResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: BulkCreateSubscriberResponseDto
