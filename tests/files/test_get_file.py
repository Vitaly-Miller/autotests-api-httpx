"""
Test Get File
"""
import http
import pytest
from clients.files_client import FilesClient
from schemas.files_schema import CreateFileSchema, CreateFileResponseSchema
from tools.assertions.base_assert import assert_status_code, assert_method
from tools.assertions.schema_assert import validate_json_schema
from tools.tool import Tool

#=======================================================================================================================
@pytest.mark.regression
@pytest.mark.files
class TestGetFile:
    def test_get_file(self, files_client: FilesClient, create_file: CreateFileSchema):
        response = files_client.get_file_api(create_file.file_id)                # ▶ Запрос через API-метод

        # Assertions
        assert_status_code(response, http.HTTPStatus.OK)   # Status code
        assert_method(response, http.HTTPMethod.GET)     # Method
        validate_json_schema(response, CreateFileResponseSchema) # Validation JSON schema


#=======================================================================================================================
        # API Report (optional)
        # Tool.api_report(response)
