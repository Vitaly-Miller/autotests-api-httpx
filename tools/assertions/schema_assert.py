"""
JSON Schema Validation
"""
import httpx
import jsonschema
import pydantic

#=======================================================================================================================
def validation_json_schema(instance: httpx.Response | dict, schema: type[pydantic.BaseModel]) -> None:
    """
    Валидация JSON-схемы со встроенным генератором (Pidantic-схема —> JSON-схема)

    :param instance: Объект для валидации <response>
    :param schema: Ожидаемая Pidantic-схема  <CreateUserResponseSchema>, из которой будет генерирована JSON-схема
    :raise: ValidationError - если instance ≠ schema
    """

    if isinstance(instance, httpx.Response):
        instance = instance.json()

    try:
        jsonschema.validate(
            instance=instance,                                 # Данные для валидации
            schema=schema.model_json_schema(),                 # JSON-схема, .сгенерированная из Pidantic-схемы
            format_checker=jsonschema.FormatChecker()          # Валидация форматов (default) (⚠️НЕ ЗАБУДЬ! - в схеме ответа - email: EmailStr, ...)
        )
        #print('✅JSON-response schema. Validation success.')  # Вывод при успешной валидации (можно закомментировать)

    except jsonschema.ValidationError as e:                    # Сохранить полное описание ошибки валидации в переменной <e>
        print(f'❌JSON-response schema. Validation error: [{e.message}]')   # Вывод краткого описания ошибки (только текст без кода)
        raise e                                                # Упасть с полным описанием ошибки (Traceback)
#-----------------------------------------------------------------------------------------------------------------------
