"""
TEST Update Exercise
"""
import http
import allure
import httpx
import pytest
from clients.exercises_client import ExercisesClient
from schemas.exercises_schema import CreateExerciseSchema, UpdateExerciseRequestSchema, UpdateExerciseResponseSchema
from tools.allure.tags import Tag
from tools.assertions.base_assert import assert_method, assert_status_code
from tools.assertions.exercises_assert import assert_update_exercise_response
from tools.assertions.schema_assert import validate_json_schema
from tools.tool import Tool

#=======================================================================================================================
@pytest.mark.exercises
@pytest.mark.regression
@allure.tag(Tag.EXERCISES, Tag.UPDATE, Tag.REGRESSION)                  # Через Enum
class TestUpdateExercise:
    @allure.title('Update Exercise (v.1 - Через API-фикстуру полного цикла)')
    def test_update_exercise_1(self, update_exercise_api: httpx.Response):    # Через API-фикстуру полного цикла
        response = update_exercise_api                                        # Сохраняем ответ API-фикстуры

        # Assertions
        assert_status_code(response, http.HTTPStatus.OK)        # Status code: 200
        assert_method(response, http.HTTPMethod.PATCH)        # Method: PATCH
        assert_update_exercise_response(response)                                     # Response data = Request data
        validate_json_schema(response, UpdateExerciseResponseSchema)  # Validate JSON schema



    @allure.title('Update Exercise (v.2 - Через фикстуры: exercises_client, create_exercise)')
    def test_update_exercise_2(self, exercises_client: ExercisesClient, create_exercise: CreateExerciseSchema):
        new_exercise_data = UpdateExerciseRequestSchema()       # Pydantic-model with fake-data (Update ALL data)
        response = exercises_client.update_exercise_api(        # ▶ Запрос через API-метод
            create_exercise.exercise_id,              # Передаем Exercise ID
            new_exercise_data                   # Передаем Pydantic-model c данными, которые необходимо обновить
        )

        # Assertions
        assert_status_code(response, http.HTTPStatus.OK)        # Status code: 200
        assert_method(response, http.HTTPMethod.PATCH)        # Method: PATCH
        assert_update_exercise_response(response)                                     # Response data = Request data
        validate_json_schema(response, UpdateExerciseResponseSchema)  # Validate JSON schema

#=======================================================================================================================
        # Tool.api_report(response)
