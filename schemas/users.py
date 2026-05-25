"""
Authentication Pydantic Schema
"""
from pydantic import BaseModel, Field, EmailStr
from schemas.auth import AuthUserSchema
from tools.data_generator import fake

"""================================================ ⬆︎REQUEST Schema ================================================"""
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

#----------------------------------------------------- Update User -----------------------------------------------------
class UpdateUserRequestSchema(BaseModel):
    """
    Схема payload для запроса на обновления данных пользователя

    .
    """
    email: EmailStr | None = Field(default_factory=fake.email)
    last_name: str | None = Field(alias='lastName', default_factory=fake.last_name)
    first_name: str | None = Field(alias='firstName', default_factory=fake.first_name)
    middle_name: str | None = Field(alias='middleName', default_factory=fake.middle_name)



"""=============================================== ⬇︎RESPONSE Schema ================================================"""
#------------------------------------------------------ Base -----------------------------------------------------------
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

class UserResponseSchema(BaseModel):
    """
    Базовая схема API ответа при работе с пользователями

    .
    """
    user: UserSchema

#---------------------------------------------------- Create User ------------------------------------------------------
class CreateUserResponseSchema(UserResponseSchema):
    """
    Схема ответа при создании нового пользователя

    Наследуется: UserResponseSchema
    """
    pass
#------------------------------------------------------ Get User -------------------------------------------------------
class GetUserResponseSchema(UserResponseSchema):
    """
    Схема ответа при получении данных пользователя по User ID

    Наследуется: UserResponseSchema
    """
    pass
#----------------------------------------------------- Get User Me -----------------------------------------------------
class GetUserMeResponseSchema(UserResponseSchema):
    """
    Схема ответа при получении данных ТЕКУЩЕГО пользователя

    Наследуется: UserResponseSchema
    """
    pass
#----------------------------------------------------- Update User -----------------------------------------------------
class UserUpdateResponseSchema(UserResponseSchema):
    """
    Схема ответа при обновлении данных пользователя

    Наследуется: UserResponseSchema
    """
    pass



"""===================================== User Full Schema (⬆︎Request + ⬇Response) ✨================================="""
class UserFullSchema(BaseModel):
    """
    Объединенная схема с данными о пользователе из Request + Response в формате Pydantic-model

    Request  -> Данные о пользователе (первичные)
    Response -> Данные о пользователе (первичные, КРОМЕ password) + User ID и еще...
    """
    request: CreateUserRequestSchema
    response: CreateUserResponseSchema
    #------------------------------------- Методы для прямого доступа к данным -----------------------------------------
    # Email
    @property
    def email(self) -> str:
        return self.request.email

    # Password
    @property
    def password(self) -> str:
        return self.request.password

    # User ID
    @property
    def user_id(self) -> str:
        return self.response.user.id

   # User Auth Data
    @property
    def auth_data(self) -> AuthUserSchema:
        return AuthUserSchema(
            email=self.email,                # Email     ┐
            password=self.password           # Password  ┘
        )

#-----------------------------------------------------------------------------------------------------------------------
