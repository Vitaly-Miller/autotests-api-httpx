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
# Response Created course data = Request Create course data
@allure.step('Response Created course data = Request Create course data')
def assert_create_course_response(actual_model: CreateCourseResponseSchema, expected_model: CreateCourseRequestSchema):
    """
    Response Created course data = Request Create course data

    :param actual_model: Pydantic-model (CreateCourseResponseSchema)
    :param expected_model: Pydantic-model (CreateCourseRequestSchema)
    :raise AssertionError
    """
    assert_equal(actual_model.course.title, expected_model.title, 'title')
    assert_equal(actual_model.course.max_score, expected_model.max_score, 'max_score')
    assert_equal(actual_model.course.min_score, expected_model.min_score, 'min_score')
    assert_equal(actual_model.course.description, expected_model.description, 'description')
    assert_equal(actual_model.course.estimated_time, expected_model.estimated_time, 'estimated_time')
    assert_equal(actual_model.course.preview_file.id, expected_model.preview_file_id, 'preview_file_id')
    assert_equal(actual_model.course.created_by_user.id, expected_model.created_by_user_id, 'created_by_user_id')



# Check get List of courses = List of Created courses
@allure.step('Check get List of courses = List of Created courses')
def assert_get_courses_responses(get_courses_response_model: GetCoursesResponseSchema, create_course_responses_model: list[CreateCourseResponseSchema]):
    """
    Проверка получения [списка] курсов с созданными курсами

    :param get_courses_response_model: Pydantic-model (GetCoursesResponseSchema)
    :param create_course_responses_model: list[CreateCourseResponseSchema]
    :return: AssertionError
    """
    expected_courses = [r.course for r in create_course_responses_model]
    assert_length_equal(get_courses_response_model.courses, expected_courses, 'courses') # Сравниваем количество элементов в объекте "courses"
    assert_equal(get_courses_response_model.courses, expected_courses, 'courses')    # Сравниваем значения элементов в объекте "courses"



# Response Updated course data = Request with New course data
@allure.step('Response Updated course data = Request with New course data')
def assert_update_course_response(response_model: UpdateCourseResponseSchema, new_course_data: UpdateCourseRequestSchema):
    """
    Response Updated course data = Request with New course data

    :param response_model: Pydantic-model (UpdateCourseResponseSchema)
    :param new_course_data: Pydantic-model (UpdateCourseRequestSchema)
    :raise AssertionError
    """
    assert_equal(response_model.course.title, new_course_data.title, 'title')
    assert_equal(response_model.course.max_score, new_course_data.max_score, 'max_score')
    assert_equal(response_model.course.min_score, new_course_data.min_score, 'min_score')
    assert_equal(response_model.course.description, new_course_data.description, 'description')
    assert_equal(response_model.course.estimated_time, new_course_data.estimated_time, 'estimated_time')


#-----------------------------------------------------------------------------------------------------------------------
