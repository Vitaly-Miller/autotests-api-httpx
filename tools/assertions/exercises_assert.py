"""
Exercises assertions
"""
import http

import httpx

from clients.exercises_client import ExercisesClient
from schemas.errors_schema import NotFoundErrorResponseSchema
from schemas.exercises_schema import (
    CreateExerciseRequestSchema, CreateExerciseResponseSchema,
    ExerciseSchema, GetExerciseResponseSchema, UpdateExerciseRequestSchema, UpdateExerciseResponseSchema
)
from tools.assertions.base_assert import assert_equal, assert_is_value, assert_length, assert_request_method, assert_status_code
from tools.assertions.errors_assert import assert_not_found_error_response
from tools.tool import Tool

#=======================================================================================================================
#---------------------------------------------------- Exercise (base) --------------------------------------------------
def assert_exercise_response_non_empty(response: ExerciseSchema):
    """
    Exercise data is NON-empty (base)

    :param response: Pydantic-model (ExerciseSchema)
    :raise AssertionError
    """
    # response_model = CreateExerciseResponseSchema.model_validate_json(response.text)   # httpx.Response —> Pydantic-model (deserialize)

    assert_is_value(response.id, 'id')
    assert_is_value(response.title, 'title')
    assert_is_value(response.course_id, 'course_id')
    assert_is_value(response.max_score, 'max_score')
    assert_is_value(response.min_score, 'min_score')
    assert_is_value(response.order_index, 'order_index')
    assert_is_value(response.description, 'description')
    assert_is_value(response.estimated_time, 'estimated_time')

#---------------------------------------------------- Create exercise --------------------------------------------------
def assert_create_exercise_response_non_empty(response: CreateExerciseResponseSchema):
    """
    Create Exercise Response data is NON-empty

    - Используется: assert_exercise_response_non_empty()

    :param response: Pydantic-model (CreateExerciseResponseSchema)
    :raise AssertionError
    """
    assert_exercise_response_non_empty(response.exercise)   # передаем exercise{}



def assert_exercise_id(response: CreateExerciseResponseSchema, exercise_id: str | None = None):
    """
    Exercise ID validation

    - NON-empty Exercise ID
    - Exercise ID length = 36 chars
    - Exercise ID = expected Exercise ID (optional)

    :param response: Pydantic-model (CreateExerciseResponseSchema)
    :param exercise_id: Exercise ID / None
    :raise AssertionError
    """
    assert_is_value(response.exercise.id, 'exercise_id')                  # NON-empty File-ID
    assert_length(response.exercise.id, 36, 'exercise_id')  # File-ID length = 36 chars
    if exercise_id:                                                                       # Если передать Exercise ID, то проверяем его:
        assert_equal(response.exercise.id, exercise_id,'exercise_id') # Actual Exercise ID = Expected Exercise ID



def assert_create_exercise_response(response: CreateExerciseResponseSchema, request: CreateExerciseRequestSchema):
    """
    Create Exercise Response data = Create Exercise Request data

    :param response: Pydantic-model (CreateExerciseResponseSchema)
    :param request: Pydantic-model (CreateExerciseRequestSchema)
    :raise AssertionError
    """
    # response_model = CreateExerciseResponseSchema.model_validate_json(response.text)           # httpx.Response —> Pydantic-model (parsing-deserialize)
    # request_model = CreateExerciseRequestSchema.model_validate_json(response.request.content)  # Request —> Pydantic-model

    assert_equal(response.exercise.title, request.title, 'title')
    assert_equal(response.exercise.course_id, request.course_id, 'course_id')
    assert_equal(response.exercise.max_score, request.max_score, 'max_score')
    assert_equal(response.exercise.min_score, request.min_score, 'min_score')
    assert_equal(response.exercise.order_index, request.order_index, 'order_index')
    assert_equal(response.exercise.description, request.description, 'description')
    assert_equal(response.exercise.estimated_time, request.estimated_time, 'estimated_time')


#---------------------------------------------------- Get exercise -----------------------------------------------------
def assert_get_exercise_response_non_empty(response: GetExerciseResponseSchema):
    """
    Get Exercise Response data is NON-empty

    - Используется: assert_exercise_response_non_empty()

    :param response: Pydantic-model (GetExerciseResponseSchema)
    :raise AssertionError
    """
    assert_exercise_response_non_empty(response.exercise)   # передаем exercise{}


#--------------------------------------------------- Update exercise ---------------------------------------------------
def assert_update_exercise_response(response: UpdateExerciseResponseSchema, request: UpdateExerciseRequestSchema):
    """
    Update Response data = Update Request data (without Course-ID)

    :param response: Pydantic-model (UpdateExerciseResponseSchema)
    :param request: Pydantic-model (UpdateExerciseRequestSchema)
    :raise AssertionError
    """

    # response_model = UpdateExerciseResponseSchema.model_validate_json(response.text)           # httpx.Response —> Pydantic-model (parsing-deserialize)
    # request_model = UpdateExerciseRequestSchema.model_validate_json(response.request.content)  # Request —> Pydantic-model

    assert_equal(response.exercise.title, request.title, 'title')
    assert_equal(response.exercise.max_score, request.max_score, 'max_score')
    assert_equal(response.exercise.min_score, request.min_score, 'min_score')
    assert_equal(response.exercise.order_index, request.order_index, 'order_index')
    assert_equal(response.exercise.description, request.description, 'description')
    assert_equal(response.exercise.estimated_time, request.estimated_time, 'estimated_time')



#====================================================== NEGATIVE =======================================================
#---------------------------------------------------- Get exercise -----------------------------------------------------
def assert_exercise_not_found_error_response(response: httpx.Response):
    """
    Get NON-existent Exercise / Error Response message

    Сравнивает Error Response с Pydantic-model (NotFoundErrorResponseSchema)

    :param response: Response
    :return: AssertionError
    """
    actual_response = NotFoundErrorResponseSchema.model_validate_json(response.text)      # httpx.Response —> Pydantic-model (parsing-deserialize)
    expected_response = NotFoundErrorResponseSchema(
        detail='Exercise not found'                                                       # Expected error message
    )
    assert_not_found_error_response(actual_response, expected_response)   # "detail": "Exercise not found"


#-----------------------------------------------------------------------------------------------------------------------
