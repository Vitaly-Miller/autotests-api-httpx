"""
Auth (Log in) assertions
"""
import allure
from logger import get_logger
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
# Auth Response data is non-empty
@allure.step('Auth Response data is non-empty')                                 # Allure step title
def assert_auth_response_non_empty(response: AuthResponseSchema):
    """
    Auth Response data is non-empty

    :param response: Pydantic-model (AuthResponseSchem)
    :raise AssertionError
    """
    logger.info('Auth Response data is non-empty')                              # Logger
    assert_is_value(response.token.token_type, 'token_type')
    assert_is_value(response.token.access_token, 'access_token')
    assert_is_value(response.token.refresh_token, 'refresh_token')


#-----------------------------------------------------------------------------------------------------------------------
# Tokens validation
@allure.step('Tokens validation')                                               # Allure step title
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
    logger.info('Tokens validation')                                            # Logger
    # Access Token type = 'bearer'
    assert_equal(
        response.token.token_type,
        'bearer',
        'token_type')

    # Access token ≠ Refresh token:
    assert_not_equal(
        response.token.access_token,
        'access_token',
        response.token.refresh_token,
        'refresh_token')

    # Access token length = 199 chars
    assert_length(
        response.token.access_token,
        199,
        'access_token')

    # Refresh token length = 199 chars
    assert_length(
        response.token.refresh_token,
        199,
        'refresh_token')


#-----------------------------------------------------------------------------------------------------------------------
