"""
Users assertions
"""
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.assertions.base import assert_equal

#=======================================================================================================================
def assert_create_user_response(response_data: CreateUserResponseSchema, create_user_payload: CreateUserRequestSchema):
    """
    Проверяет совпадение значения полей запроса на создание пользователя и его ответа (4 in 1)

    Поля: "email", "last_name", "first_name", "middle_name"
    :param create_user_payload: create_user_payload = CreateUserRequestSchema()
    :param response_data: response_data = CreateUserResponseSchema.model_validate_json(response.text)
    """
    assert_equal(response_data.user.email, create_user_payload.email, 'email')
    assert_equal(response_data.user.last_name, create_user_payload.last_name, 'last_name')
    assert_equal(response_data.user.first_name, create_user_payload.first_name, 'first_name')
    assert_equal(response_data.user.middle_name, create_user_payload.middle_name, 'middle_ame')
