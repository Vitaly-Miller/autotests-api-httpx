"""
TEST Get Exercises
"""
import http

import httpx
import pytest

from schemas.exercises_schema import CreateExerciseSchema
from tools.assertions.base_assert import assert_method, assert_status_code
from tools.tool import Tool

#=======================================================================================================================
@pytest.mark.exercises
@pytest.mark.regression
class TestGetExercises:
    def test_get_exercises(self, create_exercise_api: httpx.Response, get_exercises_api: httpx.Response):
        response_create_exercise = create_exercise_api            # Сохраняем ответ от API-фикстуры
        response = get_exercises_api                              # Сохраняем ответ от API-фикстуры



        # Assertions (Get exercises)
        assert_status_code(response, http.HTTPStatus.OK)  # Status code: 200
        assert_method(response, http.HTTPMethod.GET)    # Method: GET



#=======================================================================================================================
        Tool.api_report(response_create_exercise)
        Tool.api_report(response)
