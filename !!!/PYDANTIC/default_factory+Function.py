"""
Pydantic Default Factory ✨+ ФУНКЦИИ
Генерация тестовых данных (ID, token, email, name)
"""
from pydantic import BaseModel, Field, HttpUrl, EmailStr
from uuid import uuid4
import secrets
from faker import Faker

fake = Faker()   # 👈 генератор данных


#=======================================================================================================================
# default_factory    — вызывается при каждом создании объекта
# Faker              — реалистичные данные (email, name)
# uuid               — уникальные значения ID
# secrets.token_hex  — уникальные значения Token
#============================================= Generator functions =====================================================
def generate_id() -> str:
    return str(uuid4())

def generate_token() -> str:
    return secrets.token_hex(8) # короткий

def generate_email() -> str:
    return fake.email()

def generate_name() -> str:
    return fake.name()

#==================================================== Schema ===========================================================

class UserSchema(BaseModel):
    id: str = Field(default_factory=generate_id)
    name: str = Field(default_factory=generate_name)
    email: EmailStr = Field(default_factory=generate_email)
    token: str = Field(default_factory=generate_token)


#---------------------------------------------------- Usage ------------------------------------------------------------
user_1 = UserSchema()
user_2 = UserSchema()

#---------------------------------------------------- Output -----------------------------------------------------------
print('--------- MODEL --------')
print(user_1)                         # id='461f89ee-e25f-453e-9584-e6c18aae19c9' name='William Warren' email='pallen@example.net' token='54b58ff7df3987fd'
print(user_2)                         # id='51c518ab-a1da-4fc8-924c-f3c882986ead' name='Sara Baker' email='ericwilliams@example.org' token='f2842a202d920bcb'
print()
print('----- PYTHON DICT ------')
print(user_1.model_dump())            # {'id': '461f89ee-e25f-453e-9584-e6c18aae19c9', 'name': 'William Warren', 'email': 'pallen@example.net', 'token': '54b58ff7df3987fd'}
print()
print('----- JSON STRING ------')
print(user_1.model_dump_json())       # {"id":"461f89ee-e25f-453e-9584-e6c18aae19c9","name":"William Warren","email":"pallen@example.net","token":"54b58ff7df3987fd"}



#=======================================================================================================================
# Examples
print()
print('--------- uuid ---------')
print(f'uuid.uuid4()           | {uuid4()}')          # ac5b1b2b-1117-433c-8213-bc6e23f56946
print(f'uuid.uuid4().hex       | {uuid4().hex}')      # 674fe8e89bf84654850ac5b18ab966e5
print(f'uuid.uuid4().hex[:8]   | {uuid4().hex[:8]}')  # d8543bf0

print('-------- secrets -------')
print(f'secrets.token_hex()    | {secrets.token_hex()}')   # 69dc149046370b84ec50d79e8ec031b30c886a24d73c7a4494eabc9d955aaa48
print(f'secrets.token_hex(8)   | {secrets.token_hex(8)}')  # a5528e9c48a77aea
