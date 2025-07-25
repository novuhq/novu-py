"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from novu_py.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
import pydantic
from pydantic import model_serializer
from typing import Any, Dict
from typing_extensions import Annotated, NotRequired, TypedDict


class PatchSubscriberRequestDtoTypedDict(TypedDict):
    first_name: NotRequired[Nullable[str]]
    r"""First name of the subscriber"""
    last_name: NotRequired[Nullable[str]]
    r"""Last name of the subscriber"""
    email: NotRequired[Nullable[str]]
    r"""Email address of the subscriber"""
    phone: NotRequired[Nullable[str]]
    r"""Phone number of the subscriber"""
    avatar: NotRequired[Nullable[str]]
    r"""Avatar URL or identifier"""
    timezone: NotRequired[Nullable[str]]
    r"""Timezone of the subscriber"""
    locale: NotRequired[Nullable[str]]
    r"""Locale of the subscriber"""
    data: NotRequired[Nullable[Dict[str, Any]]]
    r"""Additional custom data for the subscriber"""


class PatchSubscriberRequestDto(BaseModel):
    first_name: Annotated[OptionalNullable[str], pydantic.Field(alias="firstName")] = (
        UNSET
    )
    r"""First name of the subscriber"""

    last_name: Annotated[OptionalNullable[str], pydantic.Field(alias="lastName")] = (
        UNSET
    )
    r"""Last name of the subscriber"""

    email: OptionalNullable[str] = UNSET
    r"""Email address of the subscriber"""

    phone: OptionalNullable[str] = UNSET
    r"""Phone number of the subscriber"""

    avatar: OptionalNullable[str] = UNSET
    r"""Avatar URL or identifier"""

    timezone: OptionalNullable[str] = UNSET
    r"""Timezone of the subscriber"""

    locale: OptionalNullable[str] = UNSET
    r"""Locale of the subscriber"""

    data: OptionalNullable[Dict[str, Any]] = UNSET
    r"""Additional custom data for the subscriber"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "firstName",
            "lastName",
            "email",
            "phone",
            "avatar",
            "timezone",
            "locale",
            "data",
        ]
        nullable_fields = [
            "firstName",
            "lastName",
            "email",
            "phone",
            "avatar",
            "timezone",
            "locale",
            "data",
        ]
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
