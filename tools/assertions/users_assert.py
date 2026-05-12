"""
Users assertions
"""
from httpx import Response
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.assertions.base_assert import assert_equal

#=======================================================================================================================
def assert_create_user_fields(response: Response, create_user_payload: CreateUserRequestSchema = None):
    """
    Проверяет совпадение значения полей Запроса и Ответа (4 in 1)

    Десериализует http.Response и .Request в —> Pydantic-model для Assertions
    Проверяемые поля: email, last_name, first_name; middle_name

    :param response: Response для десериализация в —> Pydantic-model и дальнейшего использования в assertions
    :param create_user_payload: Request data (Pydantic-model) - Внешние данные для запроса. Если не передать, то берутся из response.REQUEST.content
    :raise AssertionError - if values are not equal

    """

    # JSON-ответ —> Pydantic-model (десериализация для Assertions)
    response_model = CreateUserResponseSchema.model_validate_json(response.text)

    # Условие, если не передать create_user_payload, то вытащить Request из Response и десериализовать
    if not create_user_payload:
        create_user_payload = CreateUserRequestSchema.model_validate_json(response.request.content)

    # Assertions 4-in-1:
    assert_equal(response_model.user.email, create_user_payload.email, 'email')
    assert_equal(response_model.user.last_name, create_user_payload.last_name, 'last_name')
    assert_equal(response_model.user.first_name, create_user_payload.first_name, 'first_name')
    assert_equal(response_model.user.middle_name, create_user_payload.middle_name, 'middle_ame')

#-----------------------------------------------------------------------------------------------------------------------
