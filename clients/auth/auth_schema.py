"""
Authentication Schema
"""

from pydantic import BaseModel, Field

#=======================================================================================================================
#-------------------------------------------------- Pydantic Schemas ---------------------------------------------------
class LoginRequestSchema(BaseModel):                  # login_payload = {}
    """
    Описание структуры запроса Аутентификации.
    """
    email: str
    password: str

class AuthUserSchema(BaseModel):                      # login_payload = {}
    """
    Описание структуры пользователя для аутентификации.
    """
    email: str
    password: str


class TokenSchema(BaseModel):
    """
    Описание структуры Токена.
    """
    token_type: str = Field(alias='tokenType')
    access_token: str = Field(alias='accessToken')
    refresh_token: str = Field(alias='refreshToken')

class LoginResponseSchema(BaseModel):
    """
    Описание схемы ответа Аутентификации.
    """
    token: TokenSchema

class RefreshRequestSchema(BaseModel):
    """
    Описание структуры запроса для Обновления токена.
    """
    refresh_token: str = Field(alias='refreshToken')

#-----------------------------------------------------------------------------------------------------------------------
