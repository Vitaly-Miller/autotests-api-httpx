"""
Authentication Pydantic Schemas
"""
from pydantic import BaseModel, Field

#=================================================== REQUEST schema ====================================================
#------------------------------------------------------Auth/Login --------------------------------------------------------
class LoginRequestSchema(BaseModel):
    """
    Схема запроса на аутентификацию пользователя.
    """
    email: str
    password: str

class AuthUserSchema(BaseModel):
    """
    Схема запроса на Log in пользователя.
    """
    email: str
    password: str

#------------------------------------------------------- Refresh -------------------------------------------------------
class RefreshRequestSchema(BaseModel):
    """
    Схема запроса на обновления токена.
    """
    refresh_token: str = Field(alias='refreshToken')


#=================================================== RESPONSE schema ===================================================
#------------------------------------------------------ Auth/Login --------------------------------------------------------
class TokenSchema(BaseModel):
    """
    Схема ключа "token": {}
    """
    token_type: str = Field(alias='tokenType')
    access_token: str = Field(alias='accessToken')
    refresh_token: str = Field(alias='refreshToken')

class LoginResponseSchema(BaseModel):
    """
    Схемы ответа при Аутентификации/Login.
    """
    token: TokenSchema
#------------------------------------------------------- Refresh -------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------
