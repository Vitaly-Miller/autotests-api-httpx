"""
Authentication Pydantic Schema
"""
from pydantic import BaseModel, Field, EmailStr
from schemas.auth import AuthDataSchema
from tools.data_generator import fake

"""================================================ ⬆︎REQUEST Schema ================================================"""
#----------------------------------------------------- Create User -----------------------------------------------------
class CreateUserRequestSchema(BaseModel):
    email: EmailStr = Field(default_factory=fake.email)  # ⚠️Возможно придется заменить на str. А то будут падать негативные тесты при валидации Email
    password: str = Field(default_factory=fake.password)
    last_name: str = Field(alias='lastName', default_factory=fake.last_name)
    first_name: str = Field(alias='firstName', default_factory=fake.first_name)
    middle_name: str = Field(alias='middleName', default_factory=fake.middle_name)

#------------------------------------------------------ Get User -------------------------------------------------------




#----------------------------------------------------- Update User -----------------------------------------------------
class UpdateUserRequestSchema(BaseModel):
    email: EmailStr | None = Field(default_factory=fake.email) # ⚠️Возможно придется заменить на str. А то будут падать негативные тесты при валидации Email
    last_name: str | None = Field(alias='lastName', default_factory=fake.last_name)
    first_name: str | None = Field(alias='firstName', default_factory=fake.first_name)
    middle_name: str | None = Field(alias='middleName', default_factory=fake.middle_name)


#-----------------------------------------------------------------------------------------------------------------------

"""=============================================== ⬇︎RESPONSE Schema ================================================"""
#---------------------------------------------------- Create User ------------------------------------------------------
class UserSchema(BaseModel):
    id: str
    email: EmailStr   # ⚠️Возможно придется заменить на str. А то будут падать негативные тесты при валидации Email
    last_name: str = Field(alias='lastName')
    first_name: str = Field(alias='firstName')
    middle_name: str = Field(alias='middleName')

class CreateUserResponseSchema(BaseModel):
    user: UserSchema


#------------------------------------------------------ Get User -------------------------------------------------------
class GetUserResponseSchema(BaseModel):
    user: UserSchema


#------------------------------------------------------- Get User ------------------------------------------------------



#----------------------------------------------------- Get User Me -----------------------------------------------------
class GetUserMeResponseSchema(BaseModel):
    user: UserSchema


#----------------------------------------------------- Update User -----------------------------------------------------
class UserUpdateResponseSchema(BaseModel):
    user: UserSchema


#-----------------------------------------------------------------------------------------------------------------------
"""====================================== Full Schema (⬆︎Request + ⬇Response) ✨====================================="""
class CreateUserSchema(BaseModel):
    request: CreateUserRequestSchema    # ┐
    response: CreateUserResponseSchema  # ┘

    # --- Методы прямого доступа к данным ---
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

    # User Auth Data (Email + Password)
    @property
    def auth_data(self) -> AuthDataSchema:
        return AuthDataSchema(
            email=self.email,       # Email     ┐
            password=self.password  # Password  ┘
        )

#-----------------------------------------------------------------------------------------------------------------------
