"""
validate_by_name=True,             # new - v2.11+
validate_by_alias=True             # new - v2.11+

populate_by_name=True              # old - выпилят в Pydantic v3

Позволяет передавать данные по Python-именам полей: first_name / last_name (🐍snake_case).
Alias-имена: firstName / lastName (🐫camelCase) - принимаются по умолчанию, потому что они указаны в Field(alias='...')

Documentation:
⚠️Предупреждение
Использование populate_by_name не рекомендуется начиная с версии v2.11+ и будет удалено в v3.
Вместо этого следует использовать настройку validate_by_name в ConfigDict.
При установке validate_by_name=True и validate_by_alias=True
поведение полностью эквивалентно прежнему populate_by_name=True.
"""
from pydantic import BaseModel, Field, ConfigDict

#=======================================================================================================================
#--------------------------------------------------- Pydantic Schema ---------------------------------------------------
class UserSchema(BaseModel):
    model_config = ConfigDict(
        # populate_by_name=True            # old - выпилят в Pydantic v3
        validate_by_name=True,             # new - v2.11+
        validate_by_alias=True             # new - v2.11+
    )

    first_name: str = Field(alias='firstName')
    last_name: str = Field(alias='lastName')


#---------------------------------------------- Инициализация модели --------------------------------------------------
# 🐍snake_case
user_model = UserSchema(
    first_name='John',                    # NOQA (это из за нововведения validate_by_name=True)
    last_name='Connor'                    # NOQA (это из за нововведения validate_by_alias=True)
)

#-------------------------------------------- Input (🐍camelCase) ---------------------------------------------
# 🐍snake_case
user_api_dict = {
    'first_name': 'John',
    'last_name': 'Connor'
}

# 🐍camelCase
user_api_json = """
{
    "first_name": "John",
    "last_name": "Connor"
}
"""

#=========================================== MODEL INITIALIZATION & VALIDATION =========================================

#--------------------------------------------- DESERIALIZATION (validate ⬅︎) -------------------------------------------
# (Dict -> Model)              ┌──────┐
model_from_dict = UserSchema.model_validate(user_api_dict)        # Dict -> Model | first_name='John' last_name='Connor'
model_from_dict_ = UserSchema(**user_api_dict)                    # или (**распаковка_словаря)

# (JSON -> Model)              ┌──────┬──────┐
model_from_json = UserSchema.model_validate_json(user_api_json)   # JSON -> Model | first_name='John' last_name='Connor'
#------------------------------------------------ SERIALIZATION (dump ⮕)  ---------------------------------------------
# (Model -> Dict)         ┌────┐
dict_snake = user_model.model_dump()                     # Model -> Dict    | {'first_name': 'John', 'last_name': 'Connor'}
dict_camel = user_model.model_dump(by_alias=True)        # Model -> Dict 🐫 | {'firstName': 'John', 'lastName': 'Connor'}

# (Model -> JSON)         ┌────┬────┐
json_snake = user_model.model_dump_json()                # Model -> JSON    | {"first_name":"John","last_name":"Connor"}
json_camel = user_model.model_dump_json(by_alias=True)   # Model -> JSON 🐫 | {"firstName":"John","lastName":"Connor"}


#------------------------------------------------------ Output ---------------------------------------------------------
print()
print(f'------------ DESERIALIZATION (validate ⬅︎) ------------')
print(f'Dict -> Model | {model_from_dict}')
print(f'Dict ** Model | {model_from_dict_}')
print(f'JSON -> Model | {model_from_json}')
print()
print(f'--------------- SERIALIZATION (dump ⮕) ---------------')
print(f'Model -> Dict    | {dict_snake}')
print(f'Model -> Dict 🐫 | {dict_camel}')
print(f'Model -> JSON    | {json_snake}')
print(f'Model -> JSON 🐫 | {json_camel}')
#-----------------------------------------------------------------------------------------------------------------------
