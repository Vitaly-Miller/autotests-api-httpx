"""
TEST Update Course
"""
import http
import pytest
from clients.courses_client import CoursesClient
from schemas.courses_schema import CreateCourseSchema, UpdateCourseRequestSchema, UpdateCourseResponseSchema
from tools.assertions.base_assert import assert_method, assert_status_code
from tools.assertions.courses_assert import assert_update_course_response_equal
from tools.assertions.schema_assert import validate_json_schema
from tools.tool import Tool

#=======================================================================================================================
@pytest.mark.courses
@pytest.mark.regression
class TestUpdateCourse:
    def test_update_course(self, courses_client: CoursesClient, create_course: CreateCourseSchema):
        update_course_data = UpdateCourseRequestSchema()                            # Pydantic-model with fake-data
        response = courses_client.update_course_api(                                # ▶ Запрос через API-метод
            create_course.response.course.id,
            update_course_data
        )
        # Assertions
        assert_status_code(response, http.HTTPStatus.OK)      # Status code: 200
        assert_method(response, http.HTTPMethod.PATCH)      # Method: PATCH
        assert_update_course_response_equal(response)                               # Request data = Response data
        validate_json_schema(response, UpdateCourseResponseSchema)  # Validation JSON schema


#=======================================================================================================================
        #Tool.api_report(response)
