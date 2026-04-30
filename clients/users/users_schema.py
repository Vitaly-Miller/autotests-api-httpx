"""
Authentication Pydantic Schemas
"""
from pydantic import BaseModel, Field, EmailStr

#=================================================== REQUEST schema ====================================================
#---------------------------------------------------- Create User ------------------------------------------------------
class CreateUserRequestSchema(BaseModel):
    """
    Схема payload для запроса на создание нового пользователя
    """
    email: EmailStr
    password: str
    last_name: str = Field(alias='lastName')
    first_name: str = Field(alias='firstName')
    middle_name: str = Field(alias='middleName')

#---------------------------------------------------- Update User -------------------=----------------------------------
class UpdateUserRequestSchema(BaseModel):
    """
    Схема payload для запроса на обновления данных пользователя
    """
    email: EmailStr | None
    last_name: str | None = Field(alias='lastName')
    first_name: str | None = Field(alias='firstName')
    middle_name: str | None = Field(alias='middleName')


#================================================== RESPONSE schema ====================================================
#-------------------------------------------------------- BASE ---------------------------------------------------------
class UserSchema(BaseModel):
    """
    Базовая схема ключа "user": {}
    """
    id: str
    email: EmailStr
    last_name: str = Field(alias='lastName')
    first_name: str = Field(alias='firstName')
    middle_name: str = Field(alias='middleName')

class BaseUserResponseSchema(BaseModel):
    """
    Базовая схема API ответа при работе с пользователями.
    """
    user: UserSchema

#---------------------------------------------------- Create User ------------------------------------------------------
class CreateUserResponseSchema(BaseUserResponseSchema):
    """
    Схема ответа при создании нового пользователя
    """  # Наследуется
    pass
#------------------------------------------------------ Get User -------------------------------------------------------
class GetUserResponseSchema(BaseUserResponseSchema):
    """
    Схема ответа при получении данных пользователя
    """  # Наследуется
    pass
#----------------------------------------------------- Get User Me -----------------------------------------------------
class GetUserMeResponseSchema(BaseUserResponseSchema):
    """
    Схема ответа при получении данных текущего пользователя
    """  # Наследуется
    pass
#-----------------------------------------------------------------------------------------------------------------------
