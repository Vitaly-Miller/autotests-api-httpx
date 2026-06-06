"""
TEST Get Courses
"""
import http
import pytest

from clients.courses_client import CoursesClient
from schemas.courses_schema import CreateCourseSchema, GetCoursesQwerySchema, GetCoursesResponseSchema
from schemas.users_schema import CreateUserSchema
from tools.assertions.base_assert import assert_method, assert_status_code
from tools.assertions.courses_assert import assert_get_courses_responses_equal
from tools.assertions.schema_assert import validate_json_schema
from tools.tool import Tool

#=======================================================================================================================
@pytest.mark.courses
@pytest.mark.regression
class TestGetCourses:
    def test_get_courses(
            self,
            courses_client: CoursesClient,
            create_user: CreateUserSchema,
            create_course: CreateCourseSchema
    ):

        qwery_user_id = GetCoursesQwerySchema(userId=create_user.user_id)                 # Инициализация QWERY c User ID
        response = courses_client.get_courses_api(qwery_user_id)                          # ▶ Запрос через API-метод

        # Assertions
        assert_status_code(response, http.HTTPStatus.OK)    # Status Code: 200
        assert_method(response, http.HTTPMethod.GET)      # Method: GET
        assert_get_courses_responses_equal(response, [create_course.response])
        validate_json_schema(response, GetCoursesResponseSchema)  # Validate JSON Schema
#=======================================================================================================================
        # Tool.api_report(response)
1
