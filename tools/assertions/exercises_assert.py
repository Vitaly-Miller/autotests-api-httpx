"""
Exercises assertions
"""
import httpx
import allure
from tools.assertions.base_assert import assert_equal, assert_is_value, assert_length
from tools.assertions.errors_assert import assert_not_found_error_response
from schemas.errors_schema import NotFoundErrorResponseSchema
from schemas.exercises_schema import (
    ExerciseSchema, CreateExerciseRequestSchema, CreateExerciseResponseSchema,
    GetExerciseResponseSchema, UpdateExerciseRequestSchema, UpdateExerciseResponseSchema
)
from tools.tool import Tool

#=======================================================================================================================
#---------------------------------------------------- Exercise (base) --------------------------------------------------
# .exercise{} is NON-empty (base)
def assert_exercise_non_empty(response: ExerciseSchema):
    """
    .exercise{} is NON-empty (base)

    :param response: Pydantic-model (ExerciseSchema)
    :raise AssertionError
    """
    assert_is_value(response.id, 'id')
    assert_is_value(response.title, 'title')
    assert_is_value(response.course_id, 'course_id')
    assert_is_value(response.max_score, 'max_score')
    assert_is_value(response.min_score, 'min_score')
    assert_is_value(response.order_index, 'order_index')
    assert_is_value(response.description, 'description')
    assert_is_value(response.estimated_time, 'estimated_time')


#---------------------------------------------------- Create exercise --------------------------------------------------
# Create Exercise Response data is NON-empty
@allure.step('Response data is NON-empty')
def assert_create_exercise_response_non_empty(response: CreateExerciseResponseSchema):
    """
    Create Exercise Response data is NON-empty

    - Используется: assert_exercise_non_empty()

    :param response: Pydantic-model (CreateExerciseResponseSchema)
    :raise AssertionError
    """
    assert_exercise_non_empty(response.exercise)   # передаем exercise{}


# Created Exercise Response data = Request data
@allure.step('Created Exercise Response data = Request data')
def assert_create_exercise_response(response: CreateExerciseResponseSchema, request: CreateExerciseRequestSchema):
    """
    Created Exercise Response data = Request data

    :param response: Pydantic-model (CreateExerciseResponseSchema)
    :param request: Pydantic-model (CreateExerciseRequestSchema)
    :raise AssertionError
    """
    assert_equal(response.exercise.title, request.title, 'title')
    assert_equal(response.exercise.course_id, request.course_id, 'course_id')
    assert_equal(response.exercise.max_score, request.max_score, 'max_score')
    assert_equal(response.exercise.min_score, request.min_score, 'min_score')
    assert_equal(response.exercise.order_index, request.order_index, 'order_index')
    assert_equal(response.exercise.description, request.description, 'description')
    assert_equal(response.exercise.estimated_time, request.estimated_time, 'estimated_time')


# Exercise-ID validation
@allure.step('Exercise-ID validation')
def assert_exercise_id(response: CreateExerciseResponseSchema | GetExerciseResponseSchema, exercise_id: str | None = None):
    """
    Exercise-ID validation

    - Exercise-ID is NON-empty
    - Exercise-ID length = 36 chars
    - Actual Exercise-ID = Expected Exercise-ID (optional)

    :param response: Pydantic-model (CreateExerciseResponseSchema / GetExerciseResponseSchema)
    :param exercise_id: Exercise-ID / None
    :raise AssertionError
    """
    assert_is_value(response.exercise.id, 'exercise_id')                       # NON-empty File-ID
    assert_length(response.exercise.id, 36, 'exercise_id')       # File-ID length = 36 chars
    if exercise_id:                                                                        # Если передать Exercise-ID, то проверяем его:
        assert_equal(response.exercise.id, exercise_id,'exercise_id') # Actual Exercise-ID = Expected Exercise-ID



#---------------------------------------------------- Get exercise -----------------------------------------------------
# Get Exercise Response data is NON-empty
@allure.step('Response data is NON-empty')
def assert_get_exercise_response_non_empty(response: GetExerciseResponseSchema):
    """
    Get Exercise Response data is NON-empty

    - Используется: assert_exercise_non_empty()

    :param response: Pydantic-model (GetExerciseResponseSchema)
    :raise AssertionError
    """
    assert_exercise_non_empty(response.exercise)       # передаем exercise{}


#--------------------------------------------------- Update exercise ---------------------------------------------------
# Update Exercise Response data = Request data
@allure.step('Update Exercise Response data = Request data')
def assert_update_exercise_response(response: UpdateExerciseResponseSchema, request: UpdateExerciseRequestSchema):
    """
    Update Exercise Response data = Request data

    :param response: Pydantic-model (UpdateExerciseResponseSchema)
    :param request: Pydantic-model (UpdateExerciseRequestSchema)
    :raise AssertionError
    """
    assert_equal(response.exercise.title, request.title, 'title')
    assert_equal(response.exercise.max_score, request.max_score, 'max_score')
    assert_equal(response.exercise.min_score, request.min_score, 'min_score')
    assert_equal(response.exercise.order_index, request.order_index, 'order_index')
    assert_equal(response.exercise.description, request.description, 'description')
    assert_equal(response.exercise.estimated_time, request.estimated_time, 'estimated_time')



#====================================================== NEGATIVE =======================================================
#---------------------------------------------------- Get exercise -----------------------------------------------------
# Get File Not Found Error Response by NON-existent exercise
@allure.step('Get File Not Found Error Response by NON-existent exercise')
def assert_exercise_not_found_error_response(response: httpx.Response):
    """
    Get File Not Found Error Response by NON-existent exercise

    - actual   - Deserialize httpx.Response —> Pydantic-model (NotFoundErrorResponseSchema)
    - expected - Initialize (NotFoundErrorResponseSchema)

    :param response: httpx.Response
    :return: AssertionError
    """
    actual_response = NotFoundErrorResponseSchema.model_validate_json(response.text)  # httpx.Response —> Pydantic-model (deserialize)
    expected_response = NotFoundErrorResponseSchema(
        detail='Exercise not found'                                                   # Expected error message
    )
    assert_not_found_error_response(actual_response, expected_response)


#-----------------------------------------------------------------------------------------------------------------------
