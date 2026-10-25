"""
TEST Update Course
"""
import http
import pytest
import allure
from clients.courses_client import CoursesClient
from schemas.courses_schema import CreateCourseSchema, UpdateCourseRequestSchema, UpdateCourseResponseSchema
from tools.allure.annotations import Epic, Feature, Story, Tag
from tools.assertions.base_assert import assert_request_method, assert_status_code
from tools.assertions.courses_assert import assert_update_course_response
from tools.assertions.schema_assert import validate_json_schema
from tools.tool import Tool

#=======================================================================================================================
# Class annotations
@pytest.mark.courses
@pytest.mark.regression
@allure.tag(Tag.REGRESSION, Tag.COURSES, Tag.UPDATE)
@allure.epic(Epic.API)
@allure.feature(Feature.COURSES)
@allure.story(Story.UPDATE)
@allure.severity(allure.severity_level.NORMAL)
#-----------------------------------------------------------------------------------------------------------------------
class TestUpdateCourse:
    @allure.title('Update Course')
    def test_update_course(self, courses_client: CoursesClient, create_course: CreateCourseSchema):
        new_course_data = UpdateCourseRequestSchema()
        response = courses_client.update_course_api(
            create_course.response.course.id,
            new_course_data
        )
        response_model = UpdateCourseResponseSchema.model_validate_json(response.text)

        # Assertions
        assert_status_code(response.status_code, http.HTTPStatus.OK)
        assert_request_method(response.request.method, http.HTTPMethod.PATCH)
        assert_update_course_response(response_model, new_course_data)
        validate_json_schema(response, UpdateCourseResponseSchema)


#=======================================================================================================================
        # Tool.api_report(response)          # for PyCharm RUN-console API reporting only
