"""
Test Get File
"""
import http
import pytest
from clients.files_client import FilesClient
from schemas.errors_schema import ResponseErrorSchema
from schemas.files_schema import CreateFileSchema, CreateFileResponseSchema
from tools.assertions.base_assert import assert_status_code, assert_method
from tools.assertions.files_assert import assert_invalid_file_id_error_response
from tools.assertions.schema_assert import validate_json_schema
from tools.tool import Tool

#=======================================================================================================================
@pytest.mark.regression
@pytest.mark.files
class TestGetFile:
    def test_get_file(self, files_client: FilesClient, create_file: CreateFileSchema):
        response = files_client.get_file_api(create_file.file_id)                # ▶ Запрос через API-метод

        # Assertions
        assert_status_code(response, http.HTTPStatus.OK)   # Status code: 200
        assert_method(response, http.HTTPMethod.GET)     # Method: GET
        validate_json_schema(response, CreateFileResponseSchema) # Validation JSON schema


    #=================================================== Negative ======================================================
    # Get File by invalid File ID (non-UUID format)
    def test_negative_get_file_by_invalid_file_id(self, files_client: FilesClient):
        invalid_file_id = 'invalid_File_ID'                            # Invalid File ID (non-UUID format)
        response = files_client.get_file_api(invalid_file_id)          # ▶ Запрос через API-метод с invalid File ID

        # Assertions
        assert_status_code(response, http.HTTPStatus.UNPROCESSABLE_ENTITY) # Status code: 422
        assert_method(response, http.HTTPMethod.GET)                     # Method: GET
        assert_invalid_file_id_error_response(response)                                          # Validation Error Response data
        validate_json_schema(response, ResponseErrorSchema)                      # Validation JSON schema

#=======================================================================================================================
        #Tool.api_report(response)
