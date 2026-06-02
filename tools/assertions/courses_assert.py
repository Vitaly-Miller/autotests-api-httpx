"""
Courses Assertions
"""
import httpx

#=======================================================================================================================
def assert_update_course_response(response: httpx.Response):
    """
    4-in-1 | NON-empty response values

    Actions:

    - Response —> Pydantic-model (Deserialize for Assertions)

    :param response: httpx.Response
    :raise AssertionError
    """
