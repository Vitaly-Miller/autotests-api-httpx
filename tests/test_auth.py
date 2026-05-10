"""
Test login user (auth)
Тест на авторизацию (Log in) зарегистрированного пользователя
"""
import pytest
from clients.auth.auth_client import get_auth_client, AuthClient
from clients.auth.auth_schema import LoginRequestSchema, LoginResponseSchema
from clients.users.public_users_client import get_public_users_client, PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from http import HTTPStatus, HTTPMethod
from tools.assertions.auth import assert_login_response
from tools.assertions.base import assert_status_code, assert_method
from tools.assertions.schema import validation_json_schema


#=======================================================================================================================
@pytest.mark.smoke                                                                  # маркировка smoke
@pytest.mark.users                                                                  # маркировка users
def test_login(public_users_client: PublicUsersClient, auth_client: AuthClient):    # Передача фикстур клиента и авторизации: c аннотациями
    #------------------------------------------ [Pre-conditions] Create User -------------------------------------------
    # Инициализация модели с fake-данными нового пользователя по Pydantic-схеме
    create_user_payload = CreateUserRequestSchema()

    # ︎▶ Запрос на создание пользователя через API-метод
    public_users_client.create_user_api(payload=create_user_payload)     # Передаем сгенерированные в Pydantic-схеме fake-данные нового пользователя

    #----------------------------------------------------- Log in  -----------------------------------------------------
    # Инициализация модели с fake-данными нового пользователя по Pydantic-схеме
    login_payload = LoginRequestSchema(
        email=create_user_payload.email,                                 # Email из payload
        password=create_user_payload.password                            # Password из payload
    )

    # ▶ Запрос на Authentication (Log in) через API-метод
    auth_response = auth_client.login_api(login_payload)                 # Передаем payload c Email и Password и сохраняем ответ в переменную

    #---------------------------------------------------- Assertions ---------------------------------------------------
    # Base assertions
    assert_status_code(auth_response, HTTPStatus.OK)   # проверка статус-кода
    assert_method(auth_response, HTTPMethod.POST)      # проверка метода запроса
    # Auth assertions
    assert_login_response(response=auth_response)                        # Проверка на НЕпустоту полей (6 in 1)
    # Validation JSON Schema
    validation_json_schema(auth_response, LoginResponseSchema)

#=======================================================================================================================
