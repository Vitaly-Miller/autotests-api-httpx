"""
TEST Update Exercise
"""
import http
import httpx
import pytest
from clients.exercises_client import ExercisesClient
from schemas.exercises_schema import CreateExerciseSchema, UpdateExerciseRequestSchema
from tools.assertions.base_assert import assert_method, assert_status_code
from tools.tool import Tool

#=======================================================================================================================
@pytest.mark.exercise
@pytest.mark.regression
class TestUpdateExercise:
    def test_update_exercise_1(self, update_exercise_api: httpx.Response):    # Через API-фикстуру полного цикла
        response = update_exercise_api                                        # Сохраняем ответ API-фикстуры

        # Assertions
        assert_status_code(response, http.HTTPStatus.OK)     # Status code: 200
        assert_method(response, http.HTTPMethod.PATCH)     # Method: PATCH



    def test_update_exercise_2(self, exercises_client: ExercisesClient, create_exercise: CreateExerciseSchema):
        new_exercise_data = UpdateExerciseRequestSchema()                  # Pydantic-model with fake-data (Update ALL)
        response = exercises_client.update_exercise_api(                   # ▶ Запрос через API-метод
            create_exercise.exercise_id,
            new_exercise_data
        )
        # Assertions
        assert_status_code(response, http.HTTPStatus.OK)     # Status code: 200
        assert_method(response, http.HTTPMethod.PATCH)     # Method: PATCH


#=======================================================================================================================
        #Tool.api_report(response)
