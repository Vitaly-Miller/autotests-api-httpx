"""
Courses Assertions
"""
import httpx
from schemas.courses_schema import (
    CreateCourseRequestSchema, CreateCourseResponseSchema,
    UpdateCourseRequestSchema, UpdateCourseResponseSchema,
    GetCoursesResponseSchema
)
from tools.assertions.base_assert import assert_equal, assert_length_equal

#=======================================================================================================================
# Response data = Request data
def assert_create_course_pydantic_response(response: httpx.Response):
    """
    Response data = Request data

    :param response: Response (for deserialize —> Pydantic-model)
    :raise AssertionError
    """
    response_model = CreateCourseResponseSchema.model_validate_json(response.text)          # Response —> Pydantic-model
    request_model = CreateCourseRequestSchema.model_validate_json(response.request.content) # Request —> Pydantic-model

    assert_equal(response_model.course.title, request_model.title, 'title')
    assert_equal(response_model.course.max_score, request_model.max_score, 'max_score')
    assert_equal(response_model.course.min_score, request_model.min_score, 'min_score')
    assert_equal(response_model.course.description, request_model.description, 'description')
    assert_equal(response_model.course.estimated_time, request_model.estimated_time, 'estimated_time')
    assert_equal(response_model.course.preview_file.id, request_model.preview_file_id, 'preview_file_id')
    assert_equal(response_model.course.created_by_user.id, request_model.created_by_user_id, 'created_by_user_id')



# Response data = Request data
def assert_get_courses_responses(get_courses_response: httpx.Response, create_course_responses: list[CreateCourseResponseSchema]):
    """
    Проверка получения [списка] курсов с созданными курсами

    :param get_courses_response: get_courses_response
    :param create_course_responses: create_course_pydantic_responses
    :return: AssertionError
    """
    get_courses_response_model = GetCoursesResponseSchema.model_validate_json(get_courses_response.text)  # Response —> Pydantic-model

    expected_courses = [r.course for r in create_course_responses]                                        #

    assert_length_equal(get_courses_response_model.courses, expected_courses, 'courses') # Сравниваем количество элементов в объекте "courses"
    assert_equal(get_courses_response_model.courses, expected_courses, 'courses')    # Сравниваем значения элементов в объекте "courses"



# Response data = Request data
def assert_update_course_response(response: httpx.Response):
    """
    Response data = Request data

    - title
    - max_score
    - min_score
    - description
    - estimated_time

    Если не передать Pydantic-model with Update Course data, то вытащит из response.REQUEST.content и deserialize в —> Pydantic-model (for Assertions)

    :param response: Response (for deserialize —> Pydantic-model)
    :param request_model: Pydantic-model with Update Course data / None
    :raise AssertionError
    """
    response_model = UpdateCourseResponseSchema.model_validate_json(response.text)          # Response —> Pydantic-model                                                                # Условие, если не передать request_model, то ...
    request_model = UpdateCourseRequestSchema.model_validate_json(response.request.content) # Request —> Pydantic-model

    assert_equal(response_model.course.title, request_model.title, 'title')
    assert_equal(response_model.course.max_score, request_model.max_score, 'max_score')
    assert_equal(response_model.course.min_score, request_model.min_score, 'min_score')
    assert_equal(response_model.course.description, request_model.description, 'description')
    assert_equal(response_model.course.estimated_time, request_model.estimated_time, 'estimated_time')



#-----------------------------------------------------------------------------------------------------------------------
