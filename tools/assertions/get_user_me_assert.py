"""
Get User Me assertions
"""
import httpx
from schemas.users_schema import GetUserMeResponseSchema
from tools.assertions.base_assert import assert_is_value

#=======================================================================================================================
# NON-Empty Response values
def assert_get_user_me_response_values_non_empty(response: httpx.Response):
    """
    NON-Empty Response values:

    - id
    - email
    - first_name
    - middle_name
    - last_name

    :param response: httpx.Response (for deserialize —> Pydantic-model)
    :raise AssertionError
    """
    response_model = GetUserMeResponseSchema.model_validate_json(response.text)    # Response —> Pydantic-model

    assert_is_value(response_model.user.id, 'id')
    assert_is_value(response_model.user.email, 'email')
    assert_is_value(response_model.user.first_name, 'first_name')
    assert_is_value(response_model.user.middle_name, 'middle_name')
    assert_is_value(response_model.user.last_name, 'last_name')


# User ID validation
# - Use <def assert_user_id> from /users_assert.py


#-----------------------------------------------------------------------------------------------------------------------
