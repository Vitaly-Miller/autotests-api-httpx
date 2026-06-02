"""
Get User Me assertions
"""
import httpx
from schemas.users_schema import GetUserMeResponseSchema
from tools.assertions.base_assert import assert_length_is, assert_is_value

#=======================================================================================================================
def assert_get_user_me_values_non_empty(response: httpx.Response):
    """
    5-in-1 | NON-Empty response values:

    - id
    - email
    - first_name
    - middle_name
    - last_name

    :param response: httpx.Response (for deserialize —> Pydantic-model)
    :raise AssertionError
    """
    response_model = GetUserMeResponseSchema.model_validate_json(response.text)    # Response —> Pydantic-model (Deserialize for Assertions)

    assert_is_value(response_model.user.id, 'id')                      # Поле не пустое
    assert_is_value(response_model.user.email, 'email')                # Поле не пустое
    assert_is_value(response_model.user.first_name, 'first_name')      # Поле не пустое
    assert_is_value(response_model.user.middle_name, 'middle_name')    # Поле не пустое
    assert_is_value(response_model.user.last_name, 'last_name')        # Поле не пустое


def assert_get_user_me_user_id_len(response: httpx.Response):
    """
    Check User ID length = 36 chars

    :param response: httpx.Response (for deserialize —> Pydantic-model)
    :raise AssertionError
    """
    response_model = GetUserMeResponseSchema.model_validate_json(response.text)    # Response —> Pydantic-model (Deserialize for Assertions)

    assert_length_is(
        response_model.user.id,
        36,
        'id')

#-----------------------------------------------------------------------------------------------------------------------
