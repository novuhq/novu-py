"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .failedassignmentsdto import FailedAssignmentsDto, FailedAssignmentsDtoTypedDict
from novu_py.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class AssignSubscriberToTopicDtoTypedDict(TypedDict):
    succeeded: List[str]
    r"""List of successfully assigned subscriber IDs"""
    failed: NotRequired[FailedAssignmentsDtoTypedDict]
    r"""Details about failed assignments"""


class AssignSubscriberToTopicDto(BaseModel):
    succeeded: List[str]
    r"""List of successfully assigned subscriber IDs"""

    failed: Optional[FailedAssignmentsDto] = None
    r"""Details about failed assignments"""
