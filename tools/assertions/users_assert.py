"""
Users assertions
"""
import httpx
import allure
from schemas.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.assertions.base_assert import assert_equal, assert_is_value, assert_length

#=======================================================================================================================
# Response data is NON-empty
@allure.step('Check Response data is NON-empty')
def assert_create_user_response_non_empty(response: httpx.Response):
    """
    Response data is NON-empty

    :param response: Response (for deserialize —> Pydantic-model)
    :raise AssertionError
    """
    response_model = CreateUserResponseSchema.model_validate_json(response.text)    # httpx.Response —> Pydantic-model (parsing-deserialize)

    assert_is_value(response_model.user.id, 'id')
    assert_is_value(response_model.user.email, 'email')
    assert_is_value(response_model.user.first_name, 'first_name')
    assert_is_value(response_model.user.middle_name, 'middle_name')
    assert_is_value(response_model.user.last_name, 'last_name')



# Response data = Request data
@allure.step('Check Response data = Request data')
def assert_create_user_response(response: httpx.Response):
    """
    Response data = Request data

    :param response: Response with User data (for deserialize —> Pydantic-model)
    :raise AssertionError
    """
    response_model = CreateUserResponseSchema.model_validate_json(response.text)           # httpx.Response —> Pydantic-model (parsing-deserialize)                                               # Условие, если не передать request_model, то...
    request_model = CreateUserRequestSchema.model_validate_json(response.request.content)  # Request —> Pydantic-model

    assert_equal(response_model.user.email,request_model.email,'email')
    assert_equal(response_model.user.last_name,request_model.last_name,'last_name')
    assert_equal(response_model.user.first_name, request_model.first_name,'first_name')
    assert_equal(response_model.user.middle_name,request_model.middle_name,'middle_ame')



# User ID validation
@allure.step('Check User ID')
def assert_user_id(response: httpx.Response):
    """
    User ID validation:

    - User ID is NOT-empty
    - User ID length = 36 chars

    :param response: Response with User data (for deserialize —> Pydantic-model)
    :raise AssertionError
    """
    response_model = CreateUserResponseSchema.model_validate_json(response.text)  # httpx.Response —> Pydantic-model (parsing-deserialize)
    assert_is_value(response_model.user.id, 'id')                       # NON-Empty
    assert_length(response_model.user.id, 36, 'id')       # Length = 36 chars

#-----------------------------------------------------------------------------------------------------------------------
