"""
TEST Get Courses
"""
import http
import pytest
from clients.courses_client import CoursesClient
from schemas.courses_schema import CreateCourseSchema, GetCoursesQwerySchema, GetCoursesResponseSchema
from schemas.users_schema import CreateUserSchema
from tools.assertions.base_assert import assert_method, assert_status_code
from tools.assertions.courses_assert import assert_get_courses_responses
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
        user_id_qwery_model = GetCoursesQwerySchema(userId=create_user.user_id)         # Pydantic-model  qwery-User-ID
        response = courses_client.get_courses_api(user_id_qwery_model)                  # ▶ Запрос через API-метод

        # Assertions
        assert_status_code(response, http.HTTPStatus.OK)        # Status Code: 200
        assert_method(response, http.HTTPMethod.GET)          # Method: GET
        assert_get_courses_responses(response, [create_course.response]) # Список курсов соответствует созданным курсам
        validate_json_schema(response, GetCoursesResponseSchema)      # JSON Schema validation
#=======================================================================================================================
        # Tool.api_report(response)
