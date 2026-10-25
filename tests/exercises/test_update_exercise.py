"""
TEST Update Exercise
"""
import httpx
import http
import pytest
import allure
from clients.exercises_client import ExercisesClient
from schemas.exercises_schema import CreateExerciseSchema, UpdateExerciseRequestSchema, UpdateExerciseResponseSchema
from tools.allure.annotations import Epic, Feature, Story, Tag
from tools.assertions.base_assert import assert_request_method, assert_status_code
from tools.assertions.exercises_assert import assert_update_exercise_response
from tools.assertions.schema_assert import validate_json_schema
from tools.tool import Tool

#=======================================================================================================================
# Class annotations
@pytest.mark.exercises
@pytest.mark.regression
@allure.tag(Tag.REGRESSION, Tag.EXERCISES, Tag.UPDATE)
@allure.epic(Epic.API)
@allure.feature(Feature.EXERCISES)
@allure.story(Story.UPDATE)
@allure.severity(allure.severity_level.NORMAL)
#-----------------------------------------------------------------------------------------------------------------------
class TestUpdateExercise:
    @allure.title('Update Exercise (v.1 - Via full-cycle API fixture)')
    def test_update_exercise_1(self, update_exercise_api: httpx.Response):
        response = update_exercise_api

        # Assertions
        assert_status_code(response.status_code, http.HTTPStatus.OK)
        assert_request_method(response.request.method, http.HTTPMethod.PATCH)
        validate_json_schema(response, UpdateExerciseResponseSchema)


    @allure.title('Update Exercise (v.2 - Via fixtures: exercises_client, create_exercise)')
    def test_update_exercise_2(self, exercises_client: ExercisesClient, create_exercise: CreateExerciseSchema):
        new_exercise_data = UpdateExerciseRequestSchema()
        response = exercises_client.update_exercise_api(
            create_exercise.exercise_id,
            new_exercise_data
        )
        response_model = UpdateExerciseResponseSchema.model_validate_json(response.text)
        # Assertions
        assert_status_code(response.status_code, http.HTTPStatus.OK)
        assert_request_method(response.request.method, http.HTTPMethod.PATCH)
        assert_update_exercise_response(response_model, new_exercise_data)
        validate_json_schema(response, UpdateExerciseResponseSchema)


#=======================================================================================================================
        # Tool.api_report(response)          # for PyCharm RUN-console API reporting only
