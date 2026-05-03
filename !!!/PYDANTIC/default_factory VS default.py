"""
default_factory + lambda
"""
from pydantic import BaseModel, Field
from faker import Faker

fake = Faker()

#====================================================== default= =======================================================
#--------------------------------------------------- 'static value' ----------------------------------------------------
class Schema(BaseModel):
    id: str = Field(default='ID-123')          # Default value = 'статическое_значение' для ВСЕХ экземпляров

id_1 = Schema()
id_2 = Schema()

print(f'default="ID-123"      | {id_1}')       # id='ID-123' ┐
print(f'default="ID-123"      | {id_2}')       # id='ID-123' ┘

#-------------------------------------------------- ❌fake.numerify ----------------------------------------------------
class Schema(BaseModel):
    id: str = Field(default=fake.numerify)            # без () -> Объект в паями

id_1 = Schema()
id_2 = Schema()

print(f'default=fake.numerify  | {id_1}')             # id=<bound method BaseProvider.numerify of <faker.providers.user_agent.Provider object at 0x108c8dd30>>
print(f'default=fake.numerify  | {id_2}')             # id=<bound method BaseProvider.numerify of <faker.providers.user_agent.Provider object at 0x108c8dd30>>


#-------------------------------------------------- fake.numerify() ----------------------------------------------------
class Schema(BaseModel):
    id: str = Field(default=fake.numerify())          # () -> ОДНА генерация за сессию для ВСЕХ экземпляров

id_1 = Schema()
id_2 = Schema()

print(f'default=fake.fake.numerify()    | {id_1}')     # id='177' ┐
print(f'default=fake.fake.numerify()    | {id_2}')     # id='177' ┘



#=================================================== default_factory= ==================================================
#---------------------------------------------------- ✅fake.numerify --------------------------------------------------
class Schema(BaseModel):
    id: str = Field(default_factory=fake.numerify)     # Генерация (БЕЗ кастомизации) для КАЖДОГО экземпляра

id_1 = Schema()
id_2 = Schema()

print(f'default_factory=fake.numerify  | {id_1}')      # id='593'
print(f'default_factory=fake.numerify  | {id_2}')      # id='187'


#------------------------------------------ ✅lambda: fake.numerify(CUSTOMIZE👈) ---------------------------------------
class Schema(BaseModel):
    id: str = Field(default_factory=lambda: fake.numerify(text='id-###'))   # Генерация (с КАСТОМИЗАЦИЕЙ) для КАЖДОГО экземпляра

id_1 = Schema()
id_2 = Schema()

print(f'default_factory=fake.numerify  | {id_1}')      # id='id-884'
print(f'default_factory=fake.numerify  | {id_2}')      # id='id-884'

#=======================================================================================================================
