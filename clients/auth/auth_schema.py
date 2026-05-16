"""
Authentication Pydantic Schema
"""
from pydantic import BaseModel, Field
from tools.data_generator import fake

"""================================================ ⬆︎REQUEST Schema ================================================"""
#------------------------------------------------------Auth/Login ------------------------------------------------------
class AuthUserSchema(BaseModel):
    """
    Схема запроса на Authentication (Auth) пользователя

    ⚠️Default fake.value for NEGATIVE test ONLY
    """
    email: str = Field(default_factory=fake.email)
    password: str = Field(default_factory=fake.password)

class LoginRequestSchema(BaseModel):
    """
    Схема запроса на Log in пользователя

    ⚠️Default fake.value for NEGATIVE test ONLY
    """
    email: str = Field(default_factory=fake.email)
    password: str = Field(default_factory=fake.password)


#------------------------------------------------------- Refresh -------------------------------------------------------
class RefreshRequestSchema(BaseModel):
    """
    Схема запроса на обновления токена

    ⚠️Default fake.value for NEGATIVE test ONLY
    """
    refresh_token: str = Field(alias='refreshToken', default_factory=fake.uuid4)


"""================================================ ⬇︎RESPONSE schema ==============================================="""
#------------------------------------------------------ Auth/Login -----------------------------------------------------
class TokenSchema(BaseModel):
    """
    Схема ключа "token": {}

    .
    """
    token_type: str = Field(alias='tokenType')
    access_token: str = Field(alias='accessToken')
    refresh_token: str = Field(alias='refreshToken')

class AuthUserResponseSchema(BaseModel):
    """
    Схема ответа при Аутентификации/Login

    .
    """
    token: TokenSchema

class LoginResponseSchema(BaseModel):
    """
    Схема ответа при Аутентификации/Login

    .
    """
    token: TokenSchema

#------------------------------------------------------- Refresh -------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------------------
