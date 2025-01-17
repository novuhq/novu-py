"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from novu_py import utils
from novu_py.types import BaseModel
import pydantic
from typing import Any, Dict, Optional
from typing_extensions import Annotated


class ErrorDtoData(BaseModel):
    status_code: Annotated[float, pydantic.Field(alias="statusCode")]
    r"""HTTP status code of the error response."""

    timestamp: str
    r"""Timestamp of when the error occurred."""

    path: str
    r"""The path where the error occurred."""

    message: str
    r"""A detailed error message."""

    ctx: Optional[Dict[str, Any]] = None
    r"""Optional context object for additional error details."""

    error_id: Annotated[Optional[str], pydantic.Field(alias="errorId")] = None
    r"""Optional unique identifier for the error, useful for tracking using Sentry and
    New Relic, only available for 500.
    """


class ErrorDto(Exception):
    data: ErrorDtoData

    def __init__(self, data: ErrorDtoData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, ErrorDtoData)
