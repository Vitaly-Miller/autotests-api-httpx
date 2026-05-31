"""
 ❌ Error Schema
"""
"""
Единая схема API-ошибок для всех Endpoints
"""
from pydantic import BaseModel, Field
from typing import Any

#=======================================================================================================================
class DetailErrorSchema(BaseModel):
    type: str
    location: list[str] = Field(alias='loc')
    message: str = Field(alias='msg')
    input: Any
    context: dict[str, Any] = Field(alias='ctx')

class ErrorSchema(BaseModel):
    detail: list[DetailErrorSchema]

#-----------------------------------------------------------------------------------------------------------------------
example = {
  "detail": [
    {
      "type": "string_too_short",
      "loc": [
        "body",
        "middleName"
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
