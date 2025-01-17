"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from novu_py.types import BaseModel
from typing import Any, Dict, Optional
from typing_extensions import NotRequired, TypedDict


class WorkflowToStepControlValuesDtoTypedDict(TypedDict):
    steps: NotRequired[Dict[str, Dict[str, Any]]]
    r"""A mapping of step IDs to their corresponding data."""


class WorkflowToStepControlValuesDto(BaseModel):
    steps: Optional[Dict[str, Dict[str, Any]]] = None
    r"""A mapping of step IDs to their corresponding data."""
