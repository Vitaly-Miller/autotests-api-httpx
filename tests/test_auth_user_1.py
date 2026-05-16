"""
Test Log in (Authentication) 1
(Фикстуры: create_user, auth_client)
"""
import pytest
from clients.auth.auth_client import AuthClient
from clients.auth.auth_schema import AuthUserResponseSchema, AuthUserSchema
from http import HTTPStatus, HTTPMethod
from clients.users.users_schema import UserFullSchema
from tools.assertions.auth_assert import assert_login_response_fields
from tools.assertions.base_assert import assert_status_code, assert_method
from tools.assertions.schema_assert import validation_json_schema
from tools.tool import Tool

#=======================================================================================================================
@pytest.mark.smoke
@pytest.mark.users
def test_login(create_user: UserFullSchema, auth_client: AuthClient):  # Передача фикстур СОЗДАНИЯ ПОЛЬЗОВАТЕЛЯ и АВТОРИЗАЦИИ

    # Инициализация Pydantic-модели с авторизационными данными пользователя (Email и Password)
    auth_data = AuthUserSchema(
        email=create_user.email,                      # Email из модели <create_user>
        password=create_user.password                 # Password из модели <create_user>
    )
    # ▶ Запрос на Login (Authentication) через API-метод
    response = auth_client.login_api(auth_data)       # Передаем payload c Email и Password и сохраняем ответ в переменную

    #---------------------------------------------------- Assertions ---------------------------------------------------
    # Base assertions
    assert_status_code(response, HTTPStatus.OK)   # проверка статус-кода
    assert_method(response, HTTPMethod.POST)      # проверка метода запроса
    # Authentication (Log in) assertions
    assert_login_response_fields(response=response)                # проверка на НЕпустоту полей (6 in 1)
    # Validation JSON Schema
    validation_json_schema(response, AuthUserResponseSchema)


#=======================================================================================================================
    Tool.api_report(response)
