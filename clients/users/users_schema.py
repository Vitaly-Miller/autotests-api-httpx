"""
Authentication Schema
"""
from pydantic import BaseModel, Field

#=======================================================================================================================
#----------------------------------------------- REQUEST Pydantic Schemas ----------------------------------------------
# Create User Payload
class CreateUserRequestSchema(BaseModel):
    email: str
    password: str
    first_name: str = Field(alias='firstName')
    middle_name: str = Field(alias='middleName')
    last_name: str = Field(alias='lastName')


# Update User Payload
class UpdateUserRequestSchema(BaseModel):
    email: str | None
    first_name: str | None = Field(alias='firstName')
    middle_name: str | None = Field(alias='middleName')
    last_name: str | None = Field(alias='lastName')


#---------------------------------------------- RESPONSE Pydantic Schemas ----------------------------------------------
class UserMeResponseSchema(BaseModel):
    """
    Схема словаря user из ответа Get User Mе
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
#---------------------------------------------------
