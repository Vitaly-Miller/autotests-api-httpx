"""
TEST Create File
"""
import http
import pytest
import allure
from clients.files_client import FilesClient
from schemas.errors_schema import ErrorResponseSchema
from schemas.files_schema import CreateFileResponseSchema, CreateFileRequestSchema
from tools.allure.annotations import Epic, Feature, Story, Tag
from tools.assertions.base_assert import assert_status_code, assert_request_method
from tools.assertions.schema_assert import validate_json_schema
from tools.assertions.files_assert import (
    assert_create_file_response_non_empty, assert_file_id, assert_create_file_response,
    assert_create_file_empty_filename_error_response,
    assert_create_file_empty_directory_error_response
)
from tools.tool import Tool

#=======================================================================================================================
# Class annotations
@pytest.mark.files
@pytest.mark.regression
@allure.tag(Tag.REGRESSION, Tag.FILES, Tag.CREATE)
@allure.epic(Epic.API)
@allure.feature(Feature.FILES)
@allure.story(Story.CREATE)
@allure.severity(allure.severity_level.BLOCKER)
#-----------------------------------------------------------------------------------------------------------------------
class TestCreateFile:
    @allure.title('Create File')
    def test_create_file(self, files_client: FilesClient):
        file_data = CreateFileRequestSchema()
        response = files_client.create_file_api(file_data)
        response_model = CreateFileResponseSchema.model_validate_json(response.text)

        # Assertions
        assert_status_code(response.status_code, http.HTTPStatus.OK)
        assert_request_method(response.request.method, http.HTTPMethod.POST)
        assert_create_file_response_non_empty(response_model)
        assert_create_file_response(response_model,file_data)
        assert_file_id(response_model)
        validate_json_schema(response, CreateFileResponseSchema)



#====================================================== Negative =======================================================
# Class annotations
@pytest.mark.files
@pytest.mark.regression
@pytest.mark.negative
@allure.tag(Tag.REGRESSION, Tag.FILES, Tag.CREATE, Tag.NEGATIVE)
@allure.epic(Epic.API)
@allure.feature(Feature.FILES)
@allure.story(Story.CREATE, Story.NEGATIVE)
@allure.severity(allure.severity_level.NORMAL)
#-----------------------------------------------------------------------------------------------------------------------
class TestCreateFileNegative:
    @allure.title('Create File with EMPTY File Name (negative)')
    def test_negative_create_file_empty_filename(self, files_client: FilesClient):
        create_file_data = CreateFileRequestSchema(
           filename=''
        )
        response = files_client.create_file_api(create_file_data)

        # Assertions
        assert_status_code(response.status_code, http.HTTPStatus.UNPROCESSABLE_ENTITY)  # code: 422
        assert_request_method(response.request.method, http.HTTPMethod.POST)
        assert_create_file_empty_filename_error_response(response)
        validate_json_schema(response, ErrorResponseSchema)


    @allure.title('Create File with EMPTY Directory (negative)')
    def test_negative_create_file_empty_directory(self, files_client: FilesClient):
        create_file_data = CreateFileRequestSchema(
           directory=''
        )
        response = files_client.create_file_api(create_file_data)

        # Assertions
        assert_status_code(response.status_code, http.HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_request_method(response.request.method, http.HTTPMethod.POST)
        assert_create_file_empty_directory_error_response(response)
        validate_json_schema(response, ErrorResponseSchema)


#=======================================================================================================================
        # Tool.api_report(response)          # for PyCharm RUN-console API reporting only
