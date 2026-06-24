"""
TEST Update Course
"""
import http
import allure
import pytest
from allure_commons.types import Severity
from clients.courses_client import CoursesClient
from schemas.courses_schema import CreateCourseSchema, UpdateCourseRequestSchema, UpdateCourseResponseSchema
from tools.allure.annotations import Epic, Feature, Story, Tag
from tools.assertions.base_assert import assert_method, assert_status_code
from tools.assertions.courses_assert import assert_update_course_response
from tools.assertions.schema_assert import validate_json_schema
from tools.tool import Tool

#=======================================================================================================================
# Class annotations
@pytest.mark.courses                                          # ┐ Pytest Marks
@pytest.mark.regression                                       # ┘
@allure.tag(Tag.COURSES, Tag.UPDATE, Tag.REGRESSION)    # ] Allure Tags
@allure.epic(Epic.API)                                        # ┐
@allure.feature(Feature.COURSES)                              # │ Allure Behaviors
@allure.story(Story.UPDATE)                                   # ┘
@allure.parent_suite(Epic.API)                                # ┐
@allure.suite(Feature.COURSES)                                # │ Allure Suites
@allure.sub_suite(Story.UPDATE)                               # ┘
@allure.severity(Severity.NORMAL)                             # ] Allure Severity
#-----------------------------------------------------------------------------------------------------------------------
class TestUpdateCourse:
    @allure.title('Update Course')                            # — Allure Title
    def test_update_course(self, courses_client: CoursesClient, create_course: CreateCourseSchema):
        new_course_data = UpdateCourseRequestSchema()         # Pydantic-model with fake-data (Update ALL)
        response = courses_client.update_course_api(          # ▶ Запрос через API-метод
            create_course.response.course.id,
            new_course_data
        )

        # Assertions
        assert_status_code(response, http.HTTPStatus.OK)       # Status code: 200
        assert_method(response, http.HTTPMethod.PATCH)       # Method: PATCH
        assert_update_course_response(response)                                      # Response data = Request data
        validate_json_schema(response, UpdateCourseResponseSchema)   # Validation JSON schema


#=======================================================================================================================
        # Tool.api_report(response)
