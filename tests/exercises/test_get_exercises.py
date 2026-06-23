"""
TEST Get Exercises
"""
import http
import allure
import httpx
import pytest
from tools.allure.annotations import Epic, Feature, Story, Tag
from tools.assertions.base_assert import assert_method, assert_status_code
from tools.tool import Tool

#=======================================================================================================================
@pytest.mark.exercises
@pytest.mark.regression
@allure.tag(Tag.EXERCISES, Tag.GET, Tag.REGRESSION)                                  # Через Enum
@allure.epic(Epic.API)
@allure.feature(Feature.EXERCISES)
@allure.story(Story.GET)
@allure.severity(allure.severity_level.NORMAL)
class TestGetExercises:
    @allure.title('Get Exercises (v.1 - Через API-фикстуры: exercises_client, create_exercise)')
    def test_get_exercises(self, create_exercise_api: httpx.Response, get_exercises_api: httpx.Response):

        # Assertions
        assert_status_code(get_exercises_api, http.HTTPStatus.OK)    # Status code: 200
        assert_method(get_exercises_api, http.HTTPMethod.GET)      # Method: GET


#=======================================================================================================================
        # Tool.api_report(create_exercise_api)
        # Tool.api_report(get_exercises_api)
