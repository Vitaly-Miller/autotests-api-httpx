"""
Errors assertions
"""
from typing import Type

import httpx
from pydantic import BaseModel

from schemas.error import ErrorSchema
from tools.assertions.base_assert import assert_equal

#=======================================================================================================================
def assert_error(actual: ErrorSchema, expected: ErrorSchema):
    ...

#-----------------------------------------------------------------------------------------------------------------------
