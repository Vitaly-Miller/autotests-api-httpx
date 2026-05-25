"""
Test User Authentication (Log in)

"""
"""
Фикстуры: create_user, auth_client
"""
import pytest
from clients.auth_client import AuthClient
from schemas.auth import AuthUserResponseSchema, AuthUserSchema
from schemas.users import UserFullSchema
from tools.assertions.auth_assert import assert_auth_response_fields
from tools.assertions.base_assert import assert_status_code, assert_method
from tools.assertions.schema_assert import validation_json_schema
from http import HTTPStatus, HTTPMethod

#=======================================================================================================================
@pytest.mark.smoke
@pytest.mark.users
def test_auth_user_1(create_user: UserFullSchema, auth_client: AuthClient):  # Передача фикстур Create User + Auth Client

    auth_data = AuthUserSchema(                   # Инициализация Pydantic-model с авторизационными данными пользователя (Email и Password)
        email=create_user.email,                  # Вытаскиваем Email из модели фикстуры
        password=create_user.password             # Вытаскиваем Password из модели фикстуры
    )

    response = auth_client.login_api(auth_data)   # ▶ Запрос на Authentication (Login) через API-метод

    #---------------------------------------------------- Assertions ---------------------------------------------------
    # Base API assertions
    assert_status_code(response, HTTPStatus.OK)
    assert_method(response, HTTPMethod.POST)

    # 6-in-1 | NON-Empty value, Value equal, Value length:
    assert_auth_response_fields(response=response)

    # Validation JSON Schema
    validation_json_schema(response, AuthUserResponseSchema)


#=======================================================================================================================
