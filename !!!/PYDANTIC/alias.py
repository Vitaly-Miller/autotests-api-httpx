"""
Pydantic Alias
     🐍           🐫
snake_case <=> camelCase
"""
from pydantic import BaseModel, Field, ConfigDict

#=======================================================================================================================
# Внутри модели используются имена полей в snake_case
# alias — это альтернативное имя поля для внешних данных (API, JSON)

#--------------------------------------------------- Pydantic Schema ---------------------------------------------------
class UserSchema(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True                    # ✅позволяет передавать поля как в 🐍snake_case, так и в 🐫camelCase
    )

    first_name: str = Field(alias='firstName')   # Поле в схеме 🐍snake_case = 🐫camelCase from API
    last_name: str = Field(alias='lastName')     # Поле в схеме 🐍snake_case = 🐫camelCase from API

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
# (Dict 🐫 -> Model) ┌──────┐
user = UserSchema.model_validate(user_api_dict)        # Dict 🐫 -> Model | first_name='John' last_name='Connor'

# (JSON 🐫 -> Model) ┌──────┬──────┐
user_ = UserSchema.model_validate_json(user_api_json)  # JSON 🐫 -> Model | first_name='John' last_name='Connor'

#------------------------------------------------ SERIALIZATION (dump ⮕)  ---------------------------------------------
# (Model -> Dict)   ┌────┐
dict_snake = user.model_dump()                         # Model -> Dict 🐍 | {'first_name': 'John', 'last_name': 'Connor'}
dict_camel = user.model_dump(by_alias=True)            # Model -> Dict 🐫 | {'firstName': 'John', 'lastName': 'Connor'}

# (Model -> JSON)    ┌────┬────┐
json_snake = user.model_dump_json()                    # Model -> JSON 🐍 | {"first_name":"John","last_name":"Connor"}
json_camel = user.model_dump_json(by_alias=True)       # Model -> JSON 🐫 | {"firstName":"John","lastName":"Connor"}


#------------------------------------------------------ Output ---------------------------------------------------------
print()
print(f'----------- DESERIALIZATION (validate ⬅︎) -----------')
print(f'Dict 🐫 -> Model | {user}')
print(f'JSON 🐫 -> Model | {user_}')
print()
print(f'-------------- SERIALIZATION (dump ⮕) --------------')
print(f'Model -> Dict 🐍 | {dict_snake}')
print(f'Model -> Dict 🐫 | {dict_camel}')
print(f'Model -> JSON 🐍 | {json_snake}')
print(f'Model -> JSON 🐫 | {json_camel}')


#=======================================================================================================================
