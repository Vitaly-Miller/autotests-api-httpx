"""
Test Create User
"""
"""
- Фикстура public_users_client. 
- Без передачи create_user_data в assert-фунцию. 
- Create User data забирается из response.REQUEST.content на уровне assert-фунции.
"""
import pytest
from clients.users.public_users_client import PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from http import HTTPStatus, HTTPMethod
from tools.assertions.base_assert import assert_status_code, assert_method
from tools.assertions.schema_assert import validation_json_schema
from tools.assertions.users_assert import assert_user_data_fields
from tools.tool import Tool

#=======================================================================================================================
@pytest.mark.smoke
@pytest.mark.users
def test_create_user(public_users_client: PublicUsersClient):       # Передаем фикстуру PublicUsersClient
    create_user_data = CreateUserRequestSchema()                    # Инициализация Pydantic-модели с генерацией fake User data нового пользователя для регистрации
    response = public_users_client.create_user_api(create_user_data=create_user_data)   # ▶ Запрос на создание пользователя через API-метод

    #---------------------------------------------------- Assertions ---------------------------------------------------
    # Base API assertions
    assert_status_code(response, HTTPStatus.OK)
    assert_method(response, HTTPMethod.POST)

    # Value equal (Проверка совпадения полей запроса и ответа 4-in-1)
    assert_user_data_fields(response=response)

    # Validation JSON Schema
    validation_json_schema(response, CreateUserResponseSchema)

#=======================================================================================================================
    Tool.api_report(response)
