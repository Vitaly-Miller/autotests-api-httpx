"""
JSON Schema Validation
"""
import json
import httpx
import jsonschema
import pydantic
import allure
from tools.logger import get_logger

#------------- Logger --------------
logger = get_logger('SCHEMA-ASSERT')

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
        json_schema = schema.model_json_schema()                                        # Генерация JSON-схемы. Pydantic-model –> Dict
        json_schema_pretty = json.dumps(json_schema, indent=2, ensure_ascii=False)  # Dict —> JSON-string (Pretty)
        instance_pretty = json.dumps(instance, indent=2, ensure_ascii=False)        # Dict —> JSON-string (Pretty)

        # Allure attachment of Response JSON
        allure.attach(
            body=instance_pretty,                          # Прикрепляемый объект
            name='Response JSON',                          # Allure attachment title
            attachment_type=allure.attachment_type.JSON    # Output type (Тип отображения объекта - JSON)
        )

        # Allure attachment of JSON Schema
        allure.attach(
            body=json_schema_pretty,                       # Прикрепляемый объект
            name=f'JSON Schema ({schema.__name__})',       # Allure attachment title (динамический)
            attachment_type=allure.attachment_type.JSON    # Output type (Тип отображения объекта - JSON)
        )

        # Validation
        logger.info(f'JSON Schema validation ({schema.__name__})')    # Logger
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
