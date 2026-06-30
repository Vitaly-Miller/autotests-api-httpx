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
def assert_create_user_response_non_empty(response_model: CreateUserResponseSchema):
    """
    Response data is NON-empty

    :param response_model: Pydantic-model (CreateUserResponseSchema)
    :raise AssertionError
    """
    assert_is_value(response_model.user.id, 'id')
    assert_is_value(response_model.user.email, 'email')
    assert_is_value(response_model.user.first_name, 'first_name')
    assert_is_value(response_model.user.middle_name, 'middle_name')
    assert_is_value(response_model.user.last_name, 'last_name')



# Response data = Request data
@allure.step('Check Response data = Request data')
def assert_create_user_response_data(response_model: CreateUserResponseSchema, request_model: CreateUserRequestSchema):
    """
    Response data = Request data

    :param response_model: Pydantic-model (CreateUserResponseSchema)
    :param request_model: Pydantic-model (CreateUserRequestSchema)
    :raise AssertionError
    """
    assert_equal(response_model.user.email,request_model.email,'email')
    assert_equal(response_model.user.last_name,request_model.last_name,'last_name')
    assert_equal(response_model.user.first_name, request_model.first_name,'first_name')
    assert_equal(response_model.user.middle_name,request_model.middle_name,'middle_ame')



# User ID validation
@allure.step('User ID validation')
def assert_user_id(response_model: CreateUserResponseSchema):
    """
    User ID validation:

    - User ID is NOT-empty
    - User ID length = 36 chars

    :param response_model: Pydantic-model (CreateUserResponseSchema)
    :raise AssertionError
    """
    assert_is_value(response_model.user.id, 'id')                          # NON-Empty
    assert_length(response_model.user.id, 36, 'id')       # Length = 36 chars

#-----------------------------------------------------------------------------------------------------------------------
