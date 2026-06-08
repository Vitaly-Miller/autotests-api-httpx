"""
TEST Get Exercise
"""
import http
import pytest
from clients.exercises_client import ExercisesClient
from schemas.exercises_schema import CreateExerciseSchema
from tools.assertions.base_assert import assert_method, assert_status_code
from tools.tool import Tool

#=======================================================================================================================
@pytest.mark.exercises
@pytest.mark.regression
class TestGetExercise:
    def test_get_exercise(
            self,
            exercises_client: ExercisesClient,                        # Фикстура получения экземпляра ExercisesClient()
            create_exercise: CreateExerciseSchema                     # Pydantic-фикстура создания задания
    ):
        response = exercises_client.get_exercise_api(create_exercise.exercise_id)  # ▶ Запрос через API-метод (Получение задания)

        # Assertions
        assert_status_code(response, http.HTTPStatus.OK)        # Status Code: 200
        assert_method(response, http.HTTPMethod.GET)          # Method: GET


#=======================================================================================================================
        # Tool.api_report(response)
