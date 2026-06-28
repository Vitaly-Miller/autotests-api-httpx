"""
TEST Get Exercises
"""
import httpx
import http
import pytest
import allure
from tools.allure.annotations import Epic, Feature, Story, Tag
from tools.assertions.base_assert import assert_method, assert_status_code
from tools.tool import Tool

#=======================================================================================================================
# Class annotations
@pytest.mark.exercises                                        # ┐ Pytest Marks
@pytest.mark.regression                                       # ┘
@allure.tag(Tag.REGRESSION, Tag.EXERCISES, Tag.GET)     # ] Allure Tags
@allure.epic(Epic.API)                                        # ┐
@allure.feature(Feature.EXERCISES)                            # │ Allure Behaviors
@allure.story(Story.GET)                                      # ┘
@allure.parent_suite(Epic.API)                                # ┐
@allure.suite(Feature.EXERCISES)                              # │ Allure Suites (optional)
@allure.sub_suite(Story.GET)                                  # ┘
@allure.severity(allure.severity_level.NORMAL)                # ] Allure Severity
#-----------------------------------------------------------------------------------------------------------------------
class TestGetExercises:
    @allure.title('Get Exercises (v.1 - Через API-фикстуры: exercises_client, create_exercise_pydantic)')  # — Allure Title
    def test_get_exercises(self, create_exercise_api: httpx.Response, get_exercises_api: httpx.Response):

        # Assertions
        assert_status_code(get_exercises_api, http.HTTPStatus.OK)           # Status code: 200
        assert_method(get_exercises_api, http.HTTPMethod.GET)             # Method: GET


#=======================================================================================================================
        # Tool.api_report(create_exercise_api)
        # Tool.api_report(get_exercises_api)
