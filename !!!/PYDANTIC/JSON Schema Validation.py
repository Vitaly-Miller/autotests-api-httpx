"""
JSON Schema Validation (NOT Pydantic)
"""
import jsonschema

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
    jsonschema.validate(
        instance=valid_data,                          # Данные для валидации
        schema=schema,                                # JSON-схема
        format_checker=jsonschema.FormatChecker()     # Валидация форматов (⚠️НЕ ЗАБУДЬ! - в схеме ответа email: EmailStr)
    )
    print('✅Данные соответствуют схеме.')
except jsonschema.ValidationError as e:
    print(f'❌Ошибка JSON-Schema валидации: {e.message}')   # ✅Данные соответствуют схеме.


#----------------------------------------------- ❌Invalid data (type) -------------------------------------------------
# Dict или JSON
invalid_data_1 = {
    'name': 'John',
    'age': '30'     # 👈 аргумент 'age' имеет неправильный тип ('строка' вместо числа)
}

# Валидация
try:
    jsonschema.validate(
        instance=invalid_data_1,
        schema=schema,
        format_checker=jsonschema.FormatChecker()
    )
    print('✅Данные соответствуют схеме.')
except jsonschema.ValidationError as e:
    print(f'❌Ошибка валидации: {e.message}')           # Ошибка валидации: '30' is not of type 'number'


#---------------------------------------------- ❌Invalid data (required) ----------------------------------------------
# Dict или JSON
invalid_data_2 = {
                    # 👈 нет обязательного поля 'name'
    'age': 30
}

# Валидация
try:
    jsonschema.validate(
        instance=invalid_data_2,
        schema=schema,
        format_checker=jsonschema.FormatChecker()
    )
    print('✅Данные соответствуют схеме.')
except jsonschema.ValidationError as e:
    print(f'❌Ошибка валидации: {e.message}')           # Ошибка валидации: 'name' is a required property
#-----------------------------------------------------------------------------------------------------------------------
