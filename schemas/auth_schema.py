"""
Authentication (Pydantic Schema)
"""
from pydantic import BaseModel, Field
from tools.data_generator import fake

"""================================================ ⬆︎REQUEST Schema ================================================"""
#------------------------------------------------------Auth/Login ------------------------------------------------------
class AuthDataSchema(BaseModel, frozen=True):       # ✨← frozen делает модель иммутабельной и хэшируемой для lru_cache
    email: str = Field(default_factory=fake.email)        # ⚠️ Default fake.value for NEGATIVE test ONLY
    password: str = Field(default_factory=fake.password)  # ⚠️ Default fake.value for NEGATIVE test ONLY


#------------------------------------------------------- Refresh -------------------------------------------------------
class RefreshRequestSchema(BaseModel):
    refresh_token: str = Field(alias='refreshToken', default_factory=fake.uuid4) # ⚠️ Default fake.value for NEGATIVE test ONLY


#-----------------------------------------------------------------------------------------------------------------------


"""================================================ ⬇︎RESPONSE schema ==============================================="""
#----------------------------------------------------- "token": {} -----------------------------------------------------
class TokenSchema(BaseModel):
    token_type: str = Field(alias='tokenType')
    access_token: str = Field(alias='accessToken')
    refresh_token: str = Field(alias='refreshToken')

#------------------------------------------------------ Auth/Login -----------------------------------------------------
class AuthResponseSchema(BaseModel):
    token: TokenSchema


#------------------------------------------------------- Refresh -------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------------------
