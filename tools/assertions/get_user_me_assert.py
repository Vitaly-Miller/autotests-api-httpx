"""
Get User Me assertions
"""
import httpx
from schemas.users import GetUserMeResponseSchema
from tools.assertions.base_assert import assert_value_len, assert_is_value

#=======================================================================================================================
def assert_get_user_me_values_non_empty(response: httpx.Response):
    """
    5-in-1 | NON-Empty response values:

    - id
    - email
    - first_name
    - middle_name
    - last_name

    Actions:

    - Response —> Pydantic-model (Deserialize for Assertions)

    :param response: httpx.Response
    :raise AssertionError
    """
    response_model = GetUserMeResponseSchema.model_validate_json(response.text)          # Response —> Pydantic-model (Deserialize for Assertions)

    assert_is_value(response_model.user.id, 'id')                      # Поле не пустое
    assert_is_value(response_model.user.email, 'email')                # Поле не пустое
    assert_is_value(response_model.user.first_name, 'first_name')      # Поле не пустое
    assert_is_value(response_model.user.middle_name, 'middle_name')    # Поле не пустое
    assert_is_value(response_model.user.last_name, 'last_name')        # Поле не пустое


def assert_get_user_me_user_id_len(response: httpx.Response):
    """
    Check User ID length = 36 chars:

    Actions:

    - Response —> Pydantic-model (Deserialize for Assertions)

    :param response: httpx.Response
    :raise AssertionError
    """
    response_model = GetUserMeResponseSchema.model_validate_json(response.text)          # Response —> Pydantic-model (Deserialize for Assertions)

    assert_value_len(response_model.user.id,'id', 36)   # Длина User ID = 36 знаков

#-----------------------------------------------------------------------------------------------------------------------
