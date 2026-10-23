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
    with allure.step(f'Response JSON Schema validation ({schema.__name__})'):    # Allure step title + dynamic __name__ of the Pydantic schema
        if isinstance(instance, httpx.Response):                                 # Check <instance> data type
            instance = instance.json()                                           # httpx.Response –> Dict

        # Serialize for Allure attachments
        json_schema = schema.model_json_schema()                                        # Generate JSON schema. Pydantic-model –> Dict
        json_schema_pretty = json.dumps(json_schema, indent=2, ensure_ascii=False)  # Dict —> JSON-string (Pretty)
        instance_pretty = json.dumps(instance, indent=2, ensure_ascii=False)        # Dict —> JSON-string (Pretty)

        # Allure attachment of Response JSON
        allure.attach(
            body=instance_pretty,                          # Attached object
            name='Response JSON',                          # Allure attachment title
            attachment_type=allure.attachment_type.JSON    # Output type (Object display type - JSON)
        )

        # Allure attachment of JSON Schema
        allure.attach(
            body=json_schema_pretty,                           # Attached object
            name=f'Response JSON Schema ({schema.__name__})',  # Allure attachment title (dynamic)
            attachment_type=allure.attachment_type.JSON        # Output type (Object display type - JSON)
        )

        # Validation
        logger.info(f'Response JSON Schema validation ({schema.__name__})')
        try:
            jsonschema.validate(
                instance=instance,                         # = Instance (Dict) to validate
                schema=json_schema,                        # = Generated JSON schema (Dict)
                format_checker=jsonschema.FormatChecker()  # = Format validation (default) (⚠️DON'T FORGET! - in the response schema - email: EmailStr, ...)
            )

        except jsonschema.ValidationError as e:
            allure.attach(str(e), name='Validation Error', attachment_type=allure.attachment_type.TEXT)
            raise AssertionError(e.message)


#=======================================================================================================================
