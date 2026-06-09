"""
Exercises assertions
"""
import httpx
from schemas.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema
from tools.assertions.base_assert import assert_equal, assert_is_value, assert_length

#=======================================================================================================================
# Create Exercise Response data is NON-empty
def assert_create_exercise_response_non_empty(response: httpx.Response):
    """
    Create Exercise Response data is NON-empty

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


# Create Exercise Response data = Create Exercise Request data
def assert_create_exercise_response(response: httpx.Response):
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



# Get Exercise Response data is NON-empty
def assert_get_exercise_response_non_empty(response: httpx.Response):
    """
    Get Exercise Response data is NON-empty

    Используется: assert_create_exercise_response_non_empty()

    :param response: httpx.Response (for deserialize —> Pydantic-model)
    :raise AssertionError
    """
    assert_create_exercise_response_non_empty(response)



# Update Exercise Response data = Update Exercise Request data
def assert_update_exercise_response(response: httpx.Response):
    """
    Update Response data = Update Request data (without course_id)

    :param response: httpx.Response with Exercise data (for deserialize —> Pydantic-model)
    :raise AssertionError
    """
    from schemas.exercises_schema import UpdateExerciseRequestSchema, UpdateExerciseResponseSchema
    response_model = UpdateExerciseResponseSchema.model_validate_json(response.text)           # Response —> Pydantic-model
    request_model = UpdateExerciseRequestSchema.model_validate_json(response.request.content)  # Request —> Pydantic-model

    assert_equal(response_model.exercise.title, request_model.title, 'title')
    assert_equal(response_model.exercise.max_score, request_model.max_score, 'max_score')
    assert_equal(response_model.exercise.min_score, request_model.min_score, 'min_score')
    assert_equal(response_model.exercise.order_index, request_model.order_index, 'order_index')
    assert_equal(response_model.exercise.description, request_model.description, 'description')
    assert_equal(response_model.exercise.estimated_time, request_model.estimated_time, 'estimated_time')


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
