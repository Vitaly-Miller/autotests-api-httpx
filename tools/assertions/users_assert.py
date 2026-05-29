"""
Users assertions
"""
import httpx
from schemas.users import CreateUserRequestSchema, CreateUserResponseSchema
from tools.assertions.base_assert import assert_value_equal

#=======================================================================================================================
def assert_create_user_data_equal(response: httpx.Response, request_model: CreateUserRequestSchema | None = None):
    """
    4-in-1 | Create User Data = Created User Data

    - email
    - last_name
    - first_name
    - middle_name

    Actions:

    - Response —> Pydantic-model (Deserialize for Assertions)
    - Если не передать Pydantic-model with User data, то вытащит из response.REQUEST.content и deserialize в —> Pydantic-model (for Assertions)

    :param response: httpx.Response with User data
    :param request_model: Pydantic-model with User data / None
    :raise AssertionError
    """
    response_model = CreateUserResponseSchema.model_validate_json(response.text)  # Response —> Pydantic-model (Deserialize for Assertions)

    # Условие, если не передать request_model, то ...
    if not request_model:
        request_model = CreateUserRequestSchema.model_validate_json(response.request.content)  # Request —> Pydantic-model (Deserialize for Assertions)


    # Create User Data = Created User Data:
    assert_value_equal(
        response_model.user.email,
        'email',
        request_model.email)

    assert_value_equal(
        response_model.user.last_name,
        'last_name',
        request_model.last_name)

    assert_value_equal(
        response_model.user.first_name,
        'first_name',
        request_model.first_name)

    assert_value_equal(
        response_model.user.middle_name,
        'middle_ame',
        request_model.middle_name)

#-----------------------------------------------------------------------------------------------------------------------
