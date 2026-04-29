"""
Pydantic Default Factory + labda ✨

Генерация динамических тестовых данных (ID, token...)
------------------------------------------------------------------------------------------------------------------------
   👉lamda: - используется для генерации значений для каждого экземпляра класса
БЕЗ lambda: - будет одно и то же значение для всех экземпляров


# default_factory    — вызывается при каждом создании объекта (экземпляра класса)
# lamda              — используется для генерации значений для каждого экземпляра класса
# Faker              — реалистичные данные (email, name)
# uuid               — уникальные значения ID
# secrets.token_hex  — уникальные значения Token
------------------------------------------------------------------------------------------------------------------------
"""
from pydantic import BaseModel, Field, EmailStr
from uuid import uuid4
import secrets
from faker import Faker

fake = Faker()   # 👈 генератор данных

#==================================================== Schema ===========================================================
class UserSchema(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))             # UUID (уникальный ID)
    name: str = Field(default_factory=fake.name)                      # Faker name
    email: EmailStr = Field(default_factory=fake.email)               # Faker email
    token: str = Field(default_factory=lambda: secrets.token_hex(8))  # token (короткий)


#---------------------------------------------------- Usage ------------------------------------------------------------
user_1 = UserSchema()
user_2 = UserSchema()

#---------------------------------------------------- Output -----------------------------------------------------------
# model_dump()            —> Python Dict           (могут быть UUID, datetime и т.д.)
# model_dump(mode='json') —> JSON-совместимый dict (для API payload)
# model_dump_json()       —> JSON строка           (raw body)
#-----------------------------------------------------------------------------------------------------------------------
print('--------- MODEL --------')
print(user_1)                         # id='461f89ee-e25f-453e-9584-e6c18aae19c9' name='William Warren' email='pallen@example.net' token='54b58ff7df3987fd'
print(user_2)                         # id='51c518ab-a1da-4fc8-924c-f3c882986ead' name='Sara Baker' email='ericwilliams@example.org' token='f2842a202d920bcb'
print()
print('----- PYTHON DICT ------')
print(user_1.model_dump())            # {'id': '461f89ee-e25f-453e-9584-e6c18aae19c9', 'name': 'William Warren', 'email': 'pallen@example.net', 'token': '54b58ff7df3987fd'}
print()
print('------ JSON DICT -------')
print(user_1.model_dump(mode='json')) # {'id': '461f89ee-e25f-453e-9584-e6c18aae19c9', 'name': 'William Warren', 'email': 'pallen@example.net', 'token': '54b58ff7df3987fd'}
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
