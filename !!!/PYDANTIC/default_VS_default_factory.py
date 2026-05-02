"""
default VS default_factory
"""
from pydantic import BaseModel, Field
from faker import Faker

fake = Faker()

#=======================================================================================================================
#------------------------------------------------------- default='' ----------------------------------------------------
class Schema1(BaseModel):
    name: str = Field(default='John Connor')       # Default value (статическое значение)

user_1 = Schema1()
user_2 = Schema1()

print(f'default="John Connor"   | {user_1}')       # name='John Connor' ┐
print(f'default="John Connor"   | {user_2}')       # name='John Connor' ┘

#--------------------------------------------------- default=fake.name -------------------------------------------------
class Schema(BaseModel):
    name: str = Field(default=fake.name)           # ❌без () -> Объект в паями

user_1 = Schema()
user_2 = Schema()

print(f'default=fake.name        | {user_1}')      # name=<bound method Provider.name of <faker.providers.person.en_US.Provider object at 0x108f6d550>>
print(f'default=fake.name        | {user_2}')      # name=<bound method Provider.name of <faker.providers.person.en_US.Provider object at 0x108f6d550>>


#-------------------------------------------------- default=fake.name() ------------------------------------------------
class Schema(BaseModel):
    name: str = Field(default=fake.name())         # () -> Генерация один значение за сессию

user_1 = Schema()
user_2 = Schema()

print(f'default=fake.name()       | {user_1}')     # name='Kirsten Morales' ┐
print(f'default=fake.name()       | {user_2}')     # name='Kirsten Morales' ┘


#----------------------------------------------- default_factory=fake.name ------------------------------------------------
class Schema(BaseModel):
    name: str = Field(default_factory=fake.name)   # _factory -> Генерирует новое значение при каждом создании экземпляра

user_1 = Schema()
user_2 = Schema()

print(f'default_factory=fake.name  | {user_1}')    # name='Drew Bass'
print(f'default_factory=fake.name  | {user_2}')    # name='Beth Owen'
#-----------------------------------------------------------------------------------------------------------------------
