"""
Pydantic Вложенность
"""
from pydantic import BaseModel

#=======================================================================================================================
#----------------------------------------------------- Schemas ---------------------------------------------------------
# Схема ключа "address": {}
class AddressSchema(BaseModel):
    city: str
    zip_code: str

# ОСНОВНАЯ схема
class UserSchema(BaseModel):
    first_name: str
    last_name: str
    address: AddressSchema    # 👈Вложенная схема адреса

#---------------------------------------------- Инициализация моделей --------------------------------------------------
data = UserSchema(
    first_name='John',
    last_name='Connor',
    address=AddressSchema(    # 👈Инициализация поля по соответствующей схеме
        city='LA',
        zip_code='90210'
    )
    # address={               # Bad practice
    #     'city': 'LA',
    #     'zip_code': '90210'
    # }
)




#----------------------------------------------------- Output ----------------------------------------------------------
# Model
print(data)                    # first_name='John' last_name='Connor' address=AddressSchema(city='LA', zip_code='90210')

# Вывод .аргументов модели
print(data.first_name)         # John
print(data.last_name)          # Connor
print(data.address)            # city='LA' zip_code='90210'

print(data.address.city)       # LA
print(data.address.zip_code)   # 90210

#-------------------------------
# Dict
print(data.model_dump())                        # {'first_name': 'John', 'last_name': 'Connor', 'address': {'city': 'LA', 'zip_code': '90210'}}

# Вывод значений ключей словаря (Dict)
print(data.model_dump()['first_name'])          # John
print(data.model_dump()['last_name'])           # Connor
print(data.model_dump()['address'])             # {'city': 'LA', 'zip_code': '90210'}

print(data.model_dump()['address']['city'])     # LA
print(data.model_dump()['address']['zip_code']) # 90210

#=======================================================================================================================
