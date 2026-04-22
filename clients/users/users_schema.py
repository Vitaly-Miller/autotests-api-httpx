"""
Authentication Schema
"""
from pydantic import BaseModel, Field

#=======================================================================================================================
#-------------------------------------------------- Pydantic Schemas ---------------------------------------------------
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


#-----------------------------------------------------------------------------------------------------------------------
