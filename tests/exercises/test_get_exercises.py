"""
TEST Get Exercises [list]
"""
import httpx
import http
import pytest
import allure
from tools.allure.annotations import Epic, Feature, Story, Tag
from tools.assertions.base_assert import assert_request_method, assert_status_code
from tools.tool import Tool

#=======================================================================================================================
# Class annotations
@pytest.mark.exercises                                        # ┐ Pytest Marks
@pytest.mark.regression                                       # ┘
@allure.tag(Tag.REGRESSION, Tag.EXERCISES, Tag.GET)     # ] Allure Tags
@allure.epic(Epic.API)                                        # ┐
@allure.feature(Feature.EXERCISES)                            # │ Allure Behaviors
@allure.story(Story.GET)                                      # ┘
@allure.severity(allure.severity_level.NORMAL)                # ] Allure Severity
#-----------------------------------------------------------------------------------------------------------------------
class TestGetExercises:
    @allure.title('Get Exercises (v.1 - Через API-фикстуры: exercises_client, create_exercise)')  # Allure step Title
    def test_get_exercises(self, create_exercise_api: httpx.Response, get_exercises_api: httpx.Response):
        response = get_exercises_api                                              # Сохраняем ответ API-фикстуры

        # Assertions
        assert_status_code(response.status_code, http.HTTPStatus.OK)          # Status code: 200
        assert_request_method(response.request.method, http.HTTPMethod.GET)   # Method: GET


#=======================================================================================================================
        # Tool.api_report(create_exercise_api)
        # Tool.api_report(get_exercises_api)
