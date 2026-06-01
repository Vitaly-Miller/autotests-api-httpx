"""
❌ Validation Error Schema
"""

from pydantic import BaseModel, Field
from typing import Any

#======================================================= Create ========================================================
class ErrorSchema(BaseModel):
    type: str
    loc: list[str]
    msg: str = Field
    input: Any
    ctx: dict[str, Any] | None = None

class ResponseErrorSchema(BaseModel):
    """
    Схема ошибки при создании сущности (User, File, Exercise, etc.)

    .
    """
    detail: list[ErrorSchema]

#------------------------------------------------------ Examples -------------------------------------------------------
# Create User error
create_user_empty_first_name = \
    {
      "detail": [
        {
          "type": "string_too_short",
          "loc": [
            "body",
            "firstName"
          ],
          "msg": "String should have at least 1 character",
          "input": "",
          "ctx": {
            "min_length": 1
          }
        }
      ]
    }

# Create File error
create_file_empty_filename = \
    {
      "detail": [
        {
          "type": "missing",
          "loc": [
              "body",
              "filename"
          ],
          "msg": "Field required",
          "input": None   # null
        }
      ]
    }


#========================================================= Get =========================================================
class NotFoundErrorSchema(BaseModel):
    """
    Схема ошибки при попытке получения несуществующей сущности (User, File, Exercise, etc.)

    .
    """
    detail: str

#------------------------------------------------------ Examples -------------------------------------------------------
get_file_by_incorrect_file_id = \
    {
      "detail": "File not found"
    }


#======================================================= Delete ========================================================
