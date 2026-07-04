"""
TEST Get File
"""
import http
import pytest
import allure
from clients.files_client import FilesClient
from schemas.errors_schema import ErrorResponseSchema, NotFoundErrorResponseSchema
from schemas.files_schema import CreateFileSchema, GetFileResponseSchema
from tools.allure.annotations import Epic, Feature, Story, Tag
from tools.assertions.base_assert import assert_status_code, assert_request_method
from tools.assertions.schema_assert import validate_json_schema
from tools.data_generator import fake
from tools.assertions.files_assert import (
    assert_file_id,
    assert_get_file_not_found_error_response,
    assert_get_file_invalid_id_error_response
)
from tools.tool import Tool

#=======================================================================================================================
# Class annotations
@pytest.mark.files                                         # ┐ Pytest Marks
@pytest.mark.regression                                    # ┘
@allure.tag(Tag.REGRESSION, Tag.FILES, Tag.GET)      # ] Allure Tags
@allure.epic(Epic.API)                                     # ┐
@allure.feature(Feature.FILES)                             # │ Allure Behaviors
@allure.story(Story.GET)                                   # ┘
@allure.parent_suite(Epic.API)                             # ┐
@allure.suite(Feature.FILES)                               # │ Allure Suites (optional)
@allure.sub_suite(Story.GET)                               # ┘
@allure.severity(allure.severity_level.NORMAL)             # ] Allure Severity
#-----------------------------------------------------------------------------------------------------------------------
class TestGetFile:
    @allure.title('Get File by ID')                              # Allure step Title
    def test_get_file(self, files_client: FilesClient, create_file: CreateFileSchema):
        response = files_client.get_file_api(create_file.file_id)                       # ▶ Запрос через API-метод
        response_model = GetFileResponseSchema.model_validate_json(response.text)       # httpx.Response —> Pydantic-model (parsing-deserialize)

        # Assertions
        assert_status_code(response.status_code, http.HTTPStatus.OK)          # Status code: 200
        assert_request_method(response.request.method, http.HTTPMethod.GET)   # Method: GET
        assert_file_id(response_model, create_file.file_id)              # File-ID validation
        validate_json_schema(response, GetFileResponseSchema)                # JSON schema validation



#====================================================== Negative =======================================================
# Class annotations
@pytest.mark.files                                                  # ┐
@pytest.mark.regression                                             # │ Pytest Marks
@pytest.mark.negative                                               # ┘
@allure.tag(Tag.REGRESSION, Tag.FILES, Tag.GET, Tag.NEGATIVE) # ]Allure Tags
@allure.epic(Epic.API)                                              # ┐
@allure.feature(Feature.FILES)                                      # │ Allure Behaviors
@allure.story(Story.GET, Story.NEGATIVE)                    # ┘
@allure.parent_suite(Epic.API)                                      # ┐
@allure.suite(Feature.FILES)                                        # │ Allure Suites (optional)
@allure.sub_suite(Story.GET)                                        # ┘
@allure.severity(allure.severity_level.NORMAL)                      # ] Allure Severity
#-----------------------------------------------------------------------------------------------------------------------
class TestGetFileNegative:
    @allure.title('Get File by INVALID File-ID (non-UUID) (negative)')     # Allure step Title
    def test_get_file_by_invalid_file_id(self, files_client: FilesClient):
        invalid_file_id = 'id_123'                                         # Invalid File-ID (non-UUID format)
        response = files_client.get_file_api(invalid_file_id)              # ▶ Запрос через API-метод с Invalid File-ID

        # Assertions
        assert_status_code(response.status_code, http.HTTPStatus.UNPROCESSABLE_ENTITY) # Status code: 422
        assert_request_method(response.request.method, http.HTTPMethod.GET)            # Method: GET
        assert_get_file_invalid_id_error_response(response)                           # Validation Error Response
        validate_json_schema(response, ErrorResponseSchema)           # JSON schema validation



    @allure.title('Get File by non-existent File-ID (negative)')           # Allure step Title
    def test_get_non_existent_file(self, files_client: FilesClient):
        non_existent_file_id = fake.uuid4()                           # Generate Non-Existent File-ID (UUID format)
        response = files_client.get_file_api(non_existent_file_id)    # ▶ Запрос через API-метод с Non-existent File-ID

        # Assertions
        assert_status_code(response.status_code, http.HTTPStatus.NOT_FOUND)  # Status code: 404
        assert_request_method(response.request.method, http.HTTPMethod.GET)  # Method: GET
        assert_get_file_not_found_error_response(response)                                 # Validation Error Response data
        validate_json_schema(response, NotFoundErrorResponseSchema)    # JSON schema validation

#=======================================================================================================================
        # Tool.api_report(response)
