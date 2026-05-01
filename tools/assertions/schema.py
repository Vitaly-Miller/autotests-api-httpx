"""
Assertions
"""
from typing import Any

import jsonschema
from jsonschema.validators import Draft202012Validator  # для валидации форматов (email...)

#=======================================================================================================================
#------------------------------------------------ Validate JSON Schema -------------------------------------------------
def validation_json_schema(instance: Any, schema: dict) -> None:
    """
    Функция валидации JSON-схемы.

    :param instance: Данные для валидации
    :param schema: ОжидаемаяJSON-схема
    :raise: jsonschema.ValidationError, если instance не соответствует schema
    """
    try:
        jsonschema.validate(
            instance=instance,                                  # Данные для валидации
            schema=schema,                                      # JSON-схема
            format_checker=jsonschema.FormatChecker()           # Валидация форматов - лучше его (⚠️Проверить и решить)
            #format_checker=Draft202012Validator.FORMAT_CHECKER # Валидация форматов (требуется from jsonschema.validators import Draft202012Validator)
        )
        print('✅Данные соответствуют схеме')
    except jsonschema.ValidationError as e:                     # Сохранить полное описание ошибки валидации в переменной <e>
        print(f'❌Ошибка JSON-Schema валидации: {e.message}')   # Вывод краткого описания ошибки (только текст без кода)
        raise e
#-----------------------------------------------------------------------------------------------------------------------
