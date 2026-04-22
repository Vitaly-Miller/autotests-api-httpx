"""
Pydantic Default Factory ✨
Генерация тестовых данных (ID, token, email, name)
"""
from pydantic import BaseModel, Field, EmailStr
from uuid import uuid4
import secrets
from faker import Faker

fake = Faker()   # 👈 генератор данных


#=======================================================================================================================
# default_factory    — вызывается при каждом создании объекта
# Faker              — реалистичные данные (email, name)
# uuid               — уникальные значения ID
# secrets.token_hex  — уникальные значения Token
#================================================== Generators =========================================================

def generate_id() -> str:
    return str(uuid4())

def generate_token() -> str:
    return secrets.token_hex(8)

def generate_email() -> str:
    return fake.email()

def generate_name() -> str:
    return fake.name()

#==================================================== Schema ===========================================================

class UserSchema(BaseModel):
    id: str = Field(default_factory=generate_id)
    token: str = Field(default_factory=generate_token)
    email: EmailStr = Field(default_factory=generate_email)
    name: str = Field(default_factory=generate_name)

#==================================================== Usage ============================================================
user_1 = UserSchema()
user_2 = UserSchema()

#---------------------------------------------------- Output -----------------------------------------------------------
print('--------- MODEL --------')
print(user_1)                         # id='87de2420-8921-4b30-b9e9-4af1a6346510' token='8293848a6457f0f1' email='paige25@example.org' name='Jason Williams'
print(user_2)                         # id='6ce65c38-40b9-4dcc-ba3a-9f838ddacbab' token='f4cf0089455ce29e' email='carrkristopher@example.com' name='Amanda Wallace'
print()
print('----- PYTHON DICT ------')
print(user_1.model_dump())            # {'id': '87de2420-8921-4b30-b9e9-4af1a6346510', 'token': '8293848a6457f0f1', 'email': 'paige25@example.org', 'name': 'Jason Williams'}
print()
print('------ JSON DICT -------')
print(user_1.model_dump(mode='json')) # {'id': '87de2420-8921-4b30-b9e9-4af1a6346510', 'token': '8293848a6457f0f1', 'email': 'paige25@example.org', 'name': 'Jason Williams'}
print()
print('----- JSON STRING ------')
print(user_1.model_dump_json())       #{"id":"87de2420-8921-4b30-b9e9-4af1a6346510","token":"8293848a6457f0f1","email":"paige25@example.org","name":"Jason Williams"}
