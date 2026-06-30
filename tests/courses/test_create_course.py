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
from tools.assertions.courses_assert import assert_create_course_pydantic_response
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
@allure.parent_suite(Epic.API)                                # ┐
@allure.suite(Feature.COURSES)                                # │ Allure Suites (optional)
@allure.sub_suite(Story.CREATE)                               # ┘
@allure.severity(allure.severity_level.NORMAL)   # ] Allure Severity
#-----------------------------------------------------------------------------------------------------------------------
class TestCreateCourse:
    @allure.title('Create Course (v.1 - Через API-фикстуру полного цикла)')         # Allure step Title
    def test_create_course_pydantic_1(self, create_course_api: httpx.Response):              # Через API-фикстуру полного цикла
        response = create_course_api                                                # Сохраняем ответ API-фикстуры

        # Assertions
        assert_status_code(response.status_code, http.HTTPStatus.OK)      # Status Code: 200
        assert_request_method(response.request.method, http.HTTPMethod.POST)       # Method: POST
        assert_create_course_pydantic_response(response)                                     # Response data = Request data
        validate_json_schema(response, CreateCourseResponseSchema)  # JSON Schema validation



    @allure.title('Create Course (v.2 - Через фикстуры: CoursesClient + CreateUser + CreateFile)')   # Allure step Title
    def test_create_course_pydantic_2(
            self,
            courses_client: CoursesClient,                           # Фикстура получения экземпляра CoursesClient()
            create_user_pydantic: CreateUserSchema,                  # Pydantic-фикстура создания пользователя
            create_file_pydantic: CreateFileSchema                   # Pydantic-фикстура создания файла
            ):
        create_course_pydantic_data_model = CreateCourseRequestSchema(        # Инициализация Course Data Model c Fake data
            previewFileId=create_file_pydantic.file_id,              # Fake data —> Реальные данные из фикстуры
            createdByUserId=create_user_pydantic.user_id             # Fake data —> Реальные данные из фикстуры
        )
        response = courses_client.create_course_api(create_course_pydantic_data_model)       # ▶ Запрос через API-метод

        # Assertions
        assert_status_code(response.status_code, http.HTTPStatus.OK)      # Status Code: 200
        assert_request_method(response.request.method, http.HTTPMethod.POST)       # Method: POST
        assert_create_course_pydantic_response(response)                                     # Response data = Request data
        validate_json_schema(response, CreateCourseResponseSchema)  # JSON Schema validation


#=======================================================================================================================
        # Tool.api_report(response)
