"""
Authentication (Log in) assertions
"""
from clients.auth.auth_schema import LoginResponseSchema
from tools.assertions.base import assert_equal, assert_value_len

#=======================================================================================================================
def assert_login_response(response_data: LoginResponseSchema):
    """
    Проверяет тип токена, длину access- и refresh-токенов

    :param response_data: Response data (Pydantic-model)
    :raise AssertionError - if values are not equal
    """
    assert_equal(response_data.token.token_type, 'bearer', 'token_type')   # тип токена
    assert_value_len(response_data.token.access_token, 199, 'access_token')     # длина access-токена
    assert_value_len(response_data.token.refresh_token, 199, 'refresh_token')   # длина refresh-токена
