"""
Test Get User Me 2
(Фикстура get_user_me)
"""
import http
import httpx
import pytest
from tools.assertions.base_assert import assert_status_code, assert_method

from tools.tool import Tool

#=======================================================================================================================
@pytest.mark.smoke
@pytest.mark.users
def test_get_user_me(get_user_me_api: httpx.Response):   # Передача фикстуры get_user_me

    response = get_user_me_api                           # Сохраняем ответ в переменную

    #---------------------------------------------------- Assertions ---------------------------------------------------
    assert_status_code(response, http.HTTPStatus.OK)
    assert_method(response, http.HTTPMethod.GET)

    #assert_user_data_fields(response)
    print(response.json())
    print(response.request.content)
#=======================================================================================================================
    Tool.api_report(response)
