"""
TEST Create Course
"""
import httpx
import http
import pytest
import allure
from clients.courses_client import CoursesClient
from schemas.courses_schema import CreateCourseRequestSchema, CreateCourseResponseSchema
from schemas.files_schema import CreateFileSchema
from schemas.users_schema import CreateUserSchema
from tools.allure.annotations import Epic, Feature, Story, Tag
from tools.assertions.base_assert import assert_request_method, assert_status_code
from tools.assertions.courses_assert import assert_create_course_response
from tools.assertions.schema_assert import validate_json_schema
from tools.tool import Tool

#=======================================================================================================================
# Class annotations
@pytest.mark.courses                                          # ┐ Pytest Marks
@pytest.mark.regression                                       # ┘
@allure.tag(Tag.REGRESSION, Tag.COURSES, Tag.CREATE)    # ] Allure Tags
@allure.epic(Epic.API)                                        # ┐
@allure.feature(Feature.COURSES)                              # │ Allure Behaviors
@allure.story(Story.CREATE)                                   # ┘
@allure.severity(allure.severity_level.NORMAL)                # ] Allure Severity
#-----------------------------------------------------------------------------------------------------------------------
class TestCreateCourse:
    @allure.title('Create Course (v.1 - Via full-cycle API fixture)')
    def test_create_course_1(self, create_course_api: httpx.Response):              # Via full-cycle API fixture
        response = create_course_api                                                # Save API fixture response
        response_model = CreateCourseResponseSchema.model_validate_json(response.text)           # httpx.Response —> Pydantic-model (deserialize)
        request_model = CreateCourseRequestSchema.model_validate_json(response.request.content)  # Request —> Pydantic-model

        # Assertions
        assert_status_code(response.status_code, http.HTTPStatus.OK)             # Status Code: 200
        assert_request_method(response.request.method, http.HTTPMethod.POST)     # Method: POST
        assert_create_course_response(response_model, request_model)            # Response data = Request data
        validate_json_schema(response, CreateCourseResponseSchema)              # JSON Schema validation


    @allure.title('Create Course (v.2 - Via Pydantic fixtures)')
    def test_create_course_2(
            self,
            courses_client: CoursesClient,                           # Fixture providing an instance of CoursesClient()
            create_user: CreateUserSchema,                           # Pydantic fixture creating a user
            create_file: CreateFileSchema                            # Pydantic fixture creating a file
            ):

        create_course_data_model = CreateCourseRequestSchema(        # Initialize Pydantic model with fake data
            previewFileId=create_file.file_id,                       # Fake data —> real data from fixture
            createdByUserId=create_user.user_id                      # Fake data —> real data from fixture
        )
        response = courses_client.create_course_api(create_course_data_model)           # ▶ Request via API method
        response_model = CreateCourseResponseSchema.model_validate_json(response.text)  # httpx.Response —> Pydantic-model (deserialize)

        # Assertions
        assert_status_code(response.status_code, http.HTTPStatus.OK)             # Status Code: 200
        assert_request_method(response.request.method, http.HTTPMethod.POST)     # Method: POST
        assert_create_course_response(response_model, create_course_data_model) # Response data = Request data
        validate_json_schema(response, CreateCourseResponseSchema)              # JSON Schema validation


#=======================================================================================================================
        # Tool.api_report(response)          # for PyCharm RUN-console API reporting only
