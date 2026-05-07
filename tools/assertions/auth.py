"""
Authentication (Log in) assertions
"""
from clients.auth.auth_schema import LoginResponseSchema
from tools.assertions.base import assert_equal, assert_value_len, assert_is_true

#=======================================================================================================================
def assert_login_response(response_data: LoginResponseSchema):
    """
    Проверяет поля на НЕпустоту, тип токена, длину access- и refresh-токенов

    :param response_data: Response data (Pydantic-model)
    :raise AssertionError - if values are not equal
    """
    assert_is_true(response_data.token.token_type, 'token_type')                         # Поле не пустое
    assert_is_true(response_data.token.access_token, 'access_token')                     # Поле не пустое
    assert_is_true(response_data.token.refresh_token, 'refresh_token')                   # Поле не пустое
    assert_equal(response_data.token.token_type, 'bearer', 'token_type')           # Тип токена - 'bearer'
    assert_value_len(response_data.token.access_token, 199, 'access_token')     # Длина access-токена 199 знаков
    assert_value_len(response_data.token.refresh_token, 199, 'refresh_token')   # Длина refresh-токена 199 знаков
