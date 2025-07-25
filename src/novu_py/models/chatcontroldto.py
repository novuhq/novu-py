"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from novu_py.types import BaseModel
from typing import Any, Dict, Optional
from typing_extensions import NotRequired, TypedDict


class ChatControlDtoTypedDict(TypedDict):
    skip: NotRequired[Dict[str, Any]]
    r"""JSONLogic filter conditions for conditionally skipping the step execution. Supports complex logical operations with AND, OR, and comparison operators. See https://jsonlogic.com/ for full typing reference."""
    body: NotRequired[str]
    r"""Content of the chat message."""


class ChatControlDto(BaseModel):
    skip: Optional[Dict[str, Any]] = None
    r"""JSONLogic filter conditions for conditionally skipping the step execution. Supports complex logical operations with AND, OR, and comparison operators. See https://jsonlogic.com/ for full typing reference."""

    body: Optional[str] = None
    r"""Content of the chat message."""
