"""
Authentication (Pydantic Schema)
"""
from pydantic import BaseModel, Field
from tools.data_generator import fake

#================================================== ⬆︎REQUEST schemas ==================================================
#------------------------------------------------------Auth/Login ------------------------------------------------------
class AuthDataSchema(BaseModel, frozen=True):
    email: str = Field(default_factory=fake.email)
    password: str = Field(default_factory=fake.password)


#------------------------------------------------------- Refresh -------------------------------------------------------
class RefreshRequestSchema(BaseModel):
    refresh_token: str = Field(alias='refreshToken', default_factory=fake.uuid4)



#================================================= ⬇︎RESPONSE schemas ==================================================
#----------------------------------------------------- "token": {} -----------------------------------------------------
class TokenSchema(BaseModel):
    token_type: str = Field(alias='tokenType')
    access_token: str = Field(alias='accessToken')
    refresh_token: str = Field(alias='refreshToken')

#------------------------------------------------------ Auth/Login -----------------------------------------------------
class AuthResponseSchema(BaseModel):
    token: TokenSchema


#=======================================================================================================================
