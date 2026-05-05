"""
Assertions
"""
from typing import Any
import jsonschema


#=======================================================================================================================
#------------------------------------------------ Validate JSON Schema -------------------------------------------------
def validation_json_schema(instance: Any, json_schema: dict) -> None:
    """
    Валидация JSON-схемы.

    :param instance: Данные для валидации
    :param json_schema: Ожидаемая JSON-схема (❗️Сгенерированная: json_schema = TokenSchema.model_json_schema())
    :raise: jsonschema.ValidationError, если instance не соответствует schema
    """
    try:
        jsonschema.validate(
            instance=instance,                                  # Данные для валидации
            schema=json_schema,                                 # JSON-схема (❗️Сгенерированная: json_schema = TokenSchema.model_json_schema())
            format_checker=jsonschema.FormatChecker()           # Валидация форматов (default)
        )
        print(' - ✅Успешная валидация JSON-response')                   # Вывод при успешной валидации (закомментировать)
    except jsonschema.ValidationError as e:                     # Сохранить полное описание ошибки валидации в переменной <e>
        print(f'❌Ошибка JSON-Schema валидации: {e.message}')   # Вывод краткого описания ошибки (только текст без кода)
        raise e
#-----------------------------------------------------------------------------------------------------------------------
