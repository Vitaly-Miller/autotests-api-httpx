"""
Authentication Pydantic Schemas
"""
from pydantic import BaseModel, Field

#=================================================== REQUEST schema ====================================================
#---------------------------------------------------- Create User ------------------------------------------------------
class CreateUserRequestSchema(BaseModel):
    """
    Схема User для создания нового пользователя
    (метод create_user_api)
    """
    email: str
    password: str
    last_name: str = Field(alias='lastName')
    first_name: str = Field(alias='firstName')
    middle_name: str = Field(alias='middleName')

#---------------------------------------------------- Update User -------------------=----------------------------------
class UpdateUserRequestSchema(BaseModel):
    """
    Схема User для обновления данных пользователя
    (метод update_user_api)
    """
    email: str | None
    last_name: str | None = Field(alias='lastName')
    first_name: str | None = Field(alias='firstName')
    middle_name: str | None = Field(alias='middleName')


#================================================== RESPONSE schema ====================================================
#---------------------------------------------------- Create User ------------------------------------------------------
class UserResponseSchema(BaseModel):
    """
    Схема ключа user из ответа Create User
    """
    id: str
    email: str
    last_name: str = Field(alias='lastName')
    first_name: str = Field(alias='firstName')
    middle_name: str = Field(alias='middleName')

class CreateUserResponseSchema(BaseModel):
    """
    Схема ответа Create User
    (метод create_user)
    """
    user: UserResponseSchema

#---------------------------------------------------- Get User Me ------------------------------------------------------
class UserMeResponseSchema(BaseModel):
    """
    Схема ключа user из ответа Get User Mе
    """
    id: str
    email: str
    last_name: str = Field(alias='lastName')
    first_name: str = Field(alias='firstName')
    middle_name: str = Field(alias='middleName')

class GetUserMeResponseSchema(BaseModel):
    """
    Схема ответа Get User Me
    (метод get_user_me_api)
    """
    user: UserMeResponseSchema
#-----------------------------------------------------------------------------------------------------------------------
