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
# Request Data = Response Data
def assert_create_course_response_equal(response: httpx.Response, request_model: CreateCourseRequestSchema | None = None):
    """
    Request data = Response data

    Если не передать Pydantic-model, то вытащит из response.REQUEST.content и deserialize в —> Pydantic-model (for Assertions)

    :param response: Response (for deserialize —> Pydantic-model)
    :param request_model: Pydantic-model with Create Course data / None
    :raise AssertionError
    """

    response_model = CreateCourseResponseSchema.model_validate_json(response.text).course    # Response  —> Pydantic-model.course

    if not request_model:                                                                     # Условие, если не передать request_model, то ...
        request_model = CreateCourseRequestSchema.model_validate_json(response.request.content)  # Request —> Pydantic-model

    assert_equal(response_model.title, request_model.title, 'title')
    assert_equal(response_model.max_score, request_model.max_score, 'max_score')
    assert_equal(response_model.min_score, request_model.min_score, 'min_score')
    assert_equal(response_model.description, request_model.description, 'description')
    assert_equal(response_model.estimated_time, request_model.estimated_time, 'estimated_time')
    assert_equal(response_model.preview_file.id, request_model.preview_file_id, 'preview_file_id')
    assert_equal(response_model.created_by_user.id, request_model.created_by_user_id, 'created_by_user_id')



def assert_get_courses_responses_equal(get_courses_response: httpx.Response, create_course_responses: list[CreateCourseResponseSchema]):
    """
    Проверка получения [списка] курсов с созданными курсами

    :param get_courses_response: get_courses_response
    :param create_course_responses: create_course_responses

    :return: AssertionError
    """
    get_courses_response_model = GetCoursesResponseSchema.model_validate_json(get_courses_response.text)  # Response —> Pydantic-model (CreateCourseResponseSchema)

    expected_courses = [r.course for r in create_course_responses]                                        # CreateCourseResponseSchema —> CourseSchema

    assert_length_equal(get_courses_response_model.courses, expected_courses, 'courses') # Сравниваем количество элементов в объекте "courses"
    assert_equal(get_courses_response_model.courses, expected_courses, 'courses')    # Сравниваем значения элементов в объекте "courses"




# Request Data = Response Data
def assert_update_course_response_equal(response: httpx.Response, request_model: UpdateCourseRequestSchema | None = None):
    """
    Request data = Response data

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
    response_model = UpdateCourseResponseSchema.model_validate_json(response.text)  # Response —> Pydantic-model

    if not request_model:                                                                        # Условие, если не передать request_model, то ...
        request_model = UpdateCourseRequestSchema.model_validate_json(response.request.content)  # Request —> Pydantic-model

    assert_equal(response_model.course.title, request_model.title, 'title')
    assert_equal(response_model.course.max_score, request_model.max_score, 'max_score')
    assert_equal(response_model.course.min_score, request_model.min_score, 'min_score')
    assert_equal(response_model.course.description, request_model.description, 'description')
    assert_equal(response_model.course.estimated_time, request_model.estimated_time, 'estimated_time')



#-----------------------------------------------------------------------------------------------------------------------
