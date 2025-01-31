"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .builderfieldtypeenum import BuilderFieldTypeEnum
from .fieldfilterpartdto import FieldFilterPartDto, FieldFilterPartDtoTypedDict
from enum import Enum
from novu_py.types import BaseModel
import pydantic
from typing import List
from typing_extensions import Annotated, TypedDict


class Value(str, Enum):
    AND = "AND"
    OR = "OR"


class StepFilterDtoTypedDict(TypedDict):
    is_negated: bool
    type: BuilderFieldTypeEnum
    value: Value
    children: List[FieldFilterPartDtoTypedDict]


class StepFilterDto(BaseModel):
    is_negated: Annotated[bool, pydantic.Field(alias="isNegated")]

    type: BuilderFieldTypeEnum

    value: Value

    children: List[FieldFilterPartDto]
