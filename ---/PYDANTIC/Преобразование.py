"""
Pydantic Преобразование
"""
from pydantic import BaseModel

#=======================================================================================================================
#-------------------------------------------------- Pydantic Schema-----------------------------------------------------
# Схема
class DataSchema(BaseModel):
    # .атрибуты_схемы
    first_name: str
    last_name: str

#=========================================== MODEL INITIALIZATION & VALIDATION =========================================
# Инициализация модели (классическая)
data_model = DataSchema(                                          # first_name='John' last_name='Connor'
    first_name='John',
    last_name='Connor'
)
#--------------------------------------------------  API Objects -------------------------------------------------------
# Dict
data_dict = {                                                     # {'first_name': 'John', 'last_name': 'Connor'}
    'first_name': 'John',
    'last_name': 'Connor',
}
# JSON-string
data_json = '{"first_name":"John","last_name":"Connor"}'          # {"first_name":"John","last_name":"Connor"}

#-------------------------------------------- DESERIALIZATION (validate ⬅︎) --------------------------------------------
# Dict -> Model                ┌──────┐
model_from_dict = DataSchema.model_validate(data_dict)            # first_name='John' last_name='Connor'

# JSON -> Model                ┌──────┬──────┐
model_from_json = DataSchema.model_validate_json(data_json)       # first_name='John' last_name='Connor'

#------------------------------------------ SERIALIZATION (dump ⮕) (Парсинг) ------------------------------------------
# Model -> Python Dict       ┌─────┐
model_to_dict = data_model.model_dump()                           # {'first_name': 'John', 'last_name': 'Connor'}
# Model -> JSON-совместимый Dict✨┌─────┐╴╴╴╴╴┐
model_to_json_dict = data_model.model_dump(mode='json')           # {'first_name': 'John', 'last_name': 'Connor'}
# Model -> JSON-string       ┌─────┬─────┐
model_to_json = data_model.model_dump_json()                      # {"first_name":"John","last_name":"Connor"


#------------------------------------------------------ Output ---------------------------------------------------------
print(f'Model                | {data_model}')
print(f'Dict                 | {data_dict}')
print(f'JSON                 | {data_json}')
print()
print(f'Dict -> Model        | {model_from_dict}')
print(f'JSON -> Model        | {model_from_json}')
print()
print(f'Model -> Dict        | {model_to_dict}')
print(f'Model -> JSON (dict) | {model_to_json_dict}')
print(f'Model -> JSON        | {model_to_json}')
#-----------------------------------------------------------------------------------------------------------------------
# Вывод .аргументов модели (Model)
print(data_model.first_name)            # John
print(data_model.last_name)             # Connor

# Вывод значений ключей словаря (Dict)
print(model_to_dict['first_name'])      # John
print(model_to_dict['last_name'])       # Connor
