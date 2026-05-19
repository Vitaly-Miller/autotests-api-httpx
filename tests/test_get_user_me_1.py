"""
Test Get User Me 1
(Фикстура create_user + manual)
"""
import http
import pytest
from clients.users.private_users_client import get_private_users_client
from clients.users.users_schema import UserFullSchema, GetUserMeResponseSchema
from tools.assertions.base_assert import assert_status_code, assert_method
from tools.assertions.get_user_me_assert import assert_get_user_me_response_fields
from tools.assertions.schema_assert import validation_json_schema
from tools.assertions.users_assert import assert_user_data_fields

#=======================================================================================================================
@pytest.mark.regression
@pytest.mark.users
def test_get_user_me(create_user: UserFullSchema):            # Передача фикстуры СОЗДАНИЯ ПОЛЬЗОВАТЕЛЯ
    auth_data = create_user.auth_data                         # Вытаскиваем авторизационные данные через свойство UserFullSchema .auth_data
    get_user_me_client = get_private_users_client(auth_data)  # Получаем экземпляр PrivateUsersClient c уже настроенным HTTP-клиентом с Base URL + Auth
    response = get_user_me_client.get_user_me_api()           # ▶ Запрос на получение данных ТЕКУЩЕГО пользователя через API-метод

    #---------------------------------------------------- Assertions ---------------------------------------------------
    # Base API assertions
    assert_status_code(response, http.HTTPStatus.OK)
    assert_method(response, http.HTTPMethod.GET)

    # Fields assertions
    assert_user_data_fields(response, create_user.request)

    # Fields (NON-Empty value, User ID length)
    assert_get_user_me_response_fields(response)

    # Validation JSON Schema
    validation_json_schema(response, GetUserMeResponseSchema)

#=======================================================================================================================
