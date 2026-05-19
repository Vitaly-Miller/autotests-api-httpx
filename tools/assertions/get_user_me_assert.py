"""
Get User Me assertions
"""
import httpx
from clients.users.users_schema import GetUserMeResponseSchema
from tools.assertions.base_assert import assert_value_len, assert_is_value

#=======================================================================================================================
def assert_get_user_me_response_fields(response: httpx.Response):
    """
    6-in-1 | Check NON-Empty Value & User ID length

    :param response: httpx.Response для десериализации в —> Pydantic-model и дальнейшего использования в Assertions
    :raise AssertionError
    """

    # httpx.Response —> Pydantic-model (Deserialize for Assertions)
    response_model = GetUserMeResponseSchema.model_validate_json(response.text)

    # NON-Empty value:
    assert_is_value(response_model.user.id, 'id')                      # Поле не пустое - ⚠️Бессмысленно, т.к. есть проверка на длину
    assert_is_value(response_model.user.email, 'email')                # Поле не пустое
    assert_is_value(response_model.user.first_name, 'first_name')      # Поле не пустое
    assert_is_value(response_model.user.middle_name, 'middle_name')    # Поле не пустое
    assert_is_value(response_model.user.last_name, 'last_name')        # Поле не пустое

    # Value length:
    assert_value_len(response_model.user.id,'id', 36)   # Длина User ID = 36 знаков

#-----------------------------------------------------------------------------------------------------------------------
