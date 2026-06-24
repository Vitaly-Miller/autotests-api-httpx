"""
TEST Get Exercise
"""
import http
import allure
import httpx
import pytest
from allure_commons.types import Severity
from clients.exercises_client import ExercisesClient
from schemas.exercises_schema import CreateExerciseSchema, GetExerciseResponseSchema
from tools.allure.annotations import Epic, Feature, Story, Tag
from tools.assertions.base_assert import assert_method, assert_status_code
from tools.assertions.exercises_assert import assert_exercise_id, assert_get_exercise_response_non_empty
from tools.assertions.schema_assert import validate_json_schema
from tools.tool import Tool

#=======================================================================================================================
# Class annotations
@pytest.mark.exercises                                        # ┐ Pytest Marks
@pytest.mark.regression                                       # ┘
@allure.tag(Tag.EXERCISES, Tag.GET, Tag.REGRESSION)     # ] Allure Tags
@allure.epic(Epic.API)                                        # ┐
@allure.feature(Feature.EXERCISES)                            # │ Allure Behaviors
@allure.story(Story.GET)                                      # ┘
@allure.parent_suite(Epic.API)                                # ┐
@allure.suite(Feature.EXERCISES)                              # │ Allure Suites
@allure.sub_suite(Story.GET)                                  # ┘
@allure.severity(Severity.NORMAL)                             # ] Allure Severity
#-----------------------------------------------------------------------------------------------------------------------
class TestGetExercise:
    @allure.title('Get Exercise (v.1 - Через API-фикстуру полного цикла)')  # — Allure Title
    def test_get_exercise_1(self, get_exercise_api: httpx.Response):        # Через API-фикстуру полного цикла
        response = get_exercise_api                                         # Сохраняем ответ API-фикстуры

        # Assertions
        assert_status_code(response, http.HTTPStatus.OK)      # Status Code: 200
        assert_method(response, http.HTTPMethod.GET)        # Method: GET
        assert_get_exercise_response_non_empty(response)
        assert_exercise_id(response)
        validate_json_schema(response, GetExerciseResponseSchema)   # JSON Schema validation


    @allure.title('Get Exercise (v.2 - Через фикстуры: exercises_client, create_exercise)')   # — Allure Title
    def test_get_exercise_2(
            self,
            exercises_client: ExercisesClient,                        # Фикстура получения экземпляра ExercisesClient()
            create_exercise: CreateExerciseSchema                     # Pydantic-фикстура создания задания
    ):
        response = exercises_client.get_exercise_api(create_exercise.exercise_id)   # ▶ Запрос через API-метод

        # Assertions
        assert_status_code(response, http.HTTPStatus.OK)      # Status Code: 200
        assert_method(response, http.HTTPMethod.GET)        # Method: GET
        assert_get_exercise_response_non_empty(response)
        assert_exercise_id(response)
        validate_json_schema(response, GetExerciseResponseSchema)   # JSON Schema validation

#=======================================================================================================================
        # Tool.api_report(response)
