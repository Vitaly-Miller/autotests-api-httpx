"""
TEST Create File
"""
import http
import allure
import pytest
from clients.files_client import FilesClient
from schemas.errors_schema import ErrorResponseSchema
from schemas.files_schema import CreateFileResponseSchema, CreateFileRequestSchema
from tools.allure.annotations import Epic, Feature, Story, Tag
from tools.assertions.base_assert import assert_status_code, assert_method
from tools.assertions.schema_assert import validate_json_schema
from tools.assertions.files_assert import (
    assert_create_file_response_non_empty, assert_file_id, assert_create_file_response,
    assert_create_file_empty_filename_error_response,
    assert_create_file_empty_directory_error_response
)
from tools.tool import Tool

#=======================================================================================================================
@pytest.mark.files
@pytest.mark.regression
@allure.tag(Tag.FILES, Tag.CREATE, Tag.REGRESSION)                           # Через Enum
@allure.epic(Epic.API)
@allure.feature(Feature.FILES)
@allure.story(Story.CREATE)
@allure.severity(allure.severity_level.NORMAL)
class TestCreateFile:
    @allure.title('Create File')
    def test_create_file(self, files_client: FilesClient):
        file_data = CreateFileRequestSchema()                                      # Pydantic-model with fake-data
        response = files_client.create_file_api(file_data)                         # ▶ Запрос через API-метод

        # Assertions
        assert_status_code(response, http.HTTPStatus.OK)     # Status code: 200
        assert_method(response, http.HTTPMethod.POST)      # Method: POST
        assert_create_file_response_non_empty(response)                            # Response data is NON-empty
        assert_file_id(response)                                                   # File ID validation
        assert_create_file_response(response,file_data)      # Response data = Request data  (multipart/form-data)
        validate_json_schema(response, CreateFileResponseSchema)   # Validation JSON schema


#------------------------------------------------------ Negative -------------------------------------------------------
@pytest.mark.files
@pytest.mark.regression
@pytest.mark.negative
@allure.tag(Tag.FILES, Tag.CREATE, Tag.REGRESSION, Tag.NEGATIVE)    # Через Enum
@allure.epic(Epic.API)
@allure.feature(Feature.FILES)
@allure.story(Story.CREATE, Story.NEGATIVE)
@allure.severity(allure.severity_level.NORMAL)
class TestCreateFileNegative:
    @allure.title('Create File with empty file name')
    def test_negative_create_file_empty_filename(self, files_client: FilesClient):
        create_file_data = CreateFileRequestSchema(                       # Pydantic-model with fake-data
           filename=''                                                    # 👈fake-data —> "" (empty)
        )
        response = files_client.create_file_api(create_file_data)         # ▶ Запрос через API-метод

        # Assertions
        assert_status_code(response, http.HTTPStatus.UNPROCESSABLE_ENTITY) # Status code: 422
        assert_method(response, http.HTTPMethod.POST)                    # Method: POST
        assert_create_file_empty_filename_error_response(response)                               # Validation Error Response data
        validate_json_schema(response, ErrorResponseSchema)                      # Validation JSON schema



    @allure.title('Create File with empty directory')
    def test_negative_create_file_empty_directory(self, files_client: FilesClient):
        create_file_data = CreateFileRequestSchema(                  # Pydantic-model with fake-data
           directory=''                                              # 👈fake-data —> "" (empty)
        )
        response = files_client.create_file_api(create_file_data)    # ▶ Запрос через API-метод

        # Assertions
        assert_status_code(response, http.HTTPStatus.UNPROCESSABLE_ENTITY) # Status code: 422
        assert_method(response, http.HTTPMethod.POST)                    # Method: POST
        assert_create_file_empty_directory_error_response(response)                              # Validation Error Response data
        validate_json_schema(response, ErrorResponseSchema)                      # Validation JSON schema


#=======================================================================================================================
        # Tool.api_report(response)
