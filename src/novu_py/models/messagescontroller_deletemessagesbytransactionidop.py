"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from novu_py.types import BaseModel
from novu_py.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata
import pydantic
from typing import Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class QueryParamChannel(str, Enum):
    r"""The channel of the message to be deleted"""

    IN_APP = "in_app"
    EMAIL = "email"
    SMS = "sms"
    CHAT = "chat"
    PUSH = "push"


class MessagesControllerDeleteMessagesByTransactionIDRequestTypedDict(TypedDict):
    transaction_id: str
    channel: NotRequired[QueryParamChannel]
    r"""The channel of the message to be deleted"""


class MessagesControllerDeleteMessagesByTransactionIDRequest(BaseModel):
    transaction_id: Annotated[
        str,
        pydantic.Field(alias="transactionId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]

    channel: Annotated[
        Optional[QueryParamChannel],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The channel of the message to be deleted"""


class MessagesControllerDeleteMessagesByTransactionIDResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]


class MessagesControllerDeleteMessagesByTransactionIDResponse(BaseModel):
    headers: Dict[str, List[str]]
