"""
Auth (Log in) assertions
"""
import httpx
from schemas.auth import AuthUserResponseSchema
from tools.assertions.base_assert import (
    assert_value_equal,
    assert_value_len,
    assert_is_value,
    assert_value_not_equal
)
#=======================================================================================================================
def assert_auth_values_non_empty(response: httpx.Response):
    """
    3-in-1 | Non-empty response values:

    - token_type
    - access_token
    - refresh_token

    Actions:

    - Response —> Pydantic-model (Deserialize for Assertions)

    :param response: httpx.Response
    :raise AssertionError
    """
    response_model = AuthUserResponseSchema.model_validate_json(response.text)  # Response —> Pydantic-model (Deserialize for Assertions)

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

    Actions:
    httpx.Response —> Pydantic-model (Deserialize for Assertions)

    :param response: httpx.Response
    :raise AssertionError
    """

    # httpx.Response —> Pydantic-model (Deserialize for Assertions)
    response_model = AuthUserResponseSchema.model_validate_json(response.text)

    # Token type - 'bearer'
    assert_value_equal(
        response_model.token.token_type,
        'token_type',
        'bearer')

    # Access token length = 199 chars
    assert_value_len(
        response_model.token.access_token,
        'access_token',
        199)

    # Refresh token length = 199 chars
    assert_value_len(
        response_model.token.refresh_token,
        'refresh_token',
        199)

    # Access token ≠ Refresh token:
    assert_value_not_equal(
        response_model.token.access_token,
        'access_token',
        response_model.token.refresh_token,
        'refresh_token')

#-----------------------------------------------------------------------------------------------------------------------
