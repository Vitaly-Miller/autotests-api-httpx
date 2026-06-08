"""
Exercises assertions
"""
import httpx
from schemas.exercises_schema import (
    CreateExerciseRequestSchema, CreateExerciseResponseSchema,
    GetExerciseRequestSchema, GetExercisesResponseSchema
)
from tools.assertions.base_assert import assert_equal, assert_is_value, assert_length

#=======================================================================================================================
# Exercise Response data is NON-empty
def assert_exercise_response_non_empty(response: httpx.Response):
    """
    Exercise Response data is NON-empty

    :param response: httpx.Response (for deserialize —> Pydantic-model)
    :raise AssertionError
    """
    response_model = CreateExerciseResponseSchema.model_validate_json(response.text)   # Response —> Pydantic-model

    assert_is_value(response_model.exercise.id, 'id')
    assert_is_value(response_model.exercise.title, 'title')
    assert_is_value(response_model.exercise.course_id, 'course_id')
    assert_is_value(response_model.exercise.max_score, 'max_score')
    assert_is_value(response_model.exercise.min_score, 'min_score')
    assert_is_value(response_model.exercise.order_index, 'order_index')
    assert_is_value(response_model.exercise.description, 'description')
    assert_is_value(response_model.exercise.estimated_time, 'estimated_time')


# Exercise Response data = Exercise Request data
def assert_exercise_response(response: httpx.Response):
    """
    Response data = Request data

    :param response: httpx.Response with File data (for deserialize —> Pydantic-model)
    :raise AssertionError
    """
    response_model = CreateExerciseResponseSchema.model_validate_json(response.text)           # Response —> Pydantic-model
    request_model = CreateExerciseRequestSchema.model_validate_json(response.request.content)  # Request —> Pydantic-model

    assert_equal(response_model.exercise.title, request_model.title, 'title')
    assert_equal(response_model.exercise.course_id, request_model.course_id, 'course_id')
    assert_equal(response_model.exercise.max_score, request_model.max_score, 'max_score')
    assert_equal(response_model.exercise.min_score, request_model.min_score, 'min_score')
    assert_equal(response_model.exercise.order_index, request_model.order_index, 'order_index')
    assert_equal(response_model.exercise.description, request_model.description, 'description')


# Exercise ID validation
def assert_exercise_id(response: httpx.Response, exercise_id: str | None = None):
    """
    Exercise ID validation

    - NON-empty Exercise ID
    - Exercise ID length = 36 chars
    - Exercise ID = expected Exercise ID (optional)

    :param response: httpx.Response with File data (for deserialize —> Pydantic-model)
    :param exercise_id: Exercise ID / None
    :raise AssertionError
    """
    response_model = CreateExerciseResponseSchema.model_validate_json(response.text)      # Response —> Pydantic-model

    assert_is_value(response_model.exercise.id, 'exercise_id')                  # NON-empty File ID
    assert_length(response_model.exercise.id, 36, 'exercise_id')  # File ID length = 36 chars
    if exercise_id:
        assert_equal(response_model.exercise.id, exercise_id, 'exercise_id') # Response Exercise ID = expected Exercise ID (optional)
