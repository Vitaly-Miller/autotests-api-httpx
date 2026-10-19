"""
Validation Error (Pydantic Schema)
"""
from pydantic import BaseModel
from typing import Any

#================================================== Main Error schema ==================================================
#---------------------------------------------------- "detail": {} -----------------------------------------------------
class ErrorSchema(BaseModel):
    type: str
    loc: list[str]
    msg: str
    input: Any
    ctx: dict[str, Any] | None = None

#-----------------------------------------------------------------------------------------------------------------------
class ErrorResponseSchema(BaseModel):
    """
    Error schema for entity creation (User, File, Exercise, etc.)

    .
    """
    detail: list[ErrorSchema]

#---------------------------------------------------- NON-exist entity -------------------------------------------------
class NotFoundErrorResponseSchema(BaseModel):
    """
    Response error schema for an attempt to get a non-existent entity

   - User
   - File
   - Course
   - Exercise
    """
    detail: str


#=======================================================================================================================
