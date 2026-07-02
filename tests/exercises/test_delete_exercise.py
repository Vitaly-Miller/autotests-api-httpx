"""
TEST Delete Exercise
"""
import http
import pytest
import allure
from clients.exercises_client import ExercisesClient
from schemas.errors_schema import NotFoundErrorResponseSchema
from schemas.exercises_schema import CreateExerciseSchema, GetExerciseResponseSchema
from tools.allure.annotations import Epic, Feature, Story, Tag
from tools.assertions.base_assert import assert_request_method, assert_status_code
from tools.assertions.exercises_assert import assert_exercise_not_found_error_response
from tools.assertions.schema_assert import validate_json_schema
from tools.tool import Tool

#=======================================================================================================================
# Class annotations
@pytest.mark.exercises                                        # ┐ Pytest Marks
@pytest.mark.regression                                       # ┘
@allure.tag(Tag.REGRESSION, Tag.EXERCISES, Tag.DELETE)  # ] Allure Tags
@allure.epic(Epic.API)                                        # ┐
@allure.feature(Feature.EXERCISES)                            # │ Allure Behaviors
@allure.story(Story.DELETE)                                   # ┘
@allure.parent_suite(Epic.API)                                # ┐
@allure.suite(Feature.EXERCISES)                              # │ Allure Suites (optional)
@allure.sub_suite(Story.DELETE)                               # ┘
@allure.severity(allure.severity_level.NORMAL)                # ] Allure Severity
#-----------------------------------------------------------------------------------------------------------------------
class TestDeleteExercise:
    @allure.title('Delete Exercise')                          # Allure step Title
    def test_delete_exercise(self, exercises_client: ExercisesClient, create_exercise: CreateExerciseSchema):
        delete_response = exercises_client.delete_exercise_api(create_exercise.exercise_id)   # ▶ Запрос через API-метод (delete)
        get_response = exercises_client.get_exercise_api(create_exercise.exercise_id)         # ▶ Запрос через API-метод (get)

        # Assertions (Delete Exercise)
        assert_status_code(delete_response.status_code, http.HTTPStatus.OK)  # Status code: 200
        assert_request_method(delete_response.request.method, 'DELETE')      # Method: DELETE

        # Assertions (Get Non-existent Exercise)
        assert_status_code(get_response.status_code, http.HTTPStatus.NOT_FOUND) # Status code: 404
        assert_request_method(get_response.request.method, 'GET')               # Method: GET
        assert_exercise_not_found_error_response(get_response)                            # Error message: "Exercise not found"
        validate_json_schema(get_response, NotFoundErrorResponseSchema)   # JSON schema validation


#=======================================================================================================================
        # Tool.api_report(delete_response)
        # Tool.api_report(get_response)
