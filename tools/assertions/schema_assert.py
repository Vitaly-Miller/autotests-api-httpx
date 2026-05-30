"""
JSON Schema Validation # ⚠️Разобраться НЕ ПАДАЕТ КАК НАДО!
"""
import httpx
import jsonschema
import pydantic

#=======================================================================================================================
def validate_json_schema(instance: httpx.Response | dict, schema: type[pydantic.BaseModel]) -> None:
    """
    Валидация JSON-схемы со встроенным генератором (Pidantic-схема —> JSON-схема)

    :param instance: Объект для валидации <httpx.Response> или <dict>
    :param schema: Ожидаемая Pidantic-Schema, из которой будет генерирована JSON-схема
    :raise: ValidationError - если instance ≠ schema
    """
    # Если передали сырой httpx.Response
    if isinstance(instance, httpx.Response):                   # Проверка на тип данных <instance>
        instance = instance.json()                             # httpx.Response –> Dict

    try:
        jsonschema.validate(
            instance=instance,                                 # Словарь (dict) для валидации
            schema=schema.model_json_schema(),                 # JSON-схема (dict), сгенерированная из Pidantic-схемы
            format_checker=jsonschema.FormatChecker()          # Валидация форматов (default) (⚠️НЕ ЗАБУДЬ! - в схеме ответа - email: EmailStr, ...)
        )
        #print('✅JSON-response schema. Validation success.')  # Вывод при успешной валидации (#закомментировано)

    except jsonschema.ValidationError as e:                                 # Сохранить полное описание ошибки валидации в переменной <e>
        print(f'❌JSON-Response schema. Validation error: [{e.message}]')   # Вывод краткого описания ошибки (только текст без кода)
        raise AssertionError(e.message)                                                               # Упасть с полным описанием ошибки (Traceback)
#-----------------------------------------------------------------------------------------------------------------------
