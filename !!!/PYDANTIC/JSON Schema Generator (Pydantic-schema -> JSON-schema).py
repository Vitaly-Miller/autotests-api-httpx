"""
Генерация JSON Schema из Pydantic Schema
"""

from pydantic import BaseModel, Field

#=======================================================================================================================
#--------------------------------------------------- RESPONSE schema ---------------------------------------------------
class TokenSchema(BaseModel):
    """
    Схема ключа "token": {}
    """
    token_type: str = Field(alias='tokenType')
    access_token: str = Field(alias='accessToken')
    refresh_token: str = Field(alias='refreshToken')

#------------------------------------------------ Генерация JSON Schema ------------------------------------------------
# Pydantic Schema -> JSON Schema
json_schema = TokenSchema.model_json_schema()


#------------------------------------------------------- Output --------------------------------------------------------
print(json_schema)  # {'description': 'Схема ключа "token": {}', 'properties': {'tokenType': {'title': 'Tokentype', 'type': 'string'}, 'accessToken': {'title': 'Accesstoken', 'type': 'string'}, 'refreshToken': {'title': 'Refreshtoken', 'type': 'string'}}, 'required': ['tokenType', 'accessToken', 'refreshToken'], 'title': 'TokenSchema', 'type': 'object'}
""" ✨
{
    'description': 'Схема ключа "token": {}',
    'properties': {
        'accessToken': {'title': 'Accesstoken', 'type': 'string'},
        'refreshToken': {'title': 'Refreshtoken', 'type': 'string'},
        'tokenType': {'title': 'Tokentype', 'type': 'string'}
    },
    'required': ['tokenType', 'accessToken', 'refreshToken'],
    'title': 'TokenSchema', 'type': 'object'
}
"""
