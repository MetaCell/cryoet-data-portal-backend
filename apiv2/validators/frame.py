"""
Pydantic validator for Frame

Auto-generated by running 'make codegen'. Do not edit.
Make changes to the template codegen/templates/validators/class_name.py.j2 instead.
"""

# ruff: noqa: E501 Line too long


import uuid

from pydantic import BaseModel, ConfigDict, Field, StringConstraints
from typing_extensions import Annotated


class FrameCreateInputValidator(BaseModel):
    # Pydantic stuff
    model_config = ConfigDict(from_attributes=True)
    deposition_id: Annotated[uuid.UUID | None, Field()]
    run_id: Annotated[uuid.UUID | None, Field()]
    raw_angle: Annotated[
        float,
        Field(
            ge=-90,
            le=90,
        ),
    ]
    acquisition_order: Annotated[int | None, Field()]
    dose: Annotated[float, Field()]
    is_gain_corrected: Annotated[bool | None, Field()]
    s3_prefix: Annotated[
        str,
        StringConstraints(
            strip_whitespace=True,
        ),
    ]
    https_prefix: Annotated[
        str,
        StringConstraints(
            strip_whitespace=True,
        ),
    ]
    id: Annotated[int, Field()]


class FrameUpdateInputValidator(BaseModel):
    # Pydantic stuff
    model_config = ConfigDict(from_attributes=True)
    deposition_id: Annotated[uuid.UUID | None, Field()]
    run_id: Annotated[uuid.UUID | None, Field()]
    raw_angle: Annotated[
        float | None,
        Field(
            ge=-90,
            le=90,
        ),
    ]
    acquisition_order: Annotated[int | None, Field()]
    dose: Annotated[float | None, Field()]
    is_gain_corrected: Annotated[bool | None, Field()]
    s3_prefix: Annotated[
        str | None,
        StringConstraints(
            strip_whitespace=True,
        ),
    ]
    https_prefix: Annotated[
        str | None,
        StringConstraints(
            strip_whitespace=True,
        ),
    ]
    id: Annotated[int | None, Field()]
