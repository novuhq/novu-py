"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .subscriberresponsedto import SubscriberResponseDto, SubscriberResponseDtoTypedDict
from novu_py.types import BaseModel, Nullable, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List
from typing_extensions import TypedDict


class ListSubscribersResponseDtoTypedDict(TypedDict):
    data: List[SubscriberResponseDtoTypedDict]
    r"""List of returned Subscribers"""
    next: Nullable[str]
    r"""The cursor for the next page of results, or null if there are no more pages."""
    previous: Nullable[str]
    r"""The cursor for the previous page of results, or null if this is the first page."""


class ListSubscribersResponseDto(BaseModel):
    data: List[SubscriberResponseDto]
    r"""List of returned Subscribers"""

    next: Nullable[str]
    r"""The cursor for the next page of results, or null if there are no more pages."""

    previous: Nullable[str]
    r"""The cursor for the previous page of results, or null if this is the first page."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = ["next", "previous"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
