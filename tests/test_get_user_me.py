"""
Test Get User Me
"""
import pytest
from httpx import Response

from api_client_create_course import auth_data
from clients.auth.auth_client import AuthClient
from clients.auth.auth_schema import LoginRequestSchema, LoginResponseSchema
from http import HTTPStatus, HTTPMethod

from clients.users.private_users_client import get_private_users_client, PrivateUsersClient
from clients.users.users_schema import UserFullSchema
from tools.assertions.auth_assert import assert_login_response_fields
from tools.assertions.base_assert import assert_status_code, assert_method
from tools.assertions.schema_assert import validation_json_schema
from tools.tool import Tool

#=======================================================================================================================
@pytest.mark.smoke
@pytest.mark.users
def test_get_user_me(create_and_auth_user: UserFullSchema):  # Передача фикстур СОЗДАНИЯ ПОЛЬЗОВАТЕЛЯ и АВТОРИЗАЦИИ

    client = PrivateUsersClient()
    response = get_private_users_client(create_and_auth_user)

    #---------------------------------------------------- Assertions ---------------------------------------------------


#=======================================================================================================================
