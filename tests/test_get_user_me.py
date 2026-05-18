"""
Test Get User Me
(Фикстура private_users_client)
"""
import http
import pytest
from clients.users.private_users_client import PrivateUsersClient
from tools.assertions.base_assert import assert_status_code, assert_method
from tools.tool import Tool

#=======================================================================================================================
@pytest.mark.regression
@pytest.mark.users
def test_get_user_me(private_users_client: PrivateUsersClient):   # Передача фикстуры СОЗДАНИЯ ПОЛЬЗОВАТЕЛЯ

    response = private_users_client.get_user_me_api()             # 🟩Get-запрос на получение данных ТЕКУЩЕГО пользователя

    # ---------------------------------------------------- Assertions ---------------------------------------------------
    assert_status_code(response, http.HTTPStatus.OK)
    assert_method(response, http.HTTPMethod.GET)


# =======================================================================================================================
    Tool.api_report(response)
