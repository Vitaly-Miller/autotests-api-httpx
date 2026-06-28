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
from tools.assertions.base_assert import assert_method, assert_status_code
from tools.assertions.exercises_assert import assert_update_exercise_response
from tools.assertions.schema_assert import validate_json_schema
from tools.tool import Tool

#=======================================================================================================================
# Class annotations
@pytest.mark.exercises                                        # ┐ Pytest Marks
@pytest.mark.regression                                       # ┘
@allure.tag(Tag.REGRESSION, Tag.EXERCISES, Tag.UPDATE)  # ] Allure Tags
@allure.epic(Epic.API)                                        # ┐
@allure.feature(Feature.EXERCISES)                            # │ Allure Behaviors
@allure.story(Story.UPDATE)                                   # ┘
@allure.parent_suite(Epic.API)                                # ┐
@allure.suite(Feature.EXERCISES)                              # │ Allure Suites (optional)
@allure.sub_suite(Story.UPDATE)                               # ┘
@allure.severity(allure.severity_level.NORMAL)                # ] Allure Severity
#-----------------------------------------------------------------------------------------------------------------------
class TestUpdateExercise:
    @allure.title('Update Exercise (v.1 - Через API-фикстуру полного цикла)') # — Allure Title
    def test_update_exercise_1(self, update_exercise_api: httpx.Response):    # Через API-фикстуру полного цикла
        response = update_exercise_api                                        # Сохраняем ответ API-фикстуры

        # Assertions
        assert_status_code(response, http.HTTPStatus.OK)        # Status code: 200
        assert_method(response, http.HTTPMethod.PATCH)        # Method: PATCH
        assert_update_exercise_response(response)                                     # Response data = Request data
        validate_json_schema(response, UpdateExerciseResponseSchema)  # Validate JSON schema



    @allure.title('Update Exercise (v.2 - Через фикстуры: exercises_client, create_exercise_pydantic)')  # — Allure Title
    def test_update_exercise_2(self, exercises_client: ExercisesClient, create_exercise_pydantic: CreateExerciseSchema):
        new_exercise_data = UpdateExerciseRequestSchema()       # Pydantic-model with fake-data (Update ALL data)
        response = exercises_client.update_exercise_api(        # ▶ Запрос через API-метод
            create_exercise_pydantic.exercise_id,              # Передаем Exercise ID
            new_exercise_data                   # Передаем Pydantic-model c данными, которые необходимо обновить
        )

        # Assertions
        assert_status_code(response, http.HTTPStatus.OK)        # Status code: 200
        assert_method(response, http.HTTPMethod.PATCH)        # Method: PATCH
        assert_update_exercise_response(response)                                     # Response data = Request data
        validate_json_schema(response, UpdateExerciseResponseSchema)  # Validate JSON schema


#=======================================================================================================================
        # Tool.api_report(response)
