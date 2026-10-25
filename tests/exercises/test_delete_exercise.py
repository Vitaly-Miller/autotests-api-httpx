"""
TEST Delete Exercise
"""
import http
import pytest
import allure
from clients.exercises_client import ExercisesClient
from schemas.errors_schema import NotFoundErrorResponseSchema
from schemas.exercises_schema import CreateExerciseSchema
from tools.allure.annotations import Epic, Feature, Story, Tag
from tools.assertions.base_assert import assert_request_method, assert_status_code
from tools.assertions.exercises_assert import assert_exercise_not_found_error_response
from tools.assertions.schema_assert import validate_json_schema
from tools.tool import Tool

#=======================================================================================================================
# Class annotations
@pytest.mark.exercises
@pytest.mark.regression
@allure.tag(Tag.REGRESSION, Tag.EXERCISES, Tag.DELETE)
@allure.epic(Epic.API)
@allure.feature(Feature.EXERCISES)
@allure.story(Story.DELETE)
@allure.severity(allure.severity_level.NORMAL)
#-----------------------------------------------------------------------------------------------------------------------
class TestDeleteExercise:
    @allure.title('Delete Exercise')
    def test_delete_exercise(self, exercises_client: ExercisesClient, create_exercise: CreateExerciseSchema):
        delete_response = exercises_client.delete_exercise_api(create_exercise.exercise_id)
        get_response = exercises_client.get_exercise_api(create_exercise.exercise_id)

        # Assertions (Delete Exercise)
        assert_status_code(delete_response.status_code, http.HTTPStatus.OK)
        assert_request_method(delete_response.request.method, 'DELETE')

        # Assertions (Get Non-existent Exercise)
        assert_status_code(get_response.status_code, http.HTTPStatus.NOT_FOUND)
        assert_request_method(get_response.request.method, 'GET')
        assert_exercise_not_found_error_response(get_response)
        validate_json_schema(get_response, NotFoundErrorResponseSchema)


#=======================================================================================================================
        # Tool.api_report(delete_response)
        # Tool.api_report(get_response)
