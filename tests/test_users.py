"""
Test Create User
Тест создания нового пользователя
(Через СВОИ assertion-функции + Инициализация client через фикстуры)
"""
import pytest

from clients.users.public_users_client import PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from http import HTTPStatus, HTTPMethod
from tools.assertions.base import assert_status_code, assert_method
from tools.assertions.schema import validation_json_schema
from tools.assertions.users import assert_create_user_response

#=======================================================================================================================
@pytest.mark.smoke                                                                # маркировка smoke
@pytest.mark.users                                                                # маркировка users
def test_create_user(public_users_client: PublicUsersClient):                     # Передаем в тест фикстуру инициализации client: c аннотацией
    # --------------------------------------------------  Create User --------------------------------------------------
    # Инициализация модели с fake данными нового пользователя по Pydantic-схеме
    create_user_payload = CreateUserRequestSchema()

    # ▶ Запрос на создание пользователя через API-метод
    response = public_users_client.create_user_api(payload=create_user_payload)    # Передаем сгенерированные в Pydantic-схеме fake данные нового пользователя

    #---------------------------------------------------- Assertions ---------------------------------------------------
    # Base assertions
    assert_status_code(response, HTTPStatus.OK)                           # проверка статус-кода
    assert_method(response, HTTPMethod.POST)                              # проверка метода запроса
    # Create User assertions
    assert_create_user_response(response, create_user_payload)    # Проверка совпадения полей запроса и ответа (4 in 1)
    # Validation JSON Schema
    validation_json_schema(response, CreateUserResponseSchema)

#=======================================================================================================================
