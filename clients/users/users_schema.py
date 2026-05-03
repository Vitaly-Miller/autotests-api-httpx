"""
Authentication Pydantic Schema
"""
from pydantic import BaseModel, Field, EmailStr
from tools.data_generator import fake

#================================================== ⬆︎REQUEST Schema ===================================================
#----------------------------------------------------- Create User -----------------------------------------------------
class CreateUserRequestSchema(BaseModel):
    """
    Схема payload для запроса на создание нового пользователя

    .
    """
    email: EmailStr = Field(default_factory=fake.email)
    password: str = Field(default_factory=fake.password)
    last_name: str = Field(alias='lastName', default_factory=fake.last_name)
    first_name: str = Field(alias='firstName', default_factory=fake.first_name)
    middle_name: str = Field(alias='middleName', default_factory=fake.middle_name)

#----------------------------------------------------- Update User -------------------=---------------------------------
class UpdateUserRequestSchema(BaseModel):
    """
    Схема payload для запроса на обновления данных пользователя

    .
    """
    email: EmailStr | None = Field(default_factory=fake.email)
    last_name: str | None = Field(alias='lastName', default_factory=fake.last_name)
    first_name: str | None = Field(alias='firstName', default_factory=fake.first_name)
    middle_name: str | None = Field(alias='middleName', default_factory=fake.middle_name)


#================================================= ⬇︎RESPONSE Schema ===================================================
#-------------------------------------------------------- BASE ---------------------------------------------------------
class UserSchema(BaseModel):
    """
    Базовая схема ключа "user": {}

    .
    """
    id: str
    email: EmailStr
    last_name: str = Field(alias='lastName')
    first_name: str = Field(alias='firstName')
    middle_name: str = Field(alias='middleName')

class BaseUserResponseSchema(BaseModel):
    """
    Базовая схема API ответа при работе с пользователями

    .
    """
    user: UserSchema

#---------------------------------------------------- Create User ------------------------------------------------------
class CreateUserResponseSchema(BaseUserResponseSchema):
    """
    Схема ответа при создании нового пользователя

    Наследуется: BaseUserResponseSchema
    """
    pass
#------------------------------------------------------ Get User -------------------------------------------------------
class GetUserResponseSchema(BaseUserResponseSchema):
    """
    Схема ответа при получении данных пользователя по User ID


    Наследуется: BaseUserResponseSchema
    """
    pass
#----------------------------------------------------- Get User Me -----------------------------------------------------
class GetUserMeResponseSchema(BaseUserResponseSchema):
    """
    Схема ответа при получении данных текущего пользователя

    Наследуется: BaseUserResponseSchema
    """
    pass
#-----------------------------------------------------------------------------------------------------------------------
