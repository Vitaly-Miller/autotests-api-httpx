"""
Authentication (Log in) assertions
"""
import httpx
from clients.auth.auth_schema import AuthUserResponseSchema
from tools.assertions.base_assert import assert_value_equal, assert_value_len, assert_is_value

#=======================================================================================================================
def assert_auth_response_fields(response: httpx.Response):
    """
    6-in-1 | Проверяет поля на НЕпустоту, Тип токена, Длину токенов: access- и refresh-

    :param response: httpx.Response для десериализация в —> Pydantic-model и дальнейшего использования в assertions
    :raise AssertionError
    """

    # httpx.Response —> Pydantic-model (Deserialize for Assertions)
    response_model = AuthUserResponseSchema.model_validate_json(response.text)

    # NON-Empty value:
    assert_is_value(response_model.token.token_type, 'token_type')           # Поле не пустое ┐
    assert_is_value(response_model.token.access_token, 'access_token')       # Поле не пустое ├╴⚠️Бессмысленно, т.к. в следующих проверках проверяем значения и длину (Оставлено для примера)
    assert_is_value(response_model.token.refresh_token, 'refresh_token')     # Поле не пустое ┘

    # Value equal:
    assert_value_equal(response_model.token.token_type,'token_type', 'bearer')     # Тип токена - 'bearer'

    # Value length:
    assert_value_len(response_model.token.access_token, 'access_token', 199)     # Длина access-токена  = 199 знаков
    assert_value_len(response_model.token.refresh_token, 'refresh_token', 199)   # Длина refresh-токена = 199 знаков

#-----------------------------------------------------------------------------------------------------------------------
