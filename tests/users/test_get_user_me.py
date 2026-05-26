"""
Test Get User Me
"""
"""
- Фикстура private_users_client
"""
import http
import pytest
from clients.private_users_client import PrivateUsersClient
from schemas.users import GetUserMeResponseSchema
from tools.assertions.base_assert import assert_status_code, assert_method
from tools.assertions.get_user_me_assert import assert_get_user_me_response_fields
from tools.assertions.schema_assert import validation_json_schema
from tools.tool import Tool

#=======================================================================================================================
@pytest.mark.regression
@pytest.mark.users
def test_get_user_me(private_users_client: PrivateUsersClient):   # Передаем фикстуру PrivateUsersClient

    response = private_users_client.get_user_me_api()             # ▶ Запрос на получение данных ТЕКУЩЕГО пользователя через API-метод

    # ---------------------------------------------------- Assertions ---------------------------------------------------
    # Base API assertions
    assert_status_code(response, http.HTTPStatus.OK)
    assert_method(response, http.HTTPMethod.GET)

    # Fields assertions
    # PASS: Нет доступа к Request внутренней фикстуры <create_user>

    # (6-in-1) NON-Empty value, ID length
    assert_get_user_me_response_fields(response=response)

    # Validation JSON Schema
    validation_json_schema(response, GetUserMeResponseSchema)

#=======================================================================================================================
    Tool.api_report(response)
