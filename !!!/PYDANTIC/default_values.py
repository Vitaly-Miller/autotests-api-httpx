"""
Pydantic Default Values
"""
from pydantic import BaseModel, Field

#=======================================================================================================================
class DataSchema(BaseModel):
    first_name: str
    last_name: str
    zip_code: str = '90000' # 👈default value

# Инициализация моделей (🐍snake_case):
person_1 = DataSchema(
    first_name='John',
    last_name='Connor'
                            # 👈Ничего не передаем (default)
)

person_2 = DataSchema(
    first_name='John',
    last_name='Connor',
    zip_code='90210'        # 👈Передаем своё значения (default -> custom)
)

# Output (🐍snake_case):
print(person_1)             # first_name='John' last_name='Connor' zip_code='90000'  # 👈default
print(person_2)             # first_name='John' last_name='Connor' zip_code='90210'  # 👈custom


#============================================= Default Values + Alias ==================================================
class DataSchema(BaseModel):
    first_name: str = Field(alias='firstName')
    last_name: str = Field(alias='lastName')
    zip_code: str = Field(alias='zipCode', default='90000')  # 👈default value if alias


# Инициализация моделей (🐫CamelCase):
person_1 = DataSchema(
    firstName='John',
    lastName='Connor'
                            # 👈Ничего не передаем (default)
)

person_2 = DataSchema(
    firstName='John',
    lastName='Connor',
    zipCode='90210'         # 👈Передаем своё значения (default -> custom)
)

# Output (🐍snake_case):
print(person_1)             # first_name='John' last_name='Connor' zip_code='90000'  # 👈default
print(person_2)             # first_name='John' last_name='Connor' zip_code='90210'  # 👈custom
#-----------------------------------------------------------------------------------------------------------------------
