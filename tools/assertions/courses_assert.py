"""
Courses Assertions
"""
import allure
from tools.assertions.base_assert import assert_equal, assert_length_equal
from schemas.courses_schema import (
    CreateCourseRequestSchema, CreateCourseResponseSchema,
    UpdateCourseRequestSchema, UpdateCourseResponseSchema,
    GetCoursesResponseSchema
)

#=======================================================================================================================
# Create Course Response data = Request data
@allure.step('Create Course Response data = Request data')
def assert_create_course_response(response: CreateCourseResponseSchema, request: CreateCourseRequestSchema):
    """
    Create Course Response data = Request data

    :param response: Pydantic-model (CreateCourseResponseSchema)
    :param request: Pydantic-model (CreateCourseRequestSchema)
    :raise AssertionError
    """
    assert_equal(response.course.title, request.title, 'title')
    assert_equal(response.course.max_score, request.max_score, 'max_score')
    assert_equal(response.course.min_score, request.min_score, 'min_score')
    assert_equal(response.course.description, request.description, 'description')
    assert_equal(response.course.estimated_time, request.estimated_time, 'estimated_time')
    assert_equal(response.course.preview_file.id, request.preview_file_id, 'preview_file_id')
    assert_equal(response.course.created_by_user.id, request.created_by_user_id, 'created_by_user_id')



# Get list of Courses = List of Created courses
@allure.step('Get list of Courses = List of Created courses')
def assert_get_courses_responses(
        get_courses_response: GetCoursesResponseSchema,
        create_course_responses: list[CreateCourseResponseSchema]):
    """
    Get list of Courses = List of Created courses

    :param get_courses_response: Pydantic-model (GetCoursesResponseSchema)
    :param create_course_responses: Pydantic-model (list[CreateCourseResponseSchema])
    :return: AssertionError
    """
    expected_courses = [r.course for r in create_course_responses]
    assert_length_equal(get_courses_response.courses, expected_courses, 'courses') # Сравниваем количество элементов в объекте "courses"
    assert_equal(get_courses_response.courses, expected_courses, 'courses')    # Сравниваем значения элементов в объекте "courses"



# Updated Course Response data = Request data
@allure.step('Updated Course Response data = Request data')
def assert_update_course_response(response: UpdateCourseResponseSchema, request: UpdateCourseRequestSchema):
    """
    Updated Course Response data = Request data

    :param response: Pydantic-model (UpdateCourseResponseSchema)
    :param request: Pydantic-model (UpdateCourseRequestSchema)
    :raise AssertionError
    """
    assert_equal(response.course.title, request.title, 'title')
    assert_equal(response.course.max_score, request.max_score, 'max_score')
    assert_equal(response.course.min_score, request.min_score, 'min_score')
    assert_equal(response.course.description, request.description, 'description')
    assert_equal(response.course.estimated_time, request.estimated_time, 'estimated_time')


#-----------------------------------------------------------------------------------------------------------------------
