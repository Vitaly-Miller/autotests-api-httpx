"""
TEST Create Exercise
"""
import http
import allure
import httpx
import pytest
from allure_commons.types import Severity
from clients.exercises_client import ExercisesClient
from schemas.courses_schema import CreateCourseSchema
from schemas.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema
from tools.allure.annotations import Epic, Feature, Story, Tag
from tools.assertions.base_assert import assert_method, assert_status_code
from tools.assertions.schema_assert import validate_json_schema
from tools.assertions.exercises_assert import (
    assert_create_exercise_response,
    assert_create_exercise_response_non_empty,
    assert_exercise_id
)
from tools.tool import Tool

#=======================================================================================================================
# Class annotations
@pytest.mark.exercises                                        # ┐ Pytest Marks
@pytest.mark.regression                                       # ┘
@allure.tag(Tag.REGRESSION, Tag.EXERCISES, Tag.CREATE)  # ] Allure Tags
@allure.epic(Epic.API)                                        # ┐
@allure.feature(Feature.EXERCISES)                            # │ Allure Behaviors
@allure.story(Story.CREATE)                                   # ┘
@allure.parent_suite(Epic.API)                                # ┐
@allure.suite(Feature.EXERCISES)                              # │ Allure Suites (optional)
@allure.sub_suite(Story.CREATE)                               # ┘
@allure.severity(Severity.NORMAL)                             # ] Allure Severity
#-----------------------------------------------------------------------------------------------------------------------
class TestCreateExercise:
    @allure.title('Create Exercise (v.1 - Через API-фикстуру полного цикла)')  # — Allure Title
    def test_create_exercise_1(self, create_exercise_api: httpx.Response):     # Через API-фикстуру полного цикла        ─┐
        response = create_exercise_api                                         # Сохраняем ответ API-фикстуры            ─┘

        # Assertions
        assert_status_code(response, http.HTTPStatus.OK)        # Status Code: 200
        assert_method(response, http.HTTPMethod.POST)         # Method: POST
        assert_create_exercise_response_non_empty(response)                           # Response data is NON-empty
        assert_create_exercise_response(response)                                     # Response data = Request data
        assert_exercise_id(response)                                                  # Exercise ID validation
        validate_json_schema(response, CreateExerciseResponseSchema)  # JSON Schema validation



    @allure.title('Create Exercise (v.2 - Через фикстуры: exercises_client, create_course)')  # — Allure Title
    def test_create_exercise_2(                                       #                                                  ─┐
            self,                                                     #                                                   │
            exercises_client: ExercisesClient,                        # Фикстура получения экземпляра ExercisesClient()   │
            create_course: CreateCourseSchema                         # Pydantic-фикстура создания курса                  │
    ):                                                                #                                                   │
        create_exercise_data = CreateExerciseRequestSchema(           # Pydantic-model c fake-data                        │
            courseId=create_course.course_id                          # Fake data —> Реальное значение из фикстуры        │
        )                                                             #                                                   │
        response = exercises_client.create_exercise_api(create_exercise_data)         # ▶ Запрос через API-метод         ─┘

        # Assertions
        assert_status_code(response, http.HTTPStatus.OK)        # Status Code: 200
        assert_method(response, http.HTTPMethod.POST)         # Method: POST
        assert_create_exercise_response_non_empty(response)                           # Response data is NON-empty
        assert_create_exercise_response(response)                                     # Response data = Request data
        assert_exercise_id(response)                                                  # Exercise ID validation
        validate_json_schema(response, CreateExerciseResponseSchema)  # JSON Schema validation


#=======================================================================================================================
        # Tool.api_report(response)
