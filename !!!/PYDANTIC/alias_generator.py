"""
Pydantic Alias Generator ✨
     🐍           🐫
snake_case <=> camelCase (автоматически)
"""
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


#=======================================================================================================================
# Внутри модели используются имена полей в snake_case
# alias_generator — автоматически генерирует alias (snake_case -> camelCase)

#--------------------------------------------------- Pydantic Schema ---------------------------------------------------
class UserSchema(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,          # ✅автоматический alias (🐍snake_case -> 🐫camelCase)
        populate_by_name=True              # ✅позволяет передавать поля как в 🐍snake_case, так и в 🐫camelCase
    )

    first_name: str
    last_name: str


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

# Дополнительно (локальные данные 🐍snake_case) 👈
user_python_dict = {
    'first_name': 'Sarah',
    'last_name': 'Connor'
}


#=========================================== MODEL INITIALIZATION & VALIDATION =========================================

#--------------------------------------------- DESERIALIZATION (validate ⬅︎) -------------------------------------------
# (Dict 🐫 -> Model)          ┌──────┐
user_from_api = UserSchema.model_validate(user_api_dict)       # API Dict 🐫-> Model | first_name='John' last_name='Connor'

# (JSON 🐫 -> Model)           ┌──────┬──────┐
user_from_json = UserSchema.model_validate_json(user_api_json) # API JSON 🐫-> Model | first_name='John' last_name='Connor'

# (Dict 🐍 -> Model)
user_from_python = UserSchema.model_validate(user_python_dict) # Python   🐍-> Model | first_name='Sarah' last_name='Connor'


#------------------------------------------------ SERIALIZATION (dump ⮕) ----------------------------------------------
# (Model -> Dict)            ┌─────┐
dict_snake = user_from_api.model_dump()                        # Model -> Dict 🐍| {'first_name': 'John', 'last_name': 'Connor'}
dict_camel = user_from_api.model_dump(by_alias=True)           # Model -> Dict 🐫| {'firstName': 'John', 'lastName': 'Connor'}

# (Model -> JSON)            ┌─────┬────┐
json_snake = user_from_api.model_dump_json()                   # Model -> JSON 🐍| {"first_name":"John","last_name":"Connor"}
json_camel = user_from_api.model_dump_json(by_alias=True)      # Model -> JSON 🐫| {"firstName":"John","lastName":"Connor"}


#------------------------------------------------------ Output ---------------------------------------------------------
print()
print('----------- DESERIALIZATION (validate ⬅︎) -----------')
print(f'API Dict 🐫-> Model | {user_from_api}')
print(f'API JSON 🐫-> Model | {user_from_json}')
print(f'Python   🐍-> Model | {user_from_python}')

print()
print('-------------- SERIALIZATION (dump ⮕) --------------')
print(f'Model -> Dict 🐍    | {dict_snake}')
print(f'Model -> Dict 🐫    | {dict_camel}')
print(f'Model -> JSON 🐍    | {json_snake}')
print(f'Model -> JSON 🐫    | {json_camel}')
