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
@pytest.mark.courses                                          # ┐ Pytest Marks
@pytest.mark.regression                                       # ┘
@allure.tag(Tag.REGRESSION, Tag.COURSES, Tag.UPDATE)    # ] Allure Tags
@allure.epic(Epic.API)                                        # ┐
@allure.feature(Feature.COURSES)                              # │ Allure Behaviors
@allure.story(Story.UPDATE)                                   # ┘
@allure.severity(allure.severity_level.NORMAL)                # ] Allure Severity
#-----------------------------------------------------------------------------------------------------------------------
class TestUpdateCourse:
    @allure.title('Update Course')                            # Allure step Title
    def test_update_course(self, courses_client: CoursesClient, create_course: CreateCourseSchema):
        new_course_data = UpdateCourseRequestSchema()         # Pydantic-model with fake-data (Update ALL)
        response = courses_client.update_course_api(          # ▶ Запрос через API-метод
            create_course.response.course.id,        # ID обновляемого курса
            new_course_data                    # Обновляемые данные
        )
        response_model = UpdateCourseResponseSchema.model_validate_json(response.text)  # httpx.Response —> Pydantic-model (deserialize)

        # Assertions
        assert_status_code(response.status_code, http.HTTPStatus.OK)          # Status code: 200
        assert_request_method(response.request.method, http.HTTPMethod.PATCH) # Method: PATCH
        assert_update_course_response(response_model, new_course_data)       # Response data = Request data
        validate_json_schema(response, UpdateCourseResponseSchema)           # JSON schema validation


#=======================================================================================================================
        # Tool.api_report(response)          # for PyCharm RUN-console API reporting only
