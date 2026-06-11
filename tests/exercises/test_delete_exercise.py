"""
TEST Delete Exercise
"""
import http
import pytest
from clients.exercises_client import ExercisesClient
from schemas.errors_schema import NotFoundErrorResponseSchema
from schemas.exercises_schema import CreateExerciseSchema
from tools.assertions.base_assert import assert_method, assert_status_code
from tools.assertions.exercises_assert import assert_exercise_not_found_error_response
from tools.assertions.schema_assert import validate_json_schema
from tools.tool import Tool

#=======================================================================================================================
@pytest.mark.exercises
@pytest.mark.regression
class TestDeleteExercise:
    def test_delete_exercise(self, exercises_client: ExercisesClient, create_exercise: CreateExerciseSchema):
        delete_response = exercises_client.delete_exercise_api(create_exercise.exercise_id) # ▶ Запрос через API-метод
        get_response = exercises_client.get_exercise_api(create_exercise.exercise_id)       # ▶ Запрос через API-метод

        # Assertions (Delete Exercise)
        assert_status_code(delete_response, http.HTTPStatus.OK)      # Status code: 200
        assert_method(delete_response, 'DELETE')                   # Method: DELETE

        # Assertions (Get Non-existent Exercise)
        assert_status_code(get_response, http.HTTPStatus.NOT_FOUND)  # Status code: 404
        assert_method(get_response, 'GET')                         # Method: GET
        assert_exercise_not_found_error_response(get_response)                             # Error message: "Exercise not found"
        validate_json_schema(get_response, NotFoundErrorResponseSchema)    # Validation JSON schema



#=======================================================================================================================
        # Tool.api_report(delete_response)
        # Tool.api_report(get_response)
