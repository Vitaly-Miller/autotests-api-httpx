"""
Authentication Pydantic Schemas
"""
from pydantic import BaseModel, Field

#=================================================== REQUEST schema ====================================================
#-------------------------------------------------------- Login --------------------------------------------------------
class LoginRequestSchema(BaseModel):
    """
    Описание структуры запроса Аутентификации.
    login_payload = {}
    """
    email: str
    password: str

class AuthUserSchema(BaseModel):
    """
    Описание структуры пользователя для аутентификации.
    login_payload = {}
    """
    email: str
    password: str

#------------------------------------------------------- Refresh -------------------------------------------------------
class RefreshRequestSchema(BaseModel):
    """
    Описание структуры запроса для Обновления токена.
    """
    refresh_token: str = Field(alias='refreshToken')


#=================================================== RESPONSE schema ===================================================
#-------------------------------------------------------- Login --------------------------------------------------------
class TokenSchema(BaseModel):
    """
    Описание схемы получения Токена.
    """
    token_type: str = Field(alias='tokenType')
    access_token: str = Field(alias='accessToken')
    refresh_token: str = Field(alias='refreshToken')

class LoginResponseSchema(BaseModel):
    """
    Схемы ответа Аутентификации (login).
    """
    token: TokenSchema
#------------------------------------------------------- Refresh -------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------
