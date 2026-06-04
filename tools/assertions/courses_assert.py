"""
Courses Assertions
"""
import httpx
from schemas.courses_schema import UpdateCourseRequestSchema, UpdateCourseResponseSchema
from tools.assertions.base_assert import assert_equal

#=======================================================================================================================
# Request Data = Response Data:
def assert_update_course_data_equal(response: httpx.Response, request_model: UpdateCourseRequestSchema | None = None):
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

    #-------------------------------------------------------------------------------------------------------------------
