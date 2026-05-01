"""
JSON Schema Validation (NOT Pydantic)
"""
from jsonschema import validate, ValidationError

#=======================================================================================================================
# JSON Schema
schema = {
    'type': 'object',                   # Тип данных
    'properties': {                     # Содержание:
        'name': {'type': 'string'},     #   'поле': {'тип': 'строка'}
        'age': {'type': 'number'}       #   'поле': {'тип': 'JS-число'}
    },
    'required': ['name']                # Обязательные поля
}

#---------------------------------------------------- ✅Valid data -----------------------------------------------------
# Dict или JSON
valid_data = {
    'name': 'John',
    'age': 30
}

# Валидация
try:
    validate(instance=valid_data, schema=schema)      # <instance> - данные, <schema> - схема
    print('Данные соответствуют схеме.')              # Данные соответствуют схеме
except ValidationError as e:                          # Сохранить полное описание ошибки валидации в переменной <e>
    print(f'Ошибка валидации: {e.message}')           # Вывод краткого описания ошибки (только текст без кода)

#----------------------------------------------- ❌Invalid data (type) -------------------------------------------------
# Dict или JSON
invalid_data_1 = {
    'name': 'John',
    'age': '30'     # 👈 аргумент 'age' имеет неправильный тип ('строка' вместо числа)
}

# Валидация
try:
    validate(instance=invalid_data_1, schema=schema)
    print('Данные соответствуют схеме.')
except ValidationError as e:
    print(f'Ошибка валидации: {e.message}')           # Ошибка валидации: '30' is not of type 'number'


#---------------------------------------------- ❌Invalid data (required) ----------------------------------------------
# Dict или JSON
invalid_data_2 = {
                    # 👈 нет обязательного поля 'name'
    'age': 30
}

# Валидация
try:
    validate(instance=invalid_data_2, schema=schema)
    print('Данные соответствуют схеме.')
except ValidationError as e:
    print(f'Ошибка валидации: {e.message}')           # Ошибка валидации: 'name' is a required property
#-----------------------------------------------------------------------------------------------------------------------
