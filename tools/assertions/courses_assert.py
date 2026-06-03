"""
Courses Assertions
"""
import httpx
from schemas.courses_schema import UpdateCourseRequestSchema, UpdateCourseResponseSchema
from tools.assertions.base_assert import assert_equal

#=======================================================================================================================
def assert_update_course_data_equal(response: httpx.Response, request_model: UpdateCourseRequestSchema | None = None):
    """
    5-in-1 | Request data = Response data

    Если не передать Pydantic-model with Update Course data, то вытащит из response.REQUEST.content и deserialize в —> Pydantic-model (for Assertions)

    :param response: Response (for deserialize —> Pydantic-model)
    :param request_model: Pydantic-model with Update Course data / None
    :raise AssertionError
    """
    response_model = UpdateCourseResponseSchema.model_validate_json(response.text)  # Response —> Pydantic-model (Deserialize for Assertions)

    # Условие, если не передать request_model, то ...
    if not request_model:
        request_model = UpdateCourseRequestSchema.model_validate_json(response.request.content)  # Request —> Pydantic-model (Deserialize for Assertions)

    # Request Data = Response Data:
    assert_equal(response_model.course.title, request_model.title, 'title')
    assert_equal(response_model.course.max_score, request_model.max_score, 'max_score')
    assert_equal(response_model.course.min_score, request_model.min_score, 'min_score')
    assert_equal(response_model.course.description, request_model.description, 'description')
    assert_equal(response_model.course.estimated_time, request_model.estimated_time, 'estimated_time')

    #-------------------------------------------------------------------------------------------------------------------
