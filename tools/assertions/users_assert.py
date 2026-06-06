"""
Users assertions
"""
import httpx
from schemas.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.assertions.base_assert import assert_equal, assert_is_value, assert_length

#=======================================================================================================================
# NON-Empty Response values
def assert_create_user_response_values_non_empty(response: httpx.Response):
    """
    NON-Empty Response values:

    - id
    - email
    - first_name
    - middle_name
    - last_name

    :param response: Response (for deserialize —> Pydantic-model)
    :raise AssertionError
    """
    response_model = CreateUserResponseSchema.model_validate_json(response.text)    # Response —> Pydantic-model

    assert_is_value(response_model.user.id, 'id')
    assert_is_value(response_model.user.email, 'email')
    assert_is_value(response_model.user.first_name, 'first_name')
    assert_is_value(response_model.user.middle_name, 'middle_name')
    assert_is_value(response_model.user.last_name, 'last_name')



# Request data = Response data
def assert_create_user_response_equal(response: httpx.Response, request_model: CreateUserRequestSchema | None = None):
    """
    Request data = Response data

    - Email
    - Last Name
    - First Name
    - Middle Name

    Если не передать Pydantic-model with User data, то вытащит из response.REQUEST.content и deserialize в —> Pydantic-model (for Assertions)

    :param response: Response with User data (for deserialize —> Pydantic-model)
    :param request_model: Pydantic-model with User data / None
    :raise AssertionError
    """
    response_model = CreateUserResponseSchema.model_validate_json(response.text)   # Response —> Pydantic-model (CreateUserRequestSchema)

    if not request_model:                                                          # Условие, если не передать request_model, то...
        request_model = CreateUserRequestSchema.model_validate_json(response.request.content)  # Request —> Pydantic-model (CreateUserRequestSchema)

    assert_equal(response_model.user.email,request_model.email,'email')
    assert_equal(response_model.user.last_name,request_model.last_name,'last_name')
    assert_equal(response_model.user.first_name, request_model.first_name,'first_name')
    assert_equal(response_model.user.middle_name,request_model.middle_name,'middle_ame')



# User ID validation
def assert_user_id(response: httpx.Response):
    """
    2-in-1 | User ID validation:

    - User ID is NOT empty
    - User ID length = 36 chars

    :param response: Response with User data (for deserialize —> Pydantic-model)
    :raise AssertionError
    """
    response_model = CreateUserResponseSchema.model_validate_json(response.text)  # Response —> Pydantic-model

    assert_is_value(response_model.user.id, 'id')                       # NON-Empty
    assert_length(response_model.user.id, 36, 'id')       # Length = 36 chars

#-----------------------------------------------------------------------------------------------------------------------
