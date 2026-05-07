"""
JSON Schema Validation
"""
from typing import Any
import jsonschema


#=======================================================================================================================
def validation_json_schema(instance: Any, schema: Any) -> None:
    """
    Валидация JSON-схемы со встроенным генератором (Pidantic-схема —> JSON-схема)

    :param instance: Объект для валидации <response>
    :param schema: Ожидаемая Pidantic-схема  <CreateUserResponseSchema>, из которой будет генерирована JSON-схема
    :raise: ValidationError - если instance ≠ schema
    """
    try:
        jsonschema.validate(
            instance=instance.json(),                          # Данные для валидации в формате JSON
            schema=schema.model_json_schema(),                 # JSON-схема, .сгенерированная из Pidantic-схемы
            format_checker=jsonschema.FormatChecker()          # Валидация форматов (default) (⚠️НЕ ЗАБУДЬ! - в схеме ответа - email: EmailStr, ...)
        )
        print('✅JSON-response schema. Validation success.')   # Вывод при успешной валидации (можно закомментировать)
    except jsonschema.ValidationError as e:                    # Сохранить полное описание ошибки валидации в переменной <e>
        print(f'❌JSON-response schema. Validation error: [{e.message}]')   # Вывод краткого описания ошибки (только текст без кода)
        raise e                                                # Упасть с полным описанием ошибки (Traceback)
#-----------------------------------------------------------------------------------------------------------------------
