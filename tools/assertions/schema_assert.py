"""
JSON Schema Validation
"""
import json
import httpx
import jsonschema
import pydantic
import allure

#=======================================================================================================================
def validate_json_schema(instance: httpx.Response | dict, schema: type[pydantic.BaseModel]) -> None:
    """
    JSON Schema validation

    + Встроенный генератор (Pydantic-схема —> JSON-схема)
    + Allure attachments (Response JSON, JSON Schema)

    :param instance: Объект для валидации <httpx.Response> или <dict>
    :param schema: Ожидаемая Pydantic-schema, из которой будет генерирована JSON-схема
    :raise: ValidationError - если instance ≠ Pydantic-schema
    """
    with allure.step(f'JSON Schema validation ({schema.__name__})'):    # Allure step title + динамическое __имя__ Pydantic-схемы
        if isinstance(instance, httpx.Response):                        # Проверка на тип данных <instance>
            instance = instance.json()                                  # httpx.Response –> Dict

        # Serialize for Allure attachments
        json_schema = schema.model_json_schema()                                        # Pydantic-model –> Dict (Генерация JSON-схемы)
        json_schema_pretty = json.dumps(json_schema, indent=2, ensure_ascii=False)  # Dict —> JSON-string    (Pretty JSON-схема)
        instance_pretty = json.dumps(instance, indent=2, ensure_ascii=False)        # Dict —> JSON-string    (Pretty Instance)

        # Allure attachment of Response JSON
        allure.attach(
            body=instance_pretty,                          # Instance JSON-string (pretty)
            name='Response JSON',                          # Allure attachment title (статический)
            attachment_type=allure.attachment_type.JSON    # Allure JSON-output
        )

        # Allure attachment of JSON Schema
        allure.attach(
            body=json_schema_pretty,                       # JSON Schema JSON-string (pretty)
            name=f'JSON Schema ({schema.__name__})',       # Allure attachment title (динамический)
            attachment_type=allure.attachment_type.JSON    # Allure JSON-output
        )

        # Validation
        try:
            jsonschema.validate(
                instance=instance,                         # = Instance (Dict) для валидации
                schema=json_schema,                        # = Сгенерированная JSON-схема (Dict)
                format_checker=jsonschema.FormatChecker()  # = Валидация форматов (default) (⚠️НЕ ЗАБУДЬ! - в схеме ответа - email: EmailStr, ...)
            )

        except jsonschema.ValidationError as e:
            allure.attach(str(e), name='Validation Error', attachment_type=allure.attachment_type.TEXT)
            raise AssertionError(e.message)

#=======================================================================================================================
