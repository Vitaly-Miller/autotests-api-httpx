"""
Users assertions
"""
import httpx
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.assertions.base_assert import assert_equal

#=======================================================================================================================
def assert_create_user_fields(response: httpx.Response, create_user_data: CreateUserRequestSchema = None):
    """
    Проверяет совпадение значения полей Запроса и Ответа (4 in 1)

    Десериализует http.Response и .Request в —> Pydantic-model для Assertions
    Проверяемые поля: email, last_name, first_name; middle_name

    :param response: Response для десериализация в —> Pydantic-model и дальнейшего использования в assertions
    :param create_user_data: (payload) (Pydantic-model) - Внешние данные. Если не передать, то берутся из response.REQUEST.content
    :raise AssertionError - if values are not equal

    """

    # JSON-ответ —> Pydantic-model (десериализация для Assertions)
    response_model = CreateUserResponseSchema.model_validate_json(response.text)
    # Условие, если не передать create_user_data, то вытащить их из response.REQUEST.conten и распарсить в модель
    if not create_user_data:
        create_user_data = CreateUserRequestSchema.model_validate_json(response.request.content)

    # Assertions 4-in-1:
    assert_equal(response_model.user.email, create_user_data.email, 'email')
    assert_equal(response_model.user.last_name, create_user_data.last_name, 'last_name')
    assert_equal(response_model.user.first_name, create_user_data.first_name, 'first_name')
    assert_equal(response_model.user.middle_name, create_user_data.middle_name, 'middle_ame')

#-----------------------------------------------------------------------------------------------------------------------
