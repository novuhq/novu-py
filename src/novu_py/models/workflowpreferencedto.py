"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from novu_py.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class WorkflowPreferenceDtoTypedDict(TypedDict):
    enabled: NotRequired[bool]
    r"""A flag specifying if notification delivery is enabled for the workflow. If true, notification delivery is enabled by default for all channels. This setting can be overridden by the channel preferences."""
    read_only: NotRequired[bool]
    r"""A flag specifying if the preference is read-only. If true, the preference cannot be changed by the Subscriber."""


class WorkflowPreferenceDto(BaseModel):
    enabled: Optional[bool] = True
    r"""A flag specifying if notification delivery is enabled for the workflow. If true, notification delivery is enabled by default for all channels. This setting can be overridden by the channel preferences."""

    read_only: Annotated[Optional[bool], pydantic.Field(alias="readOnly")] = False
    r"""A flag specifying if the preference is read-only. If true, the preference cannot be changed by the Subscriber."""
