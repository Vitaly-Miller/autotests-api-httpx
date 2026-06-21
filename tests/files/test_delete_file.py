"""
TEST Delete File
"""
import http
import pytest
from clients.files_client import FilesClient
from schemas.errors_schema import NotFoundErrorResponseSchema
from schemas.files_schema import CreateFileSchema
from tools.assertions.base_assert import assert_status_code, assert_method
from tools.assertions.files_assert import assert_file_not_found_error_response
from tools.assertions.schema_assert import validate_json_schema
from tools.tool import Tool

#=======================================================================================================================
@pytest.mark.files
@pytest.mark.regression

class TestDeleteFile:
    def test_delete_file(self, files_client: FilesClient, create_file: CreateFileSchema):
        delete_file_response = files_client.delete_file_api(create_file.file_id)          # ▶ Запрос на удаление File через API-метод
        get_non_existent_file_response = files_client.get_file_api(create_file.file_id)   # ▶ Запрос на получение NON-existent File через API-метод

        # Assertions (Delete File)
        assert_status_code(delete_file_response, http.HTTPStatus.OK)      # Status code: 200
        assert_method(delete_file_response, http.HTTPMethod.DELETE)     # Method: DELETE

        # Assertions (Get Non-existent File)
        assert_status_code(get_non_existent_file_response, http.HTTPStatus.NOT_FOUND)   # Status code: 404
        assert_method(get_non_existent_file_response, http.HTTPMethod.GET)            # Method: GET
        assert_file_not_found_error_response(get_non_existent_file_response)                                  # Error message: "File not found"
        validate_json_schema(get_non_existent_file_response, NotFoundErrorResponseSchema)     # Validation JSON schema


#=======================================================================================================================
        #Tool.api_report(delete_file_response)
        #Tool.api_report(get_non_existent_file_response)
