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
@pytest.mark.courses
@pytest.mark.regression
@allure.tag(Tag.REGRESSION, Tag.COURSES, Tag.CREATE)
@allure.epic(Epic.API)
@allure.feature(Feature.COURSES)
@allure.story(Story.CREATE)
@allure.severity(allure.severity_level.NORMAL)
#-----------------------------------------------------------------------------------------------------------------------
class TestCreateCourse:
    @allure.title('Create Course (v.1 - Via full-cycle API fixture)')
    def test_create_course_1(self, create_course_api: httpx.Response):
        response = create_course_api
        response_model = CreateCourseResponseSchema.model_validate_json(response.text)
        request_model = CreateCourseRequestSchema.model_validate_json(response.request.content)

        # Assertions
        assert_status_code(response.status_code, http.HTTPStatus.OK)
        assert_request_method(response.request.method, http.HTTPMethod.POST)
        assert_create_course_response(response_model, request_model)
        validate_json_schema(response, CreateCourseResponseSchema)


    @allure.title('Create Course (v.2 - Via Pydantic fixtures)')
    def test_create_course_2(
            self,
            courses_client: CoursesClient,
            create_user: CreateUserSchema,
            create_file: CreateFileSchema
            ):

        create_course_data_model = CreateCourseRequestSchema(
            previewFileId=create_file.file_id,
            createdByUserId=create_user.user_id
        )
        response = courses_client.create_course_api(create_course_data_model)
        response_model = CreateCourseResponseSchema.model_validate_json(response.text)

        # Assertions
        assert_status_code(response.status_code, http.HTTPStatus.OK)
        assert_request_method(response.request.method, http.HTTPMethod.POST)
        assert_create_course_response(response_model, create_course_data_model)
        validate_json_schema(response, CreateCourseResponseSchema)


#=======================================================================================================================
        # Tool.api_report(response)          # for PyCharm RUN-console API reporting only
