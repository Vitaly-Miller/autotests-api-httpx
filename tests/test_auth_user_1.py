"""
Test User Authentication (Log in)
(Фикстуры: create_user, auth_client)
"""
import pytest
from clients.auth.auth_client import AuthClient
from clients.auth.auth_schema import AuthUserResponseSchema, AuthUserSchema
from http import HTTPStatus, HTTPMethod
from clients.users.users_schema import UserFullSchema
from tools.assertions.auth_assert import assert_auth_response_fields
from tools.assertions.base_assert import assert_status_code, assert_method
from tools.assertions.schema_assert import validation_json_schema
from tools.tool import Tool

#=======================================================================================================================
@pytest.mark.smoke
@pytest.mark.users
def test_auth_user_1(create_user: UserFullSchema, auth_client: AuthClient):  # Передача фикстур СОЗДАНИЯ ПОЛЬЗОВАТЕЛЯ + Auth Client

    auth_data = AuthUserSchema(                   # Инициализация Pydantic-модели с авторизационными данными пользователя (Email и Password)
        email=create_user.email,                  # Вытаскиваем .Email из модели
        password=create_user.password             # Вытаскиваем .Password из модели
    )

    response = auth_client.login_api(auth_data)   # ▶ Запрос на Login (Authentication) через API-метод

    #---------------------------------------------------- Assertions ---------------------------------------------------
    # Base API assertions
    assert_status_code(response, HTTPStatus.OK)     # проверка статус-кода
    assert_method(response, HTTPMethod.POST)      # проверка метода запроса

    # 6-in-1
    assert_auth_response_fields(response=response)

    # Validation JSON Schema
    validation_json_schema(response, AuthUserResponseSchema)


#=======================================================================================================================
