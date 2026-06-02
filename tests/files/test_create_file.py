"""
Test Create File
"""
import http
import httpx
import pytest
from clients.files_client import FilesClient
from schemas.errors_schema import ResponseErrorSchema
from schemas.files_schema import CreateFileResponseSchema, CreateFileRequestSchema, CreateFileSchema
from tools.assertions.base_assert import assert_status_code, assert_method
from tools.assertions.schema_assert import validate_json_schema
from tools.assertions.files_assert import (
    assert_create_file_id_length,
    assert_create_file_values_non_empty,
    assert_create_file_data_equal, assert_create_file_empty_filename_error_response, assert_create_file_empty_directory_error_response
)
from tools.tool import Tool
#=======================================================================================================================
@pytest.mark.regression
@pytest.mark.files
class TestCreateFile:
    """v.1 - Через фикстуру получения экземпляра FilesClient"""
    def test_create_file_1(self, files_client: FilesClient):
        create_file_data = CreateFileRequestSchema()                               # Инициализация Pydantic-модели c default fake-data
        response = files_client.create_file_api(create_file_data)                  # ▶ Запрос через API-метод

        # Assertions
        assert_status_code(response, http.HTTPStatus.OK)     # Status code: 200
        assert_method(response, http.HTTPMethod.POST)      # Method POST
        assert_create_file_values_non_empty(response)                              # 4-in-1 | NON-empty response values
        assert_create_file_id_length(response)                                     # File ID length = 36 chars
        assert_create_file_data_equal(response,create_file_data)  # 3-in-1 | Request Data = Response Data
        validate_json_schema(response, CreateFileResponseSchema)   # Validation JSON schema


    """v.2 - Через фикстуру создания файла"""
    def test_create_file_2(self, create_file_api: httpx.Response):
        response = create_file_api   # Сохраняем ответ фикстуры, но не обязательно
                                     # Исполняемую API-фикстуру можно сразу передавать в Assertions в качестве параметра
        # Assertions
        assert_status_code(response, http.HTTPStatus.OK)     # Status code: 200
        assert_method(response, http.HTTPMethod.POST)      # Method POST
        assert_create_file_values_non_empty(response)                              # 4-in-1 | NON-empty response values
        assert_create_file_id_length(response)                                     # File ID length = 36 chars
        validate_json_schema(response, CreateFileResponseSchema)   # Validation JSON schema


    def test_is_file(self, files_client: FilesClient, create_file: CreateFileSchema):
        response = files_client.get_file_api(create_file.file_id)                  # ▶ Запрос через API-метод

        # Assertions
        assert_status_code(response, http.HTTPStatus.OK)     # Status code: 200
        assert_method(response, http.HTTPMethod.GET)       # Method GET


    #==================================================== Negative =====================================================
    # Empty 'filename'
    def test_negative_create_file_empty_filename(self, files_client: FilesClient):
        create_file_data = CreateFileRequestSchema(                  # Инициализация Pydantic-модели c default fake-data
           filename=''                                               # 👈default —> "" (empty)
        )
        response = files_client.create_file_api(create_file_data)    # ▶ Запрос через API-метод

        # Assertions
        assert_status_code(response, http.HTTPStatus.UNPROCESSABLE_ENTITY) # Status code: 422
        assert_method(response, http.HTTPMethod.POST)                    # Method: POST
        assert_create_file_empty_filename_error_response(response)                               # Validation Error Response data
        validate_json_schema(response, ResponseErrorSchema)                      # Validation JSON schema


    # Empty 'directory'
    def test__negative_create_file_empty_directory(self, files_client: FilesClient):
        create_file_data = CreateFileRequestSchema(                  # Инициализация Pydantic-модели c default fake-data
           directory=''                                              # 👈default —> "" (empty)
        )
        response = files_client.create_file_api(create_file_data)    # ▶ Запрос через API-метод

        # Assertions
        assert_status_code(response, http.HTTPStatus.UNPROCESSABLE_ENTITY) # Status code: 422
        assert_method(response, http.HTTPMethod.POST)                    # Method: POST
        assert_create_file_empty_directory_error_response(response)                              # Validation Error Response data
        validate_json_schema(response, ResponseErrorSchema)                      # Validation JSON schema


#=======================================================================================================================
        # API Report
        #Tool.api_report(response)
