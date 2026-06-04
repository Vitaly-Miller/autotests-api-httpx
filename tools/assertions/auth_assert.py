"""
Auth (Log in) assertions
"""
import httpx
from schemas.auth_schema import AuthResponseSchema
from tools.assertions.base_assert import (
    assert_equal,
    assert_length,
    assert_is_value,
    assert_not_equal
)
#=======================================================================================================================
# NON-Empty Response values
def assert_auth_values_non_empty(response: httpx.Response):
    """
    Non-empty Response values

    - token_type
    - access_token
    - refresh_token

    :param response: Response (for deserialize —> Pydantic-model)
    :raise AssertionError
    """
    response_model = AuthResponseSchema.model_validate_json(response.text)   # Response —> Pydantic-model

    assert_is_value(response_model.token.token_type, 'token_type')
    assert_is_value(response_model.token.access_token, 'access_token')
    assert_is_value(response_model.token.refresh_token, 'refresh_token')


#-----------------------------------------------------------------------------------------------------------------------
# Token validation
def assert_auth_token(response: httpx.Response):
    """
    Token validation

    - Token type = 'bearer'
    - Access token length = 199 chars
    - Refresh token length = 199 chars
    - Access token ≠ Refresh token

    :param response: httpx.Response (for deserialize —> Pydantic-model)
    :raise AssertionError
    """
    response_model = AuthResponseSchema.model_validate_json(response.text)   # Response —> Pydantic-model

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
