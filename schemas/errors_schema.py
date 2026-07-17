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
    Схема ошибки при создании сущности (User, File, Exercise, etc.)

    .
    """
    detail: list[ErrorSchema]

#---------------------------------------------------- NON-exist entity -------------------------------------------------
class NotFoundErrorResponseSchema(BaseModel):
    """
    Схема Response-ошибки при попытке получения несуществующей сущности

   - User
   - File
   - Course
   - Exercise
    """
    detail: str


#=======================================================================================================================
