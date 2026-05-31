"""
❌ Validation Error Schema
"""
"""
Единая схема API-ошибок для всех Endpoints
"""
from pydantic import BaseModel, Field
from typing import Any

#=======================================================================================================================
class ErrorSchema(BaseModel):
    type: str
    loc: list[str]
    msg: str = Field
    input: Any
    ctx: dict[str, Any] | None = None

class ResponseErrorSchema(BaseModel):
    detail: list[ErrorSchema]

#-----------------------------------------------------------------------------------------------------------------------



#====================================================== Examples =======================================================
# Example Response Body for create user with empty 'first_name'
create_user_empty_first_name = {
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
#-----------------------------------------------------------------------------------------------------------------------
# Example Response Body for create user with empty 'filename'
create_file_empty_filename = {
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
#-----------------------------------------------------------------------------------------------------------------------
