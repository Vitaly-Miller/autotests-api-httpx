"""
TEST Create Course
"""
import http
import pytest

from clients.courses_client import CoursesClient
from schemas.courses_schema import CreateCourseRequestSchema
from schemas.files_schema import CreateFileSchema
from schemas.users_schema import CreateUserSchema
from tools.assertions.base_assert import assert_method, assert_status_code
from tools.assertions.courses_assert import assert_create_course_response

from tools.tool import Tool

#=======================================================================================================================
@pytest.mark.courses
@pytest.mark.regression
class TestCreateCourse:
    def test_create_course(
            self,
            courses_client: CoursesClient,
            create_user: CreateUserSchema,
            create_file: CreateFileSchema
            ):
        create_course_data_model = CreateCourseRequestSchema(             # Инициализация Course Data Model c Fake data
            previewFileId=create_file.file_id,                            # Fake data —> Реальные данные из фикстуры
            createdByUserId=create_user.user_id                           # Fake data —> Реальные данные из фикстуры
        )
        response = courses_client.create_course_api(create_course_data_model)   # ▶ Запрос через API-метод

        # Assertions
        assert_status_code(response, http.HTTPStatus.OK)  # Status Code: 200
        assert_method(response, http.HTTPMethod.POST)   # Method: POST
        assert_create_course_response(response)                         # Response data = Request data



#=======================================================================================================================
    # Tool.api_report(response)
