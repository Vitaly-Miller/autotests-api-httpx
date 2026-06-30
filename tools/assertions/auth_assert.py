"""
Auth (Log in) assertions
"""
import allure
from schemas.auth_schema import AuthResponseSchema
from tools.assertions.base_assert import (
    assert_equal,
    assert_length,
    assert_is_value,
    assert_not_equal
)
#=======================================================================================================================
# Response data is NON-empty
@allure.step('Check Response data is NON-empty')
def assert_auth_response_non_empty(response_model: AuthResponseSchema):
    """
    Check Response data is NON-empty

    :param response_model: Pydantic-model (AuthResponseSchem)
    :raise AssertionError
    """


    assert_is_value(response_model.token.token_type, 'token_type')
    assert_is_value(response_model.token.access_token, 'access_token')
    assert_is_value(response_model.token.refresh_token, 'refresh_token')


#-----------------------------------------------------------------------------------------------------------------------
# Token validation
@allure.step('Check Tokens')
def assert_token(response_model: AuthResponseSchema):
    """
    Token validation

    - Token type = 'bearer'
    - Access token length = 199 chars
    - Refresh token length = 199 chars
    - Access token ≠ Refresh token

    :param response_model: Pydantic-model (AuthResponseSchema)
    :raise AssertionError
    """
    # Token type = 'bearer'
    assert_equal(
        response_model.token.token_type,
        'bearer',
        'token_type')

    # Access token ≠ Refresh token:
    assert_not_equal(
        response_model.token.access_token,
        'access_token',
        response_model.token.refresh_token,
        'refresh_token')

    # Access token length = 199 chars
    assert_length(
        response_model.token.access_token,
        199,
        'access_token')

    # Refresh token length = 199 chars
    assert_length(
        response_model.token.refresh_token,
        199,
        'refresh_token')


#-----------------------------------------------------------------------------------------------------------------------
