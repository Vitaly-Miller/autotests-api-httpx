"""
Test Create File
"""
import http
import httpx
import pytest
from clients.files_client import FilesClient
from schemas.files import CreateFileResponseSchema, CreateFileRequestSchema, CreateFileSchema
from tools.assertions.base_assert import assert_status_code, assert_method
from tools.assertions.schema_assert import validate_json_schema
from tools.assertions.files_assert import (
    assert_create_file_id_length,
    assert_create_file_values_non_empty,
    assert_create_file_data_equal
)
from tools.tool import Tool
#=======================================================================================================================
@pytest.mark.regression
@pytest.mark.files
class TestCreateFile:
    """v.1 - Через фикстуру создания файла"""
    def test_create_file_1(self, create_file_api: httpx.Response):
        response = create_file_api   # Сохраняем ответ фикстуры, но не обязательно
                                     # Исполняемую API-фикстуру можно сразу передавать в Assertions в качестве параметра
        # Assertions
        assert_status_code(response, http.HTTPStatus.OK)     # Status code
        assert_method(response, http.HTTPMethod.POST)      # Method
        assert_create_file_values_non_empty(response)                              # 4-in-1 | NON-empty response values
        assert_create_file_id_length(response)                                     # File ID length = 36 chars
        validate_json_schema(response, CreateFileResponseSchema)   # Validation JSON schema

        # API Report (optional)
        #Tool.api_report(response)


    """v.2 - Через фикстуру получения экземпляра FilesClient"""
    def test_create_file_2(self, files_client: FilesClient):
        create_file_data = CreateFileRequestSchema()                               # Инициализация Pydantic-модели c default fake-data
        response = files_client.create_file_api(create_file_data)                  # ▶ Запрос через API-метод

        # Assertions
        assert_status_code(response, http.HTTPStatus.OK)     # Status code
        assert_method(response, http.HTTPMethod.POST)      # Method
        assert_create_file_values_non_empty(response)                              # 4-in-1 | NON-empty response values
        assert_create_file_id_length(response)                                     # File ID length = 36 chars
        assert_create_file_data_equal(response,create_file_data)  # 3-in-1 | Request File Data = Response File Data
        validate_json_schema(response, CreateFileResponseSchema)   # Validation JSON schema


        # API Report (optional)
        #Tool.api_report(response)

    def test_is_file(self, files_client: FilesClient, create_file: CreateFileSchema):
        response = files_client.get_file_api(create_file.file_id)                # ▶ Запрос через API-метод

        # Assertions
        assert_status_code(response, http.HTTPStatus.OK)   # Status code
        assert_method(response, http.HTTPMethod.GET)     # Method

        # API Report (optional)
        #Tool.api_report(response)
#=======================================================================================================================
