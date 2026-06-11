"""
TEST Get File
"""
import http
import pytest
from clients.files_client import FilesClient
from schemas.errors_schema import ErrorResponseSchema
from schemas.files_schema import CreateFileSchema, CreateFileResponseSchema
from tools.assertions.base_assert import assert_status_code, assert_method
from tools.assertions.schema_assert import validate_json_schema
from tools.data_generator import fake
from tools.assertions.files_assert import (
    assert_file_id,
    assert_file_not_found_error_response,
    assert_get_file_invalid_id_error_response
)
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
        assert_file_id(response, create_file.file_id)             # File ID validation
        validate_json_schema(response, CreateFileResponseSchema) # Validation JSON schema



#------------------------------------------------------ Negative -------------------------------------------------------
@pytest.mark.regression
@pytest.mark.files
@pytest.mark.negative
class TestGetFileNegative:
    # Get File by invalid File ID (non-UUID format)
    def test_get_file_by_invalid_file_id(self, files_client: FilesClient):
        invalid_file_id = 'invalid_File_ID'                            # Invalid File ID (NON-UUID format)
        response = files_client.get_file_api(invalid_file_id)          # ▶ Запрос через API-метод с invalid File ID

        # Assertions
        assert_status_code(response, http.HTTPStatus.UNPROCESSABLE_ENTITY) # Status code: 422
        assert_method(response, http.HTTPMethod.GET)                     # Method: GET
        assert_get_file_invalid_id_error_response(response)                                          # Validation Error Response data
        validate_json_schema(response, ErrorResponseSchema)                      # Validation JSON schema


    # Get NON-existent File
    def test_get_non_existent_file(self, files_client: FilesClient):
        non_existent_file_id = fake.uuid4()                           # Non-existent File ID (UUID format)
        response = files_client.get_file_api(non_existent_file_id)    # ▶ Запрос через API-метод с Non-existent File ID

        # Assertions
        assert_status_code(response, http.HTTPStatus.NOT_FOUND)  # Status code: 404
        assert_method(response, http.HTTPMethod.GET)           # Method: GET
        assert_file_not_found_error_response(response)                                 # Validation Error Response data

#=======================================================================================================================
        #Tool.api_report(response)
