"""
TEST Get Exercise
"""
import httpx
import http
import pytest
import allure
from clients.exercises_client import ExercisesClient
from schemas.exercises_schema import CreateExerciseSchema, GetExerciseResponseSchema
from tools.allure.annotations import Epic, Feature, Story, Tag
from tools.assertions.base_assert import assert_request_method, assert_status_code
from tools.assertions.exercises_assert import assert_exercise_id, assert_get_exercise_response_non_empty
from tools.assertions.schema_assert import validate_json_schema
from tools.tool import Tool

#=======================================================================================================================
# Class annotations
@pytest.mark.exercises
@pytest.mark.regression
@allure.tag(Tag.REGRESSION, Tag.EXERCISES, Tag.GET)
@allure.epic(Epic.API)
@allure.feature(Feature.EXERCISES)
@allure.story(Story.GET)
@allure.severity(allure.severity_level.NORMAL)
#-----------------------------------------------------------------------------------------------------------------------
class TestGetExercise:
    @allure.title('Get Exercise (v.1 - Via full-cycle API fixture)')
    def test_get_exercise_1(self, get_exercise_api: httpx.Response):
        response = get_exercise_api
        response_model = GetExerciseResponseSchema.model_validate_json(response.text)

        # Assertions
        assert_status_code(response.status_code, http.HTTPStatus.OK)
        assert_request_method(response.request.method, http.HTTPMethod.GET)
        assert_get_exercise_response_non_empty(response_model)
        assert_exercise_id(response_model)
        validate_json_schema(response, GetExerciseResponseSchema)


    @allure.title('Get Exercise (v.2 - Via fixtures: exercises_client, create_exercise)')
    def test_get_exercise_2(
            self,
            exercises_client: ExercisesClient,
            create_exercise: CreateExerciseSchema
    ):
        response = exercises_client.get_exercise_api(create_exercise.exercise_id)
        response_model = GetExerciseResponseSchema.model_validate_json(response.text)

        # Assertions
        assert_status_code(response.status_code, http.HTTPStatus.OK)
        assert_request_method(response.request.method, http.HTTPMethod.GET)
        assert_get_exercise_response_non_empty(response_model)
        assert_exercise_id(response_model)
        validate_json_schema(response, GetExerciseResponseSchema)


#=======================================================================================================================
        # Tool.api_report(response)          # for PyCharm RUN-console API reporting only
