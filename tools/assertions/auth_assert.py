"""
Auth (Log in) assertions
"""
import httpx
from schemas.auth_schema import AuthResponseSchema
from tools.assertions.base_assert import (
    assert_equal,
    assert_length_is,
    assert_is_value,
    assert_not_equal
)
#=======================================================================================================================
def assert_auth_values_non_empty(response: httpx.Response):
    """
    3-in-1 | Non-empty response values:

    - token_type
    - access_token
    - refresh_token

    :param response: httpx.Response (for deserialize —> Pydantic-model)
    :raise AssertionError
    """
    response_model = AuthResponseSchema.model_validate_json(response.text)  # Response —> Pydantic-model (Deserialize for Assertions)

    assert_is_value(response_model.token.token_type, 'token_type')           # Поле не пустое ┐
    assert_is_value(response_model.token.access_token, 'access_token')       # Поле не пустое ├╴⚠️Бессмысленно, т.к. в следующих проверках проверяем значения и длину (Оставлено для примера)
    assert_is_value(response_model.token.refresh_token, 'refresh_token')     # Поле не пустое ┘


#-----------------------------------------------------------------------------------------------------------------------
def assert_auth_token(response: httpx.Response):
    """
    4-in-1 | Проверяет:

    - Token type = 'bearer'
    - Access token length = 199 chars
    - Refresh token length = 199 chars
    - Access token ≠ Refresh token

    :param response: httpx.Response (for deserialize —> Pydantic-model)
    :raise AssertionError
    """
    response_model = AuthResponseSchema.model_validate_json(response.text) # Response —> Pydantic-model (Deserialize for Assertions)

    # Token type - 'bearer'
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
    assert_length_is(
        response_model.token.access_token,
        199,
        'access_token')

    # Refresh token length = 199 chars
    assert_length_is(
        response_model.token.refresh_token,
        199,
        'refresh_token')


#-----------------------------------------------------------------------------------------------------------------------
