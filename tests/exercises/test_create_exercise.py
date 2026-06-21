"""
TEST Create Exercise
"""
import http
import httpx
import pytest
from clients.exercises_client import ExercisesClient
from schemas.courses_schema import CreateCourseSchema
from schemas.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema
from tools.assertions.base_assert import assert_method, assert_status_code
from tools.assertions.schema_assert import validate_json_schema
from tools.assertions.exercises_assert import (
    assert_create_exercise_response,
    assert_create_exercise_response_non_empty,
    assert_exercise_id
)
from tools.tool import Tool

#=======================================================================================================================
@pytest.mark.exercises
@pytest.mark.regression
class TestCreateExercise:
    def test_create_exercise_1(self, create_exercise_api: httpx.Response):     # Через API-фикстуру полного цикла        ─┐
        response = create_exercise_api                                         # Сохраняем ответ API-фикстуры            ─┘

        # Assertions
        assert_status_code(response, http.HTTPStatus.OK)        # Status Code: 200
        assert_method(response, http.HTTPMethod.POST)         # Method: POST
        assert_create_exercise_response_non_empty(response)                           # Response data is NON-empty
        assert_create_exercise_response(response)                                     # Response data = Request data
        assert_exercise_id(response)                                                  # Exercise ID validation
        validate_json_schema(response, CreateExerciseResponseSchema)  # JSON Schema validation



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
