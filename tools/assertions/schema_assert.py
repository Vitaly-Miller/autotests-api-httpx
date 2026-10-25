"""
Response JSON Schema Validation
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

    + Built-in generator (Pydantic schema —> JSON schema)
    + Allure attachments (Response JSON, JSON Schema)

    :param instance: Object to validate <httpx.Response> or <dict>
    :param schema: Expected Pydantic-schema from which the JSON schema will be generated
    :raise: ValidationError - if instance ≠ Pydantic-schema
    """
    with allure.step(f'Response JSON Schema validation ({schema.__name__})'):
        if isinstance(instance, httpx.Response):
            instance = instance.json()

        # Serialize for Allure attachments
        json_schema = schema.model_json_schema()
        json_schema_pretty = json.dumps(json_schema, indent=2, ensure_ascii=False)
        instance_pretty = json.dumps(instance, indent=2, ensure_ascii=False)

        # Allure attachment of Response JSON
        allure.attach(
            body=instance_pretty,
            name='Response JSON',
            attachment_type=allure.attachment_type.JSON
        )

        # Allure attachment of JSON Schema
        allure.attach(
            body=json_schema_pretty,
            name=f'Response JSON Schema ({schema.__name__})',
            attachment_type=allure.attachment_type.JSON
        )

        # Validation
        logger.info(f'Response JSON Schema validation ({schema.__name__})')
        try:
            jsonschema.validate(
                instance=instance,
                schema=json_schema,
                format_checker=jsonschema.FormatChecker()
            )

        except jsonschema.ValidationError as e:
            allure.attach(str(e), name='Validation Error', attachment_type=allure.attachment_type.TEXT)
            raise AssertionError(e.message)


#=======================================================================================================================
