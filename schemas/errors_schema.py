"""
Validation Error ❌ (Pydantic Schema)
"""

from pydantic import BaseModel
from typing import Any

#======================================================== Main =========================================================
class ErrorSchema(BaseModel):
    type: str
    loc: list[str]
    msg: str
    input: Any
    ctx: dict[str, Any] | None = None

class ErrorResponseSchema(BaseModel):
    """
    Схема ошибки при создании сущности (User, File, Exercise, etc.)

    .
    """
    detail: list[ErrorSchema]

# Examples
"""
---- Create User with empty 'first_name' ----
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

--- Create File with empty 'filename' ----

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
    

---- Get File with incorrect File ID ----
{
  "detail": [
    {
      "type": "uuid_parsing",
      "loc": [
        "path",
        "file_id"
      ],
      "msg": "Input should be a valid UUID, invalid character: expected an optional prefix of `urn:uuid:` followed by [0-9a-fA-F-], found `i` at 1",
      "input": "incorrect-file-id",
      "ctx": {
        "error": "invalid character: expected an optional prefix of `urn:uuid:` followed by [0-9a-fA-F-], found `i` at 1"
      }
    }
  ]
}
"""


#---------------------------------------------------- NON-exist entity -------------------------------------------------
class NotFoundErrorResponseSchema(BaseModel):
    """
    Схема ошибки при попытке получения несуществующей сущности

   - User
   - File
   - Course
   - Exercise
    """
    detail: str

#-----------------------------------------------------------------------------------------------------------------------
