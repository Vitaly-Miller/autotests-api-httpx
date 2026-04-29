"""
Pydantic Alias
     🐍           🐫
snake_case <=> camelCase
"""
from pydantic import BaseModel, Field

#=======================================================================================================================
# Внутри модели используются имена полей в snake_case
# alias — это альтернативное имя поля для внешних данных (API, JSON)

#--------------------------------------------------- Pydantic Schema ---------------------------------------------------
class UserSchema(BaseModel):
    first_name: str = Field(alias='firstName')    # Поле в схеме 🐍snake_case = 🐫camelCase from API
    last_name: str = Field(alias='lastName')      # Поле в схеме 🐍snake_case = 🐫camelCase from API

#---------------------------------------------- Инициализация модели --------------------------------------------------
user_model = UserSchema(
    firstName='John',
    lastName='Connor'
)

#-------------------------------------------- Input from API (🐫camelCase) ---------------------------------------------
user_api_dict = {
    'firstName': 'John',
    'lastName': 'Connor'
}

user_api_json = """
{
    "firstName": "John",
    "lastName": "Connor"
}
"""

#=========================================== MODEL INITIALIZATION & VALIDATION =========================================

#--------------------------------------------- DESERIALIZATION (validate ⬅︎) -------------------------------------------
# (Dict -> Model)               ┌──────┐
model_from_dict = UserSchema.model_validate(user_api_dict)        # Dict 🐫 -> Model | first_name='John' last_name='Connor'
model_from_dict_ = UserSchema(**user_api_dict)                    # или (**распаковка_словаря)

# (JSON -> Model)              ┌──────┬──────┐
model_from_json = UserSchema.model_validate_json(user_api_json)   # JSON 🐫 -> Model | first_name='John' last_name='Connor'
#------------------------------------------------ SERIALIZATION (dump ⮕)  ---------------------------------------------
# (Model -> Dict)         ┌────┐
dict_snake = user_model.model_dump()                     # Model -> Dict 🐍 | {'first_name': 'John', 'last_name': 'Connor'}
dict_camel = user_model.model_dump(by_alias=True)        # Model -> Dict 🐫 | {'firstName': 'John', 'lastName': 'Connor'}

# (Model -> JSON)         ┌────┬────┐
json_snake = user_model.model_dump_json()                # Model -> JSON 🐍 | {"first_name":"John","last_name":"Connor"}
json_camel = user_model.model_dump_json(by_alias=True)   # Model -> JSON 🐫 | {"firstName":"John","lastName":"Connor"}


#------------------------------------------------------ Output ---------------------------------------------------------
print()
print(f'------------ DESERIALIZATION (validate ⬅︎) ------------')
print(f'Dict 🐫 -> Model | {model_from_dict}')
print(f'Dict 🐫 ** Model | {model_from_dict_}')
print(f'JSON 🐫 -> Model | {model_from_json}')
print()
print(f'--------------- SERIALIZATION (dump ⮕) ---------------')
print(f'Model -> Dict 🐍 | {dict_snake}')
print(f'Model -> Dict 🐫 | {dict_camel}')
print(f'Model -> JSON 🐍 | {json_snake}')
print(f'Model -> JSON 🐫 | {json_camel}')
#-----------------------------------------------------------------------------------------------------------------------
