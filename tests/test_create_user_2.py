"""
Test Create User 2
(Без передачи create_user_data в assert. Данные берутся из response.REQUEST.content)
"""
import pytest
from clients.users.public_users_client import PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from http import HTTPStatus, HTTPMethod
from tools.assertions.base_assert import assert_status_code, assert_method
from tools.assertions.schema_assert import validation_json_schema
from tools.assertions.users_assert import assert_create_user_fields

#=======================================================================================================================
@pytest.mark.smoke                                                  # маркировка smoke
@pytest.mark.users                                                  # маркировка users
def test_create_user_1(public_users_client: PublicUsersClient):     # Передаем фикстуру PublicUsersClient

    # Инициализация Pydantic-модели с fake данными нового пользователя для регистрации
    create_user_data = CreateUserRequestSchema()                 # by Default (fake generated)
    # ▶ Запрос на создание пользователя через API-метод
    response = public_users_client.create_user_api(create_user_data=create_user_data)   # Передаем сгенерированные в Pydantic-схеме fake данные нового пользователя

    #---------------------------------------------------- Assertions ---------------------------------------------------
    # Base assertions
    assert_status_code(response, HTTPStatus.OK)    # проверка статус-кода
    assert_method(response, HTTPMethod.POST)       # проверка метода запроса
    # Create User assertions
    assert_create_user_fields(response=response)                    # 👈(response only) Проверка совпадения полей запроса и ответа (4 in 1)
    # Validation JSON Schema
    validation_json_schema(response, CreateUserResponseSchema)

#=======================================================================================================================
