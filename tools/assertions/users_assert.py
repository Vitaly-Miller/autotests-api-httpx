"""
Users assertions
"""
import httpx
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.assertions.base_assert import assert_value_equal

#=======================================================================================================================
def assert_user_data_fields(response: httpx.Response, request_model: CreateUserRequestSchema | None = None):
    """
    4-in-1 | Проверяет совпадение значения полей Response и Request

    Десериализация в —> Pydantic-model для Assertions
    Проверяемые поля: -email, -last_name, -first_name, -middle_name

    :param response: httpx.Response c User data для десериализация в —> Pydantic-model и дальнейшего использования в assertions
    :param request_model:  Pydantic-model c User data. (Если не передать, то вытащит из response.REQUEST.content и десериализует в —> Pydantic-model)
    :raise AssertionError
    """

    # httpx.Response —> Pydantic-model (Deserialize for Assertions)
    response_model = CreateUserResponseSchema.model_validate_json(response.text)

    # Условие, если не передать request_model, то вытащить их из response.REQUEST.conten и распарсить в модель
    if not request_model:
        request_model = CreateUserRequestSchema.model_validate_json(response.request.content)

    # Value equal:
    assert_value_equal(response_model.user.email, 'email',request_model.email)
    assert_value_equal(response_model.user.last_name, 'last_name',request_model.last_name)
    assert_value_equal(response_model.user.first_name, 'first_name',request_model.first_name)
    assert_value_equal(response_model.user.middle_name, 'middle_ame',request_model.middle_name)

#-----------------------------------------------------------------------------------------------------------------------
