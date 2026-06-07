"""
TEST Create Exercises
"""
import http
import pytest
from clients.exercises_client import ExercisesClient
from schemas.courses_schema import CreateCourseSchema
from schemas.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema
from schemas.users_schema import CreateUserSchema
from tools.assertions.base_assert import assert_method, assert_status_code
from tools.assertions.exercises_assert import (
    assert_create_exercise_response,
    assert_create_exercise_response_non_empty, assert_exercise_id
)
from tools.assertions.schema_assert import validate_json_schema

#=======================================================================================================================
@pytest.mark.exercises
@pytest.mark.regression
class TestCreateExercise:
    def test_create_exercise(
            self,
            exercises_client: ExercisesClient,                        # Фикстура получения экземпляра ExercisesClient()
            create_user: CreateUserSchema,                            # Pydantic-фикстура создания пользователя
            create_course: CreateCourseSchema                         # Pydantic-фикстура создания курса
            ):
        create_exercise_data = CreateExerciseRequestSchema(           # Pydantic-model c fake-data
            courseId=create_course.course_id                          # Fake data —> Реальное значение из фикстуры
        )
        response = exercises_client.create_exercise_api(create_exercise_data)         # ▶ Запрос через API-метод

        # Assertions
        assert_status_code(response, http.HTTPStatus.OK)        # Status Code: 200
        assert_method(response, http.HTTPMethod.POST)         # Method: POST
        assert_create_exercise_response_non_empty(response)                           # Response data is NON-empty
        assert_create_exercise_response(response)                                     # Response data = Request data
        assert_exercise_id(response)                                                  # Exercise ID validation
        validate_json_schema(response, CreateExerciseResponseSchema)  # Validate JSON Schema

#-----------------------------------------------------------------------------------------------------------------------
