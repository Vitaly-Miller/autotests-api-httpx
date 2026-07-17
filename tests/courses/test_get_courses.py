"""
TEST Get Courses
"""
import httpx
import http
import pytest
import allure
from clients.courses_client import CoursesClient
from schemas.courses_schema import CreateCourseSchema, GetCoursesQwerySchema, GetCoursesResponseSchema
from schemas.users_schema import CreateUserSchema
from tools.allure.annotations import Epic, Feature, Story, Tag
from tools.assertions.base_assert import assert_request_method, assert_status_code
from tools.assertions.courses_assert import assert_get_courses_responses
from tools.assertions.schema_assert import validate_json_schema
from tools.tool import Tool

#=======================================================================================================================
# Class annotations
@pytest.mark.courses                                          # ┐ Pytest Marks
@pytest.mark.regression                                       # ┘
@allure.tag(Tag.REGRESSION, Tag.COURSES, Tag.GET)       # ] Allure Tags
@allure.epic(Epic.API)                                        # ┐
@allure.feature(Feature.COURSES)                              # │ Allure Behaviors
@allure.story(Story.GET)                                      # ┘
@allure.severity(allure.severity_level.NORMAL)                # ] Allure Severity
#-----------------------------------------------------------------------------------------------------------------------
class TestGetCourses:
    @allure.title('Get Courses (v.1 - Через фикстуру полного цикла)')
    def test_get_courses_1(self, create_course: CreateCourseSchema, get_courses_api: httpx.Response):
        response = get_courses_api                                                    # Сохранение ответа API-фикстуры
        response_model = GetCoursesResponseSchema.model_validate_json(response.text)  # httpx.Response —> Pydantic-model (deserialize)

        # Assertions
        assert_status_code(response.status_code, http.HTTPStatus.OK)         # Status Code: 200
        assert_request_method(response.request.method, http.HTTPMethod.GET)  # Method: GET
        assert_get_courses_responses(
            response_model,
            [create_course.response])                           # Список курсов соответствует созданным курсам
        validate_json_schema(response, GetCoursesResponseSchema)     # JSON Schema validation


    @allure.title('Get Courses (v.1 - Через Pydantic-фикстуры)')
    def test_get_courses_2(
            self,
            courses_client: CoursesClient,
            create_user: CreateUserSchema,                                           # Для User-ID
            create_course: CreateCourseSchema
    ):
        user_id_qwery_model = GetCoursesQwerySchema(userId=create_user.user_id)       # Pydantic-model
        response = courses_client.get_courses_api(user_id_qwery_model)                # ▶ Запрос через API-метод
        response_model = GetCoursesResponseSchema.model_validate_json(response.text)  # httpx.Response —> Pydantic-model (deserialize)

        # Assertions
        assert_status_code(response.status_code, http.HTTPStatus.OK)         # Status Code: 200
        assert_request_method(response.request.method, http.HTTPMethod.GET)  # Method: GET
        assert_get_courses_responses(
            response_model,
            [create_course.response]                              # Список курсов соответствует созданным курсам
        )
        validate_json_schema(response, GetCoursesResponseSchema)       # JSON Schema validation


#=======================================================================================================================
        # Tool.api_report(response)          # for PyCharm RUN-console API reporting only
