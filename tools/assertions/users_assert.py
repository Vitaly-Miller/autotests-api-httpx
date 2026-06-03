"""
Users assertions
"""
import httpx
from schemas.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.assertions.base_assert import assert_equal

#=======================================================================================================================
def assert_create_user_data_equal(response: httpx.Response, request_model: CreateUserRequestSchema | None = None):
    """
    4-in-1 | Request data = Response data

    - email
    - last_name
    - first_name
    - middle_name

    Если не передать Pydantic-model with User data, то вытащит из response.REQUEST.content и deserialize в —> Pydantic-model (for Assertions)

    :param response: Response with User data (for deserialize —> Pydantic-model)
    :param request_model: Pydantic-model with User data / None
    :raise AssertionError
    """
    response_model = CreateUserResponseSchema.model_validate_json(response.text)  # Response —> Pydantic-model (Deserialize for Assertions)

    # Условие, если не передать request_model, то ...
    if not request_model:
        request_model = CreateUserRequestSchema.model_validate_json(response.request.content)  # Request —> Pydantic-model (Deserialize for Assertions)

    # Request data = Response data:
    assert_equal(response_model.user.email,request_model.email,'email')
    assert_equal(response_model.user.last_name,request_model.last_name,'last_name')
    assert_equal(response_model.user.first_name, request_model.first_name,'first_name')
    assert_equal(response_model.user.middle_name,request_model.middle_name,'middle_ame')

#-----------------------------------------------------------------------------------------------------------------------
