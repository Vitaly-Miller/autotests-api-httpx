"""
Test User Auth (Log in)
"""
import httpx
import pytest
from clients.auth_client import AuthClient
from schemas.users import UserFullSchema
from schemas.auth import AuthUserResponseSchema, AuthUserSchema
from http import HTTPStatus, HTTPMethod
from tools.assertions.auth_assert import assert_auth_response_fields
from tools.assertions.base_assert import assert_status_code, assert_method
from tools.assertions.schema_assert import validation_json_schema
from tools.tool import Tool

#=======================================================================================================================
@pytest.mark.smoke
@pytest.mark.auth
class TestAuth:
    """Через фикстуру авторизации"""
    def test_auth_1(self, auth_api: httpx.Response):
        response = auth_api        # Сохраняем ответ фикстуры, но не обязательно
                                   # Исполняемую API-фикстуру можно сразу передавать в Assertions в качестве параметра

        #------------------------ Assertions ------------------------
        # Base API assertions
        assert_status_code(response, HTTPStatus.OK)
        assert_method(response, HTTPMethod.POST)

        # 6-in-1 | NON-Empty value, Value equal, Value length:
        assert_auth_response_fields(response=response)

        # Validation JSON Schema
        validation_json_schema(response, AuthUserResponseSchema)



    """Через фикстуры: Создания пользователя, Авторизации пользователя"""
    def test_auth_2(self, create_user: UserFullSchema, auth_client: AuthClient):
        auth_data = AuthUserSchema(             # Инициализация Pydantic-model с авторизационными данными пользователя (Email и Password)
            email=create_user.email,            # Вытаскиваем Email из модели фикстуры
            password=create_user.password       # Вытаскиваем Password из модели фикстуры
        )
        response = auth_client.login_api(auth_data)   # ▶ Запрос через API-метод

        #------------------------ Assertions ------------------------
        # Base API assertions
        assert_status_code(response, HTTPStatus.OK)
        assert_method(response, HTTPMethod.POST)

        # 6-in-1 | NON-Empty value, Value equal, Value length:
        assert_auth_response_fields(response=response)

        # Validation JSON Schema
        validation_json_schema(response, AuthUserResponseSchema)



#=======================================================================================================================
        Tool.api_report(response)
