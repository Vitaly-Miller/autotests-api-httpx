"""
Authentication (Log in) assertions
"""
from typing import Any
from clients.auth.auth_schema import LoginResponseSchema
from tools.assertions.base import assert_equal, assert_value_len, assert_is_true

#=======================================================================================================================
def assert_login_response(response: Any):
    """
    6-in-1 | Проверяет поля на НЕпустоту, Тип токена, Длину токенов: access- и refresh-

    :param response: Response для десериализация в —> Pydantic-model и дальнейшего использования в assertions
    :raise AssertionError - if values are not equal
    """
    response_data = LoginResponseSchema.model_validate_json(response.text)               # JSON-ответ —> Pydantic-model (десериализация)
    assert_is_true(response_data.token.token_type, 'token_type')                  # Поле не пустое
    assert_is_true(response_data.token.access_token, 'access_token')              # Поле не пустое
    assert_is_true(response_data.token.refresh_token, 'refresh_token')            # Поле не пустое
    assert_equal(response_data.token.token_type, 'bearer', 'token_type')           # Тип токена - 'bearer'
    assert_value_len(response_data.token.access_token, 199, 'access_token')     # Длина access-токена 199 знаков
    assert_value_len(response_data.token.refresh_token, 199, 'refresh_token')   # Длина refresh-токена 199 знаков
