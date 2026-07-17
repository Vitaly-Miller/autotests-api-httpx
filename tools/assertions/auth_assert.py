"""
Auth (Log in) assertions
"""
import allure
from tools.logger import get_logger
from schemas.auth_schema import AuthResponseSchema
from tools.assertions.base_assert import (
    assert_equal,
    assert_length,
    assert_is_value,
    assert_not_equal
)
#------------- Logger ------------
logger = get_logger('AUTH-ASSERT')

#=======================================================================================================================
@allure.step('Auth Response data is non-empty')
def assert_auth_response_non_empty(response: AuthResponseSchema):
    """
    Auth Response data is non-empty

    :param response: Pydantic-model (AuthResponseSchem)
    :raise AssertionError
    """
    logger.info('Auth Response data is non-empty')
    assert_is_value(response.token.token_type, 'token_type')
    assert_is_value(response.token.access_token, 'access_token')
    assert_is_value(response.token.refresh_token, 'refresh_token')


@allure.step('Tokens validation')
def assert_token(response: AuthResponseSchema):
    """
    Tokens validation

    - Token type = "bearer"
    - Access token length = 199 chars
    - Refresh token length = 199 chars
    - Access token ≠ Refresh token

    :param response: Pydantic-model (AuthResponseSchema)
    :raise AssertionError
    """
    logger.info('Tokens validation')
    assert_equal(                              # Access Token type = 'bearer'
        response.token.token_type,
        'bearer',
        'token_type')

    assert_not_equal(                          # Access token ≠ Refresh token
        response.token.access_token,
        'access_token',
        response.token.refresh_token,
        'refresh_token')

    assert_length(                             # Access token length = 199 chars
        response.token.access_token,
        199,
        'access_token')

    assert_length(                             # Refresh token length = 199 chars
        response.token.refresh_token,
        199,
        'refresh_token')


#=======================================================================================================================
